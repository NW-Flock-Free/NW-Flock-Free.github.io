#!/usr/bin/env python3
"""Build the Bayfield County mobile social card (1080x1350).
Same locked template as build_douglas_mobile.py. Layout, palette and QR unchanged.

Claims corrected 2026-09-12 against claims-register.md. Removed: the auto-renew
frame (SUPERSEDED 2026-07-30, and contradicted by areas.html), the flat "8 cameras"
device total (BARRED pending Sheriff Williams), "0 public votes" (RETIRED 2026-07-31,
the citation was false) and "You got no say" (unverified absolute negative).
Every figure below traces to a register row; see the per-line comments.
QR = douglas-qr.png (same northwoodsflockfree.com sign-up form), unchanged.
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
    a=f' font-family="{ff}" font-size="{size}"'
    a+=f' font-weight="{"bold" if bold else "normal"}"'
    spans="".join(f'<tspan fill="{c}">{esc(t)}</tspan>' for t,c in parts)
    out.append(f'<text x="{x}" y="{y}"{a}>{spans}</text>')

# ---- canvas
rect(0,0,W,H,CREAM)

# ---- HEADER
rect(0,0,W,238,GREEN)
rect(0,238,W,6,GOLDRULE)
text(540,104,"Bayfield County",66,WHITE,bold=True,anchor="middle")
text(540,172,"is under surveillance.",48,GOLD_SOFT,bold=True,italic=True,anchor="middle",ff=SERIF)

# ---- INFO PARAGRAPH (centered; frame = mass plate-logging in a small county)
# register: ALPR baseline (ACLU/EFF rows) + "a county of about 16,000" [T1 Census]
para=[
 "The Bayfield County Sheriff runs a network of automated cameras",
 "that photograph and log every car that passes, and keep the data,",
 "in a county of about 16,000 people.",
]
py=296
for ln in para:
    text(540,py,ln,30,INK,anchor="middle",ff=SERIF); py+=42

# ---- STAT ROW (100,721 vs 16,000 residents = the defensible Bayfield contrast)
text(540,422,"From the county's own records and its Flock portal:",26,MUTED,italic=True,anchor="middle",ff=SERIF)
# 100,721 is WINDOW-SCOPED, never a rate (register, index.html row, 2026-07-30)
# "8+" renders the approved "at least eight Flock devices"; a flat total is BARRED
# $17,500/yr across three agreements: order forms + INV-81561 + INV-90497 [T1]
stats=[("100,721","cars logged in 30 days","one portal read, June 2026",250),
       ("8+","Flock devices","county-wide",560),
       ("$17,500","a year","three agreements",850)]
for num,lab,sub,xc in stats:
    text(xc,500,num,(84 if num==stats[0][0] else 52),TEAL,bold=True,anchor="middle",ff=SERIF)
    text(xc,544,lab,28,INK,bold=True,anchor="middle")
    text(xc,574,sub,20,MUTED,anchor="middle",ff=SERIF)

# ---- BIG ZERO
# finding, not conclusion: nobody has read the board minutes (register, 2026-07-31)
text(291,744,"0",190,RED,bold=True,ff=SERIF)
text(429,688,"records of",44,INK,bold=True,ff=SERIF)
text(429,744,"a public vote",56,INK,bold=True,ff=SERIF)
text(540,804,"In anything Bayfield County has produced.",28,MUTED,italic=True,anchor="middle",ff=SERIF)

# ---- TAN BOX (Bayfield = where the decision actually gets made)
rect(70,876,940,112,TAN,rx=14)
# Sheriff is independently elected (Wis. Stat. ch. 59); the Board's lever is
# appropriation, and Wis. Stat. 65.90 requires an annual public budget hearing [T1]
text(540,920,"The Board's lever is the budget, not the cameras.",30,DARKTAN,bold=True,anchor="middle")
text(540,954,"Wisconsin requires a public budget hearing each year.",30,DARKTAN,bold=True,anchor="middle")

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
tspan_line(28,1340,18,[("Keep the Northwoods ",CREAMTXT),("FLOCK Free",GOLD_SOFT)],ff=SANS)
text(1052,1340,"Facts as of September 2026",18,CREAMTXT,anchor="end",ff=SANS)

svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'+"\n".join(out)+"\n</svg>\n"
open(os.path.join(FLOCK_DIR, "bayfield-mobile.svg"),"w",encoding="utf-8").write(svg)
print("wrote bayfield-mobile.svg", len(svg), "bytes")
