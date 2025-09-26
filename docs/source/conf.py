# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

project = 'hts-flow'
copyright = '2025, Alex Byrne'
author = 'Alex Byrne'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = ['**/*_scratch.py']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# RTD theme options for consistent sidebar
html_theme_options = {
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_with_keys": False,
    "style_external_links": True,
}

sys.path.insert(0, os.path.abspath("../../"))

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
    "private-members": False,
}
add_module_names = False
autodoc_member_order = "bysource"

# Ensure consistent sidebar across all pages
html_sidebars = {
    "**": [
        "globaltoc.html",
        "relations.html",
        "sourcelink.html",
        "searchbox.html",
    ],
}
