#!/usr/bin/env python3
"""Flag slide captions that paraphrase the proof instead of carrying it.

A caption walking a step of a proof must be Joyce's own sentence, tokenized —
see doc/process.md, "Captions carry Joyce's sentence, not a paraphrase of it".
Splitting one of his sentences across several slides is not only allowed but
preferred; compressing several into a summary is not.

That distinction is what this checks. A legitimate split leaves the caption's
words an in-order run of the proof's word stream; a paraphrase does not. A
naive similarity score cannot tell them apart — it marks every correct split
as suspect, which is how a first pass here accused five propositions that
turned out to be clean.

Captions that are legitimately ours — the "Let ... be ..." and "I say that ..."
beats, a closing summary, bracketed asides — are not exempt by rule, but they
usually score high anyway because Joyce's own text opens the same way.

KNOWN LIMITATION: this catches words a caption CHANGED or INVENTED, not words
it OMITTED. Dropping a word leaves the rest a perfectly good in-order run, so
II.5 slide 4 lost both of Joyce's "again"s at a clean 100%. Detecting that
needs the caption aligned to the passage it walks, and every cheap way of
guessing that passage — first occurrence of each word, a fixed-size window,
best-matching run of sentences — misfires badly enough to flag captions that
are correct. A noisy check is worse than a narrow one, so this stays narrow.
Omissions are caught by reading the diff against the proof body.

Usage:  python3 scripts/check-captions.py [bookII ...]
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
THRESHOLD = 0.92

TOKEN = re.compile(r"\{([A-Za-z][A-Za-z0-9']*)(?:\|[^}]*)?(?::canvas[^}]*)?\}")


def words(text):
    text = TOKEN.sub(r"\1", text)
    text = re.sub(r"\[!just[^\]]*\]", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.findall(r"[a-z0-9']+", text.lower())


def in_order_fraction(caption_words, proof_words):
    """How much of the caption appears, in order, in the proof."""
    j = matched = 0
    for w in caption_words:
        try:
            k = proof_words.index(w, j)
        except ValueError:
            continue
        j, matched = k + 1, matched + 1
    return matched / len(caption_words)


def check(path):
    s = open(path, encoding="utf-8").read()
    if "slides:" not in s:
        return []
    captions = re.findall(r'\{ text: "((?:[^"\\]|\\.)*)"', s)
    # Compare against proof AND guide. A page may carry a second deck on a
    # guide canvas (the I.20 / I.47 exception), and those captions track the
    # guide's prose — matching them against the proof alone marks every one
    # of them as paraphrase. The guide is also held looser by process.md, so
    # a hit there is a prompt to look, not a defect.
    body = s.split("----\nproof:", 1)[-1]
    body = re.sub(r"<script[\s\S]*?</script>", " ", body)
    proof = words(body)
    out = []
    for i, c in enumerate(captions, 1):
        cw = words(c)
        if not cw:
            continue
        frac = in_order_fraction(cw, proof)
        if frac < THRESHOLD:
            out.append((i, frac, " ".join(cw)))
    return out


def main():
    books = sys.argv[1:] or ["bookII"]
    total = pages = 0
    for book in books:
        base = os.path.join(ROOT, "content/elements/books", book, "propositions")
        for prop in sorted(os.listdir(base)) if os.path.isdir(base) else []:
            path = os.path.join(base, prop, "contents.lr")
            if not os.path.exists(path):
                continue
            bad = check(path)
            if not bad:
                continue
            pages += 1
            total += len(bad)
            print("%s  (%d)" % (prop, len(bad)))
            for i, frac, text in bad:
                print("    slide %-3d %3.0f%%  %s" % (i, frac * 100, text[:88]))
    print("\ncaptions not carried from the proof: %d, across %d propositions" % (total, pages))
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
