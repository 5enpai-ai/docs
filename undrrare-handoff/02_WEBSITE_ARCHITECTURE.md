# 02 — Website Architecture

Everything here was read live from the Shopify Admin API on 2026-09-04 against
the **live MAIN theme `undrrare-theme-phase2-f661bce`** unless a line explicitly
says otherwise. Differences in the **Development** theme are called out inline.

> **Caveat:** the theme Git repo was not accessible, so this describes the theme
> *as deployed*. The repo's `CLAUDE.md` — cited by nearly every custom file as
> the governing document ("World-First Homepage Architecture", "World-State
> Design", "ÜNDRRARE Visual Reference System", "Future Website Experience
> Architecture") — could not be read. Get it.

---

## 1. Base theme

Shopify **Horizon** (theme store ID 2481). This is Horizon's newer architecture:
a top-level `blocks/` directory, `{% content_for 'blocks' %}`, `ref=`/`on:` DOM
bindings, a `Component` base class imported from `@theme/component`, JSON
templates, and section groups. Private/nested blocks are `_`-prefixed by
convention (`_product-card`, `_collection-card`, and the custom
`_undr-world-object`).

**The custom surface is deliberately tiny** — 5 files against ~400 theme files:

| File | Size (live) | Purpose |
|---|---|---|
| `sections/undr-world-boot.liquid` | 8,956 B | PRESS START boot layer |
| `assets/undr-world-boot.js` | 3,190 B | boot overlay behavior |
| `sections/undr-world-hub.liquid` | 4,508 B | World Hub container |
| `assets/undr-world-hub.js` | 2,961 B | click→scroll enhancement |
| `blocks/_undr-world-object.liquid` | 13,076 B | one world object |

Plus two shared-file edits: `assets/base.css` (world tokens) and
`layout/theme.liquid` (token aliasing).

## 2. The landing experience (`templates/index.json`)

Nine sections, in this order. **Identical order in live and Development.**

| # | Section key | Type | What it is |
|---|---|---|---|
| 1 | `undr_world_boot` | `undr-world-boot` (custom) | PRESS START |
| 2 | `undr_world_hub` | `undr-world-hub` (custom) | World Hub, 5 objects |
| 3 | `hoshoku_flagship_hero` | `featured-product-information` | HOSHOKU Beanie 2.0 |
| 4 | `hoshoku_story` | `section` | HOSHOKU story block |
| 5 | `world_split` | `section` | ÜNDR ↔ HOSHOKU split |
| 6 | `undr_entry_product` | `featured-product-information` | Ü-000 Box Logo Shirt |
| 7 | `current_chapter` | `product-list` | Ü-002 // SEEK grid |
| 8 | `featured_products` | `product-list` | shop grid |
| 9 | `archive_teaser` | `section` | Archive teaser |

Note that sections 3–9 are **stock Horizon sections configured with real
content** — not custom code. Only 1 and 2 are custom. That is the architecture's
central bet: build the world layer, reuse Horizon for everything else.

## 3. PRESS START (`undr_world_boot`)

**Live settings:** eyebrow `ÜNDRRARE`, heading `PRESS START`, button
`PRESS START`, atmosphere product `hoshoku-2-0-beanie-orange-cream`, width
full-width.

### How it works
It renders as **plain, in-flow content by default**. `undr-world-boot.js`
*promotes* it to a full-viewport overlay by adding `data-active`; dismissal adds
`data-dismissed` alongside. It never removes or hides the sections underneath.

The component skips entirely (`data-dismissed` immediately, no overlay) when:
- `shopify-design-mode` is set (theme editor), **or**
- `prefersReducedMotion()`, **or**
- `sessionStorage['undrWorldBootSeen'] === '1'` (already seen this session).

If `sessionStorage` throws (private mode, blocked cookies) it fails open — the
sequence simply replays. Documented as "not a functional break."

### Interaction
- `on:click="/activate"` on **both** the root element (click anywhere to enter)
  and the button.
- `Escape` also activates.
- On connect: `lockScroll`, focus the start button.
- On dismiss: `unlockScroll`, write the session flag, then move focus to the
  first link/button inside `undr-world-hub-component` — *"so keyboard users land
  somewhere meaningful instead of on a now-hidden button."*
- **No auto-advance timeout**, explicitly: *"No arbitrary auto-advance timeout
  yet, per explicit instruction — a duration and its UX/performance reasoning
  must be proposed and reviewed before one is added."* **Treat as a standing
  instruction from the owner.**

### Visual construction
Two stacked atmosphere layers behind the content, inside an `isolation: isolate`
stacking context:
- `::before` — the atmosphere image, `grayscale(0.65) brightness(0.32)
  contrast(1.05)`, opacity `0.6`. Renders nothing if no image is set; the flat
  `--world-background` shows through.
- `::after` — inline-SVG `feTurbulence` fractal noise, opacity `0.05`,
  `mix-blend-mode: overlay`. First grain in the theme.

Exit transition is opacity → 0 with `transform: scale(1.04)` — described as the
**"materialization" cue**: *"a threshold being pushed through, not a dialog
closing."*

**Mobile:** below 749px the overlay switches to `justify-content: flex-start`
with `padding-top: 18vh`, so Shopify's own fixed bottom `#shopify-pc__banner`
(cookie/privacy banner, outside theme control) can never cover the button.

### CSS specificity note (important if you edit this)
Horizon's `base.css` zeroes `background` on every `.section` inside
`.shopify-section:not(.header-section)`. That reset carries **3 class-level
selectors**, so the boot section's own rules use
`.shopify-section .undr-world-boot.undr-world-boot` (4) to beat it. The doubled
class is intentional. Don't "clean it up."

### Development-theme differences
1. New `atmosphere_image` **image_picker** setting — *"PHASE 3 replaceable-asset
   slot: PRESS_START_BACKGROUND."* Takes priority over `atmosphere_product`.
   **Currently unset.**
2. A staggered content reveal on `[data-active]` — eyebrow 0.05s, mark 0.15s,
   button 0.3s, opacity + 8px translate, `prefers-reduced-motion` gated. Comment:
   *"this is the one place in the boot sequence that earns entrance motion, so it
   stays understated... rather than a game-menu flourish."*

## 4. World Hub (`undr_world_hub`)

**Live settings:** heading `ENTER THE WORLD`, width page-width. Contains five
`_undr-world-object` blocks in a `repeat(auto-fit, minmax(14rem, 1fr))` grid.

The whole hub is **HOSHOKU-scoped** via `[id$="__undr_world_hub"]` in `base.css`
— it renders on the cream HOSHOKU surface.

A restrained load animation (0.5s, opacity + 12px translate, 0.15s delay,
`backwards`) plays behind the boot overlay: *"this plays out of view for a
normal-speed visit and simply lands in its resting state for a slow one; either
way nothing ever depends on it."*

**Grid note worth preserving:** the list deliberately does **not** use
`justify-items: center`. Shopify wraps each block in its own `.shopify-block`
div, and centering shrink-wraps those wrappers — which sized an image object to
its image but the text-framed Shop object to its short label. Fix: let wrappers
stretch, center the object inside via `width:100% + max-width + margin-inline:auto`.

**No orbit/float motion.** The section comment: *"No floating/orbit motion yet —
that is Phase 3, pending review of this static prototype."*

## 5. World objects — the five, live

| Block key | Resource | Eyebrow | Target section | Behavior |
|---|---|---|---|---|
| `hoshoku_beanie` | product `hoshoku-2-0-beanie-orange-cream` | HOSHOKU | `hoshoku_flagship_hero` | scroll |
| `hoshoku_world` | collection `hoshoku` (title override "The World of HOSHOKU") | HOSHOKU | `hoshoku_story` | scroll |
| `undr_entry` | product `u-000-box-logo-shirt-1` | ÜNDR | `undr_entry_product` | scroll |
| `undr_current_chapter` | collection `u-002-seek` | ÜNDR | `current_chapter` | scroll |
| `shop_all` | url `shopify://collections/all` (title "Shop All") | ÜNDRRARE | *(none)* | navigates |

### Resolution logic (`_undr-world-object.liquid`)
Priority order: **product → collection → manual URL**. Title, image and price are
read **live** from whichever resource is assigned; nothing is hardcoded. The
manual-URL option exists only for destinations with no single resource behind
them (the full catalog) and still requires a real URL plus a title.

- Product → `product.url`, featured image, `selected_or_first_available_variant.price`
- Collection → `collection.url`, `collection.image | default: collection.products.first.featured_image`, product count instead of price
- No image → a typographic frame showing the object's real title (never a
  fabricated placeholder graphic)

### Per-object world identity
The object derives its world from **its own eyebrow label** — so there is no
second setting to keep in sync:

```
contains 'hoshoku'  → hoshoku
contains 'ndrrare'  → undrrare
contains 'ndr'      → undr
```

**Order matters and is commented as such:** "ÜNDRRARE" contains "NDR", so it must
be tested before "ÜNDR". Anything unrecognized falls through to the inherited
scope (safe default).

Matched objects re-point **only** `--world-accent-primary` and
`--world-accent-secondary` — deliberately *not* background/foreground, *"because
the objects share one continuous surface and should read as different artifacts
sitting in the same space, not as mismatched panels."* Without this, ÜNDR objects
inside the HOSHOKU-scoped hub would render orange and the identities would
collapse.

### Two comments in this file you must respect
1. **Do not write a literal `*/` sequence inside its CSS block comment.** *"It
   closes the CSS comment early and silently eats the rule that follows — that
   exact mistake broke the ÜNDR rule below once already, and it fails quietly
   rather than erroring."*
2. **Price opacity is 0.7, not lower.** At 0.6 measured contrast was 4.05:1
   against HOSHOKU cream — below the 4.5:1 AA floor for 12px text. 0.7 measures
   ~5.5:1. *"Don't lower this without re-measuring — it's real price
   information, not decoration."*

### Development-theme difference
New `world_artifact_image` image_picker per object — *"PHASE 3 replaceable-asset
slot: WORLD_OBJECT."* It layers a blurred render **behind** the real product
photo as a second background layer, additive only: `var(...)` falls back to
`none`, so unset objects render byte-identically. **Currently unset on all five.**

## 6. Progressive-reveal / scroll enhancement (`undr-world-hub.js`)

On an object click, it looks for the destination section and, if found,
`preventDefault()`s and smooth-scrolls (instant under reduced motion), then moves
focus into the target with a temporary `tabindex="-1"` removed on blur.

**Two hard-won details in the selector, both commented:**

```js
document.querySelector(
  `.shopify-section[id$="__${targetId}"], .shopify-section#shopify-section-${targetId}`
)
```

1. Shopify renders a JSON-template section's wrapper id as
   `shopify-section-template--<instance-id>__<section-key>`, **not** the bare
   `shopify-section-<key>`. Matching on the `__<key>` suffix survives template
   instance changes and renames.
2. **The `.shopify-section` qualifier is load-bearing, not decoration.** Shopify
   gives *block* wrappers the same id shape (`shopify-block-<hash>__<block-key>`),
   so a block whose key matches a section key is found first in DOM order and an
   object scrolls to itself. *"That actually happened with a block keyed
   `current_chapter`."*

If no matching section exists on the page, it does **not** preventDefault — the
real product link navigates normally.

## 7. HOSHOKU experience

**`hoshoku_flagship_hero`** — stock `featured-product-information`, product
`hoshoku-2-0-beanie-orange-cream`, media on the **left**, equal columns, 48px gap,
64px vertical padding. HOSHOKU-scoped.

**`hoshoku_story`** — stock `section`, centered column, 72px padding:
- Eyebrow: `THE WORLD OF HOSHOKU`
- Heading: `Two halves. One character.`
- Body: *"Rabbit on one side, fox on the other, stitched down the middle. HOSHOKU
  is a character first — collectible, handmade, one piece at a time. The 2.0
  Beanie is the current chapter; the OG is where it started."*
- CTA: **Shop HOSHOKU** → `shopify://collections/hoshoku` ✅ valid

HOSHOKU-scoped.

## 8. ÜNDR experience

**`undr_entry_product`** — stock `featured-product-information`, product
`u-000-box-logo-shirt-1`, media on the **right** (mirroring the HOSHOKU hero's
left). Not HOSHOKU-scoped, so it renders in the ÜNDR dark core.

**`world_split`** — full-width row, two 50%-wide groups, no gap, zero padding,
stacking vertically on mobile:

| | `group_hoshoku_side` | `group_undr_side` |
|---|---|---|
| Eyebrow | Bright side | Dark side |
| Heading | HOSHOKU | ÜNDR |
| Body | Playful, strange, colorful, collectible. Half rabbit, half fox. | Underground, technical, archival. The other half of the universe. |
| CTA | Enter HOSHOKU → `shopify://collections/hoshoku` ✅ | Enter ÜNDR → `shopify://collections/core` ❌ **BROKEN LIVE** |

`group_hoshoku_side` is HOSHOKU-scoped by class
(`body .color-custom-group_hoshoku_side`); the ÜNDR side stays core. The split is
therefore literally light-vs-dark on screen.

**The broken CTA:** `core` is not a collection handle. The real handle is
`u-000-core`. **Fixed in the Development theme, not published.**

## 9. Commerce transition

The homepage moves from world → commerce gradually rather than at a hard
boundary: PRESS START (pure world) → World Hub (world objects that *are* products)
→ flagship/story (product presented as character) → split (identity choice) →
entry product → current chapter grid → shop grid → archive teaser.

Note that world objects already carry **real prices and real product counts** —
commerce is visible inside the world layer, not hidden until later.

## 10. Current Chapter (`current_chapter`)

Stock `product-list`. Collection **`u-002-seek`**, grid, max 5 products, 4 columns
desktop / 2 mobile, carousel-on-mobile **off**, 24px column gap, 36px row gap.

> **⚠️ Naming trap:** this section points at `u-002-seek`, **not** at the
> collection whose handle is literally `current-chapter`. That separate
> collection exists, holds 2 products, and is used nowhere on the homepage. Do
> not "fix" one to match the other without asking.

## 11. Shop (`featured_products`)

Stock `product-list`, grid, max 8, 4 columns desktop / 2 mobile.

| | Live (MAIN) | Development |
|---|---|---|
| Heading | `Best Sellers` | `Shop the Collection` |
| Collection | **`best-sellers`** ❌ does not exist | `u-002-seek` ✅ |

**This is live-broken.** There is no `best-sellers` collection in the store.

The catalog-wide "Shop" entry point is instead the `shop_all` world object and
the nav item, both pointing at `/collections/all`.

## 12. Archive (`archive_teaser`)

Stock `section`, centered, 80px padding:
- Eyebrow: `ARCHIVE`
- Heading: `Recovered artifacts.`
- Body: *"Retired pieces, held rather than discarded. Curation in progress."*
- **No CTA, no link, no destination.**

There is no archive collection, page, or template. 23 products are ARCHIVED in
Shopify (which hides them from the storefront entirely — archived is not the same
as a curated archive). The section is honest about being unfinished ("Curation in
progress"), which is fine, but it currently leads nowhere.

## 13. Product storytelling

**[Live, and genuinely strong.]** The format on the flagship products:

```
ARCHIVE SYSTEM
FILE NO. HOSHOKU-02
ARTIFACT:   🐰/🦊 Beanie 2.0 — Orange / Cream
CONDITION:  ONE-OFF. HAND-LOGGED.

<narrative — what it is, physically and in the world>

PRODUCTION NOTE:
— crocheted by hand, stitch by stitch...
— every ear sits at a slightly different angle. that is the file, not a flaw.
— no two come out identical and none are reprinted.

DETAILS: <real materials, sizing, fit>
```

The Ü-collection products use a lighter variant: `Ü-00N // NAME` heading, a
short world/personal passage, then **DETAILS** and **FIT** headings with real
specs. Coverage is uneven — the beanies and the flagship Ü products have this;
many Printify products still carry raw supplier spec dumps.

## 14. Navigation

**Main menu:** Home `/` · Shop `/collections/all` · Story `/pages/story` ·
Journal `/blogs/news`

**Footer menu:** Search · Your Privacy Choices
**Footer links:** Shop · Story · Journal · Contact

Problems:
- **Story is a placeholder page.** Its own body: *"This page is a placeholder.
  Replace this copy with the full ÜNDR origin story."*
- **Journal points at a blog with 0 articles.**
- **No Archive item**, despite the homepage teaser.
- **No HOSHOKU or ÜNDR items** — the two worlds are reachable only from the
  homepage, not from the nav on any other page.

Header/footer are section groups: `sections/header-group.json`,
`sections/footer-group.json`. Header is `sections/header.liquid` (54.8 KB) with
`snippets/header-drawer.liquid` (59.2 KB) for mobile.

## 15. Mobile behavior

**Breakpoint convention: 749px** (`max-width: 749px`), stated in the boot section
as matching `assets/base.css`.

Confirmed mobile handling:
- PRESS START anchors to `18vh` from the top instead of centering (banner
  avoidance).
- World Hub grid reflows via `auto-fit / minmax(14rem, 1fr)` — no explicit mobile
  rule; it collapses to 1 column on narrow screens.
- `world_split` groups: `vertical_on_mobile: true`, `width_mobile: fill` — the
  two halves stack.
- Product grids: 2 columns mobile, `mobile_card_size: 60cqw`, carousel off.
- Cart is a **drawer**; mobile quick-add is on.
- Mobile navigation is the header drawer.

**[UNVERIFIED]** No mobile or tablet rendering was checked this session. Tablet
(750–1024px) behavior in particular is unexamined — `auto-fit minmax(14rem)`
will produce a 3-or-4-column hub there, which may or may not be intended.

## 16. Desktop behavior

- Page width: **wide**.
- World Hub: `auto-fit minmax(14rem, 1fr)` → typically 5 across at full width.
- Alternating media sides: HOSHOKU hero media left, ÜNDR entry media right.
- `world_split`: true 50/50 row, medium height.
- Product grids: 4 columns.
- PRESS START: dead-centered full viewport.

## 17. World-state design system (`layout/theme.liquid` + `base.css`)

The most architecturally significant thing in the theme.

`<html data-world="undr">` is set in `layout/theme.liquid`. Immediately after
Shopify's `color-palette` renders (so it wins the cascade), a block re-points
Shopify's own variables at the world tokens:

```
--color-background            → var(--world-background)
--color-foreground            → var(--world-foreground)
--color-border                → var(--world-foreground)
--color-primary-button-*      → var(--world-button-*)
--color-input-*               → var(--world-*)
--color-variant-*             → var(--world-*)
--color-selected-variant-*    → var(--world-*)
```

> "that indirection is what makes existing components world-aware with zero
> changes to the components themselves."

Three layers:
1. **Constants** — `--undr-*` and `--hoshoku-*`, both defined **unconditionally**
   on `:root` so any subtree can opt into either world using the same single
   source of truth.
2. **Selection** — `:root, html[data-world="undr"]` and `html[data-world="hoshoku"]`
   map constants onto `--world-*`.
3. **Aliasing** — `layout/theme.liquid` maps `--world-*` onto `--color-*`.

### Local (per-section) scoping
Live scoping targets: `[id$="__hoshoku_flagship_hero"]`,
`[id$="__hoshoku_story"]`, `[id$="__undr_world_hub"]`, and
`body .color-custom-group_hoshoku_side`.

Two documented gotchas:
- The `[id$="__key"]` form exists because of the same Shopify id-prefix issue as
  the scroll lookup. The comment records that **all three sections were rendering
  transparent** (plain dark core, not HOSHOKU cream) before this fix — *"confirmed
  live via computed styles."*
- The `body ` prefix on the group selector is deliberate: `contrast-override.liquid`
  emits its own rule for that class inline, later in the DOM, and a bare class
  selector loses the cascade race.

### Status, stated in code
> "'undr' is the sitewide default. 'hoshoku' values were APPROVED 2026-08-26...
> and are now applied **scoped to specific homepage sections**... not sitewide,
> and not behind any switching UI. **There is still no world-selection screen, no
> persistent toggle, and no mechanism for a visitor to set this themselves — that
> remains explicitly future work.**"

The per-section scoping and a future sitewide toggle are *"the same mechanism,
not two systems."*

## 18. Templates, sections, snippets, assets — inventory

**Templates (live):** `404.json` `article.json` `blog.json` `cart.json`
`collection.json` `gift_card.liquid` `index.json` `list-collections.json`
`page.contact.json` `page.json` `password.json` `product.json` `search.json`

**Development adds:** `templates/collection.hoshoku.json` (8,255 B) — see §19.

**Sections:** 44 total. Custom: `undr-world-boot.liquid`, `undr-world-hub.liquid`.
Largest stock: `header.liquid` (54.9 KB), `section.liquid` (54.2 KB),
`hero.liquid` (44.6 KB), `quick-order-list.liquid` (37.8 KB).

**Blocks:** ~95. Custom: `_undr-world-object.liquid`.

**Snippets:** ~130. Notable for this work: `theme-styles-variables.liquid`
(32.6 KB), `contrast-override.liquid` (8.5 KB — the cascade competitor noted
above), `group.liquid`, `icon.liquid` (133 KB), `product-media-gallery-content.liquid`
(37 KB).

**Assets:** ~125. Custom: `undr-world-boot.js`, `undr-world-hub.js`. Core:
`base.css` (59.2 KB live / 59.7 KB dev), `component.js`, `utilities.js`,
`morph.js`, `scrolling.js`, `product-form.js` (40.4 KB).

**Imports used by the custom JS** — these are the theme's own module aliases:
`@theme/component` (`Component`), `@theme/utilities`
(`prefersReducedMotion`, `lockScroll`, `unlockScroll`), `@theme/scrolling`
(`scrollIntoView`).

## 19. Phase 3 in flight — `templates/collection.hoshoku.json` (Development only)

An **isolated HOSHOKU collection template**, three sections:

1. **`hoshoku_intro`** (`section`) —
   - Eyebrow `HOSHOKU`
   - Statement (h2): *"HOSHOKU isn't a mascot. HOSHOKU is a character who happens
     to live here."*
     — block name: **"Opening statement — PENDING APPROVAL, see
     PHASE_3_DISCOVERY.md §0.3 item 1"**
   - Lore: `{{ closest.collection.description }}` — block name *"Lore (real
     collection description, unedited)"*. Pulls live copy rather than duplicating it.
   - Flagship group: a `product-card` for `hoshoku-2-0-beanie-orange-cream`
2. **`hoshoku_collection_main`** (`main-collection`) — the real grid, with
   horizontal filters, sorting and grid-density controls enabled
3. **`hoshoku_continue`** (`section`) — a single button: **"Continue to Ü-002 //
   SEEK"** → `shopify://collections/u-002-seek` ✅

The `base.css` diff adds those three section ids to the HOSHOKU scoping list,
with the note:

> "the three `hoshoku_*` ids added below belong to
> templates/collection.hoshoku.json (the isolated HOSHOKU collection template —
> see PHASE_3_DISCOVERY.md §0.2/§0.3 for why an isolated template + this same
> per-section-id scoping was chosen over a sitewide data-world switch on
> `<html>`). Additive only — no existing id, value, or selector above was
> changed."

**⚠️ It cannot render yet.** The `hoshoku` collection's `templateSuffix` is
`null` in Shopify. Publishing the theme is not enough — the collection must be
assigned the "hoshoku" template in the Shopify admin. That is a **catalog**
change, not a theme change, so per the project's own separation rule it needs
doing deliberately.
