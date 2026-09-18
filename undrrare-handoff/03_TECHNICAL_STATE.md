# 03 — Current Technical State

Audited 2026-09-04, read-only, via the Shopify Admin API and the local
filesystem. **Every claim is bucketed A/B/C/D. Nothing planned is presented as
existing.**

---

## ⚠️ Scope of this audit — read first

The **ÜNDRRARE theme Git repository was not reachable** from the session that
wrote this. Available repos were exactly one: `5enpai-ai/docs`.

So this audit covers:
- ✅ the theme **as deployed** to Shopify (live MAIN + Development)
- ✅ the Shopify store's data and configuration
- ❌ the theme repo: branches, commits, working tree, `CLAUDE.md`,
  `PHASE_3_DISCOVERY.md`, local build tooling, `.shopifyignore`, any local assets

Sections below marked **[NOT AUDITABLE]** are unknown, not absent.

---

# A. CONFIRMED / CURRENT

## A1. Git — this repository only

```
Repository:   5enpai-ai/docs (github.com/5enpai-ai/docs, public)
Branch:       claude/ündrrare-handoff-package-jkeyj9
Commit:       65369e8  "Initial commit"   (the only commit)
Working tree: clean at audit start
Contents:     .mintignore  AGENTS.md  LICENSE  README.md  docs.json
              favicon.svg  index.mdx  quickstart.mdx  logo/{dark,light}.svg
```

**This repository is an unmodified Mintlify documentation starter kit. It
contains nothing related to ÜNDRRARE.** `docs.json` still reads
`"name": "Mintlify Starter Kit"` with Mintlify's green palette; `index.mdx` and
`quickstart.mdx` are untouched template text; `AGENTS.md` still carries its
"customize this file" placeholder.

Do not mistake this for the ÜNDRRARE project. It is the container this handoff
package was written into.

## A2. Theme Git repo — inferred existence only

The live theme is named **`undrrare-theme-phase2-f661bce`**. The suffix is a
7-char commit SHA, which is Shopify CLI's convention when pushing a theme from a
Git checkout. So a repo exists and commit `f661bce` produced the live theme.
Everything else about it is **[NOT AUDITABLE]**.

## A3. Shopify store

| | |
|---|---|
| Name | ÜNDR 🐰/🦊 |
| Domain | `undrrare.shop` |
| Shop ID | `101223072042` |
| Plan | **Basic** |
| Currency / TZ / Country | USD / EDT / United States |

**Basic-plan consequences worth knowing:** no Shopify Functions on some tiers, no
Shopify Plus checkout extensibility, limited staff accounts, and — most relevant
here — **no `checkout.liquid`**; checkout is not themeable.

## A4. Themes on the store (6)

| Name | Role | Theme Store ID | Updated |
|---|---|---|---|
| `undrrare-theme-phase2-f661bce` | **MAIN (live)** | — | 2026-08-28 |
| `Development (912126-penguin)` | DEVELOPMENT | — | **2026-09-03** |
| `undrrare-hoshoku-phase-5-fixed` | UNPUBLISHED | — | 2026-08-26 |
| `Radiant` | UNPUBLISHED | 2481 | 2026-08-28 |
| `Updated copy of Radiant` | UNPUBLISHED | 2481 | 2026-08-11 |
| `Horizon` | UNPUBLISHED | 2481 | 2026-08-06 |

Theme store ID **2481 is Horizon**; "Radiant" here is a renamed Horizon copy, not
a different theme.

## A5. Theme architecture

Shopify **Horizon**. Modern architecture: top-level `blocks/`,
`{% content_for 'blocks' %}`, `{% stylesheet %}` / `{% schema %}` per file, JSON
templates, section groups, `ref=` / `on:` DOM bindings, a `Component` base class,
`_`-prefixed private blocks.

Approximate live counts: **~125 assets, ~95 blocks, 44 sections, ~130 snippets,
13 templates, 2 layouts, 34 locale files.**

## A6. Custom ÜNDRRARE code — live

| File | Bytes | Status |
|---|---|---|
| `sections/undr-world-boot.liquid` | 8,956 | working |
| `assets/undr-world-boot.js` | 3,190 | working |
| `sections/undr-world-hub.liquid` | 4,508 | working |
| `assets/undr-world-hub.js` | 2,961 | working |
| `blocks/_undr-world-object.liquid` | 13,076 | working |

Modified shared files: `assets/base.css` (world tokens, ~180 added lines),
`layout/theme.liquid` (`data-world="undr"` + token aliasing).

Custom web components: `<undr-world-boot-component>`,
`<undr-world-hub-component>`. Both guard registration with
`if (!customElements.get(...))`.

## A7. JavaScript

ES modules using the theme's own aliases — `@theme/component`,
`@theme/utilities`, `@theme/scrolling`. No bundler output, no external
dependencies, no npm packages in the custom code. `assets/package.json` is 23
bytes (effectively a stub). `assets/jsconfig.json` (345 B) and three `.d.ts`
files exist for editor type-checking only.

## A8. CSS

Component CSS lives in `{% stylesheet %}` blocks inside each Liquid file; global
tokens live in `assets/base.css`. No preprocessor, no build step. Modern CSS in
active use: `color-mix()`, `aspect-ratio`, `isolation`, container query units
(`60cqw`), `text-wrap: balance/pretty`, `:is()`, `[attr$=]`, custom properties
throughout.

## A9. Confirmed design tokens

ÜNDR: bg `#14141a`, fg `#eee9e0`, accent `#c8203f`, accent-2 `#2b55ff`, border
`#3a3a42`, surface `#1c1c22`, surface-muted `#0b0b0f`.
HOSHOKU: bg `#f5efe6`, fg `#2b2118`, accent `#ee7008`, accent-2 `#2090f5`, border
`#8a7057`, surface `#e8dcc8`, surface-muted `#d8c6a8`, decorative `#f0a8c0`.
Type: Merriweather Sans Bold (heading), Assistant Regular (body), Assistant Light
(subheading). Buttons square + uppercase; inputs 2px radius; cart = drawer.

## A10. Working functionality (verified by reading the deployed code)

- PRESS START overlay: promote / dismiss / session-skip / reduced-motion skip /
  design-mode skip / Escape / click-anywhere / scroll lock / focus handoff
- World Hub: 5 real objects, live resource resolution, per-object world accents,
  progressive-enhancement scroll with correct section matching, no-JS fallback
- Dual-world token system + per-section HOSHOKU scoping
- Full 9-section homepage with real copy and real products
- Standard Horizon commerce: cart drawer, quick-add, filters, sorting, predictive
  search, variant pickers, product recommendations, localization

## A11. Shopify content — headline numbers

68 products (**13 ACTIVE, 24 DRAFT, 31 ARCHIVED**) · 8 collections · 4 menus ·
4 pages · 1 blog (0 articles).
Full detail in `08_SHOPIFY_CONTENT_MAP.md`.

---

# B. PLANNED (designed, documented, NOT built or NOT live)

## B1. Sitewide world switching
The mechanism works. There is **no world-selection screen, no toggle, no
persistent visitor preference, and no UI of any kind.** Code calls this
"explicitly future work" and points at `CLAUDE.md` "Future Website Experience
Architecture" **[NOT AUDITABLE]**.

## B2. World Hub orbit / float motion
*"No floating/orbit motion yet — that is Phase 3, pending review of this static
prototype."* Not built.

## B3. PRESS START auto-advance
Deliberately absent. *"A duration and its UX/performance reasoning must be
proposed and reviewed before one is added."* Treat as a standing owner
instruction.

## B4. Grain treatment
`CLAUDE.md` documents grain as **approved but unbuilt**. The only instance is the
PRESS START noise layer.

## B5. Generated world renders
Slots exist (`atmosphere_image` / `world_artifact_image`, both Development-only).
Plan recorded in code: **temporary Meshy render → later Higgsfield render, swapped
one-for-one with no markup change.** No renders assigned anywhere.

## B6. The Archive
Teaser copy exists ("Curation in progress"). No collection, page, template, or
link.

---

# C. INCOMPLETE (started, in flight, blocked)

## C1. 🔴 Development theme is ahead of live and unpublished

Checksums differ on five files. **The Development theme contains fixes for bugs
that are live right now.**

| File | MAIN | Development | Δ |
|---|---|---|---|
| `templates/index.json` | `667c3b75…` | `f215371d…` | **2 broken links fixed** |
| `assets/base.css` | `18df2c85…` | `d323fb84…` | +3 HOSHOKU scoping ids, +comment |
| `sections/undr-world-boot.liquid` | `3e7c23ea…` | `6cf79edc…` | + `atmosphere_image` slot, + staggered reveal |
| `blocks/_undr-world-object.liquid` | `478af096…` | `86afe2af…` | + `world_artifact_image` slot |
| `config/settings_data.json` | `c361eafa…` | `8f6eb8e1…` | differs — **not diffed this session** |
| `templates/collection.hoshoku.json` | *absent* | 8,255 B | new HOSHOKU collection template |

Identical in both: `undr-world-boot.js`, `undr-world-hub.js`,
`sections/undr-world-hub.liquid`, `layout/theme.liquid`.

> ⚠️ `config/settings_data.json` differs (9,115 B live vs 7,399 B dev) and its
> contents were **not compared**. It holds global theme settings including the
> color palette. Publishing dev without diffing this file could change sitewide
> colors or typography. **Diff it before publishing.**

## C2. 🔴 Two live-broken Shopify references

1. `world_split` → `group_undr_side` → `cta` →
   `link: "shopify://collections/core"`. **No collection with handle `core`
   exists.** Real handle: `u-000-core`. The site's "Enter ÜNDR" button is broken.
   Fixed in dev.
2. `featured_products` → `collection: "best-sellers"`. **No such collection.**
   The homepage's largest product grid has no source. Fixed in dev (→ `u-002-seek`,
   heading "Best Sellers" → "Shop the Collection").

## C3. 🟠 HOSHOKU collection template cannot render
`templates/collection.hoshoku.json` exists in dev. The `hoshoku` collection's
`templateSuffix` is **`null`**. Requires a Shopify admin change (assign template
"hoshoku" to the collection) in addition to publishing the theme.

## C4. 🟠 Unapproved copy sitting in the dev template
The `hoshoku_intro` opening statement — *"HOSHOKU isn't a mascot. HOSHOKU is a
character who happens to live here."* — is named in the JSON as **"PENDING
APPROVAL, see PHASE_3_DISCOVERY.md §0.3 item 1."** Do not ship it without the
owner's sign-off.

## C5. 🟠 Phase 3 asset slots empty
Built and wired, zero images assigned. Both slots are additive: unset renders
byte-identically to today.

## C6. 🟡 Story page is a placeholder, and it's in the nav
Body: *"Long before there was ÜNDR, there was Hoshoku — a creature divided
between instinct and compassion. Neither hero. Neither villain. Only balance.
This page is a placeholder. Replace this copy with the full ÜNDR origin story."*

## C7. 🟡 Journal in nav → blog with 0 articles

## C8. 🟡 Accessories collection has 0 products

## C9. 🟡 Product copy coverage is uneven
The beanies and flagship Ü products have full ÜNDR-voice storytelling. Many
Printify products still carry raw supplier text (size tables, *"This bikini
swimsuit is designed for fashionable women…"*) and supplier-generated SEO tags
(*"Sassy Beach Look," "Flirtatious Swimwear," "panda design tee"*) that are
off-brand.

## C10. 🟡 Product data hygiene
- Vendor is inconsistent: `ÜNDR`, `ÜNDR 🐰/🦊`, `Printify`, `ODMPOD`, `My Store`.
  **`Printify` and `ODMPOD` are fulfilment partners, not the brand** — they are
  visible to customers wherever vendor is displayed.
- 4 products titled "Example product" (vendor "My Store", ARCHIVED) — Shopify
  sample data.
- 4 ODMPOD products (DRAFT) are **exact duplicates** of each other
  (`…-t-shirt` / `…-t-shirt-2`), unbranded, with placeholder inventory `9999999`.
- Several ARCHIVED products have `$0.00` price and no media.
- Printify inventory is fictitious (`9999`/`59994`/`719928` etc.), normal for POD.

## C11. 🟡 HOSHOKU Beanie 2.0 is ACTIVE with 0 inventory
`hoshoku-2-0-beanie-orange-cream`, $75, ACTIVE, `totalInventory: 0`. It is the
**flagship product of the entire homepage** — PRESS START's atmosphere image, the
first world object, and the flagship hero. If it's showing sold-out, the whole
world-first experience terminates in an unbuyable product. The OG has 4 units.
May be intentional (made-to-order) — **verify with the owner.**

---

# D. DEPRECATED / OLD

- **`Horizon`, `Radiant`, `Updated copy of Radiant`** — earlier base-theme copies
  from 2026-08-06/08-11. Superseded. Safe to ignore; ask before deleting.
- **`undrrare-hoshoku-phase-5-fixed`** (2026-08-26) — the pre-world-first HOSHOKU
  build. Predates Phase 1/2. Referenced in code comments as "the existing Phase 5
  content" that world objects scroll into, so **it is historically load-bearing
  context. Do not delete without asking.**
- **`collection: "best-sellers"`** — a dead reference, presumably from an earlier
  homepage draft.
- **4 "Example product" entries** — Shopify sample data, archived. Deletable, but
  it's a catalog change.
- **Duplicate ARCHIVED Printify products** (`u-000-undr-clogs` vs
  `u-000-undr-clogs-1`, `-hoshoku-plush-pillow` vs `-1`, `eat-me-crop-top` vs
  `-1`, etc.) — earlier import passes.

---

# E. Dev server / CLI status

**[NOT AUDITABLE]** No Shopify CLI, no `shopify.theme.toml`, no local theme
checkout, and no dev server were present in this environment. `shopify --version`
was not run because the CLI is not installed here.

**Inferred, not confirmed:** the presence of a `Development (…)` theme role means
`shopify theme dev` has been used against this store, and the
`undrrare-theme-phase2-f661bce` naming means `shopify theme push` from a Git
checkout. Confirm the actual workflow with the owner.

# F. Dependencies

**Theme:** none. No npm packages, no CDN scripts, no external libraries in the
custom code — everything imports from the theme's own modules.

**Store apps:** at least **Printify** (48+ products, vendor `Printify`) and
**ODMPOD** (4 draft products). Full installed-app list was not enumerated.

**External services referenced in code but not integrated:** Meshy, Higgsfield
(both as future asset sources for the Phase 3 slots).

---

# G. Unusual implementation details (read before editing)

1. **Doubled class for specificity** — `.undr-world-boot.undr-world-boot` beats
   Horizon's 3-selector `.section { background: none }` reset. Intentional.
2. **`[id$="__key"]` selectors everywhere** — Shopify renders JSON-template
   section wrappers as `shopify-section-template--<instance>__<key>`. Bare
   `#shopify-section-<key>` silently never matches.
3. **`.shopify-section` qualifier is load-bearing** — block wrappers share the id
   shape; without the class, an object with a matching block key scrolls to
   itself. This bug actually occurred with a block keyed `current_chapter`.
4. **`body ` prefix on `.color-custom-group_hoshoku_side`** — beats
   `contrast-override.liquid`'s inline rule which lands later in the DOM.
5. **World derived from the eyebrow label string**, and the test order
   (`hoshoku` → `ndrrare` → `ndr`) matters because "ÜNDRRARE" contains "NDR".
6. **`*/` inside `_undr-world-object.liquid`'s CSS comment silently breaks CSS.**
   It has already happened once.
7. **Price opacity 0.7 is a measured accessibility floor**, not a taste choice.
   0.6 → 4.05:1, below AA.
8. **World Hub grid avoids `justify-items: center`** — it shrink-wraps Shopify's
   `.shopify-block` wrappers and desyncs object widths.
9. **`data-active` and `data-dismissed` coexist** — dismissal adds, never
   removes. The dismissed rule wins by source order at matched specificity.
10. **`sessionStorage` failures are swallowed deliberately** — the boot sequence
    replays rather than erroring.
11. **Both world token sets are defined unconditionally** on `:root`, so a
    subtree can opt into either world with one source of truth.

---

# H. Known technical debt

| Item | Severity |
|---|---|
| Dev theme diverged from live with unshipped fixes | 🔴 |
| Two dead collection references live on the homepage | 🔴 |
| `settings_data.json` diverged and undiffed | 🟠 |
| HOSHOKU collection template built but unassignable as-is | 🟠 |
| Unapproved copy sitting in a dev template | 🟠 |
| Flagship product ACTIVE at 0 inventory | 🟠 |
| Placeholder Story page live in main nav | 🟡 |
| Empty Journal live in main nav | 🟡 |
| Archive teaser with no destination | 🟡 |
| Empty Accessories collection | 🟡 |
| Supplier boilerplate copy + off-brand SEO tags on many products | 🟡 |
| Vendor field exposes fulfilment partners as the brand | 🟡 |
| Sample "Example product" entries still present | 🟢 |
| Duplicate archived Printify products | 🟢 |
| 4 unbranded ODMPOD duplicate drafts | 🟢 |
| 3 stale Horizon/Radiant theme copies | 🟢 |
| `hoshoku_floating.gif`: 1.8 MB at 365×365 | 🟠 |

---

# I. Things another Claude could easily break

1. **Publishing the Development theme without diffing `settings_data.json`** →
   could silently change sitewide colors/typography.
2. **"Simplifying" the doubled class selector** → PRESS START loses its
   background entirely.
3. **"Fixing" `[id$="__key"]` to `#shopify-section-key`** → all HOSHOKU scoping
   and all hub scrolling silently stop working. This exact bug already shipped
   once.
4. **Dropping the `.shopify-section` qualifier** → objects scroll to themselves.
5. **Writing `*/` in that CSS comment** → silently eats the ÜNDR accent rule.
6. **Lowering price opacity** → drops below WCAG AA.
7. **Replacing `--world-*` indirection with hardcoded colors** → destroys the
   entire world system and every future switch with it.
8. **Making PRESS START required, unskippable, or JS-dependent** → violates the
   most-repeated constraint in the codebase.
9. **Turning world objects into non-links or fake destinations** → violates "no
   invented destinations" and breaks the no-JS path.
10. **Reordering or renaming homepage sections** → `target_section_id` values are
    keys from `templates/index.json`; renaming a section silently breaks the hub
    object that points at it (it degrades to navigation, so it *looks* fine).
11. **Editing theme files through the Shopify admin editor** → overwrites what
    the Git repo has; the JSON files carry an auto-generated warning header.
12. **Assuming `current-chapter` (collection) and `current_chapter` (section) are
    the same thing.** They are not.
13. **Adding an auto-advance timer to PRESS START** without proposing it first.
14. **Treating archived products as "the Archive."** Archived products are hidden
    from the storefront; the brand's Archive is an unbuilt curated concept.
