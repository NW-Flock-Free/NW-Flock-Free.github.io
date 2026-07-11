# CLAUDE.md - rules for any AI session editing this site

This file auto-loads in every Claude Code / Cowork session that touches this repo. Follow it.

## The claims rule (most important)

**Every factual claim on this site must have a row in `claims-register.md`.**

- Adding or changing a claim on any page → add/update its register row **in the same session, before the work is called done**.
- No row possible (no source) → the claim does not ship. Mark it out or ask Adam.
- Format and tier definitions are at the top of `claims-register.md`.
- Wording discipline: "charged" not "convicted"; "the records show" not guesses; no exaggeration - one overclaim discredits the whole site.

## Design/content rules

- Plain HTML/CSS/JS, no frameworks, no build step. One shared `style.css` + `nav.js`.
- **Gold contrast rule:** never put bright gold `#e8aa30` text on white/light backgrounds (fails contrast). Use `--gold-deep: #8a6200` for gold text on light; bright gold only on dark green or as graphics.
- Mobile-first; effects must work on tap; honor `prefers-reduced-motion` (reveal fallbacks must never leave content invisible).
- No em dashes in copy. Calm, plain, sourced voice.
- All `og:image`/`og:url` absolute (`https://northwoodsflockfree.com/...`). No `YOURDOMAIN` placeholders anywhere. (The site's permanent domain is `northwoodsflockfree.com`; the old `nw-flock-free.github.io` URL is dead for served pages and appears only in the GitHub repo/blob path.)
- Sticky header is ~70px: anchored sections need `scroll-margin-top`.

## Downloads discipline

- `downloads/` PDFs+PNGs must stay in sync with the campaign working folder: `C:\Users\Adam\Documents\Claude\Projects\Adam's Personal Projects\Community Outreach\Flock`. If either side changes, copy to the other in the same session.
- When a PDF changes, re-render its preview PNG on downloads.html from that PDF (consistent ~1100px width).
- Flyer QR codes point to **https://northwoodsflockfree.com/** (the site), not the Facebook group. Sign-up QRs (forms.gle) are the exception and stay.
- Douglas materials must show 19 cameras / 9 locations (older 12-cam renders are dead - never reuse).

## Git

- Adam pushes from the Code tab himself. If you are a Cowork session: do NOT run git; hand Adam a changed-file list + commit message.
- If you are a Claude Code session Adam asked to commit: stage explicit paths, plain `git push` on `main`.

<!-- EOF -->
