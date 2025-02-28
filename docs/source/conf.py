# Configuration file for the Sphinx documentation builder.

import os
import sys

sys.path.insert(0, os.path.abspath("../../src"))

# -- Project information -----------------------------------------------------
project = "ZoPy"
version = "0.1.0"
release = "0.1.0"
author = "Your Name"
copyright = "2025, Your Name"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "myst_parser",  # Enables Markdown support
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = "alabaster"
html_static_path = ["_static"]

# -- Options for MyST (Markdown) ---------------------------------------------
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}
