# 05 — Open Task Queue

Built from the **actual current state** verified 2026-09-04, not from a wishlist.
Every task here exists because something is broken, blocked, or explicitly
unfinished in the live store or the Development theme.

**Priorities:** P0 blocking · P1 important · P2 polish · P3 future exploration

**Before starting anything:** complete P0-1. Several tasks below are guesses
until `PHASE_3_DISCOVERY.md` is in hand.

---

# P0 — Blocking

## P0-1 · Obtain the theme repo and its two governing documents
**Why:** The theme's own code cites `CLAUDE.md` (World-First Homepage
Architecture, World-State Design, ÜNDRRARE Visual Reference System, Future
Website Experience Architecture, Design System) and `PHASE_3_DISCOVERY.md`
(§0.2, §0.3) as authoritative. Neither was readable. Every architectural decision
below is provisional without them, and the Phase 3 approval item is *literally*
a pointer into a document nobody here has.
**Files/areas:** the ÜNDRRARE theme Git repository.
**Dependencies:** owner grants access.
**Risk:** Low to do, **high not to do.** Working without them means re-deriving
decisions that were already made and paid for.
**Done when:** the repo is cloned, `CLAUDE.md` and `PHASE_3_DISCOVERY.md` are
read in full, and any conflict with this package is noted and this package
corrected.

## P0-2 · Fix the two live-broken collection references
**Why:** Two homepage elements are broken **in production right now**:
- **"Enter ÜNDR"** → `shopify://collections/core`. No such handle. This is one of
  only two identity CTAs on the page — half the world-split is dead.
- **`featured_products`** → collection `best-sellers`. No such collection. The
  homepage's largest product grid has no source.

**The fixes already exist in the Development theme** (→ `u-000-core`;
→ `u-002-seek` with heading "Best Sellers" → "Shop the Collection"). This is
about getting them live, not writing them.
**Files/areas:** `templates/index.json` → `world_split.blocks.group_undr_side.blocks.cta.settings.link`
and `featured_products.settings.collection` + its `static-header` text block.
**Dependencies:** P0-3 if shipping via a full theme publish. If the dev theme
isn't ready to publish wholesale, port just these two values onto the live
theme's branch instead — a two-value change is far lower risk than publishing a
diverged theme.
**Risk:** Low. Both target handles verified to exist.
**Done when:** both links resolve on the live site; "Enter ÜNDR" lands on
Ü-000 // CORE; the grid renders products.

## P0-3 · Diff `config/settings_data.json` between live and Development
**Why:** The two differ (**9,115 B live vs 7,399 B dev**) and the contents were
**not compared** this session. That file holds the global color palette,
typography, button/input styling, and cart settings. **Publishing the Development
theme without checking this could silently change sitewide colors or type.** The
size drop is large enough to suspect settings were lost, not just changed.
**Files/areas:** `config/settings_data.json` on both themes.
**Dependencies:** none.
**Risk:** **High if skipped.** This is the single most likely way to break the
live site's appearance in one action.
**Done when:** a line-by-line diff exists; every difference is explained as
intentional or reverted; the palette values in `01_BRAND_AND_DESIGN_DNA.md` §4
are confirmed unchanged.

## P0-4 · Confirm the HOSHOKU Beanie 2.0 inventory state
**Why:** `hoshoku-2-0-beanie-orange-cream` is **ACTIVE with `totalInventory: 0`**
and is the flagship of the entire homepage — PRESS START's atmosphere image, the
first world object, and the flagship hero section. If it displays as sold out,
the whole world-first journey terminates on an unbuyable product. It may be
deliberate (made-to-order, "not automatically restocked" is in its own copy), in
which case the *presentation* still needs to be right rather than a default
"Sold out" badge.
**Files/areas:** Shopify catalog (inventory policy / continue-selling setting);
possibly `hoshoku_flagship_hero` presentation.
**Dependencies:** owner decision. **Catalog change — do not make it unilaterally.**
**Risk:** Medium. Touching inventory settings affects real orders.
**Done when:** the owner confirms intent, and the storefront reflects it
correctly (either purchasable, or clearly and on-brand "made to order" rather
than a generic sold-out state).

---

# P1 — Important

## P1-1 · Get the Phase 3 HOSHOKU opening statement approved
**Why:** `templates/collection.hoshoku.json` carries a block literally named
*"Opening statement — PENDING APPROVAL, see PHASE_3_DISCOVERY.md §0.3 item 1."*
The copy is *"HOSHOKU isn't a mascot. HOSHOKU is a character who happens to live
here."* It cannot ship unapproved, and it blocks the whole template.
**Files/areas:** `templates/collection.hoshoku.json` → `hoshoku_intro.blocks.text_statement`.
**Dependencies:** P0-1 (read §0.3 first — there may be alternates already drafted).
**Risk:** Low technically. High brand risk if shipped without sign-off.
**Done when:** owner approves or replaces it, and the "PENDING APPROVAL" name is
removed from the block.

## P1-2 · Assign the `hoshoku` template to the HOSHOKU collection
**Why:** `templates/collection.hoshoku.json` exists in Development but the
`hoshoku` collection's `templateSuffix` is **`null`**. Publishing the theme alone
does nothing — the template will never render. Easy to miss and easy to
misdiagnose as "the template is broken."
**Files/areas:** Shopify admin → Collections → HOSHOKU → Theme template.
**Dependencies:** P1-1, P1-3. **This is a catalog change** — keep it separate from
the theme deploy and do it deliberately.
**Risk:** Low, and instantly reversible (set the suffix back to null).
**Done when:** `/collections/hoshoku` renders the three-section HOSHOKU template
with the cream world palette applied.

## P1-3 · Publish the Development theme (after P0-2, P0-3, P1-1)
**Why:** Phase 3 work — asset slots, staggered reveal, the HOSHOKU template, the
broken-link fixes, the added scoping ids — is all sitting unpublished. The
project cannot move forward while live and dev are diverged.
**Files/areas:** all six diverged files (see `03_TECHNICAL_STATE.md` §C1).
**Dependencies:** P0-2, **P0-3 (hard blocker)**, P1-1.
**Risk:** **Medium-high.** Six files differ, one of them global settings.
Publish from the Git repo, not the admin editor. Keep the current live theme
as an unpublished rollback copy.
**Done when:** live and dev checksums match on all custom files; the homepage is
verified on desktop, tablet and mobile; PRESS START, all five world objects, and
both split CTAs are confirmed working.

## P1-4 · Resolve the Story page
**Why:** It is **in the main navigation** and its own body says *"This page is a
placeholder. Replace this copy with the full ÜNDR origin story."* A visitor who
follows the world into "Story" hits an admission that there's nothing there —
which is the opposite of the intended discovery payoff, and one of the clearest
"generic/unfinished" signals on the site.
**Files/areas:** Shopify page `story`; possibly `templates/page.json`; main menu.
**Dependencies:** brand/lore input from the owner. Apply `01_BRAND_AND_DESIGN_DNA.md`
§14 — **lore is felt before it's explained**; this should not become an exposition
dump.
**Risk:** Medium brand risk. This is a primary lore surface; getting the register
wrong here is worse than leaving it.
**Done when:** either the page carries real ÜNDR-voice origin copy, or the nav
item is removed until it does. **Shipping the placeholder is not an option.**

## P1-5 · Resolve "Journal"
**Why:** In the main menu and the footer, pointing at `/blogs/news` which has
**zero articles**. Two dead nav items out of four is a real credibility problem
for a brand whose whole proposition is that it's already in motion.
**Files/areas:** main menu, footer links, blog `news`.
**Dependencies:** owner decision — publish something, or remove the item.
**Risk:** Low.
**Done when:** the Journal either has content or is not in the navigation.

## P1-6 · Decide what the Archive actually is
**Why:** The homepage ends on *"Recovered artifacts. Retired pieces, held rather
than discarded. Curation in progress."* — with **no link and no destination**.
It's the closing beat of the world-first journey and it currently goes nowhere.
Separately, 23 products are ARCHIVED in Shopify, which **hides them from the
storefront entirely** — archived-in-Shopify is not the same thing as the brand's
Archive, and conflating the two would break things.
**Files/areas:** new collection or page; `archive_teaser` section; navigation;
possibly product statuses (**catalog change**).
**Dependencies:** owner defines the concept. The brand files warn against letting
"archive" become ÜNDR's whole identity — worth checking scope.
**Risk:** Medium. Un-archiving products to build it changes what's purchasable.
**Done when:** the Archive is either a real destination the teaser links to, or
the teaser is honestly reframed as a coming-soon with no dead end.

## P1-7 · Verify the live site on real devices
**Why:** **No rendering was verified at all** this session — everything in this
package is code reading. Tablet (750–1024px) is specifically unexamined, and the
World Hub's `auto-fit / minmax(14rem, 1fr)` will produce some column count there
that nobody has looked at.
**Files/areas:** whole site; especially `undr_world_hub` grid, `world_split`
stacking, PRESS START on small screens.
**Dependencies:** none — do this early, it informs everything else.
**Risk:** None to check.
**Done when:** homepage + collection + product pages are verified at mobile,
tablet and desktop; PRESS START is confirmed skippable on each; all five world
objects scroll correctly; the no-JS path is spot-checked.

## P1-8 · Source and wire the Phase 3 world renders
**Why:** Both asset slots are built and empty. This is the visible payoff of
Phase 3 — the world currently has no world imagery in it beyond darkened product
photos.
**Files/areas:** `atmosphere_image` on `undr_world_boot`; `world_artifact_image`
on each of the five hub objects.
**Dependencies:** **P0-1 and an owner conversation.** The owner has referenced
known **resolution / file-size / letterform** problems with generated world
assets that could not be found or assessed here. Do not generate new assets
before understanding what already exists and what was wrong with it.
**Risk:** Medium-high **brand** risk. Generated imagery that reads as AI slop
would violate the brand's central authenticity requirement. The compositing rule
is already decided: renders go **behind**, blurred, as atmosphere; real product
photography stays sharp in front. Note also that generated *lettering* is the
likely source of the letterform issue — composite real type, don't generate it.
**Risk (technical):** Low. Both slots are additive; unset renders unchanged.
**Done when:** approved renders are assigned, page weight is checked, and the
result is verified in both worlds at all breakpoints.

---

# P2 — Polish

## P2-1 · Fix the `hoshoku_floating.gif` asset
**Why:** **1.83 MB at 365×365 px.** It is the Ü-002 // SEEK collection image, so
it loads on the homepage's `current_chapter` grid path. That is roughly 14 bytes
per pixel — enormously oversized for its display dimensions.
**Files/areas:** Shopify Files; Ü-002 // SEEK collection image.
**Dependencies:** none. Keep the animation if it's wanted — convert to animated
WebP or a short muted looping MP4/`<video>`, or reduce the frame count/palette.
**Risk:** Low. Verify it still animates where it's displayed.
**Done when:** the asset is well under ~300 KB at its display size with the
animation intact, or replaced deliberately.

## P2-2 · Clean up supplier boilerplate product copy
**Why:** The beanies and the flagship Ü products have genuinely strong ÜNDR-voice
storytelling. Many Printify products still carry raw supplier text — size tables,
*"This bikini swimsuit is designed for fashionable women…"* — which is exactly
the generic register the brand files say to avoid. The good copy makes the bad
copy more conspicuous, not less.
**Files/areas:** Shopify product descriptions. **Catalog change.**
**Dependencies:** apply `01_BRAND_AND_DESIGN_DNA.md` §12 (HOOK → IDENTITY →
DETAILS → CLOSING). Prioritize **ACTIVE products only** — there's no value
rewriting archived ones.
**Risk:** Low technically. Do it in batches with owner review; don't bulk-rewrite
the catalog in one pass.
**Done when:** every ACTIVE product reads in the correct voice for its world.

## P2-3 · Clean up off-brand product tags
**Why:** Supplier-generated SEO tags are live and off-brand: *"Sassy Beach Look,"
"Flirtatious Swimwear," "Girls Day Out," "panda design tee," "youthful vibe
shirt."* Tags surface in filters and search, so customers see them.
**Files/areas:** product tags. **Catalog change.**
**Dependencies:** none. The brand's own tag vocabulary is already established
(`u-000`/`u-001`/`u-002`, `hoshoku`, `archive`, `atlanta streetwear`, etc.) —
follow it.
**Risk:** Low. Note that filters are enabled on the HOSHOKU collection template,
so tag hygiene has a functional payoff too.
**Done when:** ACTIVE product tags are consistent and none are supplier
boilerplate.

## P2-4 · Normalize the `vendor` field
**Why:** Vendor is currently `ÜNDR`, `ÜNDR 🐰/🦊`, `Printify`, `ODMPOD`, and
`My Store` across the catalog. **`Printify` and `ODMPOD` are fulfilment partners
being displayed as the brand.** Horizon surfaces vendor in several places.
**Files/areas:** product vendor. **Catalog change.**
**Dependencies:** owner picks one canonical value (`ÜNDR` is the obvious
candidate).
**Risk:** Low, but check whether the Printify app overwrites vendor on sync —
otherwise it'll silently revert.
**Done when:** all ACTIVE products share one canonical vendor.

## P2-5 · Fill or hide the empty Accessories collection
**Why:** 0 products, with a real written description (*"plushies, and whatever
else doesn't fit on a hanger"*). If it's reachable, it's an empty room.
**Files/areas:** `accessories` collection.
**Dependencies:** owner decision — the plush pillows and stickers that would fill
it are currently ARCHIVED or DRAFT.
**Risk:** Low.
**Done when:** it has products, or it's unpublished.

## P2-6 · Reconcile `current-chapter` (collection) vs `current_chapter` (section)
**Why:** The homepage's `current_chapter` section points at **`u-002-seek`**, not
at the collection whose handle is literally **`current-chapter`** (2 products,
description *"Limited release. Limited time, never again."*), which is used
nowhere. This is a trap: a future agent will "fix" one to match the other and
change what the homepage shows.
**Files/areas:** `templates/index.json` → `current_chapter`; the `current-chapter`
collection.
**Dependencies:** owner clarifies intent.
**Risk:** Medium — a well-meaning "fix" here silently changes the homepage.
**Done when:** intent is documented, and either the section is repointed or the
unused collection is removed/renamed to stop the ambiguity.
**Also note:** that collection's description contains a **scarcity claim**
("Limited time, never again"). Per the brand files, confirm it's factually true
for its two products or remove it.

## P2-7 · Remove Shopify sample and duplicate products
**Why:** 4 "Example product" entries (vendor "My Store") and several duplicate
archived Printify products (`u-000-undr-clogs` / `-1`, plush pillows, crop tops)
plus 4 unbranded duplicate ODMPOD drafts with placeholder inventory `9999999`.
Clutter that makes real audits harder.
**Files/areas:** Shopify catalog. **Catalog change.**
**Dependencies:** owner confirms none are wanted. Archived ≠ deletable without
asking — check for order history first.
**Risk:** Low-medium. Deleting a product with order history is destructive.
**Done when:** the catalog contains only real ÜNDRRARE products.

## P2-8 · Add HOSHOKU / ÜNDR to navigation
**Why:** The two worlds are reachable **only from the homepage**. Once a visitor
is on a product page, there is no path back into either world. The nav is Home /
Shop / Story / Journal — nothing world-shaped in it.
**Files/areas:** main menu; possibly the header section.
**Dependencies:** P1-2 (the HOSHOKU collection template should exist before
sending traffic to it).
**Risk:** Low technically, **medium brand-wise** — the nav is a place where a
generic ecommerce solution would flatten the world into two more menu items.
Worth designing rather than just adding links.
**Done when:** the worlds are reachable from anywhere, in a way that doesn't read
as a standard shop menu.

## P2-9 · Clean up stale themes
**Why:** `Horizon`, `Radiant`, `Updated copy of Radiant` are superseded copies
cluttering the theme list.
**Dependencies:** owner confirms. **Do not delete `undrrare-hoshoku-phase-5-fixed`**
— code comments reference "the existing Phase 5 content" and it's historical
context.
**Risk:** Low if the three named copies only. High if the wrong one goes.
**Done when:** only meaningful themes remain, and a rollback copy of the current
live theme is retained.

---

# P3 — Future exploration

## P3-1 · World Hub orbit / float motion
Deferred from Phase 2: *"pending review of this static prototype."* Requires the
owner to review the static hub first. Constraints already implied by the
codebase: reduced-motion gated, opacity/transform only, nothing load-bearing, and
per the Phase 3 boot comment — **understated, not a game-menu flourish.**
Risk: medium brand risk (motion is where "world" tips into "gimmick"); low
technical.

## P3-2 · Visitor-controllable world switching
The mechanism is built and working; there is **no UI, no toggle, no persistence.**
Explicitly future work per the code. Note that `PHASE_3_DISCOVERY.md` §0.2/§0.3
already argued *against* the sitewide `<html>` switch for the HOSHOKU collection —
read that reasoning before designing this. Open questions: is world a visitor
preference, or is it determined by what you're looking at? A persistent toggle
implies the former; everything built so far implies the latter.

## P3-3 · PRESS START auto-advance
Deliberately absent, *"per explicit instruction."* If revisited, the owner
requires a proposed duration **with UX and performance reasoning** before it's
built. Weigh against the "never a trap" constraint.

## P3-4 · Extend grain beyond PRESS START
Documented in `CLAUDE.md` as approved-but-unbuilt; the PRESS START noise layer is
the only instance. Could become a world-wide texture. Watch performance and the
HOSHOKU cream world, where grain reads very differently than on near-black.

## P3-5 · Product-page world storytelling
The archive-system format (`FILE NO.` / `ARTIFACT` / `CONDITION` / `PRODUCTION
NOTE`) currently lives in the description field as plain rich text. It could be a
real template treatment. **Caution:** the brand files warn against letting
"archive" become the entire identity — a full archive-styled product template
might over-commit. Discuss before building.

## P3-6 · Journal as a lore surface
If the Journal is revived, it's the natural home for lore, BTS, and Bunni/Renard
character content — the brand files describe exactly this kind of material
(*"we tried making this 4 times 😭" / "5."*). Would give the world somewhere to
continue between drops.

---

# Suggested first session for the receiving Claude

1. **P0-1** — get the repo, read `CLAUDE.md` and `PHASE_3_DISCOVERY.md`.
2. **P1-7** — look at the live site on real devices. Ten minutes, and it will
   correct assumptions in this package.
3. **P0-3** — diff `settings_data.json`. Do not skip; it gates P1-3.
4. **P0-2** — get the two broken links fixed and live.
5. Report back using the format in `09_AGENT_PROTOCOL.md`, and raise the
   **DECISIONS NEEDED** items: P0-4 (beanie inventory), P1-1 (statement
   approval), P1-4/P1-5/P1-6 (Story, Journal, Archive), P1-8 (world assets).
