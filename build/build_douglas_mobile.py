#!/usr/bin/env python3
"""Build the Douglas/Superior mobile social card (1080x1350).
Hand-flat <text>/<rect> SVG (no CSS/foreignObject) so it stays Figma-editable.
QR embedded from douglas-qr.png. Render to PNG with cairosvg for review.

Claims corrected 2026-09-12 against claims-register.md. Removed: the "4 states can
search" tile (NO REGISTER ROW - "4 states" was dropped for lack of one on 2026-07-11),
"0 public votes" (RETIRED 2026-07-31), the "No vote" half of the CTA (rests on Flock
records, not board minutes) and "You got no say" (unverified absolute negative).
The stat row is now two tiles, not three: the fourth claim had no honest replacement.
Locked brand chrome: header/footer green #2C7150, gold rule #E2A42E,
gold accent #E8AA30, cream #FAF9F4, ink #1E2A26, teal #1F6079, red #B3271E.
"""
import base64, html, os

# --- paths --------------------------------------------------------------
# This file lives in <repo>/build/ and reads douglas-qr.png from beside itself.
# NOTE ON RENDERING: this script emits SVG only - it does NOT rasterise, and it
# imports no cairosvg. The SVG -> PNG step runs elsewhere (cairosvg is installed
# but broken on this machine: it cannot load libcairo-2.dll). The SVG is written
# to the campaign working folder, where the raster step picks it up.
HERE = os.path.dirname(os.path.abspath(__file__))
# MACHINE-SPECIFIC: the campaign working folder, outside the repo. One line to
# change on a new machine, or override with FLOCK_DIR. See build/README.md.
FLOCK_DIR = os.environ.get("FLOCK_DIR",
    r"C:\Users\Adam\Documents\Claude\Projects\Adam's Personal Projects\Community Outreach\Flock")
# ------------------------------------------------------------------------
QR = base64.b64encode(open(os.path.join(HERE, "douglas-qr.png"), "rb").read()).decode()

CREAM="#FAF9F4"; INK="#1E2A26"; GREEN="#2F7A56"; GOLDRULE="#E2A42E"
GOLD="#E2A42E"; GOLD_SOFT="#F7DC96"; TEAL="#266C84"; RED="#B23020"; TAN="#FBEBD0"
WHITE="#F4F8F2"; CREAMTXT="#CFE0D5"; MUTED="#6A766E"; DARKTAN="#173F2E"
SANS="Arial, Helvetica, sans-serif"; SERIF="Georgia, 'Times New Roman', serif"

W=1080; H=1350
out=[]

def esc(s): return html.escape(s, quote=True)

def rect(x,y,w,h,fill,rx=0):
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"'
    if rx: s+=f' rx="{rx}"'
    out.append(s+"/>")

def text(x,y,s,size,fill,bold=False,italic=False,anchor="start",ff=SANS):
    a=f' font-family="{ff}" font-size="{size}" fill="{fill}"'
    a+=f' font-weight="{"bold" if bold else "normal"}"'
    if italic: a+=' font-style="italic"'
    if anchor!="start": a+=f' text-anchor="{anchor}"'
    out.append(f'<text x="{x}" y="{y}"{a}>{esc(s)}</text>')

def width_est(s,size,factor=0.52):
    return len(s)*size*factor

def tspan_line(x,y,size,parts,bold=True,ff=SERIF):
    # parts = list of (string, color); no text-anchor (manual x), tspans flow contiguously
    a=f' font-family="{ff}" font-size="{size}"'
    a+=f' font-weight="{"bold" if bold else "normal"}"'
    spans="".join(f'<tspan fill="{c}">{esc(t)}</tspan>' for t,c in parts)
    out.append(f'<text x="{x}" y="{y}"{a}>{spans}</text>')

# ---- canvas
rect(0,0,W,H,CREAM)

# ---- HEADER
rect(0,0,W,238,GREEN)
rect(0,238,W,6,GOLDRULE)
text(540,104,"Douglas County",66,WHITE,bold=True,anchor="middle")
text(540,172,"is under surveillance.",48,GOLD_SOFT,bold=True,italic=True,anchor="middle",ff=SERIF)

# ---- INFO PARAGRAPH (centered, balanced margins)
para=[
 "Douglas County's Sheriff put up a network of automated cameras",
 "around Superior. They photograph and log every car that passes,",
 "keep the data, and share it across state lines.",
]
py=296
for ln in para:
    text(540,py,ln,30,INK,anchor="middle",ff=SERIF); py+=42

# ---- STAT ROW
text(540,422,"The county's own records show:",26,MUTED,italic=True,anchor="middle",ff=SERIF)
# 19 cameras at 9 locations: Douglas County records, July 2026 [T1]
# REMOVED, do not restore: "4 states can search". No register row exists for it.
# The sharing list is sourced by jurisdiction, not by count - see the areas.html row.
stats=[("19",GOLD,"cameras",390),("9",TEAL,"locations",690)]
for num,col,lab,xc in stats:
    text(xc,500,num,(84 if num==stats[0][0] else 52),TEAL,bold=True,anchor="middle",ff=SERIF)
    text(xc,544,lab,28,INK,bold=True,anchor="middle")

# ---- BIG ZERO (finding form; the larger line shares the zero's baseline)
# finding, not conclusion: the production was Flock records, not board minutes
text(291,744,"0",190,RED,bold=True,ff=SERIF)
text(429,688,"records of",44,INK,bold=True,ff=SERIF)
text(429,744,"a public vote",56,INK,bold=True,ff=SERIF)
text(540,804,"In the records Douglas County produced.",28,MUTED,italic=True,anchor="middle",ff=SERIF)

# ---- TAN BOX (no gold bar, centered)
rect(70,876,940,112,TAN,rx=14)
# "free trial - no signed contract, no money paid" [T1]; the vote half is NOT sourced
text(540,920,"No signed contract. No money paid. Just a free trial.",30,DARKTAN,bold=True,anchor="middle")
text(540,954,"The easiest time to stop it is before it ever starts.",30,DARKTAN,bold=True,anchor="middle")

# ---- FOOTER
rect(0,1014,W,336,GREEN)
rect(0,1014,W,6,GOLDRULE)
l1=[("Get corporate public surveillance ",WHITE),("OUT",GOLD_SOFT),(" of the Northwoods,",WHITE)]
l1str="Get corporate public surveillance OUT of the Northwoods,"
tspan_line((W-width_est(l1str,30))/2,1078,30,l1,ff=SERIF)
text(540,1114,"the last stronghold of privacy in the Midwest.",30,WHITE,bold=True,anchor="middle",ff=SERIF)
text(540,1150,"Add your name  ·  northwoodsflockfree.com",32,WHITE,bold=True,anchor="middle")
rect(465,1160,150,150,"#FFFFFF",rx=12)
out.append(f'<image x="477" y="1172" width="126" height="126" href="data:image/png;base64,{QR}"/>')
text(540,1340,"Scan to add your name and get updates",22,CREAMTXT,anchor="middle")
# tiny brand line, bottom-left corner
tspan_line(28,1340,18,[("Keep the Northwoods ",CREAMTXT),("FLOCK Free",GOLD_SOFT)],ff=SANS)
text(1052,1340,"Facts as of September 2026",18,CREAMTXT,anchor="end",ff=SANS)

svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'+"\n".join(out)+"\n</svg>\n"
open(os.path.join(FLOCK_DIR, "douglas-mobile.svg"),"w",encoding="utf-8").write(svg)
print("wrote douglas-mobile.svg", len(svg), "bytes")
