import os
import sys
import django

# Set up Django environment
sys.path.insert(0, os.path.abspath('../..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'hustlehub.settings'
django.setup()

# -- Project information -----------------------------------------------------
project = 'HustleHub'
copyright = '2025, Yandisa'
author = 'Yandisa'
release = '0.1'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',  # Optional, supports Google/NumPy docstring styles
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']

