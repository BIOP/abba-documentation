# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ABBA-Documentation'
copyright = '2024-2026, BIOP-EPFL'
author = 'BIOP-EPFL'

release = '0.25.0'
version = '0.25.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser'
]

master_doc = "contents"

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_logo = 'assets/img/abba_logo64x64.png'
html_theme_options = {
    'logo_only': True
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Generate GitHub-style anchors for headings up to level 3 (e.g. 'page.md#5-export-as-a-new-quicknii-dataset')
myst_heading_anchors = 3

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

source_suffix = ['.rst', '.md']
# -- Redirects from the page paths of ABBA 0.11 (linked from forum posts)
extensions.append('sphinx_reredirects')
redirects = {
    "tutorial/0_create_qupath_dataset": "../guide/prepare_qupath_project.html",
    "tutorial/1_import_qupath_project": "../guide/start_and_import.html",
    "tutorial/2_registration": "../guide/inplane_registration.html",
    "tutorial/3_export_registrations": "../guide/export_results.html",
    "tutorial/4_qupath_analysis": "../guide/qupath_analysis.html",
    "tutorial/demo_dataset": "../resources/demo_dataset.html",
    "tutorial/video_tuto": "../resources/video_tuto.html",
    "tutorial/slides_tuto": "../resources/slides_tuto.html",
    "explanation/file_formats_supported": "../reference/file_formats.html",
    "explanation/registration_storage": "../reference/state_files.html",
}

# -- Dialog screenshots
# They are rendered at 2x (scripts/shoot_dialogs.sh, --scale 2) to stay sharp on high-density
# screens. Images with the 'dialog' class get an explicit width, a bit larger than their 1x size;
# the theme caps images at the width of the text column, so wide dialogs shrink to fit.
DIALOG_DISPLAY_SCALE = 0.6


def _png_width(path):
    with open(path, 'rb') as f:
        header = f.read(24)
    return int.from_bytes(header[16:20], 'big')


def _size_dialog_images(app, doctree):
    import os
    from docutils import nodes
    for image in doctree.findall(nodes.image):
        if 'dialog' not in image.get('classes', []) or 'width' in image:
            continue
        path = os.path.join(app.srcdir, image['uri'].lstrip('/'))
        if os.path.exists(path):
            image['width'] = f"{round(_png_width(path) * DIALOG_DISPLAY_SCALE)}px"


def setup(app):
    app.connect('doctree-read', _size_dialog_images)
