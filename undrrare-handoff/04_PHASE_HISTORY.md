# 04 — Phase History

> **Confidence warning.** No conversation history was available. This timeline
> was reconstructed from: theme creation/update timestamps, theme names, product
> and collection creation dates, and — most valuable — the previous Claude's own
> code comments, which carry explicit phase labels, approval dates and stated
> reasoning.
>
> Where reasoning is quoted, it is **verbatim from the code**. Where it is
> inferred, it says so. **Phase 0 is genuinely unknown.**

---

## ⚠️ The numbering is not one sequence

There are **two overlapping numbering schemes**, and confusing them will mislead
you:

- **"Phase 5"** appears in the theme name `undrrare-hoshoku-phase-5-fixed`
  (2026-08-26) and in code comments referring to *"the existing Phase 5 content"*
  that world objects scroll into. This belongs to an **earlier HOSHOKU homepage
  build** that predates the world-first work.
- **"Phase 1 / 2 / 3"** in the custom code comments refer to the **World-First
  Homepage Architecture** effort, which began after that.

So Phase 1 (world-first) came *after* Phase 5 (HOSHOKU homepage). Ask the owner
to reconcile the naming; this package uses the code's own labels.

---

## Phase 0 — **[UNKNOWN]**

Nothing recoverable. The earliest hard dates available:

- **September 2023** — first ÜNDR release, the Ü-000 box logo.
  *(Source: live Ü-000 collection and product copy.)*
- **2026-08-06** — Shopify store scaffolded; `Horizon` theme installed 18:38;
  four "Example product" sample entries created; `Radiant` (a Horizon copy)
  created 21:10.

**Ask the owner:** what Phase 0 covered — brand founding, catalog build,
pre-Shopify presence, or the initial store setup.

---

## Phase 1 — World-First Homepage, "Beanie-only prototype"

**Label from code:** *"Phase 1 (Beanie-only prototype)"*, in both
`undr-world-boot.js` and (historically) `undr-world-hub.js`.

**What was built:** the PRESS START boot layer and a World Hub containing a
**single** object — the HOSHOKU Beanie.

**Governing constraints, quoted from `undr-world-boot.js`:**
> "see CLAUDE.md 'World-First Homepage Architecture' for the governing
> constraints this component must respect: **lightweight, skippable,
> session-aware, never a permanent trap.**"

**Why it was built this way** — the code is unusually explicit:
- The section renders as **plain in-flow content by default**; JS only ever
  *adds* `data-active` or `data-dismissed`. *"it never removes the real homepage
  content underneath, and a visitor without JS never sees an overlay at all."*
- **Progressive enhancement was non-negotiable from day one:** *"every world
  object... is a real `<a href>` to the real Shopify product page, so it works
  with no JS."*

**Explicitly deferred, with reasoning:**
> "No arbitrary auto-advance timeout yet, **per explicit instruction** — a
> duration and its UX/performance reasoning must be proposed and reviewed before
> one is added."

This is the clearest surviving evidence of the owner directly constraining the
build. Treat it as standing.

**Atmosphere decision:** the PRESS START background reuses
`atmosphere_product`'s own featured image — *"no new asset, deliberately the same
real product image already rendered by the world hub below."* The instinct is
consistent throughout: **reuse real material rather than generate placeholder
material.**

---

## Phase 2 — Five-object hub, dual-world palette, live launch

**Label from code:** *"Phase 2 (five-object hub)"*.
**Live theme:** `undrrare-theme-phase2-f661bce`, published **2026-08-28 02:21**,
last updated 02:30. Commit `f661bce`.

### What was added
1. **Four more world objects** — HOSHOKU collection, ÜNDR entry product, current
   chapter, Shop All. Five total.
2. **The HOSHOKU palette, APPROVED 2026-08-26.**
   > "derived from pixel-sampling the HOSHOKU reference library (see CLAUDE.md
   > 'ÜNDRRARE Visual Reference System' and the Phase 2 palette proposal). Warm
   > cream world, orange/blue/pink as the expanded saturated accent set."
3. **`--undr-*` constants extracted.** The reason is specific:
   > "the world hub is HOSHOKU-scoped as a whole while individual ÜNDR world
   > objects inside it must still read as ÜNDR... **Values are byte-identical to
   > the literals they replaced; only the indirection is new.**"
4. **Per-object world identity derived from the eyebrow label** —
   > "so no second setting has to be kept in sync with it."
5. **Per-section HOSHOKU scoping** rather than a sitewide switch.

### Problems solved during Phase 2, recorded in the code
These are the most valuable artifacts in the whole project — real bugs with
their diagnoses preserved.

| Problem | Fix | Quote |
|---|---|---|
| Objects scrolled to *themselves* | Add `.shopify-section` qualifier to the lookup | *"a block whose key happens to match a section key would be found first in DOM order... That actually happened with a block keyed `current_chapter`."* |
| HOSHOKU-scoped sections rendered transparent (dark core, not cream) | Match `[id$="__key"]` instead of `#shopify-section-key` | *"confirmed live via computed styles, all three sections below were rendering fully transparent"* |
| Objects had mismatched widths | Drop `justify-items: center`; stretch wrappers, center inside | *"centring the grid items shrink-wraps those wrappers to their content"* |
| Object frames ended at different heights, titles lost their baseline | Fixed `4/5` portrait ratio | *"with four objects of different native aspect ratios... the hub read as a misaligned grid rather than a set of comparable artifacts"* |
| PRESS START button covered on mobile | Anchor to `18vh` below 749px | *"Shopify's own #shopify-pc__banner (fixed, bottom-anchored, out of this theme's control)"* |
| The ÜNDR accent rule silently vanished | Never write `*/` in that comment | *"that exact mistake broke the ÜNDR rule below once already, and it fails quietly rather than erroring"* |
| PRESS START had no background | Doubled class selector for specificity | *"beating it needs 4, not 2"* |
| Group background lost a cascade race | `body ` prefix | *"emits its own rule for this same class, inline, later in the DOM"* |
| World-object price failed WCAG AA at 0.6 opacity | Raise to 0.7 | *"at 0.6 the effective contrast measured 4.05:1... 0.7 lands at ~5.5:1"* |

### Explicitly deferred at end of Phase 2
- Orbit/float motion — *"that is Phase 3, pending review of this static
  prototype."*
- Sitewide world switching — *"There is still no world-selection screen, no
  persistent toggle, and no mechanism for a visitor to set this themselves — that
  remains explicitly future work."*

---

## Phase 2.5 — "Visual refinement pass"

**Label from code:** `sections/undr-world-boot.liquid` header says *"Phase 1
(Beanie-only prototype), **visual refinement pass**"*, and the base.css scoping
fix is tagged *"BUGFIX (visual refinement pass)"*.

This was a distinct atmosphere-and-correctness pass, not new features:
- Added the two-layer PRESS START atmosphere (darkened product image + inline-SVG
  grain). The grain is flagged as the **first** grain in the theme:
  *"grain is documented as approved-but-unbuilt"* in `CLAUDE.md`.
- Added the `scale(1.04)` exit — the *"materialization"* cue,
  *"a threshold being pushed through, not a dialog closing."*
- Fixed the `[id$=]` scoping bug (three sections had been silently rendering
  wrong on the live site).
- Fixed the mobile privacy-banner collision.

The fix comment is careful about scope, and the discipline is worth copying:
> "This corrects existing, already-approved behavior to actually render as
> documented — **it does not change which sections get HOSHOKU-scoped or what
> colors they get.**"

---

## Phase 3 / Discovery — in flight, unpublished

**Evidence:** the Development theme (`Development (912126-penguin)`), last
updated **2026-09-03 17:52** — the most recent activity on the project, one day
before this handoff.

A document **`PHASE_3_DISCOVERY.md`** exists in the theme repo and is cited by
section (§0.2, §0.3 item 1). **It could not be read this session. Get it — it is
the single most important missing artifact.**

### What Phase 3 has produced so far

1. **Replaceable-asset slots.** Two new settings, both additive and both empty:
   - `atmosphere_image` — *"PHASE 3 replaceable-asset slot: PRESS_START_BACKGROUND"*
   - `world_artifact_image` — *"PHASE 3 replaceable-asset slot: WORLD_OBJECT"*

   The asset strategy is stated plainly:
   > "the intended home for a purpose-made world environment render (**temporary:
   > Meshy; later: Higgsfield one-for-one swap, no markup change needed**)."

   And the compositing rule:
   > "keeps a render reading as atmosphere behind the live product/collection
   > photo (still rendered sharp, unchanged, in front), not a second competing
   > image"

2. **Isolated HOSHOKU collection template** —
   `templates/collection.hoshoku.json`, three sections (`hoshoku_intro`,
   `hoshoku_collection_main`, `hoshoku_continue`).

   **The architectural decision, quoted:**
   > "see PHASE_3_DISCOVERY.md §0.2/§0.3 for **why an isolated template + this
   > same per-section-id scoping was chosen over a sitewide data-world switch on
   > `<html>`**."

   That is a real decision point that was reached and settled: the sitewide
   switch was considered and **not** taken for this. The reasoning lives only in
   `PHASE_3_DISCOVERY.md`.

   Its lore block pulls `{{ closest.collection.description }}` — the real
   collection copy, unedited, rather than a duplicate. Consistent with the
   project's "no invented content" instinct.

3. **Staggered PRESS START content reveal** — with a stated restraint:
   > "this is the one place in the boot sequence that earns entrance motion, so
   > it stays understated (opacity + small translate, no bounce, no scale)
   > rather than a game-menu flourish."

4. **Two broken-link fixes** — `collections/core` → `collections/u-000-core`, and
   `best-sellers` → `u-002-seek` with the heading changed from "Best Sellers" to
   "Shop the Collection".

   The heading change is quietly on-brand: "Best Sellers" is generic ecommerce
   language; "Shop the Collection" isn't making a sales claim.

### Where Phase 3 stopped

- Opening statement **PENDING APPROVAL**.
- Asset slots **empty**.
- Collection `templateSuffix` **not assigned**.
- Nothing **published**.

**This is where the project was when the handoff was requested.**

---

## Catalog timeline (live Shopify data)

| Date | Event |
|---|---|
| Sept 2023 | Ü-000 box logo — first ÜNDR release *(from copy, pre-Shopify)* |
| 2026-08-06 | Store created; Horizon installed; 4 sample products |
| 2026-08-07 | **Bulk catalog import** — ~45 Printify products in one pass |
| 2026-08-08 | **HOSHOKU Beanie 2.0** created 19:27; **Beanie (OG)** 23:22 |
| 2026-08-10 | Ü-001 "Rare" Button Up (draft); large archive/cleanup pass |
| 2026-08-11 | `Updated copy of Radiant` |
| 2026-08-15 | Firefly-generated image uploaded |
| 2026-08-25 | ODMPOD products appear (draft) |
| **2026-08-26** | **HOSHOKU palette APPROVED**; `undrrare-hoshoku-phase-5-fixed`; collection copy rewritten (Ü-000/001/002 descriptions) |
| 2026-08-27 | Development theme created |
| **2026-08-28** | `undrrare-theme-phase2-f661bce` **published live**; `hoshoku_floating.gif` uploaded |
| **2026-09-03** | Last Development theme update — Phase 3 work |
| 2026-09-04 | This handoff |

The project moved from empty store to live world-first homepage in **22 days**.

---

## Important checkpoints

| Checkpoint | Identifier |
|---|---|
| Live Phase 2 theme | `undrrare-theme-phase2-f661bce`, commit **`f661bce`** |
| Phase 5 HOSHOKU build | theme `undrrare-hoshoku-phase-5-fixed` |
| HOSHOKU palette approval | **2026-08-26** (cited twice in `base.css`) |
| Phase 3 head | Development theme @ 2026-09-03 17:52 |

---

## Why major decisions were made — the short version

Full detail in `10_DECISION_LOG.md`. The through-line:

- **Build on Horizon, don't replace it.** The custom surface is 5 files.
- **Make existing components world-aware via token indirection**, not by
  modifying components. *"zero changes to those components."*
- **Progressive enhancement, always.** The site works with no JS.
- **Never fabricate.** No invented destinations, no placeholder graphics, no
  duplicated copy, no manufactured scarcity.
- **Additive-only changes.** New capability renders byte-identically when unset.
- **Scope discipline.** Fixes correct behavior to match what was approved; they
  don't expand it.

---

## What was rejected, and why

Only what survived in code comments — there is certainly more.

| Rejected | In favor of | Why (quoted / inferred) |
|---|---|---|
| Sitewide `data-world` switch on `<html>` for the HOSHOKU collection | Isolated template + per-section-id scoping | *"see PHASE_3_DISCOVERY.md §0.2/§0.3"* — **reasoning not recoverable** |
| Auto-advance timeout on PRESS START | Manual dismissal only | *"per explicit instruction"* — owner's call |
| Orbit/float motion in Phase 2 | Static prototype first | *"pending review of this static prototype"* |
| A second world setting per object | Deriving world from the eyebrow label | *"so no second setting has to be kept in sync with it"* |
| `justify-items: center` in the hub grid | Stretch wrappers, center inside | shrink-wrapped Shopify block wrappers, desyncing widths |
| Free-form object heights | Fixed `4/5` ratio | *"read as a misaligned grid rather than a set of comparable artifacts"* |
| Placeholder graphic for the imageless Shop object | Typographic title frame | *"not a fabricated or placeholder graphic"* |
| Generating a new asset for PRESS START atmosphere | Reusing the real product image | *"no new asset, deliberately the same real product image"* |
| A "game-menu flourish" entrance | Understated opacity + translate | explicit in the Phase 3 comment |
| Price opacity 0.6 | 0.7 | measured 4.05:1, below WCAG AA |
| Re-pointing background/foreground per object | Accents only | *"should read as different artifacts sitting in the same space, not as mismatched panels"* |
| "Best Sellers" heading | "Shop the Collection" | *(inferred: generic ecommerce language)* |

---

## What remains unresolved

1. **Is the Phase 3 opening statement approved?** Blocking.
2. **Why was the isolated template chosen over the sitewide switch?** In
   `PHASE_3_DISCOVERY.md` only.
3. **What world renders exist, and what's wrong with them?** The owner cited
   resolution / file-size / letterform problems. No such assets found anywhere
   reachable.
4. **When does world switching become visitor-controllable, and via what UI?**
5. **What is the Archive, concretely?** Teaser exists; concept doesn't.
6. **Is the Story page going to be written, or should the nav item come down?**
7. **What is the Journal for?** In nav, zero articles.
8. **Is the flagship beanie's 0 inventory intentional?**
9. **What was Phase 0, and how do the two numbering schemes reconcile?**
10. **Should the catalog be cleaned** (samples, duplicates, supplier copy,
    vendor field), and is that in scope for the receiving Claude at all?
