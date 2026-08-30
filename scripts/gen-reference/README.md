# Reference-page generators

Two pages under `/geomlib/` are generated rather than hand-written, because
each is one repeated shape filled in many times and both must stay in step with
the library:

| Page | Generator | Figure specs |
|---|---|---|
| `/geomlib/constructions/` | `build_page.py` | `specs.py` |
| `/geomlib/animations/` | `build_animations.py` | `anims.py` |

`build_page.py` reads signatures and descriptions out of the library's own
`doc/constructions-reference.md` instead of restating them, and prints a
coverage report of any construction in that table without a figure here.

Edit the spec files, never the generated `contents.lr`:

```sh
python scripts/gen-reference/build_page.py
python scripts/gen-reference/build_animations.py
```

## Checking the figures before they ship

A figure can be valid geometry and still be unreadable — a square whose derived
corner lands past the canvas edge raises no error and simply gets cut off. The
two probes catch that by rendering to a bitmap and looking at the pixels: they
run each figure against the real bundle, report the library's own diagnostics,
then scan for ink touching the canvas border.

```sh
python scripts/gen-reference/emit_specs.py /tmp/specs.json
NODE_PATH=../euclid/node_modules node scripts/gen-reference/probe.js /tmp/specs.json /tmp/png

# any content page, straight from its inline figure scripts
NODE_PATH=../euclid/node_modules node scripts/gen-reference/probe-page.js \
    content/geomlib/animations/contents.lr /tmp/png
```

Both need `node-canvas`, which comes from the geomlib checkout, and both write
a PNG per figure so a contact sheet can be built with `montage`.
