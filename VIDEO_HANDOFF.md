# Handoff: the video tutorial of ABBA 0.24.1

Brief for the session that makes the new ABBA tutorial video. Read it fully, then `CLAUDE.md` of this repo, then
`ASSETS_HANDOFF.md` (the plan and status of the pictures and GIFs, which this work continues).

## Goal

Replace the video lecture of March 2022 (`docs/source/resources/video_tuto.md`, YouTube `sERGONVw4zE`, 47 min,
ABBA 0.1) with a tutorial of ABBA 0.24.1, generated reproducibly from code, like the pictures and the GIFs of the
documentation.

**First target: the raw assets**, the input of the video pipeline: one clip per step, the narration, and the
`timeline.json`. Rendering the final video comes after, once Nicolas has seen the raw clips.

## What exists

| Repo | What | Read |
|---|---|---|
| `F:\code\github\abba-doc-assets` | Generators of the pictures and GIFs. `Tutorial` (the Getting started steps: start, import, display, DeepSlice, Elastix), `DemoSession` (commands without dialogs), `AbbaWindow` (window state, framing, painting), `AbbaFilm` (films of the viewer or of the whole window) | `README.md`, `CLAUDE.md` (rules and gotchas, read them all) |
| `F:\code\github\fiji-robot` (branch `painted-motion`) | `widgets.StopMotion`, `VirtualPointer`, `Film`: synthetic mouse and key events, painted frames, dialogs painted into the film (`showWindow`), context menus (`choose`), ffmpeg to GIF or MP4. Also `core.Step`, `Timeline` (writes `timeline.json`), `ScreenRecorder` (ffmpeg screen capture), launchers for visible command runs | `README.md`, `HANDOFF.md` |
| `F:\code\github\fiji-auto-tuto` | Remotion pipeline: raw clips → video (chapter cards, freeze trimming, auto-zoom on the cursor, captions, click ripples, SRT, YouTube description) | `README.md`, `CLAUDE.md` |
| `F:\code\github\ijp-imglib2bdvdemo-ij2` | The Java capture tool of the earlier videos (BigDataViewer-Playground): `src/test/java/ch/epfl/biop/docs/videos/` | `AUTOMATION.md` there |

Pages of the documentation the video should follow: `docs/source/getting_started/first_registration.md` (the
tutorial on the demo slices) and the user guide `docs/source/guide/`. The chapters of the 2022 video, a useful
outline, are listed in `docs/source/resources/video_tuto.md`.

## The decision to take first, with Nicolas

fiji-auto-tuto expects **screen recordings**: `raw-assets/<Dir>/NNN-step.mp4` per step (constant 30 fps), recorded
over a flat violet `#8C16DB` desktop that it keys out, and a `timeline.json` with per-step narration, comments and
mouse events (timestamps relative to each clip), plus `youtube-description.md`. Two ways to make them:

1. **Painted (what the GIFs use).** `StopMotion` paints the windows frame by frame. No screen and no real mouse, so
   it runs over remote desktop, and the clips are byte-identical from run to run. It needs:
   - 30 fps clips per step (`Film.writeMp4` exists);
   - the windows on a violet (or transparent) canvas: whole windows with a drawn title bar, as `showWindow` already
     draws for dialogs;
   - the `VirtualPointer` actions written to `timeline.json` as the mouse events fiji-auto-tuto uses for auto-zoom and
     click ripples.
2. **Recorded (what the earlier videos used).** fiji-robot's `ScreenRecorder` and Robot gestures on the real screen.
   This needs Nicolas's machine, screen and mouse while it runs: **always warn him before taking the mouse**, he
   schedules it (a few minutes now and then, an hour at lunch).

My recommendation is painted: everything it needs exists or is close. Check first what fiji-auto-tuto really reads:
- `fiji-robot`'s `Timeline` writes version 4; fiji-auto-tuto's docs say version 3.
- fiji-auto-tuto's freeze detection expects real-time clips.

## Rules (from Nicolas, and learned)

- Nothing depends on the real mouse, keyboard or screen unless Nicolas agreed for that run.
- Commit in each repo separately (this one on `docs-0.24.1`). **Never push without asking.** The docs build has zero
  warnings.
- ABBA itself is not changed. Propose changes instead (GitHub issues on `BIOP/ijp-imagetoatlas`, like #247), and
  write it up for Nicolas first.
- fiji-robot: keep its quarantine (only `…robot.bdv` imports `bdv.*`). Never `mvn install` it while a Fiji using it
  runs.
- Generators run on the Java bundled with Fiji (`run.sh` default): Java 21.0.11 to 21.0.13 cut the atlas regions into
  bands (JDK-8386576).
- Never edit generator sources while a generator runs (`run.sh` compiles first).
- Check determinism on anything new: two runs, `cmp`.
- `run-all.sh` regenerates every picture and GIF (about 40 min). Run it before committing changes to shared code
  (`AbbaWindow`, `AbbaFilm`, fiji-robot widgets), and check that `git status` lists only the expected files.

## Help

The session `abba-documentation-54` built the pictures, the GIFs and the fiji-robot film classes, and is available for
technical questions: message it.

## Status (2026-10-05, evening): the raw assets, painted

Decided with Nicolas: **painted** clips (no screen, no real mouse), covering the Getting started tutorial **and** the
user guide topics it points to.

* **fiji-robot** (branch `painted-video`, on top of `painted-motion`, 0.1.4-SNAPSHOT installed locally):
  `Timeline.clock` (the film's time instead of the wall clock; `startedAt` left out, so two runs write the same
  file) and `Timeline.recordingBounds`; public `Timeline.recordClick` / `recordDrag` / `recordKey`;
  `StopMotion.onDesktop` (the window filmed whole on a desktop of the chroma-key color, under a drawn title bar, or
  as printed with its native one for AWT windows), `cut` (the next clip), menu-bar cascades painted where they open,
  combo-box lists painted next to their combo box as the film shows it, AWT windows shown in the film (an ImageJ
  image); `VirtualPointer` records its gestures on the timeline, `chooseInMenuBar`, `chooseInCombo`, `wheel`,
  `setKeyTarget`; `PaintedDialog` fills a SciJava dialog by its labels (the painted twin of `Harvester`);
  `Film.writeMp4` lasts exactly the film. Tests: `PaintedVideoTest`.
* **abba-doc-assets**: `AbbaVideo` (camera, clock, gestures on menus, dialogs, viewer, cards, file choosers) and
  `GenerateTutorialVideo` (the chapters and their narration). Raw assets in
  `target/video-assets/AbbaTutorialDemo/`: `NNN-<chapter>.mp4` (1920 x 1080, 30 fps, violet desktop),
  `timeline.json` (v4), `youtube-description.md`. See its README, *The tutorial video*.
* **fiji-auto-tuto**: the video `abba-tutorial` registered (`src/videos/registry.ts`); `npm run manifest abba-tutorial`
  with `DEMO_ASSETS_DIR` reads the painted assets as they are (clicks, drags and keys from the timeline). Its
  `CLAUDE.md` said timeline version 3: the build script reads version 4.
* **What fiji-auto-tuto reads**: version 4 already; `x`/`y` divided by `recordingBounds.w`/`h` (the painted canvas
  is `{0,0,1920,1080}`); `focus.*` events ignored; freeze detection works on painted clips (still frames are
  identical, they are trimmed cleanly).

The 14 chapters (8 min 20 s rendered, cards included): start ABBA (Fiji's search bar, Open Atlas, ABBA Start),
the ABBA window (pan, zoom, Atlas Display card), open the demo slices, remove unwanted slices (table + right-click),
select slices, adjust the display (table header, display settings dialog), check the orientation (review mode, zoom,
Edit Selected Slices card), position by hand (drag, key slice, Distribute Spacing, undo), DeepSlice (and the Atlas
Slicing card), Elastix affine and spline, review the registrations (P / N), save the state, export to QuPath, export
to ImageJ (stack with the regions overlay).

Commits (not pushed): fiji-robot `painted-video` (c1acefc), abba-doc-assets `main` (bde0b57), fiji-auto-tuto
`abba-tutorial` (5d7a7ca), this repo `docs-0.24.1`. `run-all.sh` after the fiji-robot changes: every picture and
GIF byte-identical, but the registration timelapse (real time).

A first preview render (fiji-auto-tuto `npm run preview-render`, 960 x 540 at 6 fps):
`F:\code\github\fiji-auto-tuto\out\abba-tutorial\preview.mp4`. Raw clips:
`F:\code\github\fiji-auto-tuto\raw-assets\AbbaTutorialDemo\`.

Determinism, two full runs compared: 10 of the 14 clips byte-identical, and `timeline.json` and
`youtube-description.md` too. The others differ inside what follows real time: the timelapses of the save and of
the two exports (ABBA's messages), and the Quick Search of the first chapter (its results come asynchronously: faint
differences, invisible).

**Privacy, before publishing**: Quick Search shows the location of the ABBA jar, here
`/C:/Users/chiarutt/.m2/repository/...` (the Maven classpath of abba-doc-assets, with the user name), not what a Fiji
user sees. To decide: run the generator on the jars of a Fiji installation, or hide the details of Quick Search.

Open, for Nicolas: the narration (written from the pages, to be reviewed; no voice yet), the pace (fiji-auto-tuto
adds reading freezes where the captions outlast the action), the size of the ABBA window in the frame (1600 x 1000
in 1920 x 1080, at 1x), chapters of the 2022 video still missing (manual affine editor, BigWarp, region of
interest, Remove Last Registration, exports to the ROI Manager).

Gotchas met:

* A class referring to `ij.*` must not be the `main` class: the verifier loads `ij.ImageJ` before
  `LegacyInjector.preinit` patches it (`LinkageError: duplicate class definition`). The Fiji-window code is in
  `AbbaVideo`.
* Fiji focuses its search bar: its blinking caret keeps the window from ever being stable (`paintWhenStable` times
  out). `AbbaVideo.steadyCarets`.
* `Save State` and folder inputs open native `FileDialog`s, which can be neither painted nor filled:
  `ij.Prefs.useJFileChooser = true` for the run makes them Swing file choosers (in the Windows look).
* The menu items are clicked with `invokeLater` (an item opening a modal dialog must not block the film).
* `-Ddoc.video.chapters=a,b` films only those chapters; the others run unfilmed (programmatically).

Findings in ABBA 0.24.1 (proposals, nothing changed):

* The dialog of the display settings (a click on a header of the slices table) is titled
  `command:ch.epfl.biop.atlas.aligner.command.DisplaySettingsCommand`: `DisplaySettingsCommand` has no `label`.
* Not a bug, a documentation fix: from the ABBA window menu, `DeepSlice Registration` presets the model from the atlas
  (`BdvMultislicePositionerView`), so its dialog has no `DeepSlice model`; the tutorial said to choose it (fixed in
  `first_registration.md` and `position_along_atlas.md`).

## Status (2026-10-06): chapters, states, timing overhaul

* **One folder and one timeline per chapter**, assembled at the end of every run
  (`target/video-assets/chapters/<chapter>/`, then `AbbaTutorialDemo/`). The session is saved before each chapter
  (`states/<chapter>.abba`): `-Ddoc.video.chapters=<chapter>` films that chapter alone from its state, in two to
  three minutes, and the assembled video gets the new chapter. A state keeps no display settings and no card
  layout: the run applies the display of the video again, and every chapter starts with the cards as ABBA opens them.
* **Timing bugs found and fixed**: (1) the clip of every step after the first started a whole clip late on the
  timeline's clock, so every event and narration line of the chapters after the first was clamped to 0 (all the
  clicks at the very beginning); (2) `ScreenRecorder.start` arms fiji-robot's `EventRecorder` even when recording is
  off, and it recorded every synthetic gesture a second time, at screen coordinates, and the real keyboard too: the
  pointer's events are now hidden from it, and the video turns it off.
* **Pacing overhaul**: fiji-auto-tuto was made for screen recordings: it cut every still stretch longer than 2 s
  and froze the picture at the start of every narration line for its whole reading time, then played the action.
  The painted video now paces itself (a narration line lasts at least its reading time, the last frame of its
  action held if needed), and fiji-auto-tuto takes its clips as they are (`paced: true` in its registry). The video
  went from 8 min 20 s to 6 min 28 s.
* **Checks**: every event inside its clip and its frame, none duplicated (`check-timeline`), and the drawn pointer
  where the timeline says at the time it says, for all 80 events (`check-sync`; with the times shifted by 3 s, 36
  fail). Clicks on what the film does not show now throw (a card scrolled out of the panel, a table row below the
  window): two such clicks had gone unnoticed.

## Status (2026-10-06, morning): Nicolas's first remarks

* The orange click ripple and the drag arrow of fiji-auto-tuto came 0.65 s after their event
  (`CLICK_HIGHLIGHT_OFFSET_SECONDS`, for screen recordings): a paced video writes `highlightOffsetSeconds: 0` in its
  manifest. Right-button drags are tagged `meta`, as fiji-auto-tuto reads them ("Right").
* Read before acting: the first action after a narration line waits until the line is read (1.5 s and a third of
  a second per word), and each action is followed by a beat (`VirtualPointer.setActionHooks`). The video went from
  6 min 28 s to 11 min 17 s.
* The slices are imported saturated (DAPI up to 256, set as each slice is created, never shown otherwise), so that
  the display chapter shows what it fixes; slices are clicked by their name in the table; the selection chapter
  recalls the table; the orientation chapter clicks both rotations, undoes them, and names
  `View > Display Mode > Positioning Mode`.
