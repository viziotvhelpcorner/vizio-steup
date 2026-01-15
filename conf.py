# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'VIZIO TV Setup Guide'
copyright = '2025, Independent Support'
author = 'VIZIO Setup Help'

release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

# Allow raw HTML in .rst files
raw_enabled = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_title = "How to Set Up Your VIZIO TV the Easy Way"
html_short_title = "VIZIO TV Setup"

html_show_sourcelink = False

# Allow unsafe raw HTML blocks
html_allow_unsafe = True

html_theme_options = {
    'show_powered_by': False,
}

# Static files
html_static_path = ['_static']

# Favicon (place inside _static folder)
html_favicon = '_static/favicon.ico'
