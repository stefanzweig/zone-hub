# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys, os

sys.path.insert(0, os.path.abspath("../../"))

project = "ZoneMaster"
copyright = "2025, Z-One"
author = "刘海江"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.extlinks",
    "sphinx.ext.autodoc",
    "sphinx_copybutton",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = []

language = "zh_CN"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]

autodoc_default_options = {
    "members": True,
    "special-members": "__init__",
    "undoc-members": True,
}
