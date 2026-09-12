#!/usr/bin/env python3
"""
Douglas County findings one-pager, rebuilt 2026-07-12 in the STANDARD round-2
flyer template (masthead: context BIG + org subtitle; serif headline; numbered
findings; greenbox; site-QR CTA band) so it matches the other 8.5x11 flyers.
Replaces the older card-style design (douglas-findings-onepage.svg lineage).
Every claim traces to the Douglas row in claims-register.md (county records,
Wis. open records request, July 2026). QR -> the site per SOW K.3.
Run: REPO_DOWNLOADS=/path/to/repo/downloads python3 build_douglas_round2.py
"""
import os, qrcode
from PIL import Image, ImageDraw, ImageFont

W, H = 1275, 1650
M = 80
# --- destinations -------------------------------------------------------
# This file lives in <repo>/build/. Both destinations are derived from it, so
# there is no local home directory baked into this public repo.
HERE = os.path.dirname(os.path.abspath(__file__))
# The repo's downloads/ folder: gets the PDF + a 1100px preview PNG.
REPO = os.environ.get("REPO_DOWNLOADS", os.path.normpath(os.path.join(HERE, os.pardir, "downloads")))
# MACHINE-SPECIFIC: the campaign working folder, which lives outside the repo.
# Gets the PDF + the full-size print master. One line to change on a new machine,
# or override with the FLOCK_DIR environment variable. See build/README.md.
FLOCK_DIR = os.environ.get("FLOCK_DIR",
    r"C:\Users\Adam\Documents\Claude\Projects\Adam's Personal Projects\Community Outreach\Flock")
OUT = FLOCK_DIR
# ------------------------------------------------------------------------
SITE = "https://northwoodsflockfree.com"
SITE_TXT = "northwoodsflockfree.com"

D = "/usr/share/fonts/truetype/dejavu/"
SERIF   = lambda s: ImageFont.truetype(D+"DejaVuSerif-Bold.ttf", s)
SERIFI  = lambda s: ImageFont.truetype(D+"DejaVuSerif-BoldItalic.ttf", s)
SANS    = lambda s: ImageFont.truetype(D+"DejaVuSans.ttf", s)
SANSB   = lambda s: ImageFont.truetype(D+"DejaVuSans-Bold.ttf", s)

BG=(250,249,244); INK=(30,42,38); GREEN=(47,122,86); GREEN_DK=(24,78,57)
TEAL=(38,108,132); GOLD=(226,164,46); GOLD_LT=(247,216,140); SAGE=(228,240,231)
MUT=(92,102,96); PAPER=(244,248,242)

def qr_img(px=178):
    q = qrcode.QRCode(border=4, box_size=10, error_correction=qrcode.constants.ERROR_CORRECT_Q)
    q.add_data(SITE); q.make(fit=True)
    return q.make_image(fill_color="black", back_color="white").convert("RGB").resize((px,px))

def wrap(d,txt,f,maxw):
    out=[]; cur=""
    for w in txt.split():
        t=(cur+" "+w).strip()
        if d.textlength(t,font=f)<=maxw: cur=t
        else: out.append(cur); cur=w
    if cur: out.append(cur)
    return out
def para(d,x,y,txt,f,fill,maxw,lh):
    for ln in wrap(d,txt,f,maxw): d.text((x,y),ln,font=f,fill=fill); y+=lh
    return y
def ctr(d,y,txt,f,fill):
    w=d.textlength(txt,font=f); d.text(((W-w)/2,y),txt,font=f,fill=fill)

def masthead(d, title):
    d.rectangle([0,0,W,88],fill=GREEN_DK)
    d.rectangle([0,88,W,95],fill=GOLD)
    d.text((M,16), title, font=SANSB(30), fill=PAPER)
    f=SANSB(22); x=M; ty=54
    for t,c in [("Keep the Northwoods ",(196,214,202)),("FLOCK",GOLD_LT),(" Free",(196,214,202))]:
        d.text((x,ty),t,font=f,fill=c); x+=d.textlength(t,font=f)

def cta(d,img,caption_lines):
    BANDH=300; by=H-BANDH
    d.rectangle([0,by,W,H],fill=GREEN_DK); d.rectangle([0,by,W,by+7],fill=GOLD)
    q=qr_img(190); img.paste(q,(M,by+52))
    tx=M+190+34
    d.text((tx,by+56),"Scan for the facts.",font=SERIF(40),fill=PAPER)
    y=by+112
    for ln in caption_lines:
        d.text((tx,y),ln,font=SANSB(28),fill=(222,236,226)); y+=38
    x=tx
    for t,c in [(SITE_TXT.replace(".com",""),GOLD_LT),(".com",PAPER)]:
        d.text((x,by+204),t,font=SANSB(28),fill=c); x+=d.textlength(t,font=SANSB(28))
    d.line([(M,by+250),(W-M,by+250)],fill=(70,120,94),width=2)
    ctr(d,by+261,"A nonpartisan effort of Northwoods neighbors  ·  Facts as of September 2026",SANS(19),(200,218,205))

def greenbox(d, y, title, body):
    pad=24; tf=SERIF(28); bf=SANSB(25); lh=34
    lines=wrap(d, body, bf, W-2*M-2*pad)
    h=pad + (46 if title else 0) + len(lines)*lh + pad
    d.rectangle([M,y,W-M,y+h], fill=GREEN)
    yy=y+pad
    if title: d.text((M+pad,yy), title, font=tf, fill=PAPER); yy+=46
    for ln in lines: d.text((M+pad,yy), ln, font=bf, fill=PAPER); yy+=lh
    return y+h

def douglas():
    img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)
    masthead(d,"SUPERIOR / DOUGLAS COUNTY, WISCONSIN")
    y=136
    for ln in wrap(d,"19 cameras. No record of a public vote. No contract. No rules.",SERIF(54),W-2*M):
        d.text((M,y),ln,font=SERIF(54),fill=INK); y+=64
    y+=8
    y=para(d,M,y,"Douglas County runs 19 license-plate cameras at nine locations around Superior, on a free trial, with no record of a public vote. From the county's own records:",SERIF(25),GREEN,W-2*M,34)
    y+=14; d.line([(M,y),(W-M,y)],fill=GOLD,width=4); y+=30
    steps=[("1","No contract, no payment","A free trial: no signed contract, no money paid. The county is applying for grant funds to make it permanent."),
           ("2","No written policy","No written rules govern who can search the data or for what. Plate data defaults to 30-day retention, with no policy behind it."),
           ("3","No public portal","Residents cannot see who searched their plate, when, or why. Neighboring Bayfield publishes a portal. Douglas has not."),
           ("4","No record of a public vote","Nothing in the county's own records shows a public hearing or a vote by the county board."),
           ("5","Your plate leaves the county","The county's own sharing list sends plate data to police in Texas (Fort Worth), Minnesota, Michigan, tribal agencies, and across Wisconsin.")]
    for n,h_,t in steps:
        d.ellipse([M,y,M+52,y+52], fill=GREEN)
        nx=M+26-d.textlength(n, font=SERIF(30))/2
        d.text((nx,y+7), n, font=SERIF(30), fill=GOLD_LT)
        d.text((M+80,y+2), h_, font=SANSB(27), fill=TEAL)
        yy=para(d, M+80, y+44, t, SANS(23), INK, 940, 31)
        y=max(yy, y+52)+18
    y+=2
    d.text((M,y),"All findings from Douglas County's own public records (Wisconsin open records request, July 2026).",font=SANS(17),fill=MUT); y+=32
    greenbox(d, y, "Decide it in the open.",
             "This is not about having something to hide. The county is seeking grant money to pay a private, out-of-state company to track everyone who drives through, with no rules and no way to opt out. The easiest time to stop it is before it is ever paid for.")
    cta(d,img,["The Douglas County records,","the facts, and how to help:"])
    img.save(os.path.join(OUT,"douglas-county-findings-one-pager.pdf"),"PDF",resolution=150.0)
    img.save(os.path.join(OUT,"douglas-county-findings-one-pager.png"),"PNG")
    prev=img.resize((1100,int(H*1100/W)))
    prev.save(os.path.join(REPO,"douglas-county-findings-one-pager.png"),"PNG")
    img.save(os.path.join(REPO,"douglas-county-findings-one-pager.pdf"),"PDF",resolution=150.0)
    print("built douglas-county-findings-one-pager")

douglas()
