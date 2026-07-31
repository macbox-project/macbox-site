# Sphinx configuration for the ClassicBox site (https://classic.box).
#
# Built and deployed by .github/workflows/pages.yml on every push to main.
# Build it locally the same way CI does:
#     sphinx-build -b html docs docs/_build/html

project = "ClassicBox"
author = "John Ballentine"
copyright = "2026, John Ballentine"

extensions = [
    # Writes the .nojekyll file into the build output. Without it GitHub Pages
    # runs Jekyll over the site, and Jekyll silently drops every path starting
    # with an underscore -- which is all of Sphinx's output (_static/, etc.).
    "sphinx.ext.githubpages",
    # Lets pages be written as Markdown (.md) instead of reStructuredText.
    "myst_parser",
]

html_theme = "sphinx_rtd_theme"
html_title = "ClassicBox"

# Absolute URLs in sitemap/canonical links. Must match the domain in _extra/CNAME.
html_baseurl = "https://classic.box/"

html_static_path = ["_static"]
templates_path = ["_templates"]

# Everything in _extra/ is copied verbatim to the ROOT of the built site.
# That is how docs/_extra/CNAME becomes /CNAME, which is the file GitHub Pages
# reads to learn the custom domain.
html_extra_path = ["_extra"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
