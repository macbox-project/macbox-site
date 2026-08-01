# classicbox-site

The ClassicBox website — <https://classic.box>.

Sphinx + the Read the Docs theme, built and published to GitHub Pages by
`.github/workflows/pages.yml` on every push to `main`.

This is a **separate repo** that lives inside the `classicbox-notes` working tree
(`/website/` is in the notes `.gitignore`). Commit it from inside itself:
`git -C website ...` — never `git add` it from notes.

## Build locally

```bash
python -m venv .venv
.venv/Scripts/activate        # Windows;  source .venv/bin/activate elsewhere
pip install -r requirements.txt
sphinx-build -b html docs docs/_build/html
```

Then open `docs/_build/html/index.html`.

## Writing pages

Pages are MyST Markdown (`.md`) in `docs/`, compiled to HTML by Sphinx. Every
`.md` under `docs/` becomes a page on the live site — which is why this file
sits at the repo root instead.

List a new page in the `toctree` in `docs/index.md` to put it in the nav. If a
page is deliberately unlinked, give it `orphan: true` front matter so the build
stays warning-free (see `docs/layout-template.md`).

**This repo is public — anything committed is published.** Own screenshots,
terminal output and diagrams are fine; game and Mac OS artwork is not.

### Images

Sphinx only copies images it tracks, so the right directory depends on how the
image is referenced:

| Referenced from | File goes in | Written as |
| --- | --- | --- |
| Markdown, `{image}`, `{figure}` | `docs/images/` | `images/foo.png` |
| Raw HTML | `docs/_static/` | `_static/foo.png` |

Raw-HTML `<img>` paths are **not** rewritten, so an image in `docs/images/`
referenced from raw HTML 404s silently.

### Side-by-side image and code

Full working example in `docs/layout-template.md`, live at
`/layout-template.html`.

````markdown
Text above, full width.

:::{container} side-by-side

```{image} images/shot.png
```

```python
code()   # right column, keeps syntax highlighting
```

:::

Text beneath, full width.
````

First child is the left column, second is the right — swap them to put code on
the left, or use two images for a before/after. Collapses to one column under
900px. Styling lives in `docs/_static/custom.css`.

It uses the `container` directive rather than a raw HTML `<div>` because raw
HTML bypasses Pygments, so a hand-written `<pre>` gets no highlighting. The
`:::` form needs `myst_enable_extensions = ["colon_fence"]` (already set in
`docs/conf.py`); without it `:::{container}` renders as literal text.

## Domain

`docs/_extra/CNAME` holds the custom domain. Sphinx copies everything in
`_extra/` verbatim to the root of the built site, so that file lands at `/CNAME`,
which is what GitHub Pages reads. Changing the domain means editing that file
**and** `html_baseurl` in `docs/conf.py`, then updating DNS.
