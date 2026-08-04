# LifeCove

**Current status: Under Construction.** LifeCove is a downstream immersive application shell connecting Startup and Commissioning, Headquarters, Paul, Visible Privacy, Living Library, Opportunity Center, Accidental Wonders, and This Is What Happened.

LifeCove is governed by the parent repository [kikkio00-sys/non-friction-designs](https://github.com/kikkio00-sys/non-friction-designs). Parent standards are referenced, not copied here.

## Stack
Next.js App Router, React, strict TypeScript, Tailwind CSS, npm, Vitest, React Testing Library, Playwright.

## Local setup
```bash
npm install
npm run dev
```
Open http://localhost:3000.

## Scripts
- `npm run typecheck`
- `npm run lint`
- `npm test`
- `npm run build`
- `npm run test:e2e`

## V0.1 scope
Included: mobile-first shell, commissioning flow, Headquarters, Visible Privacy, typed Experience Registry, placeholders, privacy/security notes, accessibility foundation, and tests.

Excluded: live authentication, database, analytics, trackers, paid services, native app, WebGL/game engine, final artwork, live integrations, payments, affiliate systems, and fake security claims.

## Project structure
Application code lives in `src/`; docs live in `docs/`; static assets live in `public/`.

## Privacy and accessibility posture
V0.1 stores only temporary commissioning progress in browser local state, uses no trackers, and makes no claim of server-side authorization. Future authorization must be enforced server-side. The shell starts with semantic landmarks, one meaningful h1 per page, keyboard navigation, visible focus states, skip link, labels, reduced-motion support, and decorative visuals marked appropriately.
