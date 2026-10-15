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
* The region exports and `Export Registered Slices To ImageJ` need a live session (their choices come from
  the atlas): `GenerateLiveDialogsAssets` of abba-doc-assets renders them, with `run-all.sh` (section 4). Run
  section 4 before the second `build_menu_reference.py`. The QuPath dataset options dialog hangs offscreen.
* Look at every new or changed PNG. HTML messages without a width make dialogs with big blank bands: fix
  them in the ABBA command, not here.

## 4. Pictures of the ABBA window

The pictures in `docs/source/assets/abba/<page>/` are produced by
abba-doc-assets, a sibling repository (`../abba-doc-assets`):
one generator per page runs the demo registration in a real Fiji and paints the ABBA window (see its `README.md`).

```bash
cd ../abba-doc-assets
# pom.xml: abba.version to <NEW>, and the version overrides copied again from ABBA's own pom:
git -C $ABBA show ImageToAtlasRegister-<NEW>:pom.xml | sed -n '/<properties>/,/<\/properties>/p'
./run-all.sh                    # every generator, about 40 minutes; see its README for one page at a time
```

* A Fiji and the ABBA window open on screen while a generator runs: leave them, nothing depends on the mouse,
  the keyboard or what is visible. The first run on a machine downloads the atlas and the demo slide, and
  installs DeepSlice.
* Without a change in ABBA, a rerun writes byte-identical pictures: `git status` lists exactly the pictures the
  new release changes. Look at each of them, and at the framing of the views.
* `.abba` states of the key steps are saved in `../abba-doc-assets/target/states/`.
* The generators run on the Java bundled with Fiji, the one users run (`FIJI_DIR`, or `DOC_JAVA_HOME`). Not on a JDK
  21.0.11 to 21.0.13: their `java.awt.geom.Area` cuts the atlas regions into horizontal bands (JDK-8386576).
* The GIFs of the pages (`<page>/*.gif`) are filmed by the `Generate<Page>Films` generators, also run by
  `run-all.sh` (ffmpeg on the `PATH`): synthetic mouse events, frames painted, no screen recording. They are
  byte-identical from run to run, except the timelapse of the registrations (`registration_progress.gif`).

### The tutorial video

The video (`resources/video_tuto.md` links to it) is filmed by abba-doc-assets too, then rendered by
fiji-auto-tuto (`../fiji-auto-tuto`, video `abba-tutorial`):

```bash
cd ../abba-doc-assets
./run.sh GenerateTutorialVideo   # all chapters, long: DeepSlice and Elastix run in real time
# one chapter, from the state saved before it: -Ddoc.video.chapters=<slug>; see its README
rm -rf ../fiji-auto-tuto/raw-assets/AbbaTutorialDemo
cp -r target/video-assets/AbbaTutorialDemo ../fiji-auto-tuto/raw-assets/
cd ../fiji-auto-tuto
npm run manifest abba-tutorial
npm run preview-render -- abba-tutorial-preview out/abba-tutorial/preview.mp4   # quick check, about 15 minutes
npx remotion render abba-tutorial out/abba-tutorial/abba-tutorial.mp4           # final, 1 to 1.5 hours
```

Upload it with `out/abba-tutorial/youtube-description.md` (its chapters), then update the links and times of
`resources/video_tuto.md` and `guide/inplane_registration.md`.

## 5. Update the pages

* User guide: `docs/source/guide/`, task oriented, GUI first. Link to commands with their menu path,
  ``{menuselection}`Register --> Affine --> Elastix Registration (Affine)` ``, and to the menu reference
  with the generated labels, `[...](#menu-register-affine-elastix-registration-affine)`.
* Dialog images are referenced as `![<title> dialog](/assets/dialogs/<slug>.png){.dialog}`: for the
  `.dialog` class, `conf.py` sets the display width of these 2x images from their PNG size, and the theme
  shrinks the widest ones to the text column.
* Pictures and GIFs of the ABBA window: add them to a generator of abba-doc-assets (section 4).
* `installation/installation.md` names versions: the release and the zips of the ABBA installer, its Fiji
  version (`FIJI_VERSION` in abba-installer's `launcher.py`), the QuPath version of the ABBA extension, and
  `uvx abba-mcp@<NEW>`. It is the one installation page: the READMEs of ijp-imagetoatlas, abba-installer,
  abba_python and abba-mcp link to its labels (`#install-assistant`, `#install-installer`, `#install-fiji`,
  `#install-python`, `#install-qupath`), so keep them, and put installation steps here, not in the READMEs.

## 6. Version, build, publish

* `docs/source/conf.py`: `version` and `release` to `<NEW>`.
* Build with zero warnings (see `CLAUDE.md`), and check the `href` of new cross-page label links in the
  built HTML.
* Commit the `cli-outputs/<NEW>/` files together with the page updates.
* Push to `main` (`latest` on Read the Docs), then tag `v<NEW>` and activate the tag in the Read the Docs
  admin (Versions) so that it builds.
