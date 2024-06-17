# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Website"
copyright = "2024, Paul Ritsche"
author = "Paul Ritsche"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# 📚 Extensions to be used by Sphinx
extensions = [
    "sphinx.ext.autodoc",  # Automatically generate documentation
    "sphinx.ext.napoleon",  # Support for NumPy and Google style docstrings
    "sphinx.ext.viewcode",  # Add links to highlighted source code
    "sphinx_copybutton",  # Add a "copy" button to code blocks
    "sphinx.ext.mathjax",  # Render mathematical expressions
    # "sphinx_panels",  # Create panels for a more dynamic layout
    "sphinxemoji.sphinxemoji",  # Adds embedded emojis
]

# 📂 Paths to templates
templates_path = ["_templates"]

# ❌ Patterns to exclude from the build
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# html_theme = "furo"
# html_theme_options = {
#     "light_css_variables": {
#         "color-brand-primary": "#19747E",
#         "color-brand-content": "#19747E",
#         "color-admonition-background": "#C4C5BA",
#         "color-foreground-primary": "black",
#         "color-foreground-secondary": "#5a5c63",
#         "color-background-primary": "#D1E8E2",
#         "color-background-secondary": "white",
#         "color-background-border": "black",
#         "color-foreground-border": "black",
#     },
#     "sidebar_hide_name": True,
# }


# -- Options for HTML Output -------------------------------------------------
# Reference: https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# 🎨 Choosing the theme for HTML documentation
html_theme = "furo"

# 🌈 Custom theme options for a unique and scientifically inspired look
html_theme_options = {
    "light_css_variables": {
        # 🔵 Primary brand color
        "color-brand-primary": "#19747E",
        # 🔵 Content brand color
        "color-brand-content": "#19747E",
        # 🟢 Background color for admonitions
        "color-admonition-background": "#C4C5BA",
        # ⚫ Primary foreground color (text)
        "color-foreground-primary": "black",
        # ⚪ Secondary foreground color (subdued text)
        "color-foreground-secondary": "#5a5c63",
        # 🟢 Primary background color
        "color-background-primary": "#D1E8E2",
        # ⚪ Secondary background color
        "color-background-secondary": "white",
        # ⚫ Border color for backgrounds
        "color-background-border": "black",
        # ⚫ Border color for foreground elements
        "color-foreground-border": "black",
    },
    # 🔒 Hide the project name in the sidebar for a cleaner look
    "sidebar_hide_name": True,
}

html_logo = "./figures_main/profile_image.jpg"

# -- Paths for Custom Static Files -------------------------------------------
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the built-in static files,
# so a file named "default.css" will overwrite the built-in "default.css".
html_static_path = ["_static"]


# Custom CSS file to further style the documentation
def setup(app):
    app.add_css_file("custom.css")


# Custom JavaScript for additional functionality
html_js_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js",  # jQuery for additional JS functionality
    "custom.js",  # Your custom JavaScript
]

# -- Custom Widgets and Features -------------------------------------------------
# YouTube Embedding Example
youtube_video = """
.. youtube:: https://www.youtube.com/watch?v=dQw4w9WgXcQ
   :width: 100%
   :align: center
"""

# Using Panels for a Dynamic Layout
dynamic_panel = """
.. panels::
   :column: 3

   **Analysis** 📊
   ^^^
   Learn more about the comprehensive analysis techniques.

   **Research** 🔬
   ^^^
   Discover our groundbreaking research in the field.

   **Community** 👥
   ^^^
   Join our vibrant community of scientists and researchers.
"""

# MathJax for Mathematical Expressions
math_expression = """
.. math::

   E = mc^2
"""

# -- Extension Configuration -------------------------------------------------
# Configuration for the Napoleon extension (supporting NumPy and Google style docstrings)
napoleon_google_docstring = False
napoleon_numpy_docstring = True

# Configuration for Panels extension
panels_add_bootstrap_css = False

# -----------------------------------------------------------------------------
# 🚀 End of Configuration - Let's build some amazing documentation! 🚀
# -----------------------------------------------------------------------------
