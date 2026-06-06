"""Register text/html for the numeric and Roman-numeral pseudo-extensions
our dotted def-slugs produce.

Our Book X definition folders use Heath/Joyce subsection-restart numbering
in the slug itself — defX.I, defX.II, defX.III for the bundle pages and
defX.I.1 … defX.III.6 for the leaves. The URL's last segment ends in
`.I`, `.II`, `.III`, or a digit (.1 … .6), which Python's `mimetypes`
module doesn't recognise. Lektor's filecontents.py then falls back to
`application/octet-stream` (see filecontents.py:14), and the dev server
serves index.html with that Content-Type — the browser treats it as a
download instead of rendering it.

This plugin runs `mimetypes.add_type(text/html, ext)` for each of those
pseudo-extensions at Lektor startup, so the dev server labels the
responses correctly.

Scope: process-local. Doesn't touch the OS mimetype DB. Production
deployments (nginx / Apache) serve `index.html` directly and aren't
affected by this filename-extension guess at all.

If a future work adds more subsection depth (X.IV.7 etc.) extend
ROMAN_EXTS / DIGIT_EXTS below.
"""
import mimetypes

from lektor.pluginsystem import Plugin


ROMAN_EXTS = (".I", ".II", ".III", ".IV", ".V", ".VI", ".VII", ".VIII",
              ".IX", ".X", ".XI", ".XII", ".XIII")
DIGIT_EXTS = tuple(f".{n}" for n in range(1, 10))


class RomanSlugMimetypesPlugin(Plugin):
    name = "Roman-slug mimetypes"
    description = "Make Lektor serve defX.I.1/, defX.II.3/, etc. as text/html instead of octet-stream."

    def on_setup_env(self, **extra):
        for ext in ROMAN_EXTS + DIGIT_EXTS:
            mimetypes.add_type("text/html", ext)
