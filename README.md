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

## Domain

`docs/_extra/CNAME` holds the custom domain. Sphinx copies everything in
`_extra/` verbatim to the root of the built site, so that file lands at `/CNAME`,
which is what GitHub Pages reads. Changing the domain means editing that file
**and** `html_baseurl` in `docs/conf.py`, then updating DNS.
