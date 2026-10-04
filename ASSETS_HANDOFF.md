# Handoff: screenshots of the ABBA window for the 0.24.1 documentation

Brief for a Claude Code session that produces the pictures of the ABBA window for this documentation. Read
it fully before starting, then `CLAUDE.md` of this repo.

## Goal

The documentation of ABBA 0.24.1 is written (branch `docs-0.24.1` of this repo): pages, generated menu
reference and generated dialog screenshots. What is missing are the pictures of the **ABBA window itself**
(viewer, cards, slices, registrations), still the ones of ABBA 0.11, or absent.

Produce them **reproducibly, from Java code**: a program that runs a full registration of the demo slices in a
real Fiji, sets the ABBA window in the state each picture needs, and saves the pictures into this repo. Rerun it
at each ABBA release.

Two phases, this session does the first one only:

1. **Static images (now).** No simulated mouse at all: the maintainer works over remote desktop, so nothing
   may depend on the real mouse, the keyboard or the visible screen. Everything is driven through the ABBA
   API and captured by painting the windows (see *Capture*).
2. **Videos and GIFs (later, another machine).** The same steps, driven visibly by
   [fiji-robot](https://github.com/unige-biochem/fiji-robot) and recorded, then edited by fiji-auto-tuto into a
   tutorial video replacing the 2022 one. Structure phase 1 so that phase 2 reuses it brick by brick (see
   *Towards the video*).

## Read first

| What | Where | Why |
|---|---|---|
| The pages to illustrate | `docs/source/getting_started/first_registration.md`, `docs/source/guide/*.md` | The pictures follow their text; `<!-- TODO GIF phase ... -->` comments mark what is missing |
| A complete pipeline, no dialog | `F:\code\github\abba-fiji\src\abba_fiji\data\examples\abba_demo_pipeline.groovy` | Demo slices, cleanup, display, DeepSlice, Elastix affine and spline, snapshot, save: translate it to Java |
| The ABBA window, its API | `F:\code\github\abba-fiji\src\abba_fiji\data\guides\window.md` | What the window shows, the cards, and the public methods of `BdvMultislicePositionerView` (mode, current slice, centering, visibility, overlap) |
| Painting a window without the screen | `F:\code\github\abba-fiji\src\abba_fiji\data\scripting\window_picture.groovy` | `frame.printAll(g)` on the Swing thread: right when the window is covered or the screen locked |
| fiji-robot | `F:\code\github\fiji-robot` (`README.md`, `HANDOFF.md`) | The driver to extend; its `Screenshotter` uses `Robot.createScreenCapture` (the screen), not suitable here |
| Earlier doc generators | `F:\code\github\ijp-imglib2bdvdemo-ij2\src\test\java\ch\epfl\biop\docs\` | The `Generate<Page>DocAssets` pattern (one `main` per page or scenario, `Step.begin/end`), done for BigDataViewer-Playground |
| ABBA sources | `F:\code\github\ijp-imagetoatlas`, tag `ImageToAtlasRegister-0.24.1` | `BdvMultislicePositionerView` (window, menus, cards), `MultiSlicePositioner` (session), `inspect/SliceSnapshot` |
| Agent experience driving ABBA | `F:\code\github\abba-agent-scratch\briefs\STATUS.md` (Traps), `baseline\FRICTION.md` | Known pitfalls: blocking dialogs, slice indices changing after moves, Maven and file locks |

## Where the code goes

A new sibling repository, `F:\code\github\abba-doc-assets` (suggested name), Maven, inheriting
`pom-scijava` 45.1.0:

- dependencies: `ch.epfl.biop:ImageToAtlasRegister:0.24.1` (the released artifact, never a local SNAPSHOT),
  `ch.unige.biochem:fiji-robot` (released 0.1.3, or the local 0.1.4-SNAPSHOT if you change it), `net.imagej:imagej`
  to boot Fiji;
- plain `main()` classes, no `@Plugin`: this is a tool, never deployed to an update site;
- output folder from the system property `doc.output.dir`, defaulting to
  `../abba-documentation/docs/source/assets/abba` (sibling repos);
- a short `README.md` and `CLAUDE.md`: how to run it, what it writes.

Generic capabilities (painting a component, a menu, a card) go into **fiji-robot**, which you may modify
(it is the maintainer's repo, keep its quarantine rules: only `…robot.bdv` imports `bdv.*`). Everything
ABBA-specific (session setup, view states, the shot list) stays in `abba-doc-assets`. ABBA itself should not
need changes; if one would really help, propose it rather than doing it.

The JDK: `C:\Users\chiarutt\.jdks\ms-21.0.11` (`java` is not on the PATH). Maven: IntelliJ's bundled one,
on the PATH as `mvn`. Never `mvn install` fiji-robot while a Fiji using it is running (Windows file locks).

## Capture

Paint components, never grab the screen:

```java
BufferedImage img = new BufferedImage(c.getWidth(), c.getHeight(), BufferedImage.TYPE_INT_RGB);
SwingUtilities.invokeAndWait(() -> { Graphics2D g = img.createGraphics(); c.printAll(g); g.dispose(); });
```

This works for the whole ABBA frame, the viewer alone (`bdvh.getViewerPanel()`), the card panel, or one card.
Things to settle early, on one picture, before writing the shot list:

- **Determinism.** Fixed window size (not maximized, e.g. 1600 x 1000), fixed view (`centerOnAtlas`, or an
  explicit viewer transform), fixed current slice, no mouse overlays, same slices and display ranges each run.
- **Waiting.** `mp.waitForTasks()` for the registrations, then for BigDataViewer, which renders
  asynchronously and progressively (low resolution first): find a reliable "rendering done" signal, or capture
  until two successive images are identical.
- **Resolution.** Windows display scaling (and remote desktop) changes the size of what is painted. Pick a scale
  that gives sharp images at the width of the text column (about 800 px displayed), as the dialogs do (2x).
- **Menus.** A menu is not displayed unless clicked. Render the popup of a menu of the frame's `JMenuBar`
  offscreen (size it to its preferred size, lay it out, `printAll`), to show a menu path with its items.
- **Cards.** Expand only the card a picture is about (the card panel API of BigDataViewer), and crop to it.
- **Dialogs and editors** (manual affine editor, BigWarp) are separate windows: paint them by title.

Messages of the session must not block: `view.setBlockingMessages(false)`. Startup messages: see
`Edit > Configuration > Startup Message` in ABBA (they are preferences).

## Data

The Zenodo demo slices: `ImportDemoSlicesZENODOCommand` with 1 slide (cached after the first download, about
1 GB), then delete the slices whose name does not contain `10x` (label, overview, macro), as the pipeline
does. The first DeepSlice and Elastix runs install their Python and elastix environments (minutes): run the
pipeline once before tuning the pictures.

Several pictures need the session **before** a step (unpositioned slices, no registration), others **after**.
Save `.abba` states at the key points of the pipeline, and reload them to iterate on one picture without rerunning
everything.

## Shot list

Pictures go to `docs/source/assets/abba/<page>/<name>.png`. Current pictures of ABBA 0.11 to replace, and missing ones:

| Page | Current picture (`assets/...`) | New picture: session state and view |
|---|---|---|
| getting_started/first_registration | none | One picture per step: atlas only after start; slices just imported (positioning); review mode before DeepSlice; after DeepSlice; after Elastix; registration markers |
| guide/start_and_import | `img/fiji_just_opened_project.png` | Window right after importing the demo slices, positioning mode, slices displayed |
| guide/abba_window | `gif/fiji_abba_atlas_display.gif` | `Atlas Display` card (crop), with an atlas channel unchecked |
| guide/abba_window | `img/fiji_review_mode.png`, `img/fiji_current_slice.png` | Review mode on a registered slice; positioning mode with the current slice circled |
| guide/abba_window | none | Whole window annotated or not: menu bar, viewer, card panel; one card panel picture listing the cards |
| guide/select_display_slices | `img/fiji_selected_slice.png`, `gif/fiji_select_slices.gif` | Handles with a few slices selected (green) and others not (yellow) |
| guide/select_display_slices | `gif/fiji_select_slices_table.gif`, `gif/fiji_slices_display_options.gif` | `Slices Display` card (crop): the table with some rows selected, and the `Filter by name` field in use |
| guide/select_display_slices | `gif/fiji_remove_slices.gif` | The right-click menu, rendered offscreen, or the label/overview slices before removal |
| guide/select_display_slices | `img/fiji_white_background_slice.png` | Keep (brightfield data, not the demo slices) |
| guide/orient_slices | `img/fiji_edit_slices_tab.png` | `Edit Selected Slices` card (crop); a slice before and after a flip (pair) |
| guide/orient_slices | none | The manual affine editor window (painted by title) on one slice |
| guide/position_along_atlas | `gif/fiji_slices_drag.gif`, `gif/fiji_slices_distribute.gif`, `gif/fiji_atlas_drag_then_key.gif` | Static pairs: slices before / after `Distribute Spacing`; a key slice (larger handle, `[Key]`) |
| guide/position_along_atlas | `gif/fiji_atlas_coarse_slicing.gif` | Positioning mode with a coarse "Displayed slicing" step (Atlas Display card) |
| guide/position_along_atlas | `gif/fiji_adjust_atlas_angle.gif` | `Atlas Slicing` card (crop) with non-zero angles, and the resulting atlas section |
| guide/position_along_atlas | `img/fiji_before_deepslice.png`, `img/fiji_after_deepslice.png` | Positioning mode before and after DeepSlice, same view |
| guide/inplane_registration | `gif/fiji_register_affine_spline.gif`, `gif/fiji_progression_registration.gif` | Registration markers under the handles (some waiting, running, done if you can catch it, else done); review mode after affine, after spline |
| guide/inplane_registration | `img/fiji_registration_multichannel_images.png` | Keep, or the two demo channels side by side with the two atlas channels |
| guide/inplane_registration | `img/fiji_define_ROI.png` | `Define Region Of Interest` card (crop) and a restricted region in the viewer |
| guide/inplane_registration | `gif/fiji_bigwarp_edit.gif` | BigWarp window on an Elastix spline registration (painted by title), static |
| guide/export_results | `gif/fiji_export_registered_slices.gif`, `gif/fiji_export_atlas.gif`, `img/fiji_atlas_coordinates_image.png`, `gif/fiji_export_ij1_roi_manager.gif` | The ImageJ images produced by each export (save them as PNG), the ROI Manager with regions |
| guide/export_results, reference | missing dialogs | `Export Registered Slices To ImageJ`, `Export Regions To Roi Manager`, `Export Regions To File`: their choices need a live session. Render them like the other dialogs (see `scripts/shoot_dialogs.sh` and the scijava-screenshots skill), but in the running Fiji with the session preset as input, into `docs/source/assets/dialogs/` with the slugs of `cli-outputs/0.24.1/dialogs.txt` |

QuPath pictures are out of scope. Motion (dragging, the positioning workflow) is phase 2: in phase 1, prefer
before / after pairs, and leave a `TODO GIF phase` comment where motion is really what the text describes.

For pictures judging a registration rather than showing the interface, `ABBA - Snapshot` (window independent)
may be better than the viewer.

## Integration into the documentation

- Reference the pictures from the pages, replacing the 0.11 ones; remove the `TODO GIF phase` comments that are
  resolved; delete replaced pictures from `assets/img` and `assets/gif` once nothing references them.
- The build must stay at zero warnings: `.venv\Scripts\sphinx-build -b html docs\source docs\_build\html`.
- Add a section to `BUMP_DOC.md`: how to regenerate the pictures for a new release.
- Commit in this repo on `docs-0.24.1`; commit the new repo separately. Do not push without asking.

## Towards the video (phase 2, keep it in mind)

- Write the pipeline as **named steps** matching the chapters of the Getting started tutorial, with
  fiji-robot's `Step.begin(slug, narration)` / `Step.end()`: in phase 1 they only bracket the actions and name the
  pictures; with `ScreenRecorder.ENABLED` and `Timeline.ENABLED`, the same steps produce the clips and the
  `timeline.json` that fiji-auto-tuto (`F:\code\github\fiji-auto-tuto`) turns into a video.
- Phase 1 runs commands programmatically (`programmaticLauncher()`); phase 2 swaps in visible launchers.
  fiji-robot does not have the ones ABBA needs yet: a launcher through a **window menu bar** (listed in its
  `HANDOFF.md` TODO), the right-click menu of the viewer, and buttons of a card. Designing the menu and card
  painting of phase 1 in fiji-robot (`…robot.widgets` / `…robot.bdv`) prepares them.

## Milestones

1. `abba-doc-assets` skeleton; component painting in fiji-robot; **one** picture (the window after importing the
   demo slices) in the documentation, deterministic over two runs. Stop and show it to the maintainer.
2. The Getting started pictures, from one pipeline run.
3. The user guide pictures of the shot list.
4. The three dialogs needing a live session.

## Status (2026-10-05): phase 1 done

All four milestones are committed (not pushed): this repo on `docs-0.24.1`, `abba-doc-assets` on `main`, and
fiji-robot on its branch `painted-pictures` (0.1.4-SNAPSHOT, installed locally; `abba-doc-assets` depends on it).

* **Pictures**: 32 pictures of the ABBA window in `docs/source/assets/abba/<page>/`, and the three live-session
  dialogs in `docs/source/assets/dialogs/`. `../abba-doc-assets/run-all.sh` regenerates them all (about 30 minutes);
  two runs give byte-identical files. How to rerun them at a release: `BUMP_DOC.md`, section 4.
* **fiji-robot**, generic and reusable for phase 2: `widgets.Painter` (components, windows without title bar,
  closed menus, painted as on screen), `widgets.CommandDialogPainter` (a command dialog with live inputs),
  `bdv.view.BdvCards` (expand and paint cards), `bdv.view.BdvViewer` (wait for passing messages),
  `core.InMemoryPreferences` (defaults for every remembered input, user preferences untouched).
* **Not done, phase 2**: the motion. The 0.11 GIFs left are marked `TODO GIF phase` (rectangle selection, dragging
  slices, setting a key slice, the registration sequence, the ROI Manager). The generators are written as fiji-robot
  `Step`s per chapter, ready for visible launchers and recording.
* **Open question for the maintainer**: the size and scale of the whole-window pictures (1600 x 1000, painted at
  1x). Cards and menus are painted at 1x: Swing text painted bigger than its layout gets cut.
* **Findings in ABBA 0.24.1** (proposals, nothing changed): the regions overlay of `Export Registered Slices To
  ImageJ` is drawn by ImageJ as horizontal stripes (the picture leaves it out); a manual registration whose editor is
  open shows as waiting (red), not running (yellow); the manual affine editor shows a `100 undefined` scale bar;
  after deleting the current slice, the `Slices Display` card still names it.
