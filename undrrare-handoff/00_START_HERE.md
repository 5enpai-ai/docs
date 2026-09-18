# 00 — START HERE

**ÜNDRRARE project handoff. Read this document first, completely, before doing anything.**

Built 2026-09-04 from live read-only inspection. See `README_HANDOFF.md` for what
was and wasn't inspectable.

---

## 0. The honesty section (do not skip)

The owner asked for this package to preserve context from prior conversations.
**The session that wrote this had no conversation history at all** — its first
message was the handoff request itself. So:

- Nothing here is a recalled conversation. Everything is derived from primary
  sources read live this session.
- Where reasoning about *why* a decision was made appears in this package, it
  comes from **comments the previous Claude wrote into the theme code itself** —
  which is unusually thorough and is the single best surviving record of intent.
  Those comments are quoted or paraphrased and marked.
- Anything genuinely unrecoverable is listed at the bottom of this document under
  **"What only the owner can tell you."** Ask about those before making
  creative-direction calls.

Also: **the ÜNDRRARE theme Git repository was not accessible.** The theme code
described in this package was read through the Shopify Admin API. The theme's own
code repeatedly cites two repo documents — **`CLAUDE.md`** and
**`PHASE_3_DISCOVERY.md`** — which are the project's actual governing documents
and which nobody could read this session. **Getting those is your first task.**

---

## 1. What ÜNDRRARE is

ÜNDRRARE is an independent streetwear brand and universe run by a solo owner,
operating a Shopify store at **undrrare.shop**. It is not a clothing company that
happens to have branding. It is a world, and the clothing is evidence the world
exists.

The universe has three named layers, and the distinction is load-bearing
throughout the code and copy:

- **ÜNDRRARE** — the parent universe / the store itself.
- **ÜNDR** — *the world.* Underground, technical, archival, detached, confident.
  The letters are an acronym, stated in the store's own Ü-000 collection copy:
  **Ü.NITED N.EVER D.IVIDED R.E:**. Brand line: *"If it ain't ÜNDR, I'm over it."*
  (a caption before it was a shirt).
- **HOSHOKU** — *the character inside the world.* A single creature split down
  the middle: rabbit on one side, fox on the other, joined by a black
  cross-stitch seam. Two personalities — **Bunni** (🐰 sweet, chaotic,
  affectionate) and **Renard** (🦊 cool, dry, protective).

**ÜNDR sells through world + attitude. HOSHOKU sells through character
attachment.** They are never blended into one voice. This is the brand's most
frequently restated rule.

The brand is Atlanta-based, Black-owned, and self-describes across product tags
as anime/otaku streetwear, y2k streetwear, underground fashion, and indie brand.
The first release was **September 2023** (the Ü-000 box logo).

## 2. What is being built

A **world-first Shopify storefront** — a homepage that presents ÜNDRRARE as a
place you enter and explore, rather than a product grid you scroll. Commerce is
reached *through* the world, not instead of it.

The built sequence, live today:

> **PRESS START** (boot overlay) → **World Hub** (five discoverable "world
> objects") → the object you pick scrolls you into the real section for it →
> HOSHOKU experience → ÜNDR/HOSHOKU split → ÜNDR entry product → current chapter
> → shop grid → archive teaser.

The site is deliberately **not** a from-scratch custom build. It is Shopify's
**Horizon** theme with a small, surgical set of custom sections layered on top —
a decision the code comments defend explicitly and repeatedly (see
`10_DECISION_LOG.md`).

## 3. The core creative philosophy

Distilled from the owner's own brand files (`01_BRAND_AND_DESIGN_DNA.md` has the
full text):

- **Don't sell the clothing. Sell the world surrounding it.**
- **VOICE ≠ VOCABULARY.** You do not make something feel on-brand by sprinkling
  brand words ("archive," lowercase, fragments) onto it. The voice comes from
  attitude, restraint, and the brand's relationship with its audience. Reaching
  for the familiar words is named in the brand files as *the* failure mode.
- **Meaning > trend.** The audience's motivating sequence is: *"I wasn't looking
  for another clothing brand. I just happened to find this. I don't completely
  understand it yet. But I like it. And I want to see where this goes."* Urgency,
  discounts and hard sells short-circuit that.
- **Less explanation, more presence.** Lore should be felt before it's explained.
  "wait… what is that?" is a valuable reaction, not a UX failure.
- **Never manufacture scarcity.** "Limited," "small run," "won't restock" are
  factual claims about a specific item. If not confirmed true, leave them out —
  do not infer them because they fit the vibe.

## 4. The website's intended experience

A visitor should feel they **found** something already in motion, not that they
were funneled into a store. The homepage should read as a place with objects in
it. Discovery is the mechanic: you press start, you see things you don't fully
understand, you pick one, and it takes you somewhere real.

Two constraints on that, both already honored in the built code:

- **The world must never trap anyone.** PRESS START is skippable, session-aware
  (shown once per browser session), auto-skipped for reduced-motion visitors and
  in the theme editor, dismissible by click/Escape, and never removes the real
  homepage underneath it. A visitor with JavaScript disabled never sees an
  overlay at all.
- **Every world object is a real link.** Each object in the World Hub is a real
  `<a href>` to a real Shopify product or collection. The smooth-scroll behavior
  is progressive enhancement layered on top. Nothing is a fake destination.

## 5. Current Shopify / theme / repo setup

| | |
|---|---|
| Store | **ÜNDR 🐰/🦊** — `undrrare.shop` |
| Plan | Shopify Basic, USD, EDT, United States |
| Live theme | **`undrrare-theme-phase2-f661bce`** (role MAIN, published 2026-08-28) |
| Base theme | Shopify **Horizon** (theme store ID 2481) |
| Dev theme | **`Development (912126-penguin)`** — last updated **2026-09-03**, *ahead of live* |
| Catalog | 68 products: **13 active**, 24 draft, 31 archived |
| Collections | 8, of which 5 are real ÜNDR/HOSHOKU collections |
| Fulfilment | Mostly **Printify** (print-on-demand); the two beanies are **handmade to order** |
| Theme repo | Exists (the live theme name embeds commit `f661bce`) but **was not accessible this session** |
| This repo | `5enpai-ai/docs` — an **untouched Mintlify starter kit**, unrelated to ÜNDRRARE |

## 6. What has already been completed

All verified live this session.

- **PRESS START boot layer** — `sections/undr-world-boot.liquid` +
  `assets/undr-world-boot.js`. Working, accessible, session-aware, skippable.
- **World Hub with five objects** — `sections/undr-world-hub.liquid` +
  `assets/undr-world-hub.js` + `blocks/_undr-world-object.liquid`. Working, with
  progressive-enhancement scroll and no-JS fallback.
- **Dual-world design token system** — `--undr-*` and `--hoshoku-*` token sets in
  `assets/base.css`, aliased through `--world-*` into Shopify's own `--color-*`
  vars in `layout/theme.liquid`. This makes every existing Horizon component
  world-aware *without modifying any of those components*. Genuinely elegant; do
  not casually replace it.
- **HOSHOKU palette** — approved 2026-08-26, derived by pixel-sampling the
  HOSHOKU reference library. Applied scoped to specific homepage sections, not
  sitewide.
- **Full homepage composition** — nine sections, ordered and populated with real
  copy and real products.
- **Product storytelling format** — an "ARCHIVE SYSTEM / FILE NO. / ARTIFACT /
  CONDITION" structure, written and live on the beanies and the Ü-collections.
  This is genuinely good work; treat it as reference, not as a template to
  mass-apply.
- **Accessibility care** — focus management on boot dismissal and hub scroll,
  reduced-motion gating, and a documented contrast measurement (world-object
  price opacity is 0.7 because 0.6 measured 4.05:1 against HOSHOKU cream, below
  the 4.5:1 AA floor).

## 7. What is currently unfinished

Ordered roughly by how much it matters. Full detail in `05_NEXT_TASKS.md`.

1. **The Development theme is ahead of live and contains fixes that are not
   published.** Specifically it fixes two links that are broken on the live site
   right now (see item 2). It also adds Phase 3 work. Nothing in it is live.
2. **Two live-broken Shopify references on the homepage:**
   - The **"Enter ÜNDR"** CTA in the world-split section points at
     `shopify://collections/core`. That handle does not exist — the real handle
     is `u-000-core`. Fixed in dev, not live.
   - The **"Best Sellers"** product grid points at collection `best-sellers`.
     That collection does not exist. Fixed in dev (repointed to `u-002-seek`,
     retitled "Shop the Collection"), not live.
3. **Phase 3 is mid-flight.** An isolated HOSHOKU collection template
   (`templates/collection.hoshoku.json`) exists in the dev theme with three
   sections. But the `hoshoku` collection's `templateSuffix` is still `null`, so
   even if published it would not render. Its opening statement is explicitly
   marked *"PENDING APPROVAL, see PHASE_3_DISCOVERY.md §0.3 item 1."*
4. **Phase 3 asset slots are built but empty.** Both `atmosphere_image`
   (PRESS_START_BACKGROUND) and per-object `world_artifact_image`
   (WORLD_OBJECT_0n) settings exist and are wired. No image is assigned to any of
   them. The plan recorded in the code: temporary **Meshy** renders now, swapped
   one-for-one for **Higgsfield** renders later, with no markup change needed.
5. **The Story page is a placeholder** — and it is in the main navigation. Its
   own body says *"This page is a placeholder. Replace this copy with the full
   ÜNDR origin story."*
6. **"Journal" is in the nav and points at a blog with zero articles.**
7. **The Archive is a teaser with nowhere to go.** The homepage's archive section
   says "Recovered artifacts. Retired pieces, held rather than discarded.
   Curation in progress." There is no archive collection, page, or link.
8. **The Accessories collection is empty** (0 products).
9. **No world-selection UI.** The `data-world` switch mechanism exists and works,
   but there is no toggle, no selection screen, and no way for a visitor to
   change worlds. The code explicitly calls this future work.
10. **No orbit/float motion in the World Hub.** The section comment says this is
    Phase 3, pending review of the static prototype.

## 8. What must NOT be changed

Summary only — read `06_GUARDRAILS.md` in full before working.

- **Do not blend the ÜNDR and HOSHOKU voices.** Ever.
- **Do not add scarcity/urgency copy** unless the owner confirms the fact.
- **Do not replace the Horizon base theme** or rewrite the site as a custom
  frontend. The whole architecture is built on staying inside Horizon.
- **Do not replace the `--world-*` token indirection** with hardcoded colors or a
  component-by-component rewrite. It is the load-bearing mechanism.
- **Do not make PRESS START unskippable, non-dismissible, or JS-required.**
- **Do not turn world objects into fake/decorative links.**
- **Do not modify the Shopify catalog** (products, prices, statuses,
  collections) as part of theme work. Keep them separate. The owner has
  explicitly restricted this.
- **Do not lower the world-object price opacity below 0.7** without re-measuring
  contrast. It's documented in the CSS with the measurement.
- **Do not add a `*/` sequence inside the block comment in
  `_undr-world-object.liquid`.** The code notes this already silently broke a
  rule once.

## 9. What the next phase should be

Phase 3 is already underway. The direction, read off the dev theme:

1. **Publish the pending fixes** so the live site stops having broken links.
2. **Finish the isolated HOSHOKU collection template** — get the opening
   statement approved, assign the template to the collection, verify, publish.
3. **Fill the Phase 3 asset slots** with world renders (Meshy now, Higgsfield
   later). The slots are designed so this is a settings-only change.
4. **Then** revisit motion (World Hub orbit/float) and the world-switching UI.

## 10. How the receiving Claude should approach this project

- **Read `09_AGENT_PROTOCOL.md` before touching anything.** It is short and the
  owner wrote its rules himself.
- **The previous Claude's code comments are the best surviving documentation.**
  They explain not just what but why, including specificity fights, bugs already
  hit, and measurements taken. Read them before changing the code they annotate.
  They are also where a lot of the project's reasoning lives now that the
  conversation history is gone.
- **Small, reversible, verified.** The existing work is careful and additive —
  new features arrive as opt-in slots that render byte-identically when unset.
  Match that instinct.
- **Separate theme work from catalog work.** Always.
- **When you don't know, say so.** Do not fill gaps with plausible invention.
  This brand's whole value is that it isn't generic; a confident guess that turns
  out generic is worse than a question.

## 11. How to tell whether an idea is on-brand

Run it through these, in order. They're taken from the owner's own brand files.

1. Could a generic clothing brand have done this? → **If yes, it's off-brand.**
2. Does it build the world, or merely advertise the product? → must build.
3. Would the audience recognize who's speaking without the logo? → should be yes.
4. Does it make someone feel they **discovered** something, or that they were
   **targeted**? → discovery, always.
5. Is it trying to *prove* ÜNDR is underground? → **If it has to say it, it
   isn't.** Cut the claim; let the work carry it.
6. Is it confident enough to say less? → if you can cut it, cut it.
7. For HOSHOKU: is there contrast, or is every line maximally cute? Does it read
   like two characters interacting, or one mascot talking? → contrast, and two.
8. Does it manufacture urgency, scarcity, or pressure? → **If yes, remove it.**

A useful negative test: things that read **generic / corporate / AI-generated**
here are — "elevate your style," "premium quality," "designed for the modern
individual," forced slang, corporate Gen-Z voice, over-explained lore, a
paragraph under every image, a countdown, "only a few left," and anything that
begs the audience to buy.

## 12. What only the owner can tell you

These are genuine gaps. **Ask; do not guess.**

- The contents of **`CLAUDE.md`** and **`PHASE_3_DISCOVERY.md`** in the theme
  repo — cited by the code as governing but unreadable this session. Especially
  `PHASE_3_DISCOVERY.md` §0.2 and §0.3.
- **Repo location, branch strategy, and Shopify CLI workflow.** The commit
  `f661bce` is embedded in the live theme name; nothing else about the repo is
  known here.
- **What Phase 0 was**, and what "Phase 5" referred to (the unpublished theme
  `undrrare-hoshoku-phase-5-fixed` predates the Phase 1/2 world work, so the two
  numbering schemes overlap confusingly — see `04_PHASE_HISTORY.md`).
- **The generated world assets and their known problems.** The owner referenced
  known resolution / file-size / letterform issues with generated world assets.
  No such assets are in the Shopify file library or wired into the theme, so they
  presumably live locally or in the repo. What exists, what's wrong with each,
  and what's approved is unknown here. The one asset problem that *was* found
  independently is `hoshoku_floating.gif` — see `07_ASSET_INVENTORY.md`.
- **Ideas that were explicitly rejected** and why. Only the ones the previous
  Claude wrote into code comments survived; there are certainly more.
- **What the owner liked and disliked** in past design audits.
- **Whether the two beanies' inventory state is intentional** (the 2.0 is
  ACTIVE with 0 inventory; the OG has 4).
