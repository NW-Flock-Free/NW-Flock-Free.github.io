# build/ - the flyer and social-card build scripts

These are the **canonical** sources for the artifacts in `downloads/`. They were moved
here from the campaign working folder on 2026-09-12, because the artifacts were
version-controlled and their sources were not, and three flyers kept printing retired
claims for two months as a result.

⛔ **A claim fix changes the script and the artifact it produces in the same commit.**
Every claim these scripts print must have a row in `claims-register.md`. Read a script
before changing it - the claim strings carry per-line comments naming the register row
each figure traces to.

⚠ **This repo is public**, and GitHub Pages serves it. Anything added here is browsable
on GitHub and downloadable from northwoodsflockfree.com. Do not put anything in these
files you would not publish.

## What each script produces

| Script | Produces |
| --- | --- |
| `build_flyers_round2.py` | `flock-101-onepage` (PDF + PNG). Also defines a retired `tearoff()` and a pending `records()`; neither is called. |
| `build_douglas_round2.py` | `douglas-county-findings-one-pager` (PDF + PNG) |
| `build_flyers_bayfield_round2.py` | `bayfield-who-is-watching` (PDF + PNG). Also defines a retired `turn_cameras_off()`; not called, marked do-not-re-enable. |
| `build_bayfield_mobile.py` | `bayfield-mobile.svg` |
| `build_douglas_mobile.py` | `douglas-mobile.svg` |

`douglas-qr.png` is the sign-up QR image both mobile scripts embed. It is the single
canonical copy; `build_douglas_svg.py`, which still lives in the campaign folder, falls
back to reading it from here.

## The two destinations

Each **flyer** script writes to both:

- the repo's `downloads/` - the PDF and a **1100px-wide preview PNG** (what `downloads.html` shows)
- the campaign working folder - the PDF and the **full-size 1275x1650 print master**

⚠ **"In sync" does not mean byte-identical.** The PDFs match by hash; the PNGs are
deliberately different resolutions. **Never copy the repo preview over the working-folder
master** - that downgrades the print original. The guarantee is that both came from the
same render in the same run.

The working-folder path is **machine-specific**. It is a single named constant,
`FLOCK_DIR`, at the top of each script - one line to change on a new machine, or set the
`FLOCK_DIR` environment variable. Everything else is derived from the script's own
location, so no local home directory is baked into this public repo. `REPO_DOWNLOADS`
overrides the repo destination the same way.

## Dependencies

- **The three flyer scripts** need only `qrcode` and `Pillow`. They run on Windows as-is.
  They ask for DejaVu fonts by a Linux path; Pillow falls back to the system font
  directory by filename, and `build_flyers_bayfield_round2.py` additionally falls back to
  matplotlib's bundled DejaVu copies.
- **The two mobile scripts** need only the standard library. They emit **SVG only** and do
  not rasterise. The SVG -> PNG step runs elsewhere: `cairosvg` is installed on this
  machine but **broken** (it cannot load `libcairo-2.dll`). Do not try to fix it here.

## Traps

- ⚠ **Never run these with the working directory set to `%TEMP%`.** A stray `enum.py`
  sitting in `C:\Users\<user>\AppData\Local\Temp` shadows the standard library and breaks
  every Python import. Run them from this folder.
- ⚠ **PDFs are not reproducible byte-for-byte.** Pillow stamps `/CreationDate` and
  `/ModDate`, so re-running produces a different PDF for identical content. Compare
  decoded pixels, never file size or hash, when checking whether a rebuild changed
  anything.

## Running

    cd build
    python build_flyers_bayfield_round2.py
