# AE Bogotá Website

*Last updated: 2026-04-08*

## Overview
Static bilingual (ES/EN) website for **AE Bogotá** (rebranded from EA Bogotá). Full editorial redesign completed 2026-04-07, matching effectivealtruism.org aesthetic. Major content additions 2026-04-08.

**Location:** `G:\Mon Drive\EA Bogotá\website\`
**Stack:** Pure HTML/CSS/JS, no framework
**Local dev:** `http://localhost:9876`

## All Pages Complete
1. `index.html` — Hero, "What is EA?" two-col, Four Ideas, Colombia Impact (6 orgs), Newsletter, Ways to Help (6 cards), Quote, Footer
2. `about-ea.html` — Full EA.org intro essay translation, sidebar TOC, audio player, footnotes, FAQ, share button
3. `team.html` — Organizadores (2-col layout) + Cumbre team (Hugo, Jay, Manuela in grid-3)
4. `events.html` — Lu.ma calendar embed, 4 event types, volunteer CTA
5. `get-involved.html` — 1-on-1, Events, University Groups (Tally form NpJlYN), Newsletter, Volunteer, dark CTA
6. `resources.html` — Videos, Books (free copies via Airtable), Podcasts, Careers, Giving, Funding, Spanish Resources, AE en LATAM
7. `about-us.html` — History, stats, CTA (not linked from nav)

## Updates (2026-04-08)
- **Nav order changed:** Aprende → Recursos → Participa → Eventos → Equipo → Conferencias (external)
- **Colombia Impact section** added to index.html: IPA, ACTRA, Sinergia Animal, Fundación Veg, GRANA, ORCG
- **Ways to Help** overhauled: 6 cards with local images (course, donate, career, join, conference, funding)
- **University Groups section** added to get-involved.html with Tally form
- **Cumbre team section** added to team.html (Hugo Ikta, Jay Muñoz, Manuela García)
- **Favicon:** Official EA lightbulb-heart logo (PNG, square-padded from portrait source)
- **Roles renamed:** "Colaborador/a" → "Organizador/a" across team page
- **EN toggle fix:** `.lang-toggle button { display: inline-block !important; }`
- **Email removed:** contacto@eabogota.org not accessible, removed from all footers

## Design System (v6 — 2026-04-07)
- **Palette:** `#f4efe9` (paper), `#ebe5dd` (sand), `#000000` (dark sections/footer), `#c9d7d8` (muted teal), `#f59469` (salmon CTA), `#F18251` (coral), `#0c859a` (link teal)
- **Typography:** Inter everywhere, Source Serif 4 only for blockquotes
- **Buttons:** 0px radius, black bg, white text
- **1-on-1 button:** Subtle chip style (teal text, light teal bg, no border)

## Technical Notes
- **Bilingual system:** `data-lang` attributes, CSS toggle, JS localStorage persistence
- **Image processing:** Google Drive PIL bug (0KB PNGs) — save to temp first, then copy. AVIF needs `pillow-avif-plugin`.
- **Images source folder:** `C:\Users\joseg\OneDrive - Universidad de los andes\Jose\Imágenes`

## Deployment
- **Vercel project:** "website" (prj_7ryoaaodE6EU435vu9ofv2kg4iNh)
- **Live:** https://website-three-orpin.vercel.app
- **Deploy:** `cd "G:\Mon Drive\EA Bogota\website" && npx vercel --prod --yes`

## Pending
- [ ] Push changes to GitHub
- [ ] Buttondown newsletter integration
- [ ] Cal.com setup for 1-on-1 scheduling
- [ ] Custom domain (eabogota.org)
- [ ] Regenerate audio with better TTS if OpenAI credits added
