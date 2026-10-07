# Mira Studio — v2 change log (2026-10-07)

Rebuilt against the review brief + the strand-QR addendum. Same repo, same URL.

**Live:** https://prathamsethiongithub.github.io/concept-sites/mira-studio/

## 1 · Trust gaps
- Positioning is now consistent everywhere: "Hair, colour & scalp care" (headline, title, meta, about). The skin promise was removed since the menu has no skin services.
- Opening hours come from ONE data source — hero card, contact table and footer are all driven from it (Tue–Sun · 10:00–19:30, Mondays closed).
- Concept labelling kept (top bar, drawer note, footer, per-section notes); noindex kept; no testimonials/logos/awards; stylists stay "Fictional profile".

## 2 · Signature idea — consultation first
- New "Find your starting point" section: two taps (goal → one useful question) → a suggested sample service with a plain reason, duration and starting price → "Continue with this" carries the choice into the booking demo. Optional, skippable, labelled a preference helper (not a diagnosis).

## 3 · Booking demo (complete)
- Four steps: Service → Sample time → Details → Review, then a demo confirmation.
- The slot grid is labelled "Sample availability — no real appointment will be booked" before any selection.
- Review shows service, duration, starting price and the chosen sample slot; Back works without losing selections; Cancel + Start again reset cleanly; "Use sample details" fills dummy values and the page discourages real personal data; nothing is stored or sent.
- Confirmation: "Demo complete — nothing was booked or sent" + what a real studio would do next.

## 4 · Cut and rewrite
- Landing page now: hero → finder → menu edit → one visual section → booking CTA → footer. Story band, team and steps removed from home; FAQ moved to Contact. Repeated words ("considered", "unhurried", "care") swept; vague lines replaced with concrete sample detail.

## 5 · Images
- Same licensed set, one consistent grade; now separate responsive assets (440/880 px, WebP + JPEG). Sources and licences: `docs/ASSETS.md`.

## 6 · Mobile first, motion subordinate
- Checked at 320 / 390 / 768 / 1440: no horizontal overflow; at 390px the promise, primary CTA and hero photo all land within the first screen.
- Small-text contrast raised to WCAG AA (measured 4.8–7.3:1 on the paper tones); mobile menu: focus moves into the drawer, Escape closes, focus returns to the trigger, focus wraps inside; reduced-motion honoured (static QR immediately).

## 7 · Signature interaction (addendum) — strand-QR
- In the booking section the strand system gathers into a real, scannable QR (segno-generated at build time; 37 modules; high contrast; 4-module quiet zone) pointing at this concept's booking page. Tap the QR or "Scatter again / Gather again" to toggle; "Download QR" gives `assets/mira-qr.svg`; a normal "Request an appointment" button sits beside it.
- Mobile + reduced-motion: static QR with a simple fade-in. Canvas only — no new runtime dependencies.

## 8 · Performance / proof
- `index.html`: 958 KB → 120 KB. Images are separate; the hero is preloaded; the page now renders real content without JavaScript (static home snapshot), then the app boots over it.
- Lighthouse mobile, live, 3 runs (2026-10-07; headless Chromium 1208; Lighthouse mobile throttling; GitHub Pages):
  - **Performance: 82 / 79 / 50** → range 50–82 (median 79; run 3 shows Pages/CDN network variance — FCP 4.5s that run)
  - **Accessibility: 100 / 100 / 100**
  - FCP 1.8–4.5 s · LCP 4.0–5.2 s · TBT 190–670 ms · **CLS 0.002 / 0.002 / 0**
- Verified: local full walkthrough (finder, 4-step booking, QR settle/scatter, keyboard, no-JS render) + live deploy checks; screenshots in `docs/screenshots/` (`rebuild-*.png`).

## 9 · Fixes round 2 (review response, same day)
- **Desktop QR canvas spill fixed:** the canvas was being given an inline pixel size that overrode its CSS box, so it overflowed its frame and its drawing never lined up with the static code. It is now sized to its own displayed box (measured: canvas rect == static rect exactly) and fades out once the QR resolves. Settle verified on desktop in ~1s.
- **Jump links fixed:** "Request an appointment" (QR section) and "Find your starting point" (hero) are in-page scrolls now, not hash jumps — they no longer trip the router or land on the 404 view. Both verified: hash unchanged, target lands at the viewport top.
- **Micro-text floor raised:** nothing below ~10.5 px now (most labels 10.5–11 px).
- **Transitions faster:** route transition roughly halved (0.16s out / 0.38s in).
- **Fonts preloaded:** Fraunces + Instrument Sans latin files are preloaded (crossorigin), improving first paint.
- Lighthouse re-run after these fixes (live, mobile, 3 runs): **Performance 76 / 81 / 77**, **Accessibility 100 / 100 / 100**, FCP 1.8–2.2 s · LCP 4.4–4.5 s · TBT 170–290 ms · CLS 0–0.002.

## Remaining issues / notes
- LCP (≈4 s under mobile throttling) is dominated by web-font loading plus GitHub Pages latency; the next step would be self-hosting subset fonts.
- The QR was not machine-decoded here — generated by segno (an established library) with an aligned quiet zone; scan once with a phone to confirm.
- The concept-sites hub still shows the older Mira description (optional update).
