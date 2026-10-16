#!/usr/bin/env python3
"""
Oct 27, 2026 Washburn turnout half-sheet (built 2026-10-06).

One portrait half-sheet (5.5 x 8.5 in), printed two-up on a landscape letter
page with a dashed cut line. Ask-led layout (KB advocacy-flyer-and-poster-design
module-05, archetype 4): the date and the ask lead, the what/when/where block
follows, the QR band closes.

Every factual claim below carries a comment naming its claims-register.md row
(section "2026-10-16 downloads refresh").

Rules this artifact is held to:
  - Never call Oct 27 the final budget vote. The agenda posts Fri Oct 23 and the
    vote may land Nov 10. "Budget meeting" is the safe wording.
  - No ACLU-WI on any general-audience piece.
  - Never say the records are on the site. The QR caption says the site has a
    summary of what the records show, which is true.
  - QR points to the site, not the Facebook group (CLAUDE.md).
  - DATED. Pull it from downloads/ after Wed Oct 28, 2026.

Outputs: PDF + 1100px preview PNG to the repo downloads/ (REPO_DOWNLOADS), and
PDF + full-size print master PNG to the campaign working folder (FLOCK_DIR).
Run: python build_oct27_halfsheet.py
"""
import os, qrcode
from PIL import Image, ImageDraw, ImageFont

# --- destinations (same convention as the other build scripts) ----------
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.environ.get("REPO_DOWNLOADS", os.path.normpath(os.path.join(HERE, os.pardir, "downloads")))
FLOCK_DIR = os.environ.get("FLOCK_DIR",
    r"C:\Users\Adam\Documents\Claude\Projects\Adam's Personal Projects\Community Outreach\Flock")
NAME = "oct27-washburn-halfsheet"
# ------------------------------------------------------------------------
SITE = "https://northwoodsflockfree.com/"
SITE_TXT = "northwoodsflockfree.com"
ASOF = "Oct 16, 2026"

def _font_dir():
    linux = "/usr/share/fonts/truetype/dejavu/"
    if os.path.exists(os.path.join(linux, "DejaVuSerif-Bold.ttf")):
        return linux
    import matplotlib
    return os.path.join(os.path.dirname(matplotlib.__file__), "mpl-data", "fonts", "ttf") + os.sep
D = _font_dir()
SERIF  = lambda s: ImageFont.truetype(D + "DejaVuSerif-Bold.ttf", s)
SERIFI = lambda s: ImageFont.truetype(D + "DejaVuSerif-BoldItalic.ttf", s)
SANS   = lambda s: ImageFont.truetype(D + "DejaVuSans.ttf", s)
SANSB  = lambda s: ImageFont.truetype(D + "DejaVuSans-Bold.ttf", s)

BG=(250,249,244); INK=(30,42,38); GREEN=(47,122,86); GREEN_DK=(24,78,57)
GOLD=(226,164,46); GOLD_LT=(247,216,140); GOLD_DEEP=(138,98,0); SAGE=(228,240,231)
MUT=(92,102,96); PAPER=(244,248,242)

# 150 dpi. One half-sheet is 5.5 x 8.5 in = 825 x 1275 px.
HW, HH = 825, 1275
M = 60   # 0.4 in outer margin; the page adds its own printer margin around it

def qr_img(px):
    q = qrcode.QRCode(border=4, box_size=10, error_correction=qrcode.constants.ERROR_CORRECT_Q)
    q.add_data(SITE); q.make(fit=True)
    return q.make_image(fill_color="black", back_color="white").convert("RGB").resize((px, px), Image.NEAREST)

def wrap(d, txt, f, maxw):
    out=[]; cur=""
    for w in txt.split():
        t=(cur+" "+w).strip()
        if d.textlength(t, font=f) <= maxw: cur=t
        else: out.append(cur); cur=w
    if cur: out.append(cur)
    return out

def para(d, x, y, txt, f, fill, maxw, lh):
    for ln in [l for part in txt.split("\n") for l in wrap(d, part, f, maxw)]:
        d.text((x, y), ln, font=f, fill=fill); y += lh
    return y

def half():
    img = Image.new("RGB", (HW, HH), BG); d = ImageDraw.Draw(img)
    CW = HW - 2*M

    # Masthead: org identity small, subordinate to the date (title-first rule).
    d.rectangle([0,0,HW,78], fill=GREEN_DK); d.rectangle([0,78,HW,84], fill=GOLD)
    f=SANSB(26); x=M; ty=24
    for t,c in [("Keep the Northwoods ",(196,214,202)),("FLOCK",GOLD_LT),(" Free",(196,214,202))]:
        d.text((x,ty),t,font=f,fill=c); x+=d.textlength(t,font=f)

    y = 104
    # register: "Oct 27 board meeting" + "budget meeting wording"
    d.text((M,y), "BAYFIELD COUNTY BOARD BUDGET MEETING", font=SANSB(23), fill=GREEN); y += 42
    d.text((M,y), "Tuesday", font=SERIF(56), fill=INK); y += 64
    d.text((M,y), "October 27", font=SERIF(104), fill=INK); y += 120       # the one dominant element
    d.text((M,y), "Stand outside at 5:00.", font=SERIFI(38), fill=GREEN); y += 48
    d.text((M,y), "Walk in at 5:50.", font=SERIFI(38), fill=GREEN); y += 60
    d.line([(M,y),(HW-M,y)], fill=GOLD, width=4); y += 26

    # What / when / where.  register: "Oct 27 board meeting", "courthouse address", "sidewalk stand"
    LBL = 190; tx = M + LBL; tw = CW - LBL
    rows = [("5:00 PM CT", "Stand on the E 5th St sidewalk in front of the courthouse"),
            ("6:00 PM CT", "County Board meeting,\nCounty Board Room"),
            ("WHERE",      "Bayfield County Courthouse,\n117 E 5th St, Washburn")]
    for lab, txt in rows:
        d.text((M,y+2), lab, font=SANSB(26), fill=GOLD_DEEP)
        y = max(para(d, tx, y, txt, SANS(28), INK, tw, 35), y+35) + 12
    y += 8

    # Why, in one sentence each. register: "Exec Committee removed the Flock money"
    pad=18; bf=SANS(25); lh=32
    why = ("In September the county's Executive Committee took the Flock camera money out of the 2027 budget. "
           "We're asking the full board to keep it out and to write a countywide policy.")
    lines = wrap(d, why, bf, CW-2*pad-8)
    h = pad + len(lines)*lh + pad - 6
    d.rectangle([M,y,HW-M,y+h], fill=SAGE); d.rectangle([M,y,M+7,y+h], fill=GREEN)
    yy=y+pad-2
    for ln in lines: d.text((M+pad+8,yy), ln, font=bf, fill=INK); yy+=lh
    y += h + 24

    # Reassurance + how to speak.  register: "speaking: name, municipality, sign-in sheet"
    d.text((M,y), "You don't have to speak.", font=SANSB(29), fill=INK); y += 38
    d.text((M,y), "Sitting in the room counts.", font=SANSB(29), fill=INK); y += 42
    y = para(d, M, y, "To speak, sign in with your name and your town.", SANS(25), MUT, CW, 33)

    # CTA band: QR + imperative caption + printed URL fallback, then the footer.
    BANDH = 236; by = HH - BANDH
    print("body ends", y, "band", by)
    assert y + 24 <= by, f"body overflows into the QR band: y={y}, band={by}"
    d.rectangle([0,by,HW,HH], fill=GREEN_DK); d.rectangle([0,by,HW,by+6], fill=GOLD)
    QR = 160   # 1.1 in at 150 dpi; the 4-module quiet zone is inside the image
    img.paste(qr_img(QR), (M, by+22))
    qx = M + QR + 28; qw = HW - M - qx
    yy = by + 34
    d.text((qx,yy), "Scan for the facts.", font=SERIF(32), fill=PAPER); yy += 46
    yy = para(d, qx, yy, "A summary of what the county's records show:", SANS(21), (214,228,218), qw, 28)
    x = qx; fu = SANSB(24)
    for t,c in [("northwoodsflockfree",GOLD_LT),(".com",PAPER)]:
        d.text((x,yy+6), t, font=fu, fill=c); x += d.textlength(t, font=fu)
    assert x <= HW - M + 4, "URL overflows the band"
    d.line([(qx,HH-50),(HW-M,HH-50)], fill=(70,120,94), width=2)   # starts right of the QR so it never cuts the quiet zone
    foot = "A nonpartisan effort of Northwoods neighbors  ·  Dated " + ASOF
    fw = d.textlength(foot, font=SANS(17))
    d.text(((HW-fw)/2, HH-40), foot, font=SANS(17), fill=(200,218,205))
    return img

def page():
    # Two copies on a landscape letter page (11 x 8.5 in = 1650 x 1275) with a dashed cut line.
    one = half()
    pg = Image.new("RGB", (2*HW, HH), (255,255,255))
    pg.paste(one, (0,0)); pg.paste(one, (HW,0))
    d = ImageDraw.Draw(pg)
    for yy in range(0, HH, 24):
        d.line([(HW,yy),(HW,yy+12)], fill=(150,150,150), width=2)
    return pg

def save(pg):
    os.makedirs(REPO, exist_ok=True)
    pg.save(os.path.join(REPO, NAME + ".pdf"), "PDF", resolution=150.0)
    prev = pg.resize((1100, round(pg.height * 1100 / pg.width)), Image.LANCZOS)
    prev.save(os.path.join(REPO, NAME + ".png"))
    if os.path.isdir(FLOCK_DIR):
        pg.save(os.path.join(FLOCK_DIR, NAME + ".pdf"), "PDF", resolution=150.0)
        pg.save(os.path.join(FLOCK_DIR, NAME + ".png"))
    else:
        print("FLOCK_DIR not found, print master not written:", FLOCK_DIR)

save(page())
print("done ->", REPO)
