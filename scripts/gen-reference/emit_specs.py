import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import specs as S
out = []
for typ in ("POINT","LINE","CIRCLE","POLYGON","SECTOR","PLANE","SPHERE","POLYHEDRON"):
    for name, entry in getattr(S, typ).items():
        els = entry[0]
        w, h = entry[2] if len(entry) > 2 else (260, 200)
        out.append({"id": "c_%s_%s" % (typ.lower(), name), "w": w, "h": h, "elements": els})
json.dump(out, open(sys.argv[1], "w"), indent=1)
print("%d specs" % len(out))
