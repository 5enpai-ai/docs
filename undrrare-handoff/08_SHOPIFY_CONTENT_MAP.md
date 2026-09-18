# 08 — Shopify Data / Content Map

Read live from the Shopify Admin API, 2026-09-04. Read-only; nothing changed.

**Legend:** ✅ confirmed live and resolving · ❌ **broken — does not exist** ·
🔲 placeholder / empty · ⚠️ trap or ambiguity

---

## 1. 🔴 Broken references — read this first

Two homepage references point at collections that **do not exist**. Both are live
in production. Both are already fixed in the unpublished Development theme.

| # | Where | Reference | Reality | Effect |
|---|---|---|---|---|
| 1 | `world_split` → `group_undr_side` → `cta` | `shopify://collections/**core**` | ❌ no such handle; the real one is `u-000-core` | The **"Enter ÜNDR"** button — one of only two identity CTAs on the homepage — is dead |
| 2 | `featured_products` section | collection `**best-sellers**` | ❌ no such collection | The homepage's **largest product grid** has no source |

**Dev-theme fixes (unpublished):** `core` → `u-000-core`; `best-sellers` →
`u-002-seek` with the heading changed "Best Sellers" → "Shop the Collection".

**One more to verify:** `config/settings_data.json` sets
`"empty_state_collection": "featured-products-4"`. **No collection with that
handle exists either.** It only surfaces in empty-state UI, so it's lower
priority, but it's the same class of dead reference.

---

## 2. Collections — all 8

| Handle | Title | Products | Template | Description | Status |
|---|---|---|---|---|---|
| `u-000-core` | Ü-000 // CORE | 12 | default | *"Ü.NITED N.EVER D.IVIDED R.E: … September 2023, the first batch ÜNDR ever released… If it ain't ÜNDR, I'm over it."* | ✅ live |
| `u-001-enlightenment` | Ü-001 // ENLIGHTENMENT | 6 | default | *"three realms, one origin form… Hades below. Midgard where you stand. Nirvana where the reaching stops."* | ✅ live |
| `u-002-seek` | Ü-002 // SEEK | 9 | default | *"the awakening after the enlightenment…"* | ✅ live, **image = `hoshoku_floating.gif` (1.8 MB)** |
| `hoshoku` | HOSHOKU | 14 | **`null`** ⚠️ | *"Fox half, rabbit half, one seam down the middle."* | ✅ live — but see §6 |
| `handmade-🐰` | HANDMADE // 🐰/🦊 | 2 | default | *"Not print-on-demand. Crocheted by hand, one at a time, made to order."* | ✅ live. ⚠️ **emoji in the handle** |
| `current-chapter` | Current Chapter | 2 | default | *"Limited release. Limited time, never again."* | ⚠️ **used nowhere** — see §7 |
| `accessories` | Accessories | **0** | default | *"…plushies, and whatever else doesn't fit on a hanger."* | 🔲 **empty** |
| `frontpage` | Home page | 1 | default | *(none)* | 🔲 Shopify default, unused by this theme |

**None of the collections are smart/automated** — every one is `sortOrder:
MANUAL` with `ruleSet: null`. Products must be added by hand. That means a new
product does **not** appear anywhere automatically.

⚠️ **`handmade-🐰`** contains a literal emoji. It works, but it URL-encodes to
`/collections/handmade-%F0%9F%90%B0` and is fragile in code, analytics, and
anything doing string comparison. Don't rename it casually (it would break any
existing link), but be aware.

---

## 3. Homepage sections → Shopify objects

The complete dependency map. **Anything here that changes handle breaks the
homepage.**

| # | Section key | Type | Shopify object | Status |
|---|---|---|---|---|
| 1 | `undr_world_boot` | custom | product `hoshoku-2-0-beanie-orange-cream` (atmosphere) | ✅ |
| 2 | `undr_world_hub` | custom | 5 objects — see §4 | mixed |
| 3 | `hoshoku_flagship_hero` | `featured-product-information` | product `hoshoku-2-0-beanie-orange-cream` | ✅ ⚠️ 0 inventory |
| 4 | `hoshoku_story` | `section` | CTA → `shopify://collections/hoshoku` | ✅ |
| 5 | `world_split` | `section` | HOSHOKU CTA → `collections/hoshoku` ✅ · ÜNDR CTA → `collections/core` | ❌ **BROKEN** |
| 6 | `undr_entry_product` | `featured-product-information` | product `u-000-box-logo-shirt-1` | ✅ |
| 7 | `current_chapter` | `product-list` | collection `u-002-seek` (max 5) | ✅ ⚠️ see §7 |
| 8 | `featured_products` | `product-list` | collection `best-sellers` (max 8) | ❌ **BROKEN** |
| 9 | `archive_teaser` | `section` | *(none — no link at all)* | 🔲 dead end |

---

## 4. World Hub objects → Shopify objects

| Block key | Type | Handle | Eyebrow | Scrolls to | Status |
|---|---|---|---|---|---|
| `hoshoku_beanie` | product | `hoshoku-2-0-beanie-orange-cream` | HOSHOKU | `hoshoku_flagship_hero` | ✅ |
| `hoshoku_world` | collection | `hoshoku` | HOSHOKU | `hoshoku_story` | ✅ |
| `undr_entry` | product | `u-000-box-logo-shirt-1` | ÜNDR | `undr_entry_product` | ✅ |
| `undr_current_chapter` | collection | `u-002-seek` | ÜNDR | `current_chapter` | ✅ |
| `shop_all` | url | `shopify://collections/all` | ÜNDRRARE | *(none — always navigates)* | ✅ |

**How each renders (live-resolved, never hardcoded):**
- Product objects → product title, featured image, first available variant price
- Collection objects → collection title (or override), `collection.image` falling
  back to the first product's featured image, and a **product count** instead of
  a price
- URL object → the title override, and a typographic frame (no image exists)

**Consequences worth knowing:**
- `hoshoku_world` shows the **HOSHOKU collection's product count (14)**. Changing
  what's in that collection changes the homepage.
- `undr_current_chapter` uses `u-002-seek`, whose collection image is the
  **1.8 MB `hoshoku_floating.gif`** — so that GIF is very likely loading in the
  World Hub. See `07_ASSET_INVENTORY.md`.
- `hoshoku_beanie` shows **$75** live from the variant.
- `target_section_id` values are **section keys from `templates/index.json`**.
  Rename a section and the object silently degrades to plain navigation — it
  still "works," so the regression is invisible.

---

## 5. Products

**68 total: 13 ACTIVE, 24 DRAFT, 31 ARCHIVED.**

### All 13 ACTIVE products (everything a customer can actually buy)

| Handle | Title | Price | Variants | Inventory | Vendor |
|---|---|---|---|---|---|
| `hoshoku-2-0-beanie-orange-cream` | HOSHOKU Beanie (2.0)🐰/🦊 | $75 | 1 | **0** ⚠️ | ÜNDR |
| `hoshoku-beanie-og` | HOSHOKU Beanie (OG) 🐰/🦊 | $55 | 1 | 4 | ÜNDR 🐰/🦊 |
| `u-000-box-logo-shirt-1` | Ü-000 "BOX LOGO" SHIRT | $20 | 42 | POD | Printify |
| `u-002-seek-u-shirt` | Ü-002 "Seek Ü" Shirt | $40 | 24 | POD | Printify |
| `u-002-seek-u-shorts` | Ü-002 "Seek Ü" Shorts | $30 | 5 | POD | Printify |
| `u-002-seek-u-tank-top` | Ü-002 "Seek Ü" Tank Top | $25 | 12 | POD | Printify |
| `u-002-seek-reality-oversized-shirt` | Ü-002 "Seek Reality" Oversized Shirt | $45 | 18 | POD | Printify |
| `u-002-seek-truth-oversized-shirt` | Ü-002 "Seek Truth" Oversized Shirt | $45 | 18 | POD | Printify |
| `u-002-hoshoku-shirt-1` | Ü-002 Hoshoku Shirt | $30 | 9 | POD | ÜNDR |
| `u-002-hon-shirt` | Ü-002 "Hon" Shirt | $25 | 24 | POD | Printify |
| `u-002-best-friends-bikini` | Ü-002 "Best Friends" Bikini | $30 | 8 | POD | Printify |
| `u-002-seek-bikini` | Ü-002 "Seek" Bikini | $30 | 8 | POD | Printify |
| `u-002-voorhees-shirt` | Ü-002 "Voorhees" Shirt | $25 | 17 | POD | Printify |



**Observations:**
- The live catalog is **almost entirely Ü-002 // SEEK** plus the two beanies and
  the Ü-000 box logo. Ü-001 // ENLIGHTENMENT is **entirely DRAFT or ARCHIVED** —
  the Hades / Midgard / Nirvana realm shirts, the Chibi pieces, K-BOY, Best
  Friends. **None of the three-realms worldbuilding is currently purchasable**,
  even though the collection copy describes it in detail.
- `hoshoku-2-0-beanie-orange-cream` is **ACTIVE with 0 inventory** and is the
  homepage flagship in three places.
- Printify inventory figures (9999 / 59994 / 719928…) are fictitious POD
  placeholders. Normal.

### ⚠️ Products the homepage depends on
Renaming any of these handles breaks the site:
`hoshoku-2-0-beanie-orange-cream` (×3 dependencies), `u-000-box-logo-shirt-1`.

### 🔲 Draft products of note
`u-000-undr-clogs`, `u-000-hoshoku-pj-pants`, `u-000-hoshoku-shorts`,
`u-000-box-logo-hat`, `u-000-box-logo-phone-case`, `u-000-box-logo-tote-bag`,
`u-000-hoshoku-sticker-pack-1`, `u-001-midgard-shirt`, `u-001-hades-shirt`,
`u-001-nirvana-shirt`, `u-001-chibi-crop-top`, `u-001-best-friends-shirt`,
`u-001-k-boy-shirt-1`, `u-001-rare-button-up`, and others.

**`u-001-rare-button-up`** is notable: *"The piece that carries the brand's own
name. Split topo pattern across the body, Ü stitched at the chest"* — $55, DRAFT,
**no image**, 0 inventory. Sounds significant; ask about it.

### ⚠️ Junk in the catalog
- **4 × "Example product"** — vendor `My Store`, tag `Sample Product`, ARCHIVED.
  Shopify sample data from store setup.
- **4 × ODMPOD drafts** — `womens-slim-raglan-long-sleeve-t-shirt` and
  `vintage-wash-boxy-distressed-hem-t-shirt`, each duplicated with a `-2` suffix.
  Unbranded, no ÜNDR naming, inventory `9999999`.
- **Duplicate archived Printify products** — `u-000-undr-clogs` / `-1`,
  `u-000-hoshoku-plush-pillow` / `-1`, `eat-me-crop-top` / `-1`,
  `u-000-hello-undr-crop-top` / `-1`, `u-000-punk-crop-top` / `-1`.
- **Several ARCHIVED products at $0.00 with no media.**

---

## 6. ⚠️ The HOSHOKU collection template gap

`templates/collection.hoshoku.json` exists in the **Development theme**. The
`hoshoku` collection's `templateSuffix` is **`null`**.

**Publishing the theme will not make it render.** Shopify picks a
`collection.<suffix>.json` template only when the collection is assigned that
suffix in the admin. Until then, `/collections/hoshoku` uses the default
`collection.json`, and the three-section HOSHOKU experience — plus the three
`hoshoku_*` HOSHOKU-scoping ids added to `base.css` — do nothing.

**This is a catalog change**, so per the project's own separation rule it should
be done deliberately and separately from the theme deploy. It's instantly
reversible (set the suffix back to null).

---

## 7. ⚠️ The `current_chapter` naming trap

Three similarly-named things that are **not** the same:

| Thing | What it is | Points at / contains |
|---|---|---|
| `current_chapter` | homepage **section key** in `templates/index.json` | collection **`u-002-seek`** |
| `current-chapter` | Shopify **collection handle** | 2 products; **used nowhere on the site** |
| `undr_current_chapter` | World Hub **block key** | collection `u-002-seek`, scrolls to section `current_chapter` |

A future agent will very reasonably assume the section should point at the
collection with the matching name, "fix" it, and silently change what the
homepage shows from 9 SEEK products to 2 unrelated ones. **Ask before touching.**

Also: the `current-chapter` collection's description — *"Limited release. Limited
time, never again."* — is a **scarcity claim**. Per the brand rules it must be a
confirmed fact about those specific products or be removed.

---

## 8. Navigation

### Main menu (`main-menu`)
| Item | Type | Target | Status |
|---|---|---|---|
| Home | FRONTPAGE | `/` | ✅ |
| Shop | HTTP | `/collections/all` | ✅ |
| Story | PAGE | `/pages/story` | 🔲 **placeholder page** |
| Journal | HTTP | `/blogs/news` | 🔲 **0 articles** |

### Footer menu (`footer`)
Search → `/search` ✅ · Your Privacy Choices → `/pages/data-sharing-opt-out` ✅

### Footer links (`footer-links`)
Shop ✅ · Story 🔲 · Journal 🔲 · Contact → `/pages/contact` ✅

### Customer account menu (`customer-account-main-menu`)
Orders ✅ · Profile ✅ (Shopify-hosted)

**Gaps:** half the main menu leads somewhere empty. There is **no Archive item**
despite the homepage teaser, and **no HOSHOKU or ÜNDR item** — the two worlds are
unreachable from anywhere except the homepage.

---

## 9. Pages

| Handle | Title | Published | Template | Status |
|---|---|---|---|---|
| `story` | Story | ✅ | default | 🔲 **PLACEHOLDER — in main nav** |
| `contact` | Contact | ✅ | `page.contact` | ✅ |
| `data-sharing-opt-out` | Your Privacy Choices | ✅ | default | ✅ Shopify-required |
| `undr-ambassador-terms-conditions` | ÜNDR Ambassador Terms & Conditions | ✅ | `page` | ⚠️ **orphaned** — not in any menu |

**Story page, in full:**
> "Long before there was ÜNDR, there was Hoshoku — a creature divided between
> instinct and compassion. Neither hero. Neither villain. Only balance.
>
> This page is a placeholder. Replace this copy with the full ÜNDR origin story."

The first paragraph is real, usable lore. The second is an admission of
incompleteness sitting on a page linked from the main navigation.

**The Ambassador Terms page** implies an ambassador/affiliate programme that is
otherwise invisible on the site. **Ask whether that programme is live.**

---

## 10. Blog

| Handle | Title | Articles |
|---|---|---|
| `news` | News | **0** |

Linked from both the main menu and the footer as **"Journal."** Note the
mismatch: the blog is titled "News" internally but presented as "Journal."

---

## 11. Templates → Shopify object types

| Template | Applies to | Status |
|---|---|---|
| `index.json` | homepage | ✅ 9 sections, 2 broken refs |
| `collection.json` | all collections | ✅ default |
| `collection.hoshoku.json` | *(would be)* `hoshoku` | ⚠️ **dev only, unassigned** |
| `product.json` | all products | ✅ |
| `page.json` | Story, Privacy, Ambassador | ✅ |
| `page.contact.json` | Contact | ✅ |
| `blog.json` / `article.json` | News blog | ✅ but unused (0 articles) |
| `list-collections.json` | `/collections` | ✅ |
| `search.json` / `cart.json` / `404.json` / `password.json` / `gift_card.liquid` | standard | ✅ |

**No product templates are differentiated by world.** Every product — HOSHOKU
character pieces and ÜNDR archive pieces alike — renders through the same
`product.json` in the ÜNDR dark core. The HOSHOKU world currently exists only on
the homepage (and, once shipped, its collection page).

---

## 12. Summary — what would break if assumed to exist

| Assumption | Reality |
|---|---|
| collection `best-sellers` | ❌ **does not exist** — live-broken |
| collection `core` | ❌ **does not exist** — live-broken (it's `u-000-core`) |
| collection `featured-products-4` | ❌ does not exist (empty-state setting) |
| an Archive collection or page | ❌ does not exist |
| the HOSHOKU collection template is active | ❌ `templateSuffix` is `null` |
| Story has content | ❌ placeholder |
| Journal has content | ❌ 0 articles |
| Accessories has products | ❌ 0 |
| Ü-001 realm products are buyable | ❌ all draft/archived |
| collections auto-populate | ❌ all manual, no rules |
| the beanie flagship is in stock | ❌ 0 inventory, ACTIVE |
| `current-chapter` is what Current Chapter shows | ❌ it shows `u-002-seek` |
| archived products are "the Archive" | ❌ hidden from the storefront entirely |
| Phase 3 asset slots have images | ❌ all empty |
