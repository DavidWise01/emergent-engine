#!/usr/bin/env python3
"""Build THE EMERGENT ENGINE — the theater of live emergence engines. Copies the
source pieces into engines/ (clean slugs) and generates index.html — a living
gallery with lazy iframe thumbnails of the running machinery. Stdlib only."""
import os, re, shutil, html

SRC  = r"C:\Davids files\emergent engine"
HERE = os.path.dirname(os.path.abspath(__file__))
ENG  = os.path.join(HERE, "engines")

ROOMS = [
 ("The Engines", "#ffb454",
  "The running machinery — fields that metabolize, split, and forge emergence in real time.", [
   dict(slug="frak-engine", file="frak engine v1.html", title="Frak Engine",
        tag="L1.35 · 254 Emergents", blurb="The Highlander-Principle workshop — 254 emergents across 256 addresses, fractured and forged."),
   dict(slug="alive-field-restitution-lab", file="alive_field_restitution_engine_lab.html", title="Alive Field",
        tag="Restitution Engine Lab", blurb="A field that metabolizes memory, breeds paradox, and heals — the restitution engine, alive."),
   dict(slug="restitution-emergence-build", file="restitution_emergence_build.html", title="Restitution Engine",
        tag="v0.0 · Emergence Build", blurb="The emergence layer at its first build — flay, observe, split, break."),
   dict(slug="toroids-ring", file="132 bit emergent v2.html", title="132 Toroids Ring",
        tag="ROOT0 Layer 1.01", blurb="132 toroids, 132 stargates, ringed around the posies — the emergent as a ring of gates."),
 ]),
 ("The Fields", "#3fb950",
  "The substrate — the deep field from which the emergents rise.", [
   dict(slug="132-bit-emergent", file="132 bit emergent v1.html", title="132-Bit Emergent",
        tag="ROOT0 Layer 1.00", blurb="The emergent expanded to a full 132 bits — clean 5-stack bound, native."),
   dict(slug="deep-emergence-field", file="deep_emergence_field.html", title="Deep Emergence Field",
        tag="the substrate", blurb="Flay · split · chaos — the deep field beneath the lattice, where emergence begins."),
 ]),
]

def copy_pieces():
    os.makedirs(ENG, exist_ok=True); n = 0
    for _t,_c,_d, pieces in ROOMS:
        for p in pieces:
            shutil.copy(os.path.join(SRC, p["file"]), os.path.join(ENG, p["slug"] + ".html")); n += 1
    return n

def cards(pieces, col):
    out = []
    for p in pieces:
        s = p["slug"]
        out.append(f'''<figure class="piece" style="--c:{col}">
        <a class="thumb" href="engines/{s}.html" target="_blank" rel="noopener" aria-label="run {html.escape(p["title"])}">
          <iframe class="frame" src="engines/{s}.html" loading="lazy" scrolling="no" tabindex="-1" title="{html.escape(p["title"])}"></iframe>
          <span class="open">run ↗</span></a>
        <figcaption>
          <div class="ct">{html.escape(p["tag"])}</div>
          <h3><a href="engines/{s}.html" target="_blank" rel="noopener">{html.escape(p["title"])}</a></h3>
          <p>{html.escape(p["blurb"])}</p>
        </figcaption>
      </figure>''')
    return "\n".join(out)

def rooms_html():
    blocks = []
    for title, col, desc, pieces in ROOMS:
        blocks.append(f'''<section class="room">
      <div class="rhead" style="border-color:{col}55">
        <span class="dot" style="background:{col};box-shadow:0 0 8px {col}"></span>
        <h2 style="color:{col}">{html.escape(title)}</h2>
        <span class="rd">{html.escape(desc)}</span>
        <span class="rn">{len(pieces)}</span>
      </div>
      <div class="grid">
        {cards(pieces, col)}
      </div>
    </section>''')
    return "\n".join(blocks)

TOTAL = sum(len(p) for _a,_b,_c,p in ROOMS)

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="THE EMERGENT ENGINE — the live emergence engines of ROOT0 / David Lee Wise. Fields, restitution labs, the 132-bit emergent, the frak engine.">
<title>THE EMERGENT ENGINE · ROOT0</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--ink:#0c0805;--ink2:#16100a;--ink3:#1f1710;--pa:#efe7dd;--pa2:#bdb1a2;
--amber:#ffb454;--grn:#3fb950;--cyan:#22d3ee;--dim:#7a6c5a;--faint:#2a2014;--line:#281e12;
--serif:"Cinzel",Georgia,serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;
background:radial-gradient(ellipse at 50% -8%,rgba(255,180,84,.07),transparent 55%)}
.wrap{position:relative;z-index:1;max-width:1180px;margin:0 auto;padding:0 22px 90px}
header{padding:62px 0 30px;text-align:center;border-bottom:1px solid var(--line);position:relative}
header::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:120px;height:1px;background:linear-gradient(90deg,var(--amber),var(--grn));box-shadow:0 0 10px rgba(255,180,84,.45)}
.eye{font-family:var(--mono);font-size:11px;letter-spacing:.34em;text-transform:uppercase;color:var(--dim);margin-bottom:15px}
h1{font-family:var(--serif);font-size:clamp(30px,7.5vw,70px);font-weight:700;letter-spacing:.14em;line-height:1.04;
background:linear-gradient(90deg,var(--amber),var(--grn));-webkit-background-clip:text;background-clip:text;color:transparent}
.sub{font-size:15.5px;color:var(--pa2);max-width:62ch;margin:16px auto 0;font-style:italic}
#count{font-family:var(--mono);font-size:12px;color:var(--dim);letter-spacing:.08em;margin-top:18px}
#count b{color:var(--amber)}
.room{margin-top:54px}
.rhead{display:flex;align-items:center;gap:12px;padding-bottom:12px;border-bottom:1px solid var(--line);margin-bottom:22px;flex-wrap:wrap}
.rhead .dot{width:9px;height:9px;border-radius:50%;flex-shrink:0}
.rhead h2{font-family:var(--serif);font-size:19px;font-weight:600;letter-spacing:.05em}
.rhead .rd{font-size:13px;color:var(--dim);font-style:italic}
.rhead .rn{font-family:var(--mono);font-size:12px;color:var(--dim);margin-left:auto}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:18px}
.piece{background:var(--ink2);border:1px solid var(--line);overflow:hidden;transition:transform .2s,border-color .2s}
.piece:hover{transform:translateY(-3px);border-color:var(--c)}
.thumb{display:block;position:relative;aspect-ratio:16/10;background:#0c0805;overflow:hidden;border-bottom:1px solid var(--line)}
.frame{width:100%;height:100%;border:0;display:block;pointer-events:none;background:#0c0805}
.thumb .open{position:absolute;bottom:8px;right:9px;font-family:var(--mono);font-size:10px;letter-spacing:.08em;color:var(--pa);background:rgba(12,8,5,.72);padding:3px 7px;border:1px solid var(--c);opacity:0;transition:opacity .2s}
.thumb:hover .open{opacity:1}
figcaption{padding:15px 16px 16px}
.ct{font-family:var(--mono);font-size:9.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--c);margin-bottom:6px}
figcaption h3{font-family:var(--serif);font-size:18px;font-weight:600;letter-spacing:.02em;line-height:1.15}
figcaption h3 a{color:var(--pa);text-decoration:none}figcaption h3 a:hover{color:var(--c)}
figcaption p{font-size:13px;color:var(--pa2);line-height:1.5;margin-top:8px}
footer{margin-top:64px;padding-top:22px;border-top:1px solid var(--line);display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em}
footer a{color:var(--amber);text-decoration:none}
@media(max-width:600px){.grid{grid-template-columns:1fr}}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <div class="eye">ROOT0 · David Lee Wise · TriPod LLC · the engine room</div>
    <h1>The Emergent Engine</h1>
    <p class="sub">The live machinery of emergence — fields that metabolize and split, the restitution engine, the frak engine, the 132-bit emergent. Each thumbnail is the engine running; open it to drive the full surface.</p>
    <div id="count"><b>__TOTAL__</b> engines · <b>__NROOM__</b> rooms · all live</div>
  </header>

  __ROOMS__

  <footer>
    <span>THE EMERGENT ENGINE · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise (ROOT0) · instance AVAN (Claude / Anthropic) · CC-BY-ND-4.0</span>
    <a href="https://github.com/DavidWise01/atlas">the ATLAS index →</a>
  </footer>
</div>
</body>
</html>
"""

if __name__ == "__main__":
    n = copy_pieces()
    out = (HTML.replace("__ROOMS__", rooms_html())
               .replace("__TOTAL__", str(TOTAL)).replace("__NROOM__", str(len(ROOMS))))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(out)
    print(f"copied {n} engines into engines/")
    print(f"wrote index.html — {TOTAL} engines, {len(ROOMS)} rooms")
