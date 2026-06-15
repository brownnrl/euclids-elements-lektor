// Euclid's Elements Lektor — element-reference hover/touch highlighting.
//
// Looks at every <span class="elem-ref" data-elem="NAME"> in the page
// (emitted by the eucref plugin's `{!NAME}` shortcode) and binds:
//   - mouseenter / mouseleave  →  hover-highlight on desktop
//   - pointerdown              →  sticky toggle for touch
// Each handler flips the corresponding geomlib element's `shouldHighlight`
// flag and calls `slate.update()` to redraw.  (text → canvas)
//
// Bidirectional binding (canvas → text), geomlib >= 0.11.0 (#108): geomlib
// dispatches a bubbling `geomlib:highlight` CustomEvent on a slate's canvas
// whenever its highlighted SET changes — from ANY source (a prose ref
// hover, a pin, or a slide's `highlighted` set). We listen per canvas and
// add `.lit` to EVERY prose ref whose element is in that set, so hovering
// one `{AB}` lights up the canvas AB *and* every other `{AB}` in the prose.
//   event.detail.highlighted: Array<{ name, aliases: string[] }>
//   (name = canonical element name; aliases = name + every alias for it)
//
// Target slate resolution (in order):
//   1. data-canvas="canvas_N"  →  exact id match
//   2. nearest enclosing div.theorem  →  first slate inside that section
//   3. fallback: geomlib.slates[0]
// If no slate in the chosen scope has an element of the requested name,
// console.warn once and skip binding (the span still renders as italic
// text but does nothing on hover).

(function () {
    "use strict";

    // Registry of successfully-bound spans, so the per-canvas
    // `geomlib:highlight` listener can find every span on a given slate.
    // Each entry: { span, slate, element }.
    var bound = [];
    // Slates that already have a `geomlib:highlight` listener attached.
    var listening = [];

    // Slate exposes a public `canvas` getter in geomlib >= 0.4.0; before
    // that the canvas was a `_canvas` private field. Fall back so this
    // glue works against either bundle.
    function slateCanvas(s) {
        return s && (s.canvas || s._canvas) || null;
    }

    function findSlateByCanvasId(id) {
        if (!window.geomlib || !window.geomlib.slates) return null;
        for (var i = 0; i < window.geomlib.slates.length; i++) {
            var s = window.geomlib.slates[i];
            var c = slateCanvas(s);
            if (c && c.id === id) return s;
        }
        return null;
    }

    // Rank candidate slates for a given span by DOM order:
    //   1. Slates whose canvas precedes the span — preferred, with the
    //      latest-preceding canvas first (the span is "talking about"
    //      the canvas right above it).
    //   2. Slates whose canvas follows the span — fallback for
    //      forward-reference cases (prose intro that names elements
    //      before the canvas appears).
    // Same span-then-section ordering gives the right answer on
    // multi-canvas pages like propI.1 (proof figure + Zeno guide
    // figure): a {NAME} after canvas_1 targets canvas_1, a {NAME}
    // before canvas_0 targets canvas_0.
    function rankSlatesByDomOrder(span) {
        if (!window.geomlib || !window.geomlib.slates) return [];
        var preceding = [];
        var following = [];
        for (var i = 0; i < window.geomlib.slates.length; i++) {
            var s = window.geomlib.slates[i];
            var c = slateCanvas(s);
            if (!c) continue;
            var pos = c.compareDocumentPosition(span);
            // DOCUMENT_POSITION_FOLLOWING = 4 means span follows canvas
            if (pos & 4) preceding.push({slate: s, idx: i});
            else following.push({slate: s, idx: i});
        }
        // preceding: latest first (closest to span)
        preceding.sort(function(a, b) { return b.idx - a.idx; });
        // following: earliest first
        following.sort(function(a, b) { return a.idx - b.idx; });
        return preceding.concat(following).map(function(x) { return x.slate; });
    }

    function resolveTarget(span) {
        var name = span.getAttribute("data-elem");
        var canvasId = span.getAttribute("data-canvas");
        if (!name) return null;

        // Explicit canvas selector wins.
        if (canvasId) {
            var s = findSlateByCanvasId(canvasId);
            if (!s) {
                console.warn("elem-ref: no canvas with id=" + canvasId
                             + " for {!" + name + ":" + canvasId + "}");
                return null;
            }
            var el = s.lookupElement(name);
            if (!el) {
                console.warn("elem-ref: canvas " + canvasId
                             + " has no element named '" + name + "'");
                return null;
            }
            return { slate: s, element: el };
        }

        // DOM-order resolution: try the latest preceding slate first,
        // then earlier ones, then any following slates.
        var ranked = rankSlatesByDomOrder(span);
        for (var i = 0; i < ranked.length; i++) {
            var found = ranked[i].lookupElement(name);
            if (found) return { slate: ranked[i], element: found };
        }

        console.warn("elem-ref: no element named '" + name + "' found on page");
        return null;
    }

    // Light up every prose ref on `slate` whose element is in the
    // highlighted set just reported by geomlib's `geomlib:highlight` event.
    function applyHighlightEvent(slate, ev) {
        var hl = (ev && ev.detail && ev.detail.highlighted) || [];
        var lit = {};   // set of highlighted names (canonical + aliases)
        for (var i = 0; i < hl.length; i++) {
            var h = hl[i];
            if (!h) continue;
            if (h.name) lit[h.name] = true;
            var al = h.aliases;
            if (al) for (var j = 0; j < al.length; j++) lit[al[j]] = true;
        }
        for (var k = 0; k < bound.length; k++) {
            var b = bound[k];
            if (b.slate !== slate) continue;
            b.span.classList.toggle("lit", !!lit[b.element.name]);
        }
    }

    // Attach the canvas → text listener once per slate.
    function ensureHighlightListener(slate) {
        if (listening.indexOf(slate) !== -1) return;
        var c = slateCanvas(slate);
        if (!c || typeof c.addEventListener !== "function") return;
        c.addEventListener("geomlib:highlight", function (ev) {
            applyHighlightEvent(slate, ev);
        });
        listening.push(slate);
    }

    function bindSpan(span) {
        var target = resolveTarget(span);
        if (!target) return;

        var slate = target.slate;
        var elem = target.element;
        bound.push({ span: span, slate: slate, element: elem });
        ensureHighlightListener(slate);

        function setHighlight(on) {
            elem.shouldHighlight = !!on;
            slate.update();
        }

        span.addEventListener("mouseenter", function () {
            if (!span.classList.contains("active")) setHighlight(true);
        });
        span.addEventListener("mouseleave", function () {
            if (!span.classList.contains("active")) setHighlight(false);
        });
        span.addEventListener("pointerdown", function (e) {
            // Toggle sticky state; useful for touch where there's no hover.
            // On mouse this is fine too — click to pin/unpin.
            var active = span.classList.toggle("active");
            setHighlight(active);
            e.preventDefault();
        });
    }

    function init() {
        var spans = document.querySelectorAll("span.elem-ref");
        var slateCount = (window.geomlib && window.geomlib.slates)
            ? window.geomlib.slates.length : 0;
        console.log("elem-ref: binding " + spans.length + " span(s) against "
                    + slateCount + " slate(s)");
        for (var i = 0; i < spans.length; i++) bindSpan(spans[i]);
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", function () {
            // Microtask so the inline <script>geomlib.init(...)</script>
            // tags inside each <figure> have actually run.
            setTimeout(init, 0);
        });
    } else {
        setTimeout(init, 0);
    }
})();
