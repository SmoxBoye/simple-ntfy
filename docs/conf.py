"""Sphinx configuration."""
project = "Simple ntfy"
author = "SmoxBoye"
copyright = "2023, SmoxBoye"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
