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
