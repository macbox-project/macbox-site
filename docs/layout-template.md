---
orphan: true
---

# Layout template

Copy this file when you want the image-beside-code shape. Everything below is
the pattern; swap the image and the code for your own.

---

## Text above

Ordinary paragraph text sits above the pair. Use it to say what the reader is
about to look at, so the image and the code have context before they arrive
rather than after.

:::{container} side-by-side

```{image} images/placeholder-screenshot.svg
:alt: swap this for your own screenshot
```

```python
# Right column: a real code block, so it keeps
# syntax highlighting. Comments carry the
# explanation that pairs with the image.
def fade(frames):
    for i, f in enumerate(frames):
        # the sprite is still in the buffer here
        yield blend(f, alpha=1 - i / len(frames))
```

:::

## Text beneath

And ordinary text continues underneath, at full width. This is the place for
the conclusion the pair was building toward — what the image and the code
together actually showed.

---

## How it works

Three pieces:

`:::{container} side-by-side` opens a `<div class="side-by-side">`. The triple
colons mean "this directive has nested content", so everything until the closing
`:::` is parsed as normal Markdown — which is why the code block below it is a
real code block and keeps its highlighting.

The **first** child lands in the left column, the **second** in the right. Two
children, two columns. Add a third and it will overflow the grid, so keep it to
a pair.

`docs/_static/custom.css` defines the grid and collapses it to a single column
below 900px wide, so it reads fine on a phone.

### Swapping the sides

Nothing is hardcoded about which side gets what. Put the code block first and
the image second, and the code is on the left.

### Two images instead

The same container works for a before/after pair — two `{image}` blocks rather
than an image and a code block.
