/* "Source" control for the reference-page figure cards.
 *
 * Every card already carries a working figure — a <canvas> plus the inline
 * <script> that built it. So the source doesn't need to be duplicated into
 * the page as data: it IS the page. This reads the card's own canvas and
 * script back out of the DOM and shows the runnable file they add up to.
 *
 * From there, "Open in CodePen" hands that same source to CodePen's prefill
 * endpoint. Prefill is a plain form POST of a JSON blob — nothing is uploaded
 * anywhere first, no account or API key is involved, and the reader lands in
 * an editable pen. It has to be a POST rather than a link because the source
 * is far past a usable URL length.
 */
(function () {
    "use strict";

    var CODEPEN = "https://codepen.io/pen/define";

    // The bundle this page is actually running, so a pen opened from here
    // pins the same version the figure above it was verified against.
    function bundleUrl() {
        var meta = document.querySelector('meta[name="geomlib-version"]');
        var ver = meta ? meta.getAttribute("content") : "";
        var cdn = "https://cdn.jsdelivr.net/npm/@brownnrl/geomlib" +
                  (ver ? "@" + ver : "") + "/dist/bundle.js";
        var s = document.querySelector('script[src*="geomlib"]');
        if (!s) return cdn;
        // On the dev server the bundle is local (/geomlib-dev.js). A pen
        // can't reach that, so always hand out the CDN copy of the same
        // version rather than a same-origin path.
        var url = new URL(s.src, location.href);
        return url.host === location.host ? cdn : url.href;
    }

    function partsFor(card) {
        var canvas = card.querySelector("canvas");
        var script = card.querySelector("figure script");
        if (!canvas || !script) return null;
        var w = canvas.getAttribute("width"), h = canvas.getAttribute("height");
        return {
            title: (card.querySelector("h3") || {}).textContent || "geomlib figure",
            html: '<canvas id="' + canvas.id + '" width="' + w + '" height="' + h +
                  '" tabindex="0"></canvas>',
            js: script.textContent.replace(/^\n+|\s+$/g, ""),
            bundle: bundleUrl()
        };
    }

    function fullPage(p) {
        return '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n' +
               '<title>' + p.title + '</title>\n' +
               '<script src="' + p.bundle + '"><\/script>\n' +
               '</head>\n<body>\n' + p.html + '\n<script>\n' +
               p.js.replace(/^/gm, "") + '\n<\/script>\n</body>\n</html>\n';
    }

    var dialog = null, current = null;

    function ensureDialog() {
        if (dialog) return dialog;
        dialog = document.createElement("dialog");
        dialog.className = "ctor-source-dialog";
        dialog.innerHTML =
            '<h4 class="ctor-source-title"></h4>' +
            '<p class="ctor-source-lead">A complete, self-contained page. Save it as ' +
            '<code>.html</code> and open it — no build step.</p>' +
            '<pre class="ctor-source-code"><code></code></pre>' +
            '<div class="ctor-source-actions">' +
            '<button type="button" data-act="copy">Copy</button>' +
            '<button type="button" data-act="pen">Open in CodePen</button>' +
            '<button type="button" data-act="close">Close</button>' +
            '</div>';
        document.body.appendChild(dialog);

        dialog.addEventListener("click", function (e) {
            var b = e.target.closest("button[data-act]");
            // Clicking the backdrop lands on the dialog itself, not a child.
            if (!b) { if (e.target === dialog) dialog.close(); return; }
            var act = b.getAttribute("data-act");
            if (act === "close") { dialog.close(); return; }
            if (act === "copy") {
                var text = dialog.querySelector("code").textContent;
                var done = function () { b.textContent = "Copied"; setTimeout(function () { b.textContent = "Copy"; }, 1400); };
                if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, function () {});
                else {
                    var ta = document.createElement("textarea");
                    ta.value = text; document.body.appendChild(ta); ta.select();
                    try { document.execCommand("copy"); done(); } catch (_) {}
                    document.body.removeChild(ta);
                }
                return;
            }
            if (act === "pen" && current) openPen(current);
        });
        return dialog;
    }

    function openPen(p) {
        var data = {
            title: "geomlib — " + p.title,
            description: "Live example from Euclid's Elements: " +
                         "https://www.euclids-elements.org/geomlib/constructions/",
            html: p.html,
            js: p.js,
            js_external: p.bundle,
            editors: "1010"   // HTML + JS open, CSS collapsed
        };
        var form = document.createElement("form");
        form.method = "POST";
        form.action = CODEPEN;
        form.target = "_blank";
        form.rel = "noopener";
        var input = document.createElement("input");
        input.type = "hidden";
        input.name = "data";
        // Plain JSON. CodePen's docs show the quotes escaped as &quot;, but
        // that is only because their example writes the JSON into an HTML
        // value="" attribute. Setting .value through the DOM takes the
        // string verbatim, so escaping here would send corrupt JSON.
        input.value = JSON.stringify(data);
        form.appendChild(input);
        document.body.appendChild(form);
        form.submit();
        document.body.removeChild(form);
    }

    document.addEventListener("click", function (e) {
        var btn = e.target.closest(".ctor-src");
        if (!btn) return;
        var card = btn.closest(".ctor-card");
        if (!card) return;
        var p = partsFor(card);
        if (!p) return;
        current = p;
        var d = ensureDialog();
        d.querySelector(".ctor-source-title").textContent = p.title;
        d.querySelector("code").textContent = fullPage(p);
        if (d.showModal) d.showModal(); else d.setAttribute("open", "");
    });
})();
