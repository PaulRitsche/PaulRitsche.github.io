# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Website"
copyright = "2023, Paul Ritsche"
author = "Paul Ritsche"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "furo"
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#19747E",
        "color-brand-content": "#19747E",
        "color-admonition-background": "#C4C5BA",
        "color-foreground-primary": "black",
        "color-foreground-secondary": "#5a5c63",
        "color-background-primary": "#D1E8E2",
        "color-background-secondary": "white",
        "color-background-border": "black",
        "color-foreground-border": "black",
    },
    "sidebar_hide_name": True,
}

html_logo = "./figures_main/profile_image.jpg"
