# CLAUDE.md - rules for any AI session editing this site

This file auto-loads in every Claude Code / Cowork session that touches this repo. Follow it.

## The claims rule (most important)

**Every factual claim on this site must have a row in `claims-register.md`.**

- Adding or changing a claim on any page → add/update its register row **in the same session, before the work is called done**.
- No row possible (no source) → the claim does not ship. Mark it out or ask Adam.
- Format and tier definitions are at the top of `claims-register.md`.
- Wording discipline: "charged" not "convicted"; "the records show" not guesses; no exaggeration - one overclaim discredits the whole site.
- **Count published items from `git diff`, never from a heading.** claims-register.md headings describe what someone intended to stage. On 2026-09-12 a batch described as "Two curated links" shipped four, and two went live with no row. Before any publish, diff the file and enumerate what is actually being added.

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

## Branching (PR only - and the merge is a fast-forward)

`main` has **no branch protection enabled** on GitHub as of 2026-09-12, and Adam has decided to leave it that way. A direct push would succeed. The PR flow below is therefore honor-system, and it is not optional: this is an open-records project where one wrong published number costs more than any amount of process is worth.

1. `git checkout main && git pull origin main` - start from an up-to-date main
2. `git checkout -b <type>/<slug>` - branch BEFORE staging, so local `main` never diverges
3. edit, then `git add -- <explicit paths>` - never `git add -A`. The working tree routinely carries unrelated in-progress edits (claims-register.md, news.html, downloads/bayfield-who-is-watching.*) that must NOT be swept into a commit. If your change touches a file that already has uncommitted work in it, `git stash push -- <that file>` first, edit, commit, then `git stash pop`.
4. `git commit -m "<message>"`
5. `git push -u origin <branch>`
6. `gh pr create --base main --fill`. The PR is the audit record. Wait for Adam's review, UNLESS he has already approved the change in chat (a weekly news refresh he signed off on, for example) - then merge immediately.
7. `git checkout main && git merge --ff-only <branch> && git push origin main`
8. `git push origin --delete <branch>` and `git branch -d <branch>`

**Why fast-forward and not squash.** `claims-register.md` cites commits by hash. Squash and rebase both rewrite the commit, so a hash recorded against a claim would no longer exist on `main`. Fast-forward preserves it. If `--ff-only` is refused because main moved, rebase the branch onto main and try again - never fall back to a merge commit.

This is the one sanctioned push to `main`: a fast-forward of a branch that has already been through a PR. Never push unreviewed work to `main`.

No status checks are configured on this repo, so there is nothing to wait for - do not run `gh pr checks --watch`, it will hang forever. If a check is ever added: never merge while it is failing or pending, and never disable one to force a merge. Stop and report.

### Pushing requires the second GitHub account

Two `gh` accounts are authorized on this machine. `buildwithbaker` is the default and does **not** have push access to the NW-Flock-Free org - it fails with a 403. The repo's git identity is already Northwoods Flock Free, but `credential.helper` is `store` and the cached credential belongs to buildwithbaker, so identity and credential disagree.

    gh auth switch --user NW-Flock-Free
    git -c credential.helper= -c credential.helper="!gh auth git-credential" push -u origin <branch>
    gh auth switch --user buildwithbaker      # leave the machine as found

The `-c credential.helper=` override is required; without it `store` re-supplies the wrong cached credential even after the account switch.

### Shell note

The shell is PowerShell - there are no heredocs. `git commit -F - <<'MSG'` is a parser error. Write the commit message or PR body to a temp file, pass `-F` / `--body-file`, then delete the temp file.

### Image acceptance

Never accept a rebuilt PNG on file size. Transfers re-encode PNGs and the byte count will differ for a pixel-identical image. Compare decoded pixels instead.

### If you are a Cowork session

Do NOT run git at all. Hand Adam a changed-file list, a commit message, and a paste-ready Claude Code prompt that performs the flow above. (This rule was broken on 2026-09-12 by a Cowork session that ran the branch/PR flow itself. The rule stands.)
