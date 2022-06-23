# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]
source_suffix = '.rst'
master_doc = 'index'
project = 'logall'
year = '2022'
author = 'Farshid Varno'
copyright = '{0}, {1}'.format(year, author)
version = release = '0.0.0'

pygments_style = 'trac'
templates_path = ['.']
# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only set the theme if we're building docs locally
    html_theme = 'pydata_sphinx_theme'

exclude_patterns = ["build", "**.ipynb_checkpoints", "_*"]

html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = False
html_sidebars = {
    '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
}
html_short_title = '%s-%s' % (project, version)

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
