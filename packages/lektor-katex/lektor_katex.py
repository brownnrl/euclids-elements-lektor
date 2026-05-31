"""Build-time KaTeX rendering hooked into Lektor's Mistune renderer.

Authoring syntax (in any markdown body / proof field):

    <div class="math display">…TeX…</div>      block / displayed math
    <span class="math">…TeX…</span>             inline math

Mistune's `block_html` / `inline_html` hooks pass these through verbatim.
This plugin's renderer mixin intercepts them, shells out to Node + KaTeX
via `scripts/render-katex.js`, and substitutes the rendered HTML.

The TeX content is cached per-process so that incremental rebuilds
(`lektor server`) don't re-spawn Node for unchanged blocks.
"""
import os
import re
import subprocess
from pathlib import Path

from lektor.pluginsystem import Plugin


BLOCK_RE = re.compile(
    r'^<div\s+class="math display">(.*?)</div>\s*$', re.DOTALL | re.IGNORECASE
)
INLINE_RE = re.compile(
    r'^<span\s+class="math">(.*?)</span>\s*$', re.DOTALL | re.IGNORECASE
)

# Per-process cache: tex string + display-mode flag → rendered HTML.
_cache: dict = {}


def _project_root() -> Path:
    # This file: packages/lektor-katex/lektor_katex.py
    # Project root: two levels up.
    return Path(__file__).resolve().parent.parent.parent


def _node_script() -> Path:
    return _project_root() / "scripts" / "render-katex.js"


def _node_binary() -> str:
    # Prefer the user's nvm Node if present; fall back to system node.
    nvm_node = os.path.expanduser("~/.nvm/versions/node/v24.14.1/bin/node")
    if Path(nvm_node).exists():
        return nvm_node
    return "node"


def render_tex(tex: str, display: bool) -> str:
    key = (tex, display)
    if key in _cache:
        return _cache[key]
    args = [_node_binary(), str(_node_script())]
    if display:
        args.append("--display")
    try:
        result = subprocess.run(
            args, input=tex, capture_output=True, text=True, timeout=15
        )
    except Exception as e:  # node missing, timeout, etc.
        html = (
            '<span class="katex-error" style="color:#cc0000">'
            f"KaTeX render failure: {e}</span>"
        )
        _cache[key] = html
        return html
    html = result.stdout
    _cache[key] = html
    return html


class KatexRendererMixin:
    """Mixed into Lektor's Mistune Renderer via on_markdown_config."""

    def block_html(self, html):
        m = BLOCK_RE.match(html.strip())
        if m:
            return render_tex(m.group(1).strip(), display=True)
        return super().block_html(html)

    def inline_html(self, html):
        m = INLINE_RE.match(html.strip())
        if m:
            return render_tex(m.group(1).strip(), display=False)
        return super().inline_html(html)


class KatexPlugin(Plugin):
    name = "KaTeX"
    description = "Build-time KaTeX rendering for <div class='math'> blocks."

    def on_markdown_config(self, config, **extra):
        config.renderer_mixins.append(KatexRendererMixin)
