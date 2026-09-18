# 10 — Decision Log

Purpose: **stop the receiving Claude from re-litigating decisions that are
already settled.**

> **Sourcing.** With no conversation history available, these were reconstructed
> from the previous Claude's code comments (which are unusually explicit and
> often quote the reasoning directly), theme/product timestamps, and live store
> data. **Quoted reasoning is verbatim from the code.** Where the reasoning
> couldn't be recovered, the row says so rather than inventing one.

**Status key:** ✅ settled & live · 🟡 settled but unshipped · 🔵 settled,
deferred to a later phase · ⚪ decided, reasoning not recoverable

---

## Architecture

### D-01 · Build on Shopify Horizon rather than a custom frontend ✅
**Phase:** 0–1 (store created 2026-08-06 with Horizon installed)
**Reason:** *(inferred from the shape of the work)* The entire custom surface is
**5 files against ~400**. Everything else — cart, filters, search, variants,
localization, accessibility, product pages — is Horizon's, maintained by Shopify.
For a solo brand on the Basic plan, this is the difference between shipping a
world in 22 days and not shipping.
**Alternatives:** custom headless/Hydrogen frontend; a different theme; heavy
theme modification.
**Status:** ✅ Live. **Reversing this would discard the entire architecture.**

### D-02 · Make components world-aware via CSS variable indirection, not by editing components ✅
**Phase:** 2 · **Date:** ~2026-08-26
**Reason — quoted:**
> "Existing components don't reference these directly — they keep consuming the
> Shopify-generated vars they always have… Those vars are re-pointed at these
> world tokens in layout/theme.liquid… **that indirection is what makes existing
> components world-aware with zero changes to the components themselves.**"

**Alternatives:** editing each component; a second stylesheet per world;
duplicate section variants.
**Status:** ✅ Live. Load-bearing. See `06_GUARDRAILS.md` §2.

### D-03 · Define both world token sets unconditionally on `:root` ✅
**Phase:** 2
**Reason — quoted:**
> "a single source of truth that is available unconditionally, so a subtree can
> opt into ÜNDR locally using the exact same values the sitewide
> data-world='undr' default uses… **Values are byte-identical to the literals
> they replaced; only the indirection is new.**"

**Why it mattered immediately:** the World Hub is HOSHOKU-scoped as a whole, but
ÜNDR objects inside it must still read as ÜNDR.
**Status:** ✅ Live.

### D-04 · Per-section HOSHOKU scoping instead of a sitewide world switch ✅
**Phase:** 2 · **Date:** 2026-08-26
**Reason — quoted:**
> "'hoshoku' values were APPROVED 2026-08-26… and are now applied **scoped to
> specific homepage sections**… not sitewide, and not behind any switching UI."

And on why this isn't a stopgap architecture:
> "**proof that a future sitewide toggle and today's per-section scoping are the
> same mechanism, not two systems.**"

**Status:** ✅ Live. The sitewide switch remains explicitly future work (D-16).

### D-05 · Isolated `collection.hoshoku.json` template instead of a sitewide `data-world` switch 🟡
**Phase:** 3 · **Date:** ~2026-09-03
**Reason:** **⚪ NOT RECOVERABLE.** The code points at the document:
> "see **PHASE_3_DISCOVERY.md §0.2/§0.3** for why an isolated template + this
> same per-section-id scoping was chosen over a sitewide data-world switch on
> `<html>`."

**Alternatives considered (and rejected):** flipping `data-world="hoshoku"` on
`<html>` for HOSHOKU pages.
**Status:** 🟡 Built in Development, unpublished, and the collection isn't
assigned the template. **Do not re-propose the sitewide switch without reading
§0.2/§0.3 — it was already argued and lost.**

### D-06 · Progressive enhancement as a hard requirement ✅
**Phase:** 1, maintained throughout
**Reason — quoted:**
> "Progressive enhancement only: every world object… is a real `<a href>` to the
> real Shopify product page, so it works with no JS."
> "a visitor without JS never sees an overlay at all."

**Status:** ✅ Live. Non-negotiable.

### D-07 · Additive-only feature introduction ✅
**Phase:** 3, but the instinct runs throughout
**Reason — quoted (on the Phase 3 asset slots):**
> "Additive only: … var()'s fallback of `none` means an unset object renders
> **byte-for-byte the same** gradient glow it always has — nothing here changes
> existing objects until an image is deliberately added."

And on the scoping bugfix:
> "This corrects existing, already-approved behavior to actually render as
> documented — **it does not change which sections get HOSHOKU-scoped or what
> colors they get.**"

**Status:** ✅ The project's working method. Copy it.

---

## Brand & creative

### D-08 · ÜNDR and HOSHOKU are two voices, never one ✅
**Phase:** pre-dates the website; in the owner's brand files
**Reason — quoted:** *"ÜNDR = the world… Hoshoku = the character/soul inside the
world."* Blending them collapses the whole premise. Expressed structurally in the
`world_split` section (Bright side / Dark side) and visually in the two palettes.
**Status:** ✅ Settled and enforced in code, copy, and color.

### D-09 · HOSHOKU palette approved 2026-08-26 ✅
**Reason — quoted:**
> "derived from **pixel-sampling the HOSHOKU reference library**… Warm cream
> world, orange/blue/pink as the expanded saturated accent set — see CLAUDE.md
> for the full evidence, accessibility notes, and relationship to the ÜNDR core
> palette."

Values: `#f5efe6` / `#2b2118` / `#ee7008` / `#2090f5` / `#f0a8c0`.
**Status:** ✅ Approved with a date and an evidence trail. Don't casually adjust.

### D-10 · ÜNDRRARE (the parent) shares the ÜNDR core palette ✅
**Reason — quoted:** *"ÜNDRRARE (the parent brand, e.g. the Shop object) uses the
shared core accents, same as ÜNDR — **per CLAUDE.md the core palette is what both
identities have in common.**"*
**Status:** ✅ Live in `_undr-world-object.liquid`.

### D-11 · Per-object world scoping changes accents only, never background/foreground ✅
**Reason — quoted:**
> "deliberately NOT background/foreground, because the objects share one
> continuous surface and should read as **different artifacts sitting in the same
> space, not as mismatched panels.**"

**Status:** ✅ Live.

### D-12 · Derive an object's world from its eyebrow label ✅
**Reason — quoted:** *"so no second setting has to be kept in sync with it."*
Test order (`hoshoku` → `ndrrare` → `ndr`) matters because "ÜNDRRARE" contains
"NDR" — also documented in the code.
**Alternative:** a separate per-object world setting. Rejected as a sync hazard.
**Status:** ✅ Live.

### D-13 · Reuse a real product image for PRESS START atmosphere rather than generate one ✅
**Phase:** 1 · **Reason — quoted:** *"no new asset, **deliberately** the same real
product image already rendered by the world hub below."*
**Status:** ✅ Live, with `atmosphere_image` (Phase 3) now able to override it
when a purpose-made render exists.

### D-14 · No fabricated or placeholder graphics ✅
**Reason — quoted (on the imageless Shop object):** *"It shows the object's real
title typographically — **not a fabricated or placeholder graphic.**"*
And more broadly: *"**No invented destinations:** the object resolves to exactly
one of a real product, a real collection, or a manually configured real URL…
title/image/price are read live from whichever resource is assigned, **never
hardcoded**."*
**Status:** ✅ Live. A principle, not just an implementation detail.

### D-15 · Generated renders go behind real photography, blurred, as atmosphere ✅
**Phase:** 3 · **Reason — quoted:**
> "keeps a render reading as atmosphere behind the live product/collection photo
> (still rendered sharp, unchanged, in front), **not a second competing image** —
> same 'soft world glow behind real content' idiom already used for PRESS START's
> atmosphere layer."

**Status:** ✅ Decided and built; awaiting assets.

### D-16 · Asset pipeline: temporary Meshy → later Higgsfield, swappable without code changes 🔵
**Phase:** 3 · **Reason — quoted:** *"temporary: Meshy; later: Higgsfield
one-for-one swap, no markup change needed"* / *"Swapping this image later… is a
**settings-only change**; no markup or CSS edit needed."*
**Status:** 🔵 Slots built, empty. The design anticipates the assets being
replaced — relevant given the reported problems with the existing generated set.

---

## UX & interaction

### D-17 · No auto-advance timeout on PRESS START 🔵
**Phase:** 1 · **Reason — quoted:**
> "No arbitrary auto-advance timeout yet, **per explicit instruction** — a
> duration and its UX/performance reasoning must be **proposed and reviewed**
> before one is added."

**This is the clearest surviving record of the owner directly constraining the
build.** Treat as standing.
**Status:** 🔵 Deferred pending a proposal.

### D-18 · PRESS START is session-scoped, not permanent ✅
**Reason — quoted:** the governing constraints are *"lightweight, skippable,
session-aware, **never a permanent trap**."* Implemented as
`sessionStorage['undrWorldBootSeen']`, with skips for design mode and
`prefers-reduced-motion`, and a deliberate fail-open when storage throws.
**Status:** ✅ Live.

### D-19 · No orbit/float motion in Phase 2 🔵
**Reason — quoted:** *"No floating/orbit motion yet — that is Phase 3, **pending
review of this static prototype.**"*
**Status:** 🔵 Awaiting the owner's review of the static hub. See
`05_NEXT_TASKS.md` P3-1.

### D-20 · Understated motion, not a game-menu flourish ✅
**Phase:** 3 · **Reason — quoted:** *"this is the one place in the boot sequence
that earns entrance motion, so it stays understated (opacity + small translate,
**no bounce, no scale**) rather than a game-menu flourish."*
And on the exit: *"a threshold being pushed through, **not a dialog closing**."*
**Status:** 🟡 Built in Development, unpublished. Sets the motion register for
everything that follows.

### D-21 · Fixed 4:5 portrait ratio for world objects ✅
**Phase:** 2 · **Reason — quoted:** *"with four objects of different native aspect
ratios the frames ended at different heights and the titles below them stopped
sharing a baseline, which made the hub read as **a misaligned grid rather than a
set of comparable artifacts.**"*
**Alternative:** free-form heights (Phase 1's single-object behavior). Rejected
once there was more than one object.
**Status:** ✅ Live.

### D-22 · World-object price opacity is 0.7, not 0.6 ✅
**Reason — quoted:** *"at 0.6 the effective contrast measured **4.05:1** against
the HOSHOKU-scoped cream background in a live browser — below the 4.5:1 WCAG AA
floor for text this size (12px). 0.7 lands at ~5.5:1… **Don't lower this without
re-measuring — it's real price information, not decoration.**"*
**Status:** ✅ Live. A measured floor, not a taste call.

### D-23 · Functional ecommerce UI stays plain ✅
**Source:** the owner's ÜNDR voice file — *"Functional ecommerce UI can stay clear
and normal — brand copy surrounding it keeps the personality."*
**Status:** ✅ Settled. Prevents the obvious failure of making checkout cryptic.

---

## Content & catalog

### D-24 · Numbered archive-file product system (Ü-000 / Ü-001 / Ü-002) ✅
**Phase:** pre-website; collection copy rewritten 2026-08-26
**Reason:** *(inferred from the copy itself)* Turns a catalog into a chronology
and gives each drop a place in the world. Ü-000 CORE = origin (Sept 2023),
Ü-001 ENLIGHTENMENT = the three realms, Ü-002 SEEK = the awakening after.
**Status:** ✅ Live across collections, product titles, tags, and copy.

### D-25 · "ARCHIVE SYSTEM / FILE NO. / ARTIFACT / CONDITION" product format ✅
**Status:** ✅ Live on both beanies and, in a lighter form, the flagship Ü
products. **Coverage is uneven** — many Printify products still carry supplier
boilerplate (`05_NEXT_TASKS.md` P2-2).
**Caution:** the brand files warn that *"archive"* shouldn't become ÜNDR's whole
identity, so this format is a tool, not a default for everything.

### D-26 · Pull real collection copy into the HOSHOKU template rather than duplicate it 🟡
**Phase:** 3 · The lore block is `{{ closest.collection.description }}`, named
*"Lore (real collection description, unedited)."*
**Reason:** *(inferred)* Single source of truth; consistent with D-14's no-invented-content
instinct.
**Status:** 🟡 Built, unpublished.

### D-27 · "Best Sellers" → "Shop the Collection" 🟡
**Phase:** 3 · **Reason:** ⚪ not stated. *(Inferred: "Best Sellers" is generic
ecommerce language and makes a sales claim; "Shop the Collection" doesn't. Also
the `best-sellers` collection never existed, so the heading was describing
nothing.)*
**Status:** 🟡 In Development, unpublished. Ships alongside the broken-link fix.

### D-28 · `current_chapter` section points at `u-002-seek`, not at the `current-chapter` collection ⚪
**Reason:** ⚪ **NOT RECOVERABLE.** Both exist; the section uses SEEK (9 products,
max 5 shown); the `current-chapter` collection (2 products) is used nowhere.
**Status:** ⚪ **Verify with the owner before changing either.** This is the most
likely thing for a future agent to "fix" wrongly. See `08_SHOPIFY_CONTENT_MAP.md` §7.

---

## Still open — not yet decided

These are **not** settled. They're listed here so nobody assumes they are.

| Question | Where it's tracked |
|---|---|
| Is the HOSHOKU opening statement approved? | `05_NEXT_TASKS.md` P1-1 — flagged PENDING APPROVAL in the template itself |
| When and how does world switching become visitor-controllable? | P3-2 · code says "explicitly future work" |
| What is the Archive, concretely? | P1-6 · teaser is live with no destination |
| Does the Story page get written, or does the nav item come down? | P1-4 |
| What is the Journal for? | P1-5 |
| Is the flagship beanie's 0 inventory intentional? | P0-4 |
| What are the existing world assets and what's wrong with them? | P1-8 + `07_ASSET_INVENTORY.md` §6 |
| Should the catalog be cleaned, and is that in scope? | P2-2/3/4/7 |
| Is the ambassador programme live? | `08_SHOPIFY_CONTENT_MAP.md` §9 — orphaned terms page |
| Does grain extend beyond PRESS START? | P3-4 · approved-but-unbuilt in `CLAUDE.md` |
| How do the two phase-numbering schemes reconcile? | `04_PHASE_HISTORY.md` |
