# 07 — Asset Inventory

Inventoried 2026-09-04 from the live Shopify theme, the Shopify Files library,
and this repository.

> **⚠️ Major gap up front.** The owner specifically asked for attention to *"the
> generated world assets and the known resolution/file-size/letterform issues."*
> **No generated world assets were found anywhere reachable this session** — not
> in the Shopify Files library, not in either theme's assets, not wired into any
> Phase 3 slot. They presumably live locally or in the theme repo, neither of
> which was accessible. The known problems with them could not be assessed or
> reproduced. **This is the largest single gap in this package. See §6.**

---

## 1. Custom theme code assets (live MAIN theme)

| Name | Location | Purpose | Status | Format | Size | Wired | Approved |
|---|---|---|---|---|---|---|---|
| `undr-world-boot.js` | `assets/` | PRESS START overlay behavior | ✅ working, live | ES module | 3,190 B | Yes — `sections/undr-world-boot.liquid` | Yes (Phase 1/2, live) |
| `undr-world-hub.js` | `assets/` | Hub click→scroll enhancement | ✅ working, live | ES module | 2,961 B | Yes — `sections/undr-world-hub.liquid` | Yes |
| `undr-world-boot.liquid` | `sections/` | PRESS START section | ✅ working, live | Liquid + inline CSS | 8,956 B | Yes — `templates/index.json` | Yes |
| `undr-world-hub.liquid` | `sections/` | Hub container | ✅ working, live | Liquid + inline CSS | 4,508 B | Yes — `templates/index.json` | Yes |
| `_undr-world-object.liquid` | `blocks/` | One world object | ✅ working, live | Liquid + inline CSS | 13,076 B | Yes — 5 instances in the hub | Yes |

**Development-theme versions** (newer, unpublished): `undr-world-boot.liquid`
11,069 B (+`atmosphere_image` slot, +staggered reveal),
`_undr-world-object.liquid` 14,873 B (+`world_artifact_image` slot),
`base.css` 59,712 B (+3 scoping ids), `templates/collection.hoshoku.json` 8,255 B
(new). The two JS files and `undr-world-hub.liquid` are **byte-identical** across
both themes.

## 2. Generated / procedural visual assets in code

These are assets in the sense that they're visual material — but they're
generated at render time, with no file to manage.

| Name | Location | Purpose | Status | Notes |
|---|---|---|---|---|
| **PRESS START noise texture** | `sections/undr-world-boot.liquid` `::after` | Grain over the boot atmosphere | ✅ live | Inline SVG `feTurbulence` data-URI, 120×120 tile, `baseFrequency 0.9`, 2 octaves, `stitchTiles`. Opacity 0.05, `mix-blend-mode: overlay`. **No network request, no file.** Code notes this is the theme's **first** grain — `CLAUDE.md` documents grain as approved-but-unbuilt. |
| **World-object glow** | `_undr-world-object.liquid` `::before` | "Discovered object" spotlight | ✅ live | `radial-gradient` using `color-mix(in srgb, var(--world-accent-primary) 28%, transparent)`, `blur(6px)`, inset −12%. World-aware automatically. |
| **Reticle marker** | `_undr-world-object.liquid` | Discovery affordance | ✅ live | Pure CSS: 1.5rem translucent ring + 0.5rem accent dot. Deliberately echoes `sections/product-hotspots.liquid`'s bullseye language. `aria-hidden`. |
| **PRESS START atmosphere filter** | `sections/undr-world-boot.liquid` `::before` | Darkened world backdrop | ✅ live | `grayscale(0.65) brightness(0.32) contrast(1.05)`, opacity 0.6, applied to whatever image is in the slot. |

These are worth protecting — they achieve the world look with **zero asset
weight**, which is a genuinely good outcome given the site's other file-size
problems.

## 3. Phase 3 replaceable-asset slots — **BUILT AND EMPTY**

| Slot ID | Setting | Where | Status | Intended content |
|---|---|---|---|---|
| **`PRESS_START_BACKGROUND`** | `atmosphere_image` (image_picker) | `undr-world-boot` section | 🔲 **empty** — dev theme only | *"a purpose-made world environment render"* |
| **`WORLD_OBJECT_0n`** | `world_artifact_image` (image_picker) | each `_undr-world-object` block ×5 | 🔲 **empty** — dev theme only | a per-object world render |

**Documented behavior (both slots):**
- **Additive only.** `var(--…, none)` fallback means an unset slot renders
  **byte-identically** to today. Nothing changes until an image is deliberately
  assigned.
- **`atmosphere_image` takes priority** over `atmosphere_product`; the product-photo
  fallback remains.
- **Renders sit behind, blurred, as atmosphere.** *"keeps a render reading as
  atmosphere behind the live product/collection photo (still rendered sharp,
  unchanged, in front), not a second competing image."*

**The recorded asset pipeline:**
> **temporary: Meshy → later: Higgsfield one-for-one swap, no markup change
> needed.**
> *"Swapping this image later (temporary Meshy render → Higgsfield render) is a
> settings-only change; no markup or CSS edit needed."*

The slot design is the point: whatever the current asset problems are, replacing
the assets is a settings change, not a code change.

## 4. Shopify Files library — notable assets

Most of the ~40 image files are Printify/ODMPOD product mockups (2048×2048 or
1400×1400, auto-generated by the fulfilment apps, not managed by hand). The ones
that matter:

### 🔴 `hoshoku_floating.gif` — **KNOWN PROBLEM**
| | |
|---|---|
| Location | Shopify Files → `hoshoku_floating.gif` |
| Purpose | Collection image for **Ü-002 // SEEK** |
| Dimensions | **365 × 365 px** |
| File size | **1,832,111 B (1.83 MB)** |
| Format | GIF (animated) |
| Wired in | ✅ Yes — `u-002-seek` collection image |
| Uploaded | 2026-08-28 02:45 |
| Approved | Presumably (it's live) |

**The problem:** ~14 bytes per pixel. This is enormously oversized for a
365×365 display. It's the only hand-made brand animation in the store, and it
loads on the homepage's `current_chapter` path and anywhere the SEEK collection
card appears.

**Note the interaction with the world-object code:** a collection object falls
back to `collection.image` first, so if a SEEK world object were configured, this
1.8 MB GIF would be its image. Today the SEEK object (`undr_current_chapter`)
does use collection `u-002-seek` — **so this GIF is very likely loading in the
World Hub, immediately behind PRESS START.**

**Next step:** convert to animated WebP or a muted looping MP4 in `<video>`, or
reduce frames/palette. Target well under 300 KB. Keep the animation — it's the
one piece of character motion in the store.

### 🟡 Firefly-generated image
`Firefly_-_Dress_the_character_in_Image1_in_the_following_outfit-_shirt_from_Image2_shorts_fro.png`
— 992×1072, 1.32 MB, uploaded 2026-08-15. **Not wired into anything.** The
filename preserves the prompt (dressing the character in product garments). This
is evidence of a character-visualization workflow — Adobe Firefly, alongside the
Meshy/Higgsfield plan. **Ask the owner whether this line of work is active.**

### 🟡 Large source photographs
`2731366B-…jpg` — 3024×4032, **4.38 MB**, uploaded 2026-08-10. Raw phone
photography, unoptimized. Not obviously wired in. Two smaller companions
(1170×1555, 1170×1549) from the same batch.

### ✅ Beanie photography (the only real product photography in the store)
| Asset | Dimensions | Format | Wired |
|---|---|---|---|
| `760502903_18420117190149462_…jpg` | — | JPEG | HOSHOKU Beanie 2.0 featured image |
| `5AD3A118-…webp` | — | WebP | HOSHOKU Beanie (OG) featured image |

These matter disproportionately: the 2.0's image is **also** PRESS START's
atmosphere background and the first world object's image. It is doing three jobs.

### Printify / ODMPOD mockups
~35 files, 2048×2048 or 1400×1400 JPEG/PNG, 130 KB – 2.0 MB. Auto-generated,
auto-wired to their products, managed by the fulfilment apps. **Don't hand-edit
these** — the apps re-sync them. Several exceed 1 MB (`…041951-…png` at 1.99 MB,
`…041923-…png` at 1.14 MB), which is worth knowing for page-weight work but isn't
directly fixable in the theme.

## 5. Theme icon assets (stock Horizon)

~35 SVG icons in `assets/` (`icon-cart.svg`, `icon-search.svg`, `icon-menu.svg`,
etc.), 215 B – 6.9 KB, plus `snippets/icon.liquid` at **133 KB** (the inline icon
library). All stock Horizon, all wired, none ÜNDRRARE-specific.

**There is no custom ÜNDR or HOSHOKU icon, logo asset, favicon, or wordmark in
the theme.** The ÜNDRRARE identity on the homepage is carried entirely by
typography (Merriweather Sans, uppercase, letterspaced) and the color tokens.
Whether a real wordmark exists elsewhere is **unknown** — and this may connect
directly to the reported **letterform** problems (see §6).

## 6. The missing generated world assets — what to ask about

The owner referenced known **resolution**, **file-size**, and **letterform**
issues with generated world assets. Nothing matching was found. Concretely:

- ❌ No world/environment renders in Shopify Files
- ❌ No renders in either theme's `assets/`
- ❌ No Phase 3 slot populated in either theme
- ❌ No `.meshy`, `.glb`, render exports, or similar anywhere reachable

**Questions for the owner:**
1. **Where do they live?** Local machine, theme repo, Meshy/Higgsfield account?
2. **What exists?** How many, of what — PRESS START backgrounds, per-object
   artifacts, or something else?
3. **Resolution issue:** too low for the display size, wrong aspect ratio, or too
   high (feeding the file-size issue)?
4. **File-size issue:** what are the actual sizes? Given the 1.8 MB GIF already
   in the store, a page loading several multi-MB renders behind PRESS START would
   be a serious performance problem — and PRESS START is the *first* thing that
   renders.
5. **Letterform issue — most likely the important one.** If ÜNDR/HOSHOKU
   lettering is being *generated* inside the renders, near-miss glyphs are a
   standard generative-image failure and are not fixable by re-rolling. **The fix
   is to composite real type over a clean render rather than generate the text.**
   The Phase 3 slots make this easy: the render is a background layer, and real
   type is already rendered in front of it by the section's own markup.
   **[RECOMMENDATION — needs approval]**
6. **Is anything approved?** Or is the whole set a rejected first pass?

Until these are answered, **do not generate replacement assets.** See
`05_NEXT_TASKS.md` P1-8.

## 7. Assets in this repository

`5enpai-ai/docs` is an untouched Mintlify starter kit. Its assets are Mintlify's,
not ÜNDRRARE's:

| File | Size | Status |
|---|---|---|
| `favicon.svg` | 1,547 B | ❌ Mintlify default — **not ÜNDRRARE** |
| `logo/light.svg` | — | ❌ Mintlify default |
| `logo/dark.svg` | — | ❌ Mintlify default |

`docs.json` still declares `"name": "Mintlify Starter Kit"` and Mintlify's green
palette (`#16A34A` / `#07C983` / `#15803D`) — **not** ÜNDRRARE's colors. Nothing
here is a brand asset. Ignore this repository for asset purposes.

## 8. Summary — what needs attention

| Priority | Asset | Issue | Next step |
|---|---|---|---|
| 🔴 | `hoshoku_floating.gif` | 1.83 MB at 365×365; likely loading in the World Hub | Convert to animated WebP / MP4, <300 KB |
| 🔴 | Generated world assets | **Not found.** Reported resolution/file-size/letterform problems unassessed | Ask the owner (§6) before generating anything |
| 🟠 | Phase 3 slots ×6 | Built, wired, **empty** | Fill only after §6 is resolved |
| 🟠 | Large source photos (4.38 MB) | Unoptimized, purpose unclear | Confirm use; optimize or remove |
| 🟡 | Firefly character image | Unwired; workflow status unknown | Ask whether this line is active |
| 🟡 | Printify mockups >1 MB | Page weight | Note only — app-managed |
| 🟡 | No ÜNDRRARE wordmark/icon assets | Identity is type-only | Confirm whether a real wordmark exists |
| 🟢 | Procedural CSS/SVG assets | Working well, zero weight | Protect; extend grain per P3-4 |
