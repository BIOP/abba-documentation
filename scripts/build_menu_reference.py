"""Build the Menu reference page of the documentation from the release data.

Inputs, for one ABBA version:
  - cli-outputs/<version>/menu-abba-window.txt   (scripts/abba_menu_map.py)
  - cli-outputs/<version>/snapshot-ch.epfl.biop.atlas.json   (scijava-introspect snapshot)
  - the ijp-imagetoatlas sources at the release tag, for the order of the parameters in the
    dialogs and for the commands the snapshot leaves out (DynamicCommands)

Outputs:
  - docs/source/reference/menu_reference.md   (generated, do not edit by hand)
  - cli-outputs/<version>/dialogs.txt          (Class=slug list for the dialog screenshots)

Usage:
  python scripts/build_menu_reference.py <ijp-imagetoatlas repo> <version>
"""
import json
import re
import subprocess
import sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIALOGS_DIR = "/assets/dialogs"  # served from docs/source/assets/dialogs

# Inputs that never get a widget in the dialog: the session is passed by the ABBA window,
# the others are filled from context by SciJava preprocessors.
NO_WIDGET_TYPES = {"MultiSlicePositioner", "BdvMultislicePositionerView", "ImagePlus", "Atlas"}

# Top-level menus whose entries are not documented: replaced by newer commands.
SKIPPED_PREFIXES = ("Edit>Obsolete>",)

# Menu entries that are plain actions, not SciJava commands: they have no dialog and no
# description in the snapshot, so they are described here.
ACTIONS = {
    "File>Save State (+View)": "Saves the current ABBA session (slices, positions, registrations, display settings and view) to an `.abba` state file.",
    "File>Load State (+View)": "Opens an `.abba` state file in the current session. Start from a fresh ABBA window: a state cannot be merged into a session that already contains slices.",
    "Edit>Undo [Ctrl+Z]": "Undoes the last action (slice move, registration, key slice, rotation, flip...).",
    "Edit>Redo [Ctrl+Shift+Z]": "Redoes the last undone action.",
    "Edit>Configuration>Startup Message>Reset Preferences": "Shows the startup messages again, including the ones you chose not to display anymore.",
    "Edit>Configuration>Mouse Options>Show Atlas Position": "Displays, next to the mouse pointer, the atlas coordinates of the point under it.",
    "Edit>Configuration>Mouse Options>Hide Atlas Position": "Hides the atlas coordinates next to the mouse pointer.",
    "Edit>Configuration>Mouse Options>Show Slice Info": "Displays, next to the mouse pointer, information about the slice under it.",
    "Edit>Configuration>Mouse Options>Hide Slice Info": "Hides the slice information next to the mouse pointer.",
    "View>Display Mode>Positioning Mode": "Switches to the positioning mode: all slices are displayed side by side along the atlas, to sort them and position them along the slicing axis.",
    "View>Display Mode>Review Mode": "Switches to the review mode: one slice at a time is overlaid on the atlas, to check and refine its registration.",
    "View>Display Mode>Positioning - Change Overlap Mode [O]": "In positioning mode, cycles through the ways slices are drawn relative to the atlas and to each other.",
    "View>Cards>Expand Card Panel": "Opens the side panel that contains the cards (atlas display, slice display, editing tools...).",
    "View>Cards>Collapse Card Panel": "Closes the side panel.",
    "View>Cards>Add Resources Monitor": "Adds a card that monitors memory and CPU usage, useful when many registrations run in parallel.",
    "View>Navigate>Next Slice [Right]": "Makes the next slice along the atlas the current slice.",
    "View>Navigate>Previous Slice [Left]": "Makes the previous slice along the atlas the current slice.",
    "View>Navigate>Center On Current Slice [C]": "Centers the view on the current slice.",
    "View>Navigate>Center On Atlas": "Centers the view on the atlas and zooms to fit the window.",
    "Slices>Select All Slices [Ctrl+A]": "Selects all slices.",
    "Slices>Deselect All Slices [Ctrl+Shift+A]": "Deselects all slices.",
    "Slices>Remove Slices": "Removes the selected slices from the session. This can be undone.",
    "Slices>Distribute Slices [D]": "In positioning mode, spaces the selected slices evenly along the slicing axis. Key slices keep their position.",
    "Cite>About Current Atlas (Web)": "Opens the web page of the atlas used in this session, with its reference and how to cite it.",
}

# Extra notes for entries that only exist in some sessions.
NOTES = {
    "Register>DeepSlice>DeepSlice Registration": "Only present when the session uses an atlas compatible with DeepSlice (adult mouse Allen CCFv3 or Waxholm rat), in coronal orientation.",
}

ACRONYMS = {"QuPath": "Qupath", "ImageJ": "Imagej", "ImagePlus": "Imageplus", "QuickNII": "Quicknii",
            "DeepSlice": "Deepslice", "BigWarp": "Bigwarp", "BDV": "Bdv", "ABBA": "Abba", "ROI": "Roi",
            "OMERO": "Omero", "ZENODO": "Zenodo"}


def slugify_class(simple_name):
    """RegisterSlicesElastixAffineCommand -> register-slices-elastix-affine."""
    name = re.sub(r"Command$", "", simple_name)
    for acronym, word in ACRONYMS.items():
        name = name.replace(acronym, word)
    return re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "-", name).lower()


def slugify_text(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def git_show(repo, tag, path):
    return subprocess.run(["git", "-C", repo, "show", f"{tag}:{path}"], capture_output=True,
                          text=True, encoding="utf-8").stdout


def find_source(repo, tag, simple_name):
    files = subprocess.run(["git", "-C", repo, "ls-tree", "-r", "--name-only", tag], capture_output=True,
                           text=True, encoding="utf-8").stdout.splitlines()
    matches = [f for f in files if f.endswith("/" + simple_name + ".java")]
    return git_show(repo, tag, matches[0]) if matches else ""


def annotation_args(source, start):
    """Returns the text between the parentheses of the annotation opening at start."""
    depth, i = 0, start
    while i < len(source):
        if source[i] == "(":
            depth += 1
        elif source[i] == ")":
            depth -= 1
            if depth == 0:
                return source[start + 1:i], i + 1
        elif source[i] == '"':
            i = source.index('"', i + 1)
            while source[i - 1] == "\\":
                i = source.index('"', i + 1)
        i += 1
    return "", len(source)


def string_attr(args, key):
    """Concatenated string literal of attribute key ("a" + "b" supported)."""
    m = re.search(key + r'\s*=\s*((?:"(?:[^"\\]|\\.)*"\s*\+?\s*)+)', args)
    if not m:
        return None
    return "".join(re.findall(r'"((?:[^"\\]|\\.)*)"', m.group(1))).replace('\\"', '"')


def source_parameters(source):
    """@Parameter fields in declaration order: [{name, type, label, description, choices, message, default}]."""
    params = []
    for m in re.finditer(r"@Parameter\s*\(", source):
        args, end = annotation_args(source, m.end() - 1)
        decl = re.match(r"\s*(?:@\w+(?:\([^)]*\))?\s*)*(?:(?:public|protected|private|static|final|transient|volatile)\s+)*"
                        r"([\w.<>\[\]]+)\s+(\w+)\s*(=\s*([^;]+))?;", source[end:])
        if not decl:
            continue
        choices = None
        cm = re.search(r"choices\s*=\s*\{([^}]*)\}", args)
        if cm:
            choices = re.findall(r'"((?:[^"\\]|\\.)*)"', cm.group(1))
        params.append({
            "type": decl.group(1), "name": decl.group(2),
            "label": string_attr(args, "label"), "description": string_attr(args, "description"),
            "choices": choices, "message": "ItemVisibility.MESSAGE" in args,
            "output": "ItemIO.OUTPUT" in args or "ItemIO.BOTH" in args,
            "default": java_literal(decl.group(4)),
        })
    return params


def read_menu(path):
    entries = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## Right-click"):
            break
        m = re.match(r"(.+?)  ->  (\(action\)|\w+)$", line.strip())
        if m:
            entries.append((m.group(1), None if m.group(2) == "(action)" else m.group(2)))
    return entries


def menu_tree(entries):
    """Nested OrderedDict in insertion order, as Swing builds the menu bar."""
    tree = OrderedDict()
    for path, cls in entries:
        if path.startswith(SKIPPED_PREFIXES):
            continue
        parts = path.split(">")
        node = tree
        for part in parts[:-1]:
            node = node.setdefault(part, OrderedDict())
        node[parts[-1]] = (path, cls)
    return tree


def java_literal(expression):
    """Value of a Java field initializer if it is a literal, None for an expression computed at runtime."""
    if not expression:
        return None
    text = expression.strip()
    if re.fullmatch(r'"(?:[^"\\]|\\.)*"', text):
        return text[1:-1]
    if text in ("true", "false"):
        return text == "true"
    if re.fullmatch(r"-?\d+(\.\d*)?([eE]-?\d+)?[dDfFlL]?", text):
        return float(text.rstrip("dDfFlL"))
    return None


def fmt_default(value):
    if value is None:
        return ""
    if isinstance(value, bool):
        return "checked" if value else "unchecked"
    if isinstance(value, float) and value.is_integer():
        value = int(value)
    text = str(value).strip()
    return f"`{text}`" if text else ""


def cell(text):
    return (text or "").replace("|", "\\|").replace("\n", " ").strip()


class Builder:
    def __init__(self, repo, version):
        self.repo, self.version, self.tag = repo, version, f"ImageToAtlasRegister-{version}"
        out = ROOT / "cli-outputs" / version
        self.entries = read_menu(out / "menu-abba-window.txt")
        snapshot = json.loads((out / "snapshot-ch.epfl.biop.atlas.json").read_text(encoding="utf-8"))
        self.snapshot = {k.split(".")[-1]: v for k, v in snapshot.items()}
        self.classes = {}  # simple name -> fully qualified name, from the sources
        self.lines, self.dialogs = [], OrderedDict()

    def declared_parameters(self, source):
        """Parameters of the class and its superclasses, superclass first, as SciJava orders the dialog."""
        parent = re.search(r"class\s+\w+(?:<[^>]*>)?\s+extends\s+(\w+)", source)
        inherited = []
        if parent and parent.group(1) not in ("DynamicCommand", "ContextCommand", "InteractiveCommand", "Object"):
            parent_source = find_source(self.repo, self.tag, parent.group(1))
            if parent_source:
                inherited = self.declared_parameters(parent_source)
        return inherited + source_parameters(source)

    def command_info(self, simple_name):
        source = find_source(self.repo, self.tag, simple_name)
        pkg = re.search(r"^package\s+([\w.]+);", source, re.M)
        fqn = f"{pkg.group(1)}.{simple_name}" if pkg else simple_name
        declared = self.declared_parameters(source)
        snap = self.snapshot.get(simple_name)
        description = snap.get("description") if snap else None
        if description is None:
            pm = re.search(r"@Plugin\s*\(", source)
            if pm:
                description = string_attr(annotation_args(source, pm.end() - 1)[0], "description")
        by_name = {i["name"]: i for i in snap.get("input", [])} if snap else {}
        params = []
        for p in declared:  # declaration order = dialog order
            if p["message"] or p["output"] or p["type"] in NO_WIDGET_TYPES or p["type"] in ("Context", "LogService"):
                continue
            if p["type"].endswith("Service") or p["type"] == "Button":
                continue
            s = by_name.pop(p["name"], {})
            params.append({**p, **{k: v for k, v in s.items() if v is not None}})
        for s in by_name.values():  # inherited parameters, not in this file
            if s["type"] not in NO_WIDGET_TYPES:
                params.append(s)
        has_message = any(p["message"] for p in declared)
        return fqn, description, params, has_message

    def emit_entry(self, path, cls, depth):
        label = path.split(">")[-1]
        anchor = "menu-" + slugify_text(path)
        self.lines += [f"({anchor})=", f"{'#' * depth} {label}", ""]
        self.lines += ["{menuselection}`" + " --> ".join(path.split(">")) + "`", ""]
        if cls is None:
            self.lines += [ACTIONS.get(path, "_No description yet._"), ""]
            return
        fqn, description, params, has_message = self.command_info(cls)
        if path in NOTES:
            self.lines += [":::{note}", NOTES[path], ":::", ""]
        if description:
            self.lines += [description, ""]
        if len(params) == 1 and params[0]["type"] in ("File", "File[]"):
            # SciJava skips the dialog and opens a file chooser directly when a single file is asked.
            p = params[0]
            self.lines += [f"A file chooser opens to select the **{cell(p.get('label') or p['name'])}**"
                           + (f": {cell(p.get('description'))}" if p.get("description") else ".") , ""]
        elif params or has_message:
            slug = slugify_class(cls)
            self.dialogs[fqn] = slug
            # Referenced once shot: run this script again after scripts/shoot_dialogs.sh.
            if (ROOT / "docs" / "source" / DIALOGS_DIR.lstrip("/") / f"{slug}.png").exists():
                self.lines += [f"![{label} dialog]({DIALOGS_DIR}/{slug}.png){{.dialog}}", ""]
            if not params:
                return  # a dialog with a message only
            self.lines += ["| Parameter | Description | Default |", "|---|---|---|"]
            for p in params:
                desc = cell(p.get("description"))
                if p.get("choices"):
                    desc += (" " if desc else "") + "Choices: " + ", ".join(f"`{c}`" for c in p["choices"]) + "."
                self.lines.append(f"| {cell(p.get('label') or p['name'])} | {desc} | {fmt_default(p.get('default'))} |")
            self.lines.append("")
        else:
            self.lines += ["This command opens no dialog.", ""]

    def emit(self, node, depth, prefix):
        for name, child in node.items():
            if isinstance(child, OrderedDict):
                if depth == 2:
                    self.lines += [f"({'menu-' + slugify_text(name)})=", f"## {name}", ""]
                else:
                    self.lines += [f"{'#' * depth} {name}", ""]
                self.emit(child, depth + 1, prefix + name + " > ")
            else:
                self.emit_entry(child[0], child[1], depth)

    def build(self):
        self.lines += [
            "<!-- Generated by scripts/build_menu_reference.py from cli-outputs/"
            f"{self.version}/ - do not edit by hand. -->", "",
            "# Menu reference", "",
            f"This page lists every entry of the menus of the ABBA window, in ABBA {self.version}, in the order "
            "they appear. Each command shows its dialog and its parameters, with their default values. "
            "The user guide explains when and how to use them.", "",
            ":::{note}",
            "Most commands act on the **selected slices**. Select slices first (see "
            "[Select & display slices](../guide/select_display_slices.md)), then run the command.",
            ":::", "",
        ]
        self.emit(menu_tree(self.entries), 2, "")
        page = ROOT / "docs" / "source" / "reference" / "menu_reference.md"
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text("\n".join(self.lines).rstrip() + "\n", encoding="utf-8", newline="\n")
        dialogs = ROOT / "cli-outputs" / self.version / "dialogs.txt"
        dialogs.write_text("".join(f"{fqn}={slug}\n" for fqn, slug in self.dialogs.items()),
                           encoding="utf-8", newline="\n")
        print(f"{page.relative_to(ROOT)}: {len(self.lines)} lines; {dialogs.relative_to(ROOT)}: {len(self.dialogs)} dialogs")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    Builder(sys.argv[1], sys.argv[2]).build()
