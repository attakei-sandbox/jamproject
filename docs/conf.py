"""Configuration for documents.

This directory is premise to work on poetry environment of project.
"""
import jamproject


# Project information
project = "jamproject"
copyright = "2019, Kazuya Takei"
author = "Kazuya Takei"
release = jamproject.__version__

# General configuration
extensions = [
    "sphinx.ext.autodoc",
]
templates_path = ["_templates"]
language = "ja"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Options for HTML output
html_theme = "alabaster"
html_static_path = ["_static"]
