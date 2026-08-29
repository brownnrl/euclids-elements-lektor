// Render every figure on one content page, straight from its inline scripts,
// and flag any whose ink touches the canvas border.
const fs = require("fs"), path = require("path"), vm = require("vm");
const { createCanvas } = require("canvas");
const EUCLID = process.env.EUCLID_REPO || "/data-mirrored/projects/geometry/euclid";
const bundle = fs.readFileSync(path.join(EUCLID, "dist/bundle.js"), "utf-8");
const LR = process.argv[2], OUT = process.argv[3];
fs.mkdirSync(OUT, { recursive: true });
const text = fs.readFileSync(LR, "utf-8");

const figs = [];
const figRe = /<figure[^>]*>([\s\S]*?)<\/figure>/g;
let fm;
while ((fm = figRe.exec(text)) !== null) {
    const block = fm[1];
    const c = block.match(/<canvas id="([^"]+)" width="(\d+)" height="(\d+)"/);
    const js = block.match(/<script[^>]*>([\s\S]*?)<\/script>/);
    if (c && js) figs.push({ id: c[1], w: +c[2], h: +c[3], js: js[1] });
}

let bad = 0;
for (const f of figs) {
    const canvases = {};
    const doc = {
        getElementById(id) {
            if (!canvases[id]) {
                const c = createCanvas(f.w, f.h);
                c.style = {}; c.clientWidth = f.w; c.clientHeight = f.h;
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
    vm.runInContext(bundle, s, { filename: "bundle" });

    const problems = [];
    try { vm.runInContext(f.js, s, { filename: f.id, timeout: 10000 }); }
    catch (e) { problems.push("THREW: " + String(e).slice(0, 200)); }
    let diags = { slates: [] };
    try { diags = s.geomlib.diagnostics(); } catch (_) {}
    for (const sl of diags.slates || [])
        for (const e of sl.entries) problems.push(`[${e.severity}] ${e.code}: ${e.message}`);

    const c = doc.getElementById(f.id);
    try {
        const d = c.getContext("2d").getImageData(0, 0, f.w, f.h).data;
        const bg0 = d[0], bg1 = d[1], bg2 = d[2];
        let x0 = f.w, y0 = f.h, x1 = -1, y1 = -1;
        for (let y = 0; y < f.h; y++) for (let x = 0; x < f.w; x++) {
            const i = (y * f.w + x) * 4;
            if (Math.abs(d[i] - bg0) < 6 && Math.abs(d[i+1] - bg1) < 6 &&
                Math.abs(d[i+2] - bg2) < 6) continue;
            if (x < x0) x0 = x; if (x > x1) x1 = x;
            if (y < y0) y0 = y; if (y > y1) y1 = y;
        }
        const edges = [];
        if (x0 <= 1) edges.push("left"); if (y0 <= 1) edges.push("top");
        if (x1 >= f.w - 2) edges.push("right"); if (y1 >= f.h - 2) edges.push("bottom");
        if (edges.length) problems.push(`CLIPPED at ${edges.join(",")} (ink ${x0},${y0}..${x1},${y1})`);
        fs.writeFileSync(path.join(OUT, f.id + ".png"), c.toBuffer("image/png"));
    } catch (e) { problems.push("render failed: " + e.message); }

    if (problems.length) { bad++; console.log("FAIL " + f.id); for (const p of problems) console.log("      " + p); }
    else console.log("ok   " + f.id);
}
process.exit(bad ? 1 : 0);
