# Sphinx configuration for the ClassicBox site (https://classic.box).
#
# Built and deployed by .github/workflows/pages.yml on every push to main.
# Build it locally the same way CI does:
#     sphinx-build -b html docs docs/_build/html

project = "ClassicBox"
author = "John Ballentine"

# No copyright line in the footer. Sphinx only renders one when this is True,
# so there is no `copyright` value to keep in sync.
html_show_copyright = False

extensions = [
    # Writes the .nojekyll file into the build output. Without it GitHub Pages
    # runs Jekyll over the site, and Jekyll silently drops every path starting
    # with an underscore -- which is all of Sphinx's output (_static/, etc.).
    "sphinx.ext.githubpages",
    # Lets pages be written as Markdown (.md) instead of reStructuredText.
    "myst_parser",
]

# colon_fence enables the ::: form of a directive. Needed because a ``` fenced
# directive cannot contain a ``` code block without escalating backtick counts;
# ::: nests around ``` cleanly, which is what the side-by-side layout needs.
# Without this, ":::{container}" renders as literal paragraph text.
myst_enable_extensions = ["colon_fence"]

html_theme = "sphinx_rtd_theme"
html_title = "ClassicBox"

# Absolute URLs in sitemap/canonical links. Must match the domain in _extra/CNAME.
html_baseurl = "https://classic.box/"

html_static_path = ["_static"]
templates_path = ["_templates"]

# Loaded on every page, from _static/. Defines the .side-by-side grid.
html_css_files = ["custom.css"]

# Everything in _extra/ is copied verbatim to the ROOT of the built site.
# That is how docs/_extra/CNAME becomes /CNAME, which is the file GitHub Pages
# reads to learn the custom domain.
html_extra_path = ["_extra"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
