# 06 — Guardrails / DO NOT BREAK

Short by design. Read all of it before touching anything.

Each item says **what** and **why**. The "why" matters — several of these look
like sloppy code you'd want to tidy up, and tidying them breaks the site
silently.

---

## 1. Brand identity constraints

**Never blend the ÜNDR and HOSHOKU voices.** They are two voices, not one brand
tone. If a piece needs both, keep them distinct within it — ÜNDR sets
atmosphere, HOSHOKU brings personality. This is the most-repeated rule in the
owner's own brand files.

**Never write ÜNDR as a clothing company.** ATTITUDE → WORLD → PRODUCT. Never
PRODUCT → FEATURES → SALE.

**Never make Bunni babyish**, and never let every sentence be maximally cute.
Contrast against Renard is what makes the character work.

**Never add scarcity, urgency, or exclusivity copy that hasn't been confirmed
true for that specific item.** "Limited," "small run," "won't restock," "only a
few left," countdowns. Not inferred, not implied, not added because it fits the
vibe. This appears in *both* the voice file and the audience file — it matters
more than it looks.

**Never claim the brand is underground.** *"If the brand has to keep saying 'we're
underground,' it isn't."* Cut the claim; let the work carry it.

**Never chase on-brand-ness by planting brand words.** VOICE ≠ VOCABULARY. If a
rewrite reaches for "archive," lowercase, and fragments to sound right, that is
the named failure mode. Fix the attitude, not the word list.

**Never let "archive" become the whole identity.** Explicitly warned against.

**Never over-explain the lore.** Felt before explained. "wait… what is that?" is
a valuable reaction.

**Never use:** "elevate your style," "premium quality," "designed for the modern
individual," "step into your power," "unleash your potential," forced slang,
corporate Gen-Z voice, influencer-style selling, a paragraph under every image.

**Carve-out:** functional ecommerce UI — cart, checkout, filters, sizing, errors
— **stays clear and normal.** Do not make it cryptic. Personality lives in the
brand copy around it.

## 2. Visual identity constraints

**Do not change the approved palettes** without approval. Both were approved
2026-08-26 and derived from real reference material.
ÜNDR: `#14141a` / `#eee9e0` / `#c8203f` / `#2b55ff`.
HOSHOKU: `#f5efe6` / `#2b2118` / `#ee7008` / `#2090f5` / `#f0a8c0`.

**Do not replace the `--world-*` token indirection** with hardcoded colors, or by
editing components directly. The whole point is that existing Horizon components
are world-aware *with zero changes to those components*. Replacing it destroys
the world system and every future switch built on it.

**Do not re-point background/foreground per world object.** Accents only.
Objects share one surface and must read as *different artifacts in the same
space*, not mismatched panels.

**Do not lower `.undr-world-object__price` opacity below 0.7.** At 0.6 it
measured 4.05:1 against HOSHOKU cream — below the 4.5:1 WCAG AA floor for 12px
text. It's real price information, not decoration. Re-measure if you change it.

**Do not put generated renders in front of product photography.** Renders go
**behind**, blurred, as atmosphere. Real product photos stay sharp in front.

**Do not change the square-corner language** (0 radius on buttons and cards,
2px on inputs) without approval.

## 3. Existing working functionality — do not regress

**PRESS START must remain:**
- skippable (click anywhere, the button, or Escape)
- session-aware (once per browser session)
- auto-skipped under `prefers-reduced-motion` and in the theme editor
- **non-blocking with no JS** — it renders as plain in-flow content and never
  hides the real homepage underneath
- **without an auto-advance timeout**, unless one is proposed with UX and
  performance reasoning and approved. This is a standing owner instruction
  recorded in the code as *"per explicit instruction."*

**World objects must remain real links.** Every object is an `<a href>` to a real
Shopify product, collection, or a real configured URL. No invented destinations.
No decorative non-links. No fabricated placeholder graphics — the imageless
object shows its real title typographically for a reason.

**Progressive enhancement must survive.** JS enhances; it is never required. If a
target section doesn't exist, the real link navigates — don't "fix" that into a
no-op.

**Focus management must survive.** Focus moves to the hub on boot dismissal, and
into the target section on hub scroll (with a `tabindex="-1"` removed on blur).

## 4. Code that looks wrong but isn't

Five things a tidy-minded agent will want to "fix." Don't.

1. **`.undr-world-boot.undr-world-boot` (doubled class).** Horizon's
   `.shopify-section:not(.header-section) :is(.section, .cart-summary)` reset
   zeroes `background` at 3 selectors of specificity. Beating it needs 4.
   De-duplicating it removes PRESS START's background entirely.

2. **`[id$="__section_key"]` instead of `#shopify-section-<key>`.** Shopify
   renders JSON-template section wrappers as
   `shopify-section-template--<instance>__<key>`. The "obvious" selector silently
   never matches. **This bug already shipped once** — three HOSHOKU sections
   rendered fully transparent on the live site.

3. **The `.shopify-section` qualifier in the hub's scroll lookup.** Block
   wrappers share the id shape (`shopify-block-<hash>__<key>`), so without it a
   block whose key matches a section key is found first and the object scrolls to
   itself. **This actually happened with a block keyed `current_chapter`.**

4. **The `body ` prefix on `.color-custom-group_hoshoku_side`.**
   `contrast-override.liquid` emits a competing inline rule later in the DOM; a
   bare class selector loses the cascade race.

5. **No `justify-items: center` on the World Hub grid.** It shrink-wraps
   Shopify's `.shopify-block` wrappers, sizing image objects to their image and
   the Shop object to its short label. Centering happens *inside* the object
   instead.

**And one hard prohibition:**

6. **Never write a literal `*/` inside the CSS block comment in
   `blocks/_undr-world-object.liquid`.** It closes the comment early and silently
   eats the rule after it. *"That exact mistake broke the ÜNDR rule below once
   already, and it fails quietly rather than erroring."*

## 5. Shopify constraints

- **Basic plan.** No `checkout.liquid` — checkout is not themeable. Don't plan
  world experiences that extend into checkout.
- **`templates/*.json` and `config/settings_data.json` are auto-generated** and
  carry a warning header. The Shopify admin theme editor **will** overwrite them.
  Decide with the owner whether the repo or the editor is authoritative, and
  don't edit both.
- **Section keys in `templates/index.json` are the contract** for
  `target_section_id` on world objects. Renaming or reordering a section silently
  breaks the object pointing at it — and it *degrades to navigation*, so it looks
  like it still works.
- **Publish from the Git repo, not the admin editor**, or the repo falls behind
  the live theme.
- **Always keep a rollback copy** of the current live theme before publishing.

## 6. Product / catalog constraints

- **Do not modify the Shopify catalog as part of theme work.** Products, prices,
  statuses, inventory, and collections are a separate workstream with separate
  approval. The owner has been explicit about this.
- **Archived ≠ the Archive.** 23 products are ARCHIVED in Shopify, which hides
  them from the storefront entirely. The brand's "Archive" is an unbuilt curated
  concept. Do not un-archive products to build it without approval — that changes
  what's purchasable.
- **Do not delete products without checking order history.** Destructive.
- **Printify inventory numbers are fictitious** (9999, 59994, 719928…). Normal
  for print-on-demand. Don't "fix" them.
- **`hoshoku-2-0-beanie-orange-cream` is the homepage's flagship.** Changing its
  status, handle, or featured image affects PRESS START's atmosphere, the first
  world object, and the flagship hero section simultaneously.
- **Handles are load-bearing.** `hoshoku`, `u-000-core`, `u-002-seek`,
  `u-000-box-logo-shirt-1`, `hoshoku-2-0-beanie-orange-cream` are all referenced
  by the homepage. Renaming any of them breaks the site.
- **`current-chapter` (collection) and `current_chapter` (section) are different
  things.** The section points at `u-002-seek`. Don't "fix" the mismatch without
  asking.

## 7. Treat as read-only

- **The Shopify store** — unless the task is explicitly a catalog task with
  approval.
- **Locale files** (34 of them) — regenerated by Shopify.
- **Stock Horizon files** — prefer adding a scoped custom file over editing a
  stock section, snippet, or block. The two shared edits that do exist
  (`base.css`, `layout/theme.liquid`) are deliberate and documented; adding more
  should be a decision, not a convenience.
- **`undrrare-hoshoku-phase-5-fixed`** — historical Phase 5 reference, cited by
  code comments. Don't delete.
- **This handoff package** — correct it when the code contradicts it, but don't
  quietly rewrite it to match a change you just made.

## 8. Things explicitly decided against

Do not re-propose these without new information. Reasoning in
`10_DECISION_LOG.md`.

- A **from-scratch custom frontend** instead of Horizon.
- A **sitewide `data-world` switch on `<html>`** for the HOSHOKU collection —
  rejected in favor of an isolated template plus per-section scoping
  (`PHASE_3_DISCOVERY.md` §0.2/§0.3).
- An **auto-advance timeout** on PRESS START.
- **Orbit/float motion** before the static hub is reviewed.
- A **second per-object world setting** (world is derived from the eyebrow label).
- **`justify-items: center`** in the hub grid.
- **Free-form world-object heights** (fixed 4:5 instead).
- A **placeholder graphic** for the imageless Shop object.
- **Generating a new asset** for PRESS START atmosphere when a real product image
  worked.
- A **"game-menu flourish"** entrance animation.
- **Price opacity 0.6.**

## 9. Things that previously caused problems

All verified from code comments — these are real incidents, not hypotheticals.

| What happened | Root cause |
|---|---|
| Three HOSHOKU sections rendered fully transparent **on the live site** | `#shopify-section-<key>` never matches JSON-template sections |
| A world object scrolled to itself | Block wrapper ids collide with section wrapper ids; `current_chapter` |
| The ÜNDR accent rule silently disappeared | A `*/` inside a CSS comment |
| PRESS START had no background | Horizon's `.section` background reset out-specificity'd it |
| The HOSHOKU group's background didn't apply | `contrast-override.liquid`'s later inline rule won the cascade |
| World objects had mismatched widths | `justify-items: center` shrink-wrapping Shopify block wrappers |
| The hub read as a misaligned grid | Objects with different native aspect ratios |
| PRESS START's button was covered on mobile | Shopify's fixed bottom privacy banner |
| World-object price failed WCAG AA | Opacity 0.6 → 4.05:1 |

**The pattern:** most of these **failed silently**. Nothing errored. The site
looked fine and was wrong. Verify visually and with computed styles — do not
assume a change worked because nothing broke.

## 10. Dangerous assumptions

1. **"There's no conversation history, so I should reconstruct the brand."** No.
   The brand is documented in `01_BRAND_AND_DESIGN_DNA.md`, sourced from the
   owner's own files. Don't reinvent it.
2. **"This documentation is current."** It's a snapshot of 2026-09-04, written
   without repo access. **The code wins every conflict.**
3. **"The live theme is the latest work."** It isn't. Development is ahead.
4. **"The dev theme is safe to publish."** `settings_data.json` differs by
   1,716 bytes and was never diffed.
5. **"Publishing the theme will make the HOSHOKU template work."** It won't. The
   collection's `templateSuffix` is `null`.
6. **"The asset slots are in use."** Both are empty.
7. **"Archived products are the Archive."** They're hidden from the storefront.
8. **"`best-sellers` and `core` collections exist."** Neither does. That's the
   live bug.
9. **"`current-chapter` is what the Current Chapter section shows."** It isn't.
10. **"The repo is `5enpai-ai/docs`."** That's an untouched Mintlify starter with
    nothing to do with ÜNDRRARE.
11. **"`CLAUDE.md` means the root instructions file I usually read."** Here it's a
    specific ÜNDRRARE theme-repo document with named sections, cited by the code
    as governing.
12. **"Nobody will notice a small redesign."** The owner has approved specific
    palettes, a specific motion register, and specific copy. Unrequested visual
    changes are a violation, not initiative.
13. **"I can generate the missing world assets."** The owner has existing
    generated assets with known problems that nobody here could see. Ask first.
