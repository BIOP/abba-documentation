# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ABBA-Documentation'
copyright = '2024, BIOP-EPFL'
author = 'BIOP-EPFL'

release = '0.9'
version = '0.11.0-SNAPSHOT'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_search.extension',
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