# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------
from distutils.version import LooseVersion
import glob
import os
import shutil

import arch

on_rtd = os.environ.get("READTHEDOCS", None) == "True"
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath("."))

##########################################################
# Copy Examples
##########################################################
root = os.path.split(os.path.abspath(__file__))[0]
example_path = os.path.join(root, "..", "..", "examples")
examples = glob.glob(os.path.join(example_path, "*.ipynb"))
for example in examples:
    _, filename = os.path.split(example)
    mod = filename.split("_")[0]
    target = os.path.join(root, mod, filename)
    shutil.copyfile(example, target)

# -- Project information -----------------------------------------------------

project = "arch"
copyright = "2019, Kevin Sheppard"
author = "Kevin Sheppard"

# The short X.Y version
version = arch.__version__
ver = LooseVersion(arch.__version__).version
if "+" in ver:
    loc = ver.index("+")
    version = ".".join(map(str, ver[:loc]))
    version += " (+{0})".format(ver[loc + 1])
# The full version, including alpha/beta/rc tags.
release = arch.__version__

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = "1.0"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.extlinks",
    "sphinx.ext.todo",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.coverage",
    "sphinx.ext.ifconfig",
    "sphinx.ext.napoleon",
    "IPython.sphinxext.ipython_console_highlighting",
    "IPython.sphinxext.ipython_directive",
    "nbsphinx"
]

try:
    import sphinxcontrib.spelling  # noqa: F401
except ImportError as err:  # noqa: F841
    pass
else:
    extensions.append("sphinxcontrib.spelling")

spelling_word_list_filename = ["spelling_wordlist.txt", "names_wordlist.txt"]
spelling_ignore_pypi_package_names = True

suppress_warnings = ["ref.citation"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = [".rst", ".md"]
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "colorful"  # "sphinx"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "default"
# on_rtd is whether we are on readthedocs.org
if not on_rtd:  # only import and set the theme if we"re building docs locally
    import sphinx_material

    # Adds an HTML table visitor to apply Bootstrap table classes
    html_theme_path = sphinx_material.html_theme_path()
    html_context = sphinx_material.get_html_context()
    html_theme = "sphinx_material"

    # Register the theme as an extension to generate a sitemap.xml
    extensions.append("sphinx_material")

    # sphinx_material theme options (see theme.conf for more information)
    html_theme_options = {
        'base_url': 'http://bashtage.github.io/arch/',
        'repo_url': 'https://github.com/bashtage/arch/',
        'repo_name': 'ARCH',
        # Set the name of the project to appear in the sidebar
        "nav_title": project + u" " + version,
        'globaltoc_depth': 2,
        'globaltoc_collapse': True,
        'globaltoc_includehidden': True,
        'theme_color': '#4caf50',
        'color_primary': 'blue ',
        'color_accent': 'indigo',
        'html_minify': True,
        'css_minify': True,
        'master_doc': False
    }

html_favicon = 'images/favicon.ico'
html_logo = 'images/logo.svg'
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
if not on_rtd:
    html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don"t match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``["localtoc.html", "relations.html", "sourcelink.html",
# "searchbox.html"]``.
#
# html_sidebars = {}
if not on_rtd:
    html_sidebars = {
        "**": ["logo-text.html", "globaltoc.html", "searchbox.html"]
    }

# If false, no module index is generated.
html_domain_indices = True

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "arch"

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ("letterpaper" or "a4paper").
    #
    # "papersize": "letterpaper",

    # The font size ("10pt", "11pt" or "12pt").
    #
    # "pointsize": "10pt",

    # Additional stuff for the LaTeX preamble.
    #
    # "preamble": '',

    # Latex figure (float) alignment
    #
    # "figure_align": "htbp",
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "arch.tex", "arch Documentation",
     "Kevin Sheppard", "manual"),
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, "arch", "arch Documentation",
     [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, "arch", "arch Documentation",
     author, "arch", "ARCH models in Python",
     "Finance/Econometrics"),
]

# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]

# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "statsmodels": ("http://www.statsmodels.org/dev/", None),
    "matplotlib": ("https://matplotlib.org", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference/", None),
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://docs.scipy.org/doc/numpy", None),
    "np": ("https://docs.scipy.org/doc/numpy", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "pd": ("https://pandas.pydata.org/pandas-docs/stable/", None),
}

extlinks = {"issue": ("https://github.com/bashtage/arch/issues/%s", "GH")}
