# BUMP_DOC.md — moving the docs to a new ABBA release

Runbook to retarget this documentation at a new `ch.epfl.biop:ImageToAtlasRegister` release.
`<OLD>` is the version currently documented (`release` in `docs/source/conf.py`), `<NEW>` the new one.

Check what is actually released before starting:

```bash
curl -s https://maven.scijava.org/content/groups/public/ch/epfl/biop/ImageToAtlasRegister/maven-metadata.xml | grep -E "<release>"
```

The examples below use the maintainer's Windows machine (Git Bash); adapt the paths.

```bash
export JAVA_HOME="$USERPROFILE/.jdks/ms-21.0.11"; export PATH="$JAVA_HOME/bin:$PATH"
ABBA=/f/code/github/ijp-imagetoatlas      # local clone of the ABBA sources, with its tags fetched
```

## 1. Command snapshots and diff

[scijava-introspect](https://github.com/unige-biochem/scijava-introspect) describes the commands of a
release offline. `--lenient --class-path-only` are mandatory with jgo 3.1, the main class goes on the
first coordinate, and the SciJava repository must be declared in `~/.jgorc` (not with `-r`).

```bash
T="ch.unige.biochem:scijava-introspect:0.2.0:ch.unige.biochem.scijava.introspect.CLI"
mkdir -p cli-outputs/<NEW>
jgo --lenient --class-path-only "$T+ch.epfl.biop:ImageToAtlasRegister:<NEW>" snapshot ch.epfl.biop.atlas \
  > cli-outputs/<NEW>/snapshot-ch.epfl.biop.atlas.json 2>/dev/null
jgo --lenient --class-path-only "$T+ch.epfl.biop:ImageToAtlasRegister:<NEW>" tree ch.epfl.biop.atlas \
  > cli-outputs/<NEW>/tree-ch.epfl.biop.atlas.txt 2>/dev/null
jgo --lenient --class-path-only "$T" diff cli-outputs/<OLD>/snapshot-ch.epfl.biop.atlas.json \
  cli-outputs/<NEW>/snapshot-ch.epfl.biop.atlas.json > cli-outputs/<NEW>/diff-ch.epfl.biop.atlas.json 2>/dev/null
```

Snapshots made by different scijava-introspect versions are not comparable: if the tool changed,
regenerate `<OLD>` with the new tool before diffing.

The snapshot leaves out DynamicCommands (for instance the region exports); the menu reference
generator reads their parameters from the sources instead.

## 2. ABBA window menu map

Users launch commands from the menu bar of the ABBA window, not from the Fiji menus that the snapshot
reports. Extract it from the sources at the release tag:

```bash
python scripts/abba_menu_map.py $ABBA ImageToAtlasRegister-<NEW> > cli-outputs/<NEW>/menu-abba-window.txt
diff cli-outputs/<OLD>/menu-abba-window.txt cli-outputs/<NEW>/menu-abba-window.txt
```

Read both diffs, together with `git -C $ABBA log ImageToAtlasRegister-<OLD>..ImageToAtlasRegister-<NEW>`,
and agree on the list of pages to update before editing them.

## 3. Menu reference and dialog screenshots

```bash
python scripts/build_menu_reference.py $ABBA <NEW>     # writes the page and cli-outputs/<NEW>/dialogs.txt
scripts/shoot_dialogs.sh <NEW> "ch.epfl.biop.atlas.aligner.gui.bdv.ABBABdvStartCommand=abba-start,ch.epfl.biop.atlas.scijava.AtlasChooserCommand=atlas-chooser"
python scripts/build_menu_reference.py $ABBA <NEW>     # again: references the screenshots now on disk
```

* `docs/source/reference/menu_reference.md` is generated: never edit it by hand. Plain menu actions
  (not SciJava commands) are described in the `ACTIONS` table of the generator: add new ones there.
* The screenshots are rendered offscreen by the `scijava-screenshots` tool (`ShotCommands.java`), from the
  released artifact, into `docs/source/assets/dialogs/`. The extra list adds the two start dialogs used
  by the user guide.
* The screenshots use the light theme, like the documentation (`SHOT_THEME=dark` for the other one).
* Commands without parameters get no screenshot. A command whose only input is a file opens a file
  chooser directly: it gets no screenshot either, and running it offscreen would hang, which is why the
  generator leaves it out of `dialogs.txt`.
* Known failures: the region exports and `Export Registered Slices To ImageJ` need a live session
  (their choices come from the atlas), and the QuPath dataset options dialog hangs offscreen.
* Look at every new or changed PNG. HTML messages without a width make dialogs with big blank bands: fix
  them in the ABBA command, not here.

## 4. Update the pages

* User guide: `docs/source/guide/`, task oriented, GUI first. Link to commands with their menu path,
  ``{menuselection}`Register --> Affine --> Elastix Registration (Affine)` ``, and to the menu reference
  with the generated labels, `[...](#menu-register-affine-elastix-registration-affine)`.
* Dialog images are referenced as `![<title> dialog](/assets/dialogs/<slug>.png){.dialog}`: for the
  `.dialog` class, `conf.py` sets the display width of these 2x images from their PNG size, and the theme
  shrinks the widest ones to the text column.
* Pictures of the ABBA window itself (GIFs, views) cannot be generated offscreen: mark outdated ones with
  `<!-- TODO GIF phase: ... -->`.

## 5. Version, build, publish

* `docs/source/conf.py`: `version` and `release` to `<NEW>`.
* Build with zero warnings (see `CLAUDE.md`), and check the `href` of new cross-page label links in the
  built HTML.
* Commit the `cli-outputs/<NEW>/` files together with the page updates.
* Push to `main` (`latest` on Read the Docs), then tag `v<NEW>` and activate the tag in the Read the Docs
  admin (Versions) so that it builds.
