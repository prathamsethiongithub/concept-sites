# concept-sites

Web design concept samples — hand-built, self-contained, motion-first. Every sample is a fictional concept (not client work) with all data labelled as sample data.

**Live:** https://prathamsethiongithub.github.io/concept-sites/

| Sample | Live | What it is |
|---|---|---|
| Mira Studio | [open](https://prathamsethiongithub.github.io/concept-sites/mira-studio/) | Hair, colour & scalp-care studio (fictional). Editorial concept with a GSAP + Lenis motion system, a scroll-reactive strand-field canvas, a consultation-first finder, a 4-step demo booking walkthrough, and a strand-QR that gathers into a scannable code. |

## Layout

Each sample folder contains:

- `index.html` — the deployable page: a static home snapshot (renders without JS) plus the app; CDN libs only. Imagery lives in `assets/` as responsive WebP + JPEG pairs.
- `docs/` — creative brief, full copy, **CHANGELOG.md**, **ASSETS.md** (image sources + licences), and screenshots.
- `_build/` — source parts and the build script (`python _build/build.py` reassembles `index.html`, generates the QR + responsive images; it expects the working image library at `../_direction`, which is not committed).

## Notes

- All samples are `noindex` and visibly labelled as fictional concepts.
- No analytics, no data transmission, no real business details.
