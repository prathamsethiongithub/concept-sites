# Mira Studio — concept brief v1

> **Fictional concept website. Not a real business or client project.** Demo only — every price, hour and profile below is sample data created for this concept.

**Status:** Proposal for review. Next step: Pratham picks a visual direction (three live swatches attached), then I build → deploy (free plan) → test the live version.

---

## 1 · The visitor

Women and men, roughly 22–45, in metro India, choosing a hair and skin studio. They are design-aware, mildly time-poor, and allergic to the usual salon noise — "best salon in [city]", five-star badges, phone-tag for a slot. They decide visually and they decide fast.

## 2 · The visitor's main task (the one job)

**Find a service with its duration and sample price, then request an appointment — without hunting.**

Every route funnels to this. If a visitor can't answer *"what does a haircut cost, how long is it, and can I ask for a time?"* inside ~30 seconds on a phone, the site has failed.

## 3 · Brand direction (fixed by the build brief)

Editorial beauty studio. **Warm ivory, espresso, one muted rose accent.** Strong typography, well-cropped hair/beauty photography, quiet motion. No template-like gradient cards.

Voice: warm, confident, specific. No superlatives, no fake ratings, no invented client praise.

## 4 · Visual directions — pick one (swatches: `_direction/mira-studio/a|b|c.html`)

| | Direction | Type | Layout signature | Feels like |
|---|---|---|---|---|
| **A** | **Atelier** | Fraunces (serif display) + Instrument Sans | Monumental serif hero, full-bleed image column, hard edges, hairline rules | High-fashion editorial, quiet and monumental |
| **B** | **The Menu** | Schibsted Grotesk + Newsreader italic accents | The priced service menu is the hero motif — dotted leaders, numbered rows, big prices | Calm precision; the visitor can literally *read prices* first |
| **C** | **Evening** | Prata (didone serif) + Manrope | Dark espresso field, ivory didone type, one rose hairline; light/dark alternation | Night-atelier mood; bolder, more dramatic |

Mixing is allowed — e.g. A's typography with B's menu treatment. If you have no preference: **A** is the most faithful to "editorial beauty studio"; **B** if you want the price-clarity message loudest; **C** if you want the more distinctive dark look.

## 5 · Sitemap (5 routes + 404)

- `/` — Home: positioning, categories, selected menu, team, gallery strip, how booking works, FAQs, hours/location, contact.
- `/services` — Services: full menu per category, durations, sample prices, what to expect.
- `/gallery` — Gallery: cropped studio photography with captions.
- `/about` — About: the studio story, values, the space, the (fictional) team.
- `/contact` — Book: demo enquiry form, WhatsApp demo, sample hours, illustrative location.
- `/404` — useful not-found state.

## 6 · Content inventory

| Route | Content blocks |
|---|---|
| Home | Hero + CTA · service categories (4) · selected menu (6 items w/ duration + sample ₹) · team (3 fictional profiles) · gallery strip (4–6) · how booking works (3 steps) · FAQs (6) · hours + location (sample) · contact block |
| Services | Category intro ×4 · full menu (18–22 services, duration + from-price) · "what to expect" notes · CTA |
| Gallery | Intro · 8 captioned images + alt text · CTA |
| About | Story · 3 values · the space · team (fictional, labelled) · CTA |
| Contact | Form intro · fields (name, service, preferred day/window, contact, notes) · demo states · WhatsApp demo · hours · location note · short FAQ |
| All | Nav, footer, persistent fiction notice, demo labels, meta titles/descriptions, OG image |

## 7 · The single primary CTA

**"Book an appointment"** — one label, used on every route. Sticky on mobile (thumb-zone, never covering content or form controls). Secondary: **"See services & prices"**. WhatsApp appears as a *demo* button (modal explains nothing is sent).

## 8 · Enquiry flow (demo-only, honest)

1. Choose a service (from the menu).
2. Choose a preferred day + time window.
3. See a summary card ("Your enquiry") → submit → demo confirmation.

Copy guardrails: availability is confirmed *by the studio* — nothing is ever "reserved". Every state is labelled demo; no data leaves the browser.

## 9 · Signature interaction (one memorable move)

**The appointment slip** — as the visitor picks service + day, a small paper-like slip assembles itself in the corner of the booking section, like a studio booking card being written out. Supporting micro-move: a quiet "sheen" passing across photography on hover (mirror-light), used sparingly.

## 10 · Mobile, accessibility, performance

Tested at 360px and 390px, tablet, 1280px desktop. Semantic headings/landmarks, labelled fields, keyboard access, visible focus, contrast-checked text, alt text, reduced-motion honoured. No scroll-hijacking, no autoplay sound, no animation-only navigation. Lighthouse targets ≥90 mobile where applicable, measured and reported honestly.

## 11 · Honesty rails (from the build brief — non-negotiable)

Persistent "Fictional concept website" notice on every route · inline demo labels beside forms, prices, booking controls · no real addresses or public phone numbers · no map pins · no reviews or ratings · no medical claims · forms validate locally and never transmit · brand name treated as placeholder, not a cleared trademark.

## 12 · SEO preparation

Unique title + description per route (drafted in `COPY.md`), one meaningful H1 per page, clean route names, descriptive links, alt text, social preview image. Public concept **noindex** (meta robots, verified). No LocalBusiness/physician/rating schema.

## 13 · Tech & delivery plan

- **Stack:** plain HTML/CSS/JS, multi-page, no framework, no build step. Content in an editable data file (menus/prices/hours) + hand-authored HTML.
- **Fonts:** Google Fonts (open licences) — recorded in the assets list.
- **Photography:** curated free-licence imagery (Pexels/Unsplash), graded to the palette; each file's source + licence recorded in `ASSETS.md`.
- **Deploy:** new public repo `concept-sites` → **GitHub Pages** (free tier; limits verified before deploy), subfolder `/mira-studio/`, working direct routes, refresh-safe, custom 404.
- **Deliverables:** repo/source, edit instructions, live link, screenshots (phone + desktop), QA notes with measured results.

## 14 · Acceptance test (from the brief)

A visitor can find a haircut's sample price and duration, inspect the gallery, and complete the demo appointment request — on a phone.

---

### Open choices for Pratham

1. **Direction:** A / B / C — or a mix?
2. **Copy:** anything to change in the voice (see `COPY.md`)?
3. Confirm the CTA label stays **"Book an appointment"**.
