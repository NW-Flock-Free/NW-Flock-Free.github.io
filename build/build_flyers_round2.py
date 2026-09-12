#!/usr/bin/env python3
"""
Round-2 flyer rebuild (2026-07-11). Reproducible source for three site flyers.
Every QR points to the site (https://northwoodsflockfree.com), NOT the Facebook
group and NOT the sign-up form (educational flyers route to the site per the
QR rule). Every factual claim traces to claims-register.md. Population is 16,000.
Outputs PDF + a 1100px-wide preview PNG for each flyer, into both this folder
and the repo downloads/ folder (via REPO_DOWNLOADS env var).
Run: REPO_DOWNLOADS=/path/to/repo/downloads python3 build_flyers_round2.py
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
MUT=(92,102,96); PAPER=(244,248,242); RED=(178,48,32)

def qr_img(px=176, url=None):
    q = qrcode.QRCode(border=4, box_size=10, error_correction=qrcode.constants.ERROR_CORRECT_Q)
    q.add_data(url or SITE); q.make(fit=True)
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
    # Title-hierarchy swap (2026-07-12): the flyer/context name is the BIG
    # masthead line; "Keep the Northwoods FLOCK Free" is the small subtitle.
    d.rectangle([0,0,W,88],fill=GREEN_DK)
    d.rectangle([0,88,W,95],fill=GOLD)
    d.text((M,16), title, font=SANSB(30), fill=PAPER)
    f=SANSB(22); x=M; ty=54
    for t,c in [("Keep the Northwoods ",(196,214,202)),("FLOCK",GOLD_LT),(" Free",(196,214,202))]:
        d.text((x,ty),t,font=f,fill=c); x+=d.textlength(t,font=f)

def cta(d,img,caption_lines,title="Scan for the facts.",qr_url=None):
    BANDH=300; by=H-BANDH
    d.rectangle([0,by,W,H],fill=GREEN_DK); d.rectangle([0,by,W,by+7],fill=GOLD)
    q=qr_img(190, qr_url); img.paste(q,(M,by+52))
    tx=M+190+34
    d.text((tx,by+56),title,font=SERIF(40),fill=PAPER)
    y=by+112
    for ln in caption_lines:
        d.text((tx,y),ln,font=SANSB(28),fill=(222,236,226)); y+=38
    x=tx
    for t,c in [(SITE_TXT.replace(".com",""),GOLD_LT),(".com",PAPER)]:
        d.text((x,by+204),t,font=SANSB(28),fill=c); x+=d.textlength(t,font=SANSB(28))
    d.line([(M,by+250),(W-M,by+250)],fill=(70,120,94),width=2)
    ctr(d,by+261,"A nonpartisan effort of Northwoods neighbors  ·  Facts as of September 2026",SANS(19),(200,218,205))

def flock101():
    # v4 2026-07-13 (mockup B chosen): side-by-side stat info cards, boxless
    # centered misuse section, red-zero + recruiting-question finale clamped
    # clear of the CTA band. Recruitment flyer: QR -> sign-up form.
    # Claims: register "Flyers" section + index rows. Format: grassroots module-04.
    img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)
    LINE=(216,210,196); SURF=(255,255,255)
    masthead(d,"FLOCK 101: THE CAMERAS EXPLAINED")
    y=126
    for ln in wrap(d,"An AI-powered camera just scanned your plate.",SERIF(58),W-2*M):
        d.text((M,y),ln,font=SERIF(58),fill=INK); y+=68
    y+=6
    y=para(d,M,y,"An ALPR (automatic license-plate reader) photographs every passing car, has AI read the plate, and uploads it to a private company's nationwide search network. Bought with your tax money.",SERIF(25),GREEN,W-2*M,35)
    y+=14; d.line([(M,y),(W-M,y)],fill=GOLD,width=4); y+=32
    # stat cards
    gap=36; cw=(W-2*M-gap)//2; ch=238
    cards=[("0.05%","of what these cameras collect is tied to a crime when captured. The rest is ordinary people driving.","EFF, Data Driven 2"),
           ("20 billion","plate scans a month, across 5,000+ communities, feed one searchable network.","ACLU, citing Flock's figures")]
    for i,(num,txt,src) in enumerate(cards):
        x=M+i*(cw+gap)
        d.rounded_rectangle([x,y,x+cw,y+ch],radius=14,fill=SURF,outline=LINE,width=2)
        d.rounded_rectangle([x,y,x+cw,y+8],radius=3,fill=GOLD)
        nf=SERIF(74 if i==0 else 52)
        d.text((x+(cw-d.textlength(num,font=nf))/2,y+26 if i==0 else y+40),num,font=nf,fill=TEAL)
        ty=y+108; bf=SANS(22)
        for ln in wrap(d,txt,bf,cw-56):
            d.text((x+(cw-d.textlength(ln,font=bf))/2,ty),ln,font=bf,fill=INK); ty+=30
        sf=SANS(17)
        d.text((x+(cw-d.textlength(src,font=sf))/2,y+ch-32),src,font=sf,fill=MUT)
    y+=ch
    # misuse section (boxless, centered column)
    items=[("Stalking.","At least 18 officers caught using these cameras on a romantic interest.","Institute for Justice"),
           ("Abortion hunt.","A Texas officer searched 83,000 cameras nationwide for one woman.","404 Media; EFF"),
           ("ICE lookups.","Thousands run by local police. No contract, no warrant.","404 Media"),
           ("Wrong man jailed.","A San Diego man spent about a month locked up over a misread. He was five miles away.","Times of San Diego")]
    colw=980; bf=SANS(23); bfb=SANSB(23); sf=SANS(17)
    ah=50+22
    for lead,t,src in items:
        n=len(wrap(d,lead+" "+t,bf,colw-34)); ah += n*31 + 19 + 14
    ah-=18
    ZERO_H=238
    band_top=H-300
    free=band_top - y - ah - ZERO_H
    g=max(28,free//3)
    y+=g
    ctr(d,y,"How police have already misused it",SERIF(30),INK); y+=42
    d.rounded_rectangle([(W-90)/2,y,(W+90)/2,y+6],radius=3,fill=GOLD); y+=30
    lx=(W-colw)/2
    for lead,t,src in items:
        d.ellipse([lx,y+9,lx+12,y+21],fill=RED)
        tx=lx+34; maxw=colw-34
        lw2=d.textlength(lead+" ",font=bfb)
        d.text((tx,y),lead,font=bfb,fill=INK)
        first=wrap(d,t,bf,maxw-lw2)
        d.text((tx+lw2,y),first[0] if first else "",font=bf,fill=INK)
        y2=y+31
        rest=" ".join(first[1:])
        if rest: y2=para(d,tx,y2,rest,bf,INK,maxw,31)
        d.text((tx,y2),src,font=sf,fill=MUT)
        y=y2+19+14
    y-=14
    # red zero + question, clamped clear of the band
    zstart=min(y+g+18, band_top-ZERO_H-14)
    zf=SERIF(144); zt="0"; lf=SERIF(50); lt="records of a public vote"
    zw=d.textlength(zt,font=zf); lw=d.textlength(lt,font=lf)
    x0=(W-(zw+30+lw))/2
    d.text((x0,zstart-16),zt,font=zf,fill=RED)
    d.text((x0+zw+30,zstart+66),lt,font=lf,fill=INK)
    yq=zstart+156
    ctr(d,yq,"No record of a public vote. No way to opt out. That is the usual story.",SANS(21),MUT); yq+=40
    ctr(d,yq,"Should a private company track everyone who drives through your town?",SERIFI(26),GREEN_DK)
    cta(d,img,["Scan to add your name. Neighbors","only - no spam, just meeting dates:"],title="This is happening near you.",qr_url="https://forms.gle/V1HjseDto6eLX1FW8")
    save(img,"flock-101-onepage")


def tearoff():
    img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)
    masthead(d,"Ashland & Bayfield County, Wisconsin")
    y=150
    for ln in wrap(d,"Who is watching the roads?",SERIF(62),W-2*M):
        d.text((M,y),ln,font=SERIF(62),fill=INK); y+=72
    y+=10
    y=para(d,M,y,"Cameras across Bayfield County photograph and log every car that passes. From the county's own public records:",SERIFI(26),GREEN,W-2*M,36)
    y+=26
    stats=[("100,721","vehicles logged in a single 30-day period, in a county of about 16,000 people"),
           ("~250","agencies across five states can search the data"),
           ("0","records of a public vote before the cameras went up")]
    for num,label in stats:
        d.text((M,y),num,font=SERIF(60),fill=TEAL)
        lx=M+d.textlength(num,font=SERIF(60))+28
        yy=para(d,lx,y+6,label,SANSB(24),INK,W-lx-M,30)
        y=max(yy,y+66)+22
    d.rectangle([M,y,W-M,y+120],fill=SAGE); d.rectangle([M,y,M+7,y+120],fill=GREEN)
    para(d,M+28,y+22,"Towns like Ashland, Verona, and Oshkosh have already dropped Flock. Bayfield can too.",SANSB(22),INK,W-2*M-56,30)
    y+=120+34
    ctr(d,y,"Learn the facts and get involved:",SANS(24),INK); y+=42
    x=(W - d.textlength(SITE_TXT,font=SANSB(34)))/2
    for t,c in [(SITE_TXT.replace(".com",""),GREEN),(".com",TEAL)]:
        d.text((x,y),t,font=SANSB(34),fill=c); x+=d.textlength(t,font=SANSB(34))
    ty=H-160
    d.line([(0,ty-18),(W,ty-18)],fill=(150,150,150),width=2)
    n=8; tabw=W/n
    for i in range(n):
        xx=i*tabw
        if i>0:
            for yy in range(ty-12,H,14): d.line([(xx,yy),(xx,yy+7)],fill=(170,170,170),width=1)
        q=qr_img(74); img.paste(q,(int(xx+tabw/2-37),ty))
    ctr(d,H-36,"Scan any tab  -  "+SITE_TXT,SANSB(20),GREEN_DK)
    save(img,"wi-flyer-tearoff-halfsheet")

def records():
    img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)
    masthead(d,"A plain guide for Wisconsin residents")
    y=150
    for ln in wrap(d,"Find out what is watching your town.",SERIF(54),W-2*M):
        d.text((M,y),ln,font=SERIF(54),fill=INK); y+=64
    y+=8
    y=para(d,M,y,"Wisconsin's open-records law lets any resident ask for these records. It is free or low-cost and takes about five minutes. Send your request to the county sheriff, your city police department, and WisDOT.",SERIFI(25),GREEN,W-2*M,35)
    y+=20; d.line([(M,y),(W-M,y)],fill=GOLD,width=4); y+=36
    d.text((M,y),"Ask for, in writing:",font=SANSB(26),fill=INK); y+=44
    asks=["How many cameras there are, and their exact locations",
          "The full annual cost, the contract term, and the renewal date",
          "How long plate data is kept (the retention period)",
          "The full list of agencies the data is shared with",
          "Any written policy for who may search it and why",
          "Whether a public transparency portal is turned on"]
    for a in asks:
        d.ellipse([M,y+6,M+12,y+18],fill=GREEN)
        para(d,M+30,y,a,SANS(23),INK,W-2*M-30,30); y+=44
    y+=10
    d.rectangle([M,y,W-M,y+190],fill=SAGE); d.rectangle([M,y,M+7,y+190],fill=TEAL)
    d.text((M+28,y+20),"A request you can copy:",font=SANSB(22),fill=INK)
    para(d,M+28,y+56,"\"Under Wisconsin's public records law, I request copies of all records regarding automated license-plate reader (Flock) cameras operated by or for your agency: number and locations of cameras, cost and contract, data-retention period, data-sharing agreements, and any use policy. I request a fee waiver or an estimate before any charges.\"",SERIFI(20),INK,W-2*M-56,27)
    cta(d,img,["Full guide, templates, and what","other towns found:"])
    save(img,"wi-records-request-onepager")

def save(img, name):
    img.save(os.path.join(OUT,name+".pdf"),"PDF",resolution=150.0)
    img.save(os.path.join(OUT,name+".png"),"PNG")
    prev=img.resize((1100,int(H*1100/W)))
    prev.save(os.path.join(REPO,name+".png"),"PNG")
    img.save(os.path.join(REPO,name+".pdf"),"PDF",resolution=150.0)
    print("built",name)

flock101()  # tearoff retired from the site 2026-07-12; records() pending the blue-flyer replacement - do not rebuild without checking downloads.html
print("done")
