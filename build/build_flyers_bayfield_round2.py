#!/usr/bin/env python3
"""
Round-2 rebuild of the two standalone Bayfield flyers (2026-07-11):
  bayfield-who-is-watching.pdf / bayfield-turn-cameras-off.pdf

Replaces the June-27 build (build_flyers_v3_bayfield.py), which printed
"about 15,000" and carried claims not in claims-register.md ("running since
2022", "Red Cliff added one in 2025", "Wisconsin DOJ", "Milwaukee officer 170
times", "man jailed nearly a month").

Every factual claim below traces to a row in claims-register.md (same rows the
two-sided WI set uses). QR points to the SITE per SOW K.3 ("who-is-watching" is
an educational flyer; its companion goes to the site too, matching the round-2
flyers). Outputs -final-style PDF + full PNG here, PDF + 1100px preview to the
repo downloads/ via REPO_DOWNLOADS.
Run: REPO_DOWNLOADS=/path/to/repo/downloads python build_flyers_bayfield_round2.py

REVISED 2026-08-19. Three corrections, none of them regenerated yet, so THIS SCRIPT
AND THE SHIPPED 2026-07-13 ARTIFACT NOW DISAGREE until someone runs it:
  1. The ~250 subhead read "Including out-of-state police and agencies you never
     voted for." That overstated Sheriff Williams, who stated in writing on
     2026-07-08 that out-of-state sharing is off by default, that the ~25
     out-of-state agencies are approved one at a time and kept to surrounding
     states, and that ALL federal-agency access is off. Overstating a cooperative
     sheriff is the error most likely to get the campaign corrected in public.
  2. The "8" row called all eight units cameras logging cars. The 2026-07-29
     production established 6 plate readers plus 2 solar video cameras, and
     Williams confirmed the portal's 8 includes the video units. The video
     distinction is the strongest Bayfield point the campaign owns.
  3. The as-of date is now a cta() parameter. who-is-watching says August 2026
     because its figures were re-verified 2026-08-19. turn-cameras-off keeps
     July 2026 on purpose: it has NOT been audited, and bumping its date would
     assert a freshness nobody checked.
Still absent by choice: the $17,500 / three-agreements cost figure. Adding a
fourth statrow risks overflowing the fixed layout and was not attempted blind.
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

def _font_dir():
    linux = "/usr/share/fonts/truetype/dejavu/"
    if os.path.exists(os.path.join(linux, "DejaVuSerif-Bold.ttf")):
        return linux
    import matplotlib
    return os.path.join(os.path.dirname(matplotlib.__file__), "mpl-data", "fonts", "ttf") + os.sep
D = _font_dir()
SERIF   = lambda s: ImageFont.truetype(D + "DejaVuSerif-Bold.ttf", s)
SERIFI  = lambda s: ImageFont.truetype(D + "DejaVuSerif-BoldItalic.ttf", s)
SANS    = lambda s: ImageFont.truetype(D + "DejaVuSans.ttf", s)
SANSB   = lambda s: ImageFont.truetype(D + "DejaVuSans-Bold.ttf", s)

BG=(250,249,244); INK=(30,42,38); GREEN=(47,122,86); GREEN_DK=(24,78,57)
TEAL=(38,108,132); GOLD=(226,164,46); GOLD_LT=(247,216,140); SAGE=(228,240,231)
MUT=(92,102,96); PAPER=(244,248,242)

def qr_img(px=178):
    q = qrcode.QRCode(border=4, box_size=10, error_correction=qrcode.constants.ERROR_CORRECT_Q)
    q.add_data(SITE); q.make(fit=True)
    return q.make_image(fill_color="black", back_color="white").convert("RGB").resize((px, px))

def wrap(d, txt, f, maxw):
    out=[]; cur=""
    for w in txt.split():
        t=(cur+" "+w).strip()
        if d.textlength(t, font=f) <= maxw: cur=t
        else: out.append(cur); cur=w
    if cur: out.append(cur)
    return out

def para(d, x, y, txt, f, fill, maxw, lh):
    for ln in wrap(d, txt, f, maxw): d.text((x, y), ln, font=f, fill=fill); y += lh
    return y

def ctr(d, y, txt, f, fill):
    w=d.textlength(txt, font=f); d.text(((W-w)/2, y), txt, font=f, fill=fill)

def masthead(d, title):
    # Title-hierarchy swap (2026-07-12): the flyer/context name is the BIG
    # masthead line; "Keep the Northwoods FLOCK Free" is the small subtitle.
    d.rectangle([0,0,W,88],fill=GREEN_DK)
    d.rectangle([0,88,W,95],fill=GOLD)
    d.text((M,16), title, font=SANSB(30), fill=PAPER)
    f=SANSB(22); x=M; ty=54
    for t,c in [("Keep the Northwoods ",(196,214,202)),("FLOCK",GOLD_LT),(" Free",(196,214,202))]:
        d.text((x,ty),t,font=f,fill=c); x+=d.textlength(t,font=f)

def cta(d, img, caption_lines, asof="July 2026"):
    BANDH=300; by=H-BANDH
    d.rectangle([0,by,W,H], fill=GREEN_DK); d.rectangle([0,by,W,by+7], fill=GOLD)
    img.paste(qr_img(190), (M, by+52))
    tx=M+190+34
    d.text((tx,by+56), "Scan for the facts.", font=SERIF(40), fill=PAPER)
    y=by+112
    for ln in caption_lines:
        d.text((tx,y), ln, font=SANS(22), fill=(214,228,218)); y += 32
    x=tx
    for t,c in [(SITE_TXT.replace(".com",""),GOLD_LT),(".com",PAPER)]:
        d.text((x,by+206), t, font=SANSB(26), fill=c); x += d.textlength(t, font=SANSB(26))
    d.line([(M,by+250),(W-M,by+250)], fill=(70,120,94), width=2)
    ctr(d, by+262, "A nonpartisan effort of Northwoods neighbors  ·  Facts as of " + asof, SANS(17), (200,218,205))

def statrow(d, y, num, label, sub, size=52):
    fn=SERIF(size)
    d.text((M,y), num, font=fn, fill=TEAL)
    lx=M+d.textlength(num, font=fn)+28
    d.text((lx,y+8), label, font=SANSB(26), fill=INK)
    para(d, lx, y+48, sub, SANS(23), MUT, W-lx-M, 31)

def callout(d, y, title, body, bar):
    pad=26; tf=SERIF(28); bf=SANS(23); lh=31
    lines=wrap(d, body, bf, 900)
    h=pad + (44 if title else 0) + len(lines)*lh + pad
    d.rectangle([M,y,W-M,y+h], fill=SAGE); d.rectangle([M,y,M+7,y+h], fill=bar)
    yy=y+pad
    if title: d.text((M+pad,yy), title, font=tf, fill=INK); yy+=44
    for ln in lines: d.text((M+pad,yy), ln, font=bf, fill=INK); yy+=lh
    return y+h

def greenbox(d, y, title, body):
    pad=24; tf=SERIF(28); bf=SANSB(25); lh=34
    lines=wrap(d, body, bf, 900)
    h=pad + (46 if title else 0) + len(lines)*lh + pad
    d.rectangle([M,y,W-M,y+h], fill=GREEN)
    yy=y+pad
    if title: d.text((M+pad,yy), title, font=tf, fill=PAPER); yy+=46
    for ln in lines: d.text((M+pad,yy), ln, font=bf, fill=PAPER); yy+=lh
    return y+h

def save(img, name):
    img.save(os.path.join(OUT, name+".pdf"), "PDF", resolution=150.0)
    img.save(os.path.join(OUT, name+".png"), "PNG")
    prev=img.resize((1100, int(H*1100/W)))
    prev.save(os.path.join(REPO, name+".png"), "PNG")
    img.save(os.path.join(REPO, name+".pdf"), "PDF", resolution=150.0)
    print("built", name)

def who_is_watching():
    img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)
    masthead(d, "BAYFIELD COUNTY, WISCONSIN")
    y=132
    for ln in wrap(d, "Who is watching the roads in Bayfield County?", SERIF(56), W-2*M):
        d.text((M,y), ln, font=SERIF(56), fill=INK); y+=66
    y+=10
    y=para(d, M, y, "Cameras across Bayfield County photograph and log every car that passes, including one confirmed on US-63 in Cable. You never opted in, and you cannot opt out.", SERIF(26), GREEN, W-2*M, 34)
    y+=12; d.line([(M,y),(W-M,y)], fill=GOLD, width=4); y+=30
    statrow(d, y, "100,721", "vehicles logged in a single 30-day period", "One portal read, June 2026. In a county of about 16,000 people.", size=76); y+=168
    statrow(d, y, "~250", "agencies in five states can search the data", "About 25 sit outside Wisconsin, and the Sheriff keeps federal access off. All of that is a setting, not a law."); y+=146
    statrow(d, y, "8+", "Flock devices: 6 plate readers and 2 video cameras", "A plate reader reads plates. A video camera watches the people in front of it. Plates kept 30 days."); y+=150
    y=callout(d, y, "\"But I have nothing to hide.\"",
              "A Kansas police lieutenant was charged with using one of these systems to stalk his estranged wife. In independent tests, as many as 1 in 10 reads come back wrong, and people have been pulled over at gunpoint over a misread plate. Sources: KWCH; Institute for Justice.",
              GREEN)
    greenbox(d, y+28, None,
             "This is not left or right. It is whether a private, out-of-state company gets to track a whole community, with no warrant and no record of a public vote.")
    cta(d, img, ["The facts on your county's", "cameras, and how to help:"], asof="September 2026")
    save(img, "bayfield-who-is-watching")

# RETIRED 2026-07-12, superseded by how-we-fight-back. Artifact lives in downloads/archive/.
# DO NOT re-enable without re-checking every claim in it against claims-register.md.
def turn_cameras_off():
    img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)
    masthead(d, "BAYFIELD COUNTY, WISCONSIN")
    y=140
    for ln in wrap(d, "We can turn these cameras off.", SERIF(58), W-2*M):
        d.text((M,y), ln, font=SERIF(58), fill=INK); y+=68
    y+=8
    y=para(d, M, y, "Towns across Wisconsin already have. Here is how Bayfield County does the same.", SERIFI(26), GREEN, W-2*M, 36)
    y+=18; d.line([(M,y),(W-M,y)], fill=GOLD, width=4); y+=36
    steps=[("1","Get on the list","Add your name so we move as a group, not a crowd that scatters. A connected handful beats a hundred strangers."),
           ("2","Get the facts","Public-records requests to the Bayfield County Sheriff and WisDOT: how many cameras, the cost, the contract dates, and who gets the data."),
           ("3","Find the allies","Link up with neighbors, the ACLU of Wisconsin, and EFF, who work on exactly this."),
           ("4","Build the pressure","A petition, an op-ed in the local paper, and a packed room when the county decides the money at the annual budget hearing."),
           ("5","Outlast the cameras","Keep at it until they come down, and write the rules so they cannot quietly come back.")]
    for n,h_,t in steps:
        d.ellipse([M,y,M+52,y+52], fill=GREEN)
        nx=M+26-d.textlength(n, font=SERIF(30))/2
        d.text((nx,y+7), n, font=SERIF(30), fill=GOLD_LT)
        d.text((M+80,y+2), h_, font=SANSB(26), fill=TEAL)
        yy=para(d, M+80, y+42, t, SANS(20), INK, W-M-(M+80), 27)
        y=max(yy, y+52)+26
    greenbox(d, y, "It is winnable.",
             "Verona, Oshkosh, and Dane County have dropped Flock, and Ashland has told Flock it will not renew. Bayfield County is next.")
    cta(d, img, ["Get on the list and see what", "other towns did. The facts", "and how to help:"])
    save(img, "bayfield-turn-cameras-off")

who_is_watching()  # turn-cameras-off retired from the site 2026-07-12 - do not rebuild
print("done ->", REPO)
