# concept-sites

Web design concept samples — hand-built, self-contained, motion-first. Every sample is a fictional concept (not client work) with all data labelled as sample data.

**Live:** https://prathamsethiongithub.github.io/concept-sites/

| Sample | Live | What it is |
|---|---|---|
| Mira Studio | [open](https://prathamsethiongithub.github.io/concept-sites/mira-studio/) | Hair & skin studio (fictional). Editorial concept with a GSAP + Lenis motion system, scroll-reactive strand-field canvas, and a demo booking slip. |

## Layout

Each sample folder contains:

- `index.html` — the deployable site, fully self-contained (imagery inlined, CDN libs only).
- `docs/` — the creative brief, full copy, and screenshots.
- `_build/` — source parts and the build script (`python _build/build.py` reassembles `index.html`; it expects the working image library at `../_direction`, which is not committed).

## Notes

- All samples are `noindex` and visibly labelled as fictional concepts.
- No analytics, no data transmission, no real business details.
