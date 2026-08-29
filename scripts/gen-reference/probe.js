// Probe one figure spec against the real bundle: reports init errors,
// #154 diagnostics, and each element's computed on-screen position so a
// derived point that lands off-canvas is visible before it ships.
const fs = require("fs"), path = require("path"), vm = require("vm");
const { createCanvas } = require("canvas");
const EUCLID = process.env.EUCLID_REPO || "/data-mirrored/projects/geometry/euclid";
const bundle = fs.readFileSync(path.join(EUCLID, "dist/bundle.js"), "utf-8");

function sandboxFor(w, h) {
    const canvases = {};
    const doc = {
        getElementById(id) {
            if (!canvases[id]) {
                const c = createCanvas(w, h);
                c.style = {}; c.clientWidth = w; c.clientHeight = h;
                c.getAttribute = () => null; c.setAttribute = () => {};
                c.addEventListener = () => {}; c.removeEventListener = () => {};
                c.dispatchEvent = () => true; c.parentElement = null; c.id = id;
                canvases[id] = c;
            }
            return canvases[id];
        },
        createElement: () => ({ style: {}, setAttribute() {}, appendChild() {},
                                addEventListener() {}, getContext: () => null }),
        head: { appendChild() {} }, documentElement: { appendChild() {} },
        addEventListener() {},
    };
    const s = { console: { log(){}, warn(){}, error(){}, info(){} }, document: doc,
        navigator: { userAgent: "node" }, setTimeout, clearTimeout, Math, Date, JSON,
        Object, Array, String, Number, RegExp, Error, TypeError, Map, Set, WeakMap,
        isNaN, parseFloat, parseInt };
    s.window = s; s.globalThis = s;
    s.matchMedia = () => ({ matches: false });
    s.requestAnimationFrame = () => 0; s.cancelAnimationFrame = () => {};
    vm.createContext(s);
    vm.runInContext(bundle, s, { filename: "geomlib-bundle.js" });
    return s;
}

const specs = JSON.parse(fs.readFileSync(process.argv[2], "utf-8"));
const PNGDIR = process.argv[3] || null;
if (PNGDIR) fs.mkdirSync(PNGDIR, { recursive: true });
let bad = 0;
for (const { id, w, h, elements, opts } of specs) {
    const s = sandboxFor(w, h);
    const canvasOf = (id) => s.document.getElementById(id);
    const problems = [];
    try {
        s.geomlib.init(Object.assign({ canvasid: id, background: "0,0,100", elements }, opts || {}));
    } catch (e) { problems.push("THREW: " + String(e).slice(0, 200)); }
    let diags = { slates: [] };
    try { diags = s.geomlib.diagnostics(); } catch (_) {}
    for (const sl of diags.slates || [])
        for (const e of sl.entries) problems.push(`[${e.severity}] ${e.code}: ${e.message}`);

    // Off-canvas check: a derived point that computes to a position outside
    // the canvas is a silently broken figure, not an error the library raises.
    const slate = (s.geomlib.slates || [])[0];
    const off = [];
    if (slate) {
        for (const el of (slate.elements || [])) {
            const p = el.x !== undefined ? { x: el.x, y: el.y } : null;
            if (p && (p.x < -6 || p.y < -6 || p.x > w + 6 || p.y > h + 6))
                off.push(`${el.name}@(${Math.round(p.x)},${Math.round(p.y)})`);
        }
    }
    const nEl = slate ? (slate.elements || []).length : 0;

    // Ink-based clipping check. The diagnostics can't see a square whose
    // derived corner lands past the canvas edge — but the pixels can. Scan
    // for non-background ink and flag anything touching the border.
    let clipped = null;
    try {
        const c = canvasOf(id);
        const d = c.getContext("2d").getImageData(0, 0, w, h).data;
        let x0 = w, y0 = h, x1 = -1, y1 = -1;
        for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) {
            const i = (y * w + x) * 4;
            if (d[i] > 245 && d[i+1] > 245 && d[i+2] > 245) continue;  // background
            if (x < x0) x0 = x; if (x > x1) x1 = x;
            if (y < y0) y0 = y; if (y > y1) y1 = y;
        }
        const edges = [];
        if (x0 <= 1) edges.push("left"); if (y0 <= 1) edges.push("top");
        if (x1 >= w - 2) edges.push("right"); if (y1 >= h - 2) edges.push("bottom");
        if (edges.length) clipped = edges.join(",") + ` (ink ${x0},${y0}..${x1},${y1})`;
    } catch (e) { /* no pixels available */ }
    if (PNGDIR) {
        try {
            const c = canvasOf(id);
            fs.writeFileSync(path.join(PNGDIR, id + ".png"), c.toBuffer("image/png"));
        } catch (e) { console.log("      png failed: " + e.message); }
    }
    if (clipped) problems.push("CLIPPED at " + clipped);
    if (problems.length) {
        bad++;
        console.log(`FAIL ${id}  (${nEl} elements)`);
        for (const p of problems) console.log("      " + p);
        if (off.length) console.log("      (offcanvas, informational): " + off.join(" "));
    } else {
        console.log(`ok   ${id}  (${nEl} elements)`);
    }
}
process.exit(bad ? 1 : 0);
