# CLAUDE.md

End-user documentation of ABBA (Aligning Big Brains & Atlases), the Fiji plugin
`ch.epfl.biop:ImageToAtlasRegister` (sources: https://github.com/BIOP/ijp-imagetoatlas), published at
https://abba-documentation.readthedocs.io. Readers are bio-image analysts using Fiji's GUI, not developers.

## Scope

Currently documented release: see `release` in `docs/source/conf.py`.

Not covered for now, on purpose: abba_python, and the ABBA MCP server (abba-fiji), which is underway:
`installation/installation.md` only announces it. Write GUI first; scripting tabs may come later.

## Layout

- Sphinx + MyST Markdown; the toctree is `docs/source/contents.rst` (`master_doc = "contents"`).
- `getting_started/`: one end-to-end tutorial on the Zenodo demo slices.
- `guide/`: the user guide, one page per workflow step, in workflow order.
- `reference/menu_reference.md`: **generated** by `scripts/build_menu_reference.py`, never edit by hand.
- `reference/`: shortcuts, file formats, state & transform files.
- `assets/dialogs/`: generated dialog screenshots; `assets/img`, `assets/gif`: hand-made pictures.
- `cli-outputs/<version>/`: command snapshots, diffs and ABBA window menu maps, one folder per release.
- Old page paths (ABBA 0.11) redirect to the new pages through `sphinx_reredirects` (`redirects` in `conf.py`):
  update the map when moving a page.

## Updating to a new ABBA release

Follow [BUMP_DOC.md](BUMP_DOC.md).

Pictures and GIFs of the ABBA window (not the dialogs), and the tutorial video, are generated from Java by the
sibling repository abba-doc-assets: see sections 4 and 5 of [BUMP_DOC.md](BUMP_DOC.md).

## Build

```bash
python -m venv .venv && .venv/Scripts/pip install -r docs/requirements.txt   # or uv
.venv/Scripts/sphinx-build -b html docs/source docs/_build/html
```

The build has **zero warnings**: treat any new warning as a defect. Read the Docs installs only
`docs/requirements.txt`: every extension in `conf.py` needs its package there.

## Editing gotchas

- Working copies are CRLF (`core.autocrlf=true`).
- Explicit labels (`(region-of-interest)=` above a heading) are linked by name alone, from any page:
  `[region of interest](#region-of-interest)`, never `page.md#label`. Heading slugs (`myst_heading_anchors = 3`)
  are linked with the page: `abba_window.md#display-modes`. Labels must be unique across the project:
  check the generated `href` after adding one.
- Facts come from the ABBA sources at the release tag (`git -C <ijp-imagetoatlas> show ImageToAtlasRegister-<version>:<path>`)
  and from the snapshot descriptions, not from memory or from the previous docs.
