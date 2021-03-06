# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sys
import pkg_resources


# -- Project information -----------------------------------------------------

project = 'asgi-tools'
copyright = '2021, Kirill Klenov'
author = 'Kirill Klenov'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
try:
    release = pkg_resources.get_distribution('asgi-tools').version
except pkg_resources.DistributionNotFound:
    print('To build the documentation, The distribution information of ASGI-Tools')
    print('Has to be available.  Either install the package into your')
    print('development environment or run "setup.py develop" to setup the')
    print('metadata.  A virtualenv is recommended!')
    sys.exit(1)
del pkg_resources

version = release

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'
html_logo = '../.github/assets/asgi-tools.png'
html_theme_options = {
    'github_url': 'https://github.com/klen/asgi-tools',
    'use_edit_page_button': True,
    'icon_links': [
        {
            'name': 'PyPI',
            'url': 'https://pypi.org/project/asgi-tools',
            'icon': 'fas fa-box',
        }
    ],
}
html_sidebars = {
    "**": ["search-field.html", "sidebar-nav-bs.html", "custom-sidebar.html"],
}
html_context = {
    'github_user': 'klen',
    'github_repo': 'asgi-tools',
    'github_version': 'develop',
    'doc_path': 'docs',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [
    '_static'
]

autodoc_member_order = 'bysource'
autodoc_typehints = 'description'

highlight_language = "python3"

intersphinx_mapping = {
    "python": ("http://docs.python.org/3", None),
    "multidict": ("https://multidict.readthedocs.io/en/stable/", None),
    "yarl": ("https://yarl.readthedocs.io/en/stable/", None),
}
