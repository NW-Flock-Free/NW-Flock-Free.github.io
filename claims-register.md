# Claims Register - source of truth for every claim on this site

**What this is:** every factual claim published on northwoodsflockfree.com, with the source it traces to. If anyone challenges a claim, this file is where we go. The footer promise ("Every claim on this site traces to a public record or a reputable report") is enforced HERE.

**Source tiers:** T1 = public record, court filing, statute, or official document (strongest). T2 = reputable press or advocacy-legal org (ACLU, EFF, IJ). T3 = community/unverified (never publish from T3 alone).

**The rule:** no claim goes on the site without a row in this file. Any edit that adds or changes a factual claim MUST update this register in the same commit. (Enforced by `CLAUDE.md` in this repo for AI-assisted edits.)

**Companion file:** the deeper receipts drawer with fact-discipline rules lives at `Community Outreach/Flock/news-receipts-links.md` (working folder, not published).

**Last updated:** 2026-07-12

**Public link:** this file is now linked from the site on `resources.html` ("The claims on this site, and where they come from"): https://github.com/NW-Flock-Free/NW-Flock-Free.github.io/blob/main/claims-register.md

---

## index.html

- **"100,721 vehicles logged in one 30-day period in Bayfield County"** (also on areas, stats band) - Bayfield County Sheriff's Flock transparency portal / county records obtained under Wisconsin open records law, 2026. Records on file in the campaign folder. [T1]
- **"a county of about 16,000"** - US Census Bureau, Bayfield County population estimate (~16,200). [T1] ✅ STANDARD (Adam, 2026-07-10): "about 16,000" everywhere - site and campaign materials. Sweep drafts still saying 15,000 (op-ed, comment script, LTE) before they go out.
- **"Flock Safety is the biggest company selling them"** - widely reported; see ACLU Flock coverage and EFF Street-Level Surveillance. [T2]
- **"Motorola, Axon, and others sell the same thing"** - EFF, Street-Level Surveillance: ALPRs - https://sls.eff.org/technologies/automated-license-plate-readers-alprs [T2]
- **"The data feeds a national network. Thousands of police departments can search it."** - ACLU, How to Fight Flock - https://www.aclu.org/news/privacy-technology/tracking-alpr-cameras/how-to-fight-deployment-of-flock-and-other-mass-surveillance-license-plate-readers-in-your-community [T2]
- **"more than 20 billion plate scans a month across 5,000-plus communities"** - ACLU, citing Flock's own figures (same link as above). [T2]
- **"~250 agencies in five states could see the data"** - Bayfield County sharing records / transparency portal, 2026. [T1]
- **"0 public votes taken before the cameras went up"** - absence of any vote in Bayfield County Board minutes; confirmed via records request, 2026. [T1]
- **"it has already been searched on behalf of ICE"** - EFF/ACLU on SFPD sharing - https://www.eff.org/deeplinks/2025/09/eff-aclu-sfpd-stop-illegally-sharing-data-ice-and-anti-abortion-states ; The Source (Bend, OR): 279 federal immigration queries in three weeks - https://www.bendsource.com/news/localnews/federal-immigration-officials-made-279-queries-into-bends-flock-safety-data-in-its-first-three-weeks/ [T2]
- **"Bayfield County's contract [renews] this fall"** - Bayfield Flock contract (auto-renewal clause, written-notice requirement); copy on file: `Bayfield Flock Contract.pdf`. [T1]
- **Hero photo + caption: "This one is on US-63 in Cable, Bayfield County. It logs every car that passes."** (photo `images/flock-camera-cable-hero.jpg`, full version on areas.html) - photo taken by the campaign on US-63 in Cable at the Wild River Trail / Birkebeiner junction, 2026-07. Camera location backed by: (a) Bayfield County records confirming a Flock camera on US-63 in Cable [T1]; (b) OpenStreetMap node 12895308161 at 46.2070163, -91.2954992 tagged man_made=surveillance, surveillance:type=ALPR, direction 350, mapped 2025 - matches the photographed pole's position and facing [T3 corroboration, not relied on alone]. "It logs every car that passes" restates the register-backed ALPR baseline (ACLU/EFF rows above). [T1 + T3 corroboration]

## the-issue.html (nine reasons - each card also links its source on-page)

Card order reworked 2026-07-11 (round-2 SOW C.2): the "no warrant, can't opt out" card moved to position 2; the rest renumbered. Two titles softened for accuracy (C.3, C.4): card 5 now reads "Errors get innocent people stopped - sometimes even at gunpoint" and card 6 now reads "Officers can misuse it." Claims and sources are unchanged; only the display order and two headings changed. List below is in the new on-page order.

1. **Only ~0.05% of collected data related to a crime when captured** - EFF, Data Driven 2 (63 California agencies) - https://www.eff.org/deeplinks/2021/04/data-driven-2-california-dragnet-new-dataset-shows-scale-vehicle-surveillance [T2]
2. **Searchable with almost no reason, no warrant; law requires displaying a plate** - ACLU, How to Fight Flock (above) [T2]
3. **Pattern-of-life profiling (where you sleep, pray, drink)** - ACLU, "You Are Being Tracked" - https://www.aclu.org/feature/you-are-being-tracked [T2]
4. **Shared with ICE for deportations; Texas sheriff searched nationwide for a woman who had an abortion; DEA considered logging gun-show attendees** - EFF/ACLU SFPD piece (above); ACLU on the DEA gun-show plan - https://www.aclu.org/news/national-security/dea-planned-monitor-gun-show-attendees-license-plate-readers-new-emails-reveal [T2]
5. **Errors get innocent people stopped, sometimes even at gunpoint: up to 1 in 10 reads wrong in independent tests; gunpoint stops (San Francisco woman, Aurora CO Black family)** - Institute for Justice - https://ij.org/dozens-of-innocent-motorists-have-been-pulled-over-detained-at-gunpoint-or-jailed-due-to-ai-license-plate-camera-errors/ ; ACLU (Denise Green) ; Denver7 (Aurora) [T2]
6. **Officers can misuse it: Kansas police lieutenant charged with using Flock to stalk his estranged wife** - KWCH - https://www.kwch.com/2022/11/04/kechi-police-lieutenants-arrest-puts-flock-technology-under-scrutiny/ [T2] (charged, not convicted - keep that wording)
7. **A federal surveillance vendor was hacked and traveler data ended up online** - EFF on ALPR vulnerabilities - https://www.eff.org/deeplinks/2024/06/new-alpr-vulnerabilities-prove-mass-surveillance-public-safety-threat (Perceptics breach; also Washington Post 2019) [T2]
8. **Edge-of-town cameras log everyone entering/leaving (virtual gated community)** - EFF, Street-Level Surveillance - https://sls.eff.org/technologies/automated-license-plate-readers-alprs [T2]
9. **Mission creep: school-residency checks, background checks, unpaid fees** - EFF, May 2026 - https://www.eff.org/deeplinks/2026/05/more-license-plate-reader-mission-creep-school-residency-verification-background [T2]

## areas.html

- **Bayfield: 8 Flock cameras county-wide, one confirmed on US-63 in Cable; plates kept 30 days; shared with ~250 agencies in five states** - Bayfield County records + Flock transparency portal, 2026. [T1]
- **Photo + caption: "One of Bayfield County's eight cameras: US-63 in Cable, quietly logging every car through town."** (`images/flock-camera-cable.jpg`) - same evidence chain as the index hero photo row: campaign photo 2026-07 + county records [T1] + OSM ALPR node 12895308161 at the same spot [T3 corroboration]. "Eight cameras" per the row above. [T1 + T3 corroboration]
- **Bayfield contract auto-renews unless the county declines in writing; decision this fall** - `Bayfield Flock Contract.pdf` (on file). [T1] Exact deadline still being pinned down - update this row and the site when confirmed.
- **Ashland: on May 27, 2026 the police chief notified Flock the city would not renew and asked for removal; told the City Council the same day; department found the cameras unreliable** - Fox21 - https://www.fox21online.com/news/political/ashland-police-department-to-remove-flock-cameras-from-city/article_794afeda-e1e4-4762-84c0-3952d291204c.html + Ashland City Council meeting, 5/27/2026. [T1/T2]
- **Sawyer: sheriff runs cameras in the Hayward area; no published use policy or public transparency portal that we can find** - SOFTENED wording (Adam, 2026-07-10; replaces the unsourced "still drafting its use policy as of late 2025"). Absence-based claim: verified by checking Flock's transparency portal index and Sawyer County's public postings, July 2026. Re-check before repeating in print; upgrade to a dated claim only if a record or article gets pinned. [T1-observation]
- **Sawyer has not turned on a public transparency portal** - absence check against Flock's transparency portal index (transparency.flocksafety.com), checked July 2026. Re-check before repeating in print. [T1-observation]
- **Douglas: 19 camera units at nine locations; free trial - no signed contract, no money paid; county seeking grant money; no written use policy; no transparency portal; sharing list includes Texas, Minnesota, Michigan, tribal agencies, and Wisconsin; no public body voted** - Douglas County records obtained under Wisconsin open records law, July 2026. On file: `Douglas County Flock Records.pdf`, `Douglas County Camera Locations.pdf`, `Douglas County Flock Summary.pdf`. [T1]

## how-we-win.html

- **Verona, WI ended its Flock contract** - Bolts - https://boltsmag.org/verona-wisconsin-ends-contract-flock-ai-surveillance-cameras/ [T2]
- **Oshkosh canceled its renewal (council voted after the chief said he could no longer recommend the product)** - Wisconsin Watch - https://wisconsinwatch.org/2026/05/wisconsin-flock-camera-ai-surveillance-backlash-police-privacy-dane-county-milwaukee/ [T2]
- **Dane County pulled its cameras** - Wisconsin Watch (same piece). [T2]
- **New Hampshire deletes non-hit plate data within three minutes** - N.H. RSA 261:75-b (statute). [T1]

## faq.html

- **Carpenter ruling: police need a warrant for phone location history** - Carpenter v. United States, 585 U.S. 296 (2018). [T1]
- **Courts have mostly let police read plates without a warrant** - legal landscape summary; see EFF ALPR litigation coverage (note: Schmidt v. Norfolk and related 4A challenges are live - keep wording as "mostly"). [T2]
- **Flock's own training videos describe tracking a vehicle "from location to location to location"** - InvestigateTV - https://www.investigatetv.com/2026/06/15/flock-says-its-cameras-dont-track-people-its-own-training-videos-say-otherwise/ [T2]
- **30-day default retention, flagged data kept longer, 30 days is a setting not a legal limit** - Flock documentation + transparency portals. [T2]
- **0.05% figure** - same EFF Data Driven 2 source as the-issue card 1. [T2]

## news.html

Every list item on the news page links directly to its own source - the page is self-sourcing. Governance for adding items (verify link, date it, label source type, don't overclaim) lives in `news-receipts-links.md` in the campaign working folder.

## Site-wide / footer

- **"Every claim on this site traces to a public record or a reputable report"** - this file is that trace. If a claim can't get a row here, it doesn't ship.

## Flyers (downloads) - claims that appear on flyers but not on a site page

Added 2026-07-13 for the reworked Flock 101 (the abuse list). KB grounding: `flock-safety-and-alpr-opposition/module-04` (proven-tier items only; Aurora-style unconfirmed-Flock cases and advocacy aggregate tallies deliberately excluded). Format per `grassroots-organizing-and-protest-playbook/module-04`: three-second test, one message / one ask, recruit-don't-preach question frame, taxpayer value frame. **QR reclassification (Adam, 2026-07-13):** Flock 101 is now the campaign's RECRUITMENT flyer, so its QR points to the sign-up form (forms.gle/V1HjseDto6eLX1FW8, the approved contact-capture channel) per the grassroots module's recruitment-flyer spec ("goal: get a name") - superseding the K.3 educational-flyer site-QR rule for this one flyer. The printed URL remains northwoodsflockfree.com as the no-scan fallback. Flyer footers also restored to "A nonpartisan effort of Northwoods neighbors" alongside the as-of date ("Not anti-police" stays removed from all docs).

- **"At least 18 officers have been caught using these cameras to stalk a romantic interest"** - Institute for Justice compilation (count as of April 2026) - https://ij.org/police-have-reportedly-used-license-plate-readers-to-stalk-romantic-interests-at-least-14-times-in-recent-years/ [T2] (proven as a compilation; re-check the count before any reprint)
- **"A Texas officer searched 83,000 cameras nationwide for a woman who had an abortion"** - 404 Media (Johnson County TX logs: 6,809 networks / 83,345 cameras) - https://www.404media.co/a-texas-cop-searched-license-plate-cameras-nationwide-for-a-woman-who-got-an-abortion/ ; EFF - https://www.eff.org/deeplinks/2025/05/she-got-abortion-so-texas-cop-used-83000-cameras-track-her-down [T2]
- **"Local police have run thousands of lookups on behalf of ICE, with no contract and no warrant"** - 404 Media (Danville IL FOIA: 4,000+ nationwide/statewide lookups for federal or immigration purposes; Flock had no ICE contract) - https://www.404media.co/ice-taps-into-nationwide-ai-enabled-camera-network-data-shows/ [T2]
- **"A San Diego man spent about a month in jail over a misread. He was five miles away."** - Times of San Diego, 2026-06-07 - https://timesofsandiego.com/crime/2026/06/07/a-flock-license-plate-reader-linked-a-san-diego-man-to-a-violent-crime-he-was-five-miles-away/ [T2]
- **"0 public votes ... the usual story"** - generic-flyer framing of the register-backed local rows (Bayfield and Douglas: 0 votes, county records [T1]); hedged with "usual" because some jurisdictions did vote. Not a claim that no town anywhere voted.

---

## Known inconsistencies to resolve

**Round-2 update (2026-07-11):**

- **Facebook-group QRs eliminated.** The three educational flyers that shipped with a Facebook-group QR (`flock-101-onepage`, `wi-flyer-tearoff-halfsheet`, `wi-records-request-onepager`) were rebuilt from scratch with a reproducible source, `Community Outreach/Flock/build_flyers_round2.py`. Their QRs now point to the site (https://northwoodsflockfree.com), every claim on them traces to this register, and population reads 16,000. No published flyer QR now points at the Facebook group. Sign-up QRs on the Bayfield and Douglas flyers correctly stay on the Google sign-up form (contact-capture channel).
- **Records one-pager restyled (2026-07-12).** `wi-records-request-onepager` was replaced with the richer copy-paste layout (What-to-ask list + full draft request + "if they stall" guidance), recolored to the NW Flock Free brand green, built from a new reproducible source `Community Outreach/Flock/build_wi_records_onepager.py`. QR still points to the site. The draft request now covers "automated license-plate reader (ALPR)... whether Flock Safety or another vendor" rather than Flock alone. No new site claims added; the statutory cites (19.31-19.39, 19.35(1), "without delay," redaction-not-chargeable, vendor-not-the-custodian) trace to the `wisconsin-public-records-practice` KB module. A blue-leaning teal variant is kept in the working folder as `wi-records-request-onepager-teal.*`; it did not ship.
- **Two-sided WI set rebuilt (2026-07-11).** `why-we-care-final.pdf` / `how-we-fight-back-final.pdf` were rebuilt from a new reproducible source, `Community Outreach/Flock/build_flyers_wi_twosided_round2.py`, replacing the June-25 `build_flyers_v2.py` output. Every claim now traces to a row above: 8 cameras / one on US-63 in Cable / 30-day retention / ~250 agencies in FIVE states / 100,721 in a month / about 16,000 / 0 public votes / renewal this fall (Bayfield rows); Kansas lieutenant charged (KWCH); 1-in-10 + gunpoint (Institute for Justice); Verona, Oshkosh, Dane County ended Flock (how-we-win rows). Dropped for lack of a register row: US-2/WI-13 locations, "since 2022", "Red Cliff 6th planned", "4 states", "Milwaukee officer 170 times", "jailed nearly a month", "Appleton." QR points to the site (educational flyers, SOW K.3). Added to downloads.html.
- **Bayfield pair rebuilt (2026-07-11).** `bayfield-who-is-watching` and `bayfield-turn-cameras-off` were rebuilt from a new reproducible source, `Community Outreach/Flock/build_flyers_bayfield_round2.py`, replacing the June-27 `build_flyers_v3_bayfield.py` output. Now 16,000 + register-backed only. Dropped for lack of a register row: "running since 2022", "Red Cliff added one in 2025", "Wisconsin DOJ", "Milwaukee officer 170 times", "man jailed nearly a month". Every remaining claim traces to a Bayfield / how-we-win row above. QR now points to the site (educational flyers, SOW K.3), replacing the old sign-up-form QR. `build_flyers_v3_bayfield.py` is retired; do not re-run it (still hardcodes 15,000). No more flyer PDFs in `downloads/` print 15,000.
- **Downloads set consolidated + Michigan added (2026-07-12).** (a) Masthead title hierarchy swapped on all shipped print flyers (flyer/context name big, "Keep the Northwoods FLOCK Free" as subtitle) - `build_flyers_round2.py`, `build_flyers_bayfield_round2.py`, `build_flyers_wi_twosided_round2.py` patched; no claim text changed. (b) `douglas-county-findings-one-pager` rebuilt in the standard template from new source `build_douglas_round2.py`; same five findings + "decide it in the open" copy, all tracing to the Douglas row above; the on-flyer "five questions the county board should answer" list did NOT carry over (space); QR now points to the site (was the sign-up form). (c) Retired from the site as duplicates: `why-we-care-final` (duplicated bayfield-who-is-watching) and `bayfield-turn-cameras-off` (superseded by the generic how-we-fight-back); files moved to `downloads/archive/` with the other unpublished artifacts, still world-readable but unlinked. (d) `mi-records-request-onepager` added to downloads.html: Michigan FOIA guide (MCL 15.231 et seq., 5-business-day response + 10-day extension MCL 15.235, itemized-estimate rule MCL 15.234); statutory cites trace to its build session's sourcing, same layout family as the WI one-pager. (e) The restyled `wi-records-request-onepager` (note above) shipped to downloads.html this same day. (f) **Every shipped artifact now carries an as-of date** (Adam, 2026-07-12): print flyers show "Facts as of July 2026" in the CTA band (replacing the removed "A nonpartisan effort... Not anti-police." footer line), social cards show it bottom-right, records one-pagers show "Current as of July 2026" in the footer. Update the date string in the build scripts whenever a stat row changes, then rebuild - a stale as-of date is itself a claim. (g) `build_wi_records_onepager.py` suffix mapping corrected to match disk + this register: unsuffixed = shipped brand green, `-teal` = working-folder variant (the script previously had them swapped, which would have silently shipped the teal on the next rebuild).
- **Site domain.** Permanent site URLs (og:url, canonical, sitemap, robots, flyer QRs) use https://northwoodsflockfree.com (the real domain). The `CNAME` file was added to the repo root 2026-07-11 (round-2 SOW section A.5). Remaining manual steps, both outside the repo: point DNS at GitHub Pages, then set the custom domain + enable Enforce HTTPS in the Pages settings. Until DNS resolves, the site still serves on the temporary github.io URL.

1. RESOLVED on the site 2026-07-10: county population standardized to "about 16,000" (Adam). The published site + `claims-register` say 16,000. STILL CARRYING 15,000 as of 2026-07-11 (working folder, not the site): the RETIRED build scripts `build_flyers_v2.py` and `build_flyers_v3_bayfield.py` (they hardcode 15,000 — do not re-run; every flyer PDF now shipped in `downloads/` was rebuilt to 16,000 on 2026-07-11 via `build_flyers_wi_twosided_round2.py` and `build_flyers_bayfield_round2.py`, and no shipped flyer prints 15,000), plus drafts `ally-outreach-emails.md`, `bayfield-asset-suite-2026-07-10.md`, `bayfield-go-plan-and-readiness.md`, `charly-ray-outreach-email-DRAFT.md`, `email-supporters-bayfield-update-DRAFT.md`, `fb-group-setup.html/.md`, `fb-posts-2026-06-26-welcome-update-resources.md`, `james-thankyou-warm-DRAFT.md`, `launch-post-regional-teamup.md`, `sean-bayfield-heads-up-DRAFT.md`. Sweep to 16,000 before any reprint/resend. (`bayfield-portal-findings.md` already uses 16,000.)
2. RESOLVED 2026-07-10: Sawyer claim softened to the absence-based wording (see areas section). Site copy edit shipped in round-2.
3. **Annual cost `$[COST]`** in campaign materials is pending invoices - when it lands, if the site starts citing cost, add the row here with the invoice as T1 source.

## How to update this file

1. Adding/changing any factual claim on the site, add/update its row in the same commit.
2. New row format: **claim as worded on the site** - source name + URL or on-file document name. [tier]
3. If the source is a paper record, name the exact file in `Community Outreach/Flock/`.
4. Quarterly (or before any big print run): click-check the T2 links; links rot.

<!-- EOF -->
