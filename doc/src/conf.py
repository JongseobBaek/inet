# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'INET Framework'
copyright = '2018, OpenSim Ltd.'
author = 'OpenSim Ltd'

# The short X.Y version
version = '4.0.0'
# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
#    'sphinx.ext.imgmath',
    'sphinx.ext.mathjax',
    'sphinx.ext.extlinks',
    'sphinx.ext.ifconfig',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinx.ext.graphviz',
    'sphinx.ext.imgconverter',
    'sphinxcontrib.doxylink',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = [ '.rst',
# '.md',
]

# Source parsers
source_parsers = {
#   '.md': 'recommonmark.parser.CommonMarkParser',
}


# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', '_deploy', 'Thumbs.db', '.DS_Store', '**/_docs', 'global.rst',
#  'users-guide/**',
#  'developers-guide/**',
  'showcases/**',
  'tutorials/**',
  'reference/**',
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# graphviz options
graphviz_output_format = 'svg'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'sphinx_materialdesign_theme'
html_theme = "sphinx_rtd_theme"
# html_theme_path = ['_templates']


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# read the docs config
html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
#    'vcs_pageview_mode': '',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': False,
    'navigation_depth': 3,
    'includehidden': False,
    'titles_only': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

#html_extra_path = ['.']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'INETFrameworkdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'INETFramework.tex', 'INET Framework Documentation',
     'OpenSim Ltd.', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'inetframework', 'INET Framework Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'INETFramework', 'INET Framework Documentation',
     author, 'INETFramework', 'One line description of project.',
     'Miscellaneous'),
]

# -- Doxylink config ---------------------------------------------------------

#doxylink = {
#        'cpp' : ('_static/reference/doxytags.xml', '_static/reference/cpp/'),
#        'ned' : ('_static/reference/nedtags.xml', '_static/reference/ned/'),
#}

# -- Extension configuration -------------------------------------------------
rst_prolog = open('global.rst', 'r').read()

todo_include_todos = True
todo_emit_warnings = False

def opp_preprocess(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.
    """
    # Make sure we're outputting HTML
    if app.builder.format != 'html':
        return
    src = source[0]

    # implicitly import global macros in into the opp namespace at the beginning of each source file
    src = "{% import 'global-macros.inc' as opp %}\n" + src

    # run the templating engine on the source file
    rendered = app.builder.templates.render_string(
        src, app.config.html_context
    )
    source[0] = rendered

###########################################################################
# pygments
from pygments.lexer import RegexLexer, bygroups, words
from pygments.token import Name, Keyword, Comment, Text, Operator, String
from sphinx.highlighting import lexers

# keywords not yet fully working. Model it after the C lexer in pygments:
class MsgLexer(RegexLexer):
    name = 'msg'
    filenames = ['*.msg']

    tokens = {
        'root': [
            (r'extends', Keyword),
            (r'\w+', Keyword),
            (r'[^/]+', Text),
            (r'/\*', Comment.Multiline, 'comment'),
            (r'//.*?$', Comment.Singleline),
            (r'/', Text)
        ],
        'comment': [
            (r'[^*/]', Comment.Multiline),
            (r'/\*', Comment.Multiline, '#push'),
            (r'\*/', Comment.Multiline, '#pop'),
            (r'[*/]', Comment.Multiline)
        ],
    }

lexers['msg'] = MsgLexer(startinline=True)

class IniLexer(RegexLexer):
    name = 'OMNeT++ Ini File'
    aliases = ['ini']
    filenames = ['*.ini']

    tokens = {
        'root': [
            (r'\s+', Text),
            (r';.*?$', Comment),
            (r'\[.*?\]$', Keyword),
            (r'(.*?)(\s*)(=)(\s*)(.*?)$',
             bygroups(Name.Attribute, Text, Operator, Text, String))
        ],
    }

lexers['OppIni'] = IniLexer(startinline=True)

#######################################################################
# -- setup the customizations
import tools.video

def setup(app):
    app.connect("source-read", opp_preprocess)
    app.add_directive('youtube', tools.video.Youtube)
    app.add_directive('vimeo', tools.video.Vimeo)
    app.add_directive('video', tools.video.Video)

