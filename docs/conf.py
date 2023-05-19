# Configuration file for the Sphinx documentation builder.
#

import os
import sys
from os import path

import okama  # isort:skip

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

root = path.realpath(path.join(path.dirname(__file__), ".."))
sys.path.insert(1, root)
sys.path.append(os.path.abspath("matplotlib_ext"))
# sys.path.insert(0, os.path.abspath("."))


# -- Project information -----------------------------------------------------

project = "okama"
copyright = "2021, MBK Development LLC"
author = "Sergey Kikevich"

# The full version, including alpha/beta/rc tags
# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.

# version = '%s r%s' % (pandas.__version__, svn_version())
version = okama.__version__

# The full version, including alpha/beta/rc tags.
release = version

# -- General configuration ---------------------------------------------------

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = "en"

# The encoding of source files.
source_encoding = "utf-8"

add_module_names = False

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # "sphinx.ext.napoleon",
    "matplotlib.sphinxext.plot_directive",
    "numpydoc",  # handle NumPy documentation formatted docstrings instead of napoleon
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.mathjax",
    "sphinx_rtd_theme",
    "nbsphinx",
    "nbsphinx_link",
    "recommonmark",
    # "myst_parser",  # for markdown
]

# source_suffix = '.rst'
# source_suffix = ['.rst', '.md']

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
# html_theme = "pydata_sphinx_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    # "external_links": [],
    # "github_url": "https://github.com/mbk-dev/okama",
    # "google_analytics_id": "UA-27880019-2",
    # Toc options
    "titles_only": False,
    "navigation_depth": 4,
}

# If false, no module index is generated.
html_use_modindex = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

# -- Options for autodoc    ------------------------------------------------

autodoc_default_flags = ["members"]
autodoc_default_options = {
    "undoc-members": False,
    "exclude-members": "__init__",
    "inherited-members": True,
    "show-inheritance": True,
}
# autodoc_inherit_docstrings = True
autodoc_typehints = "none"
autodoc_member_order = "bysource"
autoclass_content = "class"  # to not insert __init__ docstrings
autodoc_class_signature = "mixed"  # Display the signature with the class name.
autosummary_generate = True
autosummary_imported_members = False

# -- Options for numpydoc ------------------------------------------------
numpydoc_attributes_as_param_list = False
numpydoc_show_class_members = False
numpydoc_use_plots = True
numpydoc_class_members_toctree = True

# -- Options for nbsphinx ------------------------------------------------

nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
    "--InlineBackend.rc=figure.dpi=96",
]
# nbsphinx do not use requirejs (breaks bootstrap)
nbsphinx_requirejs_path = ""

# -- matplotlib plot directive settings -----------------------------------
plot_html_show_formats = False
plot_include_source = True
plot_html_show_source_link = False
plot_formats = [("png", 90)]
plot_pre_code = """
import numpy as np
import okama as ok
"""

# # Napoleon settings
# napoleon_google_docstring = False
# napoleon_numpy_docstring = True
# napoleon_include_init_with_doc = False
# napoleon_include_private_with_doc = False
# napoleon_include_special_with_doc = False
# napoleon_use_admonition_for_examples = False
# napoleon_use_admonition_for_notes = False
# napoleon_use_admonition_for_references = False
# napoleon_use_ivar = False
# napoleon_use_param = True
# napoleon_use_rtype = True
# napoleon_type_aliases = None
# napoleon_attr_annotations = True
