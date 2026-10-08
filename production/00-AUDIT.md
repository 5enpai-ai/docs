# Phase 1 — Audit (as of 2026-10-08)

Method: read-only calls to Notion, Higgsfield, Google Drive, Canva, Shopify, Kling, and the local repo. No generations were run and no credits were spent. **I could not view any image or video pixels.** I only read file names, metadata, and page text. Anything that depends on how an asset *looks* is marked "needs human eyes."

## 0. Gating facts (read first)

| # | Finding | Impact |
|---|---|---|
| G1 | Higgsfield reports `unlim.available: false`, `remaining: null`, `expires_at: null`. 1,200 credits on the **Plus** plan, one private workspace. | **Unlimited is not confirmed from this connector.** The 7-day clock may be a web-UI promo the API doesn't expose. You must read the exact unlimited models/settings in the website UI (Action 1). Until then, treat everything as paid. |
| G2 | 14 models are flagged `supports_unlim` (see §3). The flag means "accepts unlimited," not "you are currently allowed to." | Plan around these models, but verify per model, resolution, and duration. |
| G3 | Notion `Brand Rules` says to use **Canva and existing assets before spending generation credits**, until direction is confirmed. | Conflicts mildly with a generation sprint. It's your rule, so this plan honors it by reusing existing assets as references first. You can override. |
| G4 | Notion `CURRENT SPRINT` says **commerce first**. | Priority 3 (Beanie 2.0 campaign) directly serves the stated $1,000/mo goal. See §6 on reordering. |
| G5 | **Notion has no AI-influencer spec, no "VANTA," and no "PROJKT OBJKT"** (searches returned nothing). Drive has none either. | Priority 1 and 5 have no source of truth on file. I will not invent canon. See §5 and Decision D1. |
| G6 | Kling has 0 credits. | Kling is unavailable except through Higgsfield's hosted Kling models. |

## 1. Inventory

Status key: **APPROVED** (marked so in Notion by D'nuke), **PROVISIONAL**, **SUPERSEDED**, **UNKNOWN**. Notion entries read 2026-08-26 (6 weeks stale), and all pages show `verification: unverified`.

| Asset | Location / access | Brand | Status | Missing | Reuse opportunity | Needs human approval |
|---|---|---|---|---|---|---|
| ÜNDRRARE HQ (canon source) | Notion, readable | ÜNDRRARE | Canon source | Original brand bible file not uploaded (blocks typography, ÜNDR hex values, forbidden list) | Governs all work | Any change to canon is D'nuke-only |
| AI OPERATING RULES | Notion, readable | All | APPROVED | None | Binding checklist for every generation | n/a |
| Brand Bible 1–11 | Notion, readable | All | Mixed per line | Typography unresolved. Colour hexes partly placeholder. | Rules, DO/DON'T, visual language | Typography, any Era A/B choice |
| CANON LOCK database | Notion, schema read; **rows not yet read** | All | Overrides Bible | Need to read rows before any HOSHOKU art | Check before generating | Only D'nuke changes status |
| HOSHOKU character (locked design) | Notion `4. HOSHOKU` | HOSHOKU | APPROVED, but eye/mark assignment 🔴 CONFLICTED vs v1.0 bible | See §4 | Bunni red eye + diamond; Renard cyan eye + X, per working lock | Conflict resolution (D2) |
| HOSHOKU 12-expression sheet + turnaround | Notion Reference Library entry | HOSHOKU | APPROVED ("production identity anchor") but **file not attached** ("File not yet attached here") | The actual image file | Primary identity reference | **Locate the file** (Action 3) |
| HOSHOKU Soul/Element on Higgsfield | Higgsfield: soul `pai`, soul `5enpai`, elements `pai`, `5enpai` | 5ENPAI | Unknown which person/character these are | No HOSHOKU soul or element exists | See below | Confirm what each is |
| "Everything Hoshoku" Drive folders (2) | Drive, readable (listing only) | HOSHOKU | UNKNOWN | — | Contains `hoshoku_main_logo`, `hoshoku_text_logo`, `hoshoku_bunny_red_v2`, `hoshoku_fox_blue_v2`, `hoshoku_split_stitched_v2`, `hoshoku_yinyang` PNGs, ~6 webp images | **Not viewed.** Need human eyes. Unclear if these are approved or v1.0-bible era. |
| Canva: HOSHOKU Brand Color Palette ×2, Chapter 1 Webtoon Panels (4 pp), Lettering & SFX Guide (8 pp) | Canva, listing readable | HOSHOKU | Notion calls Canva the "primary HOSHOKU art store (52+ assets)" | Not individually reviewed | Panels are the richest identity source | Review |
| Canva: ÜNDR photo collages (Ü-001 Midgard/Nirvana/Hades/Best Friends), Instagram posts, T-shirt mockups | Canva | ÜNDRRARE | UNKNOWN | — | Existing campaign layouts | Review |
| Canva brand kits | Canva | — | **None exist** | Brand kit | Create after typography is settled | Typography approval |
| Shopify: HOSHOKU Beanie (2.0) | Live, ACTIVE, $75, "made to order," inventory 0, image `HOSHOKU_BEANIE_2_MASTER-v2.jpg` | ÜNDRRARE | Shopify is commerce truth | Notion record is stale (see §2) | **Master product image exists.** Product reference for campaign. | I will not touch the store without authorization |
| Shopify: HOSHOKU Beanie (OG) | Live, $55, inventory 4 | ÜNDRRARE | Shopify truth | — | Comparison / "origin file" content | — |
| Drive: ÜNDR CONTENT DUMP 7/30/26, ÜNDR x Taco 08/03/26 (8 MOV), UNDR Photo gallery (JPGs), 6 PNGs `1.png–6.png` | Drive | ÜNDRRARE | UNKNOWN | — | Real footage and photos are the safest product/identity source | **Not viewed.** Need human eyes. |
| 5ENPAI music files (WAVs 2020–2022), AMV MP4s | Drive | 5ENPAI | Legacy | — | Audio beds possible, but check ownership. Several are collabs owned by others. | **Rights approval** before any public use |
| Notion refs: Nason & Niko sheets, Broly sheet, `@jscyberdream` composite | Notion | HOSHOKU | Nason & Niko **NEEDS APPROVAL (not finalised)** | Final designs | Do not generate | D'nuke |
| AI influencer (VANTA) | **Not found anywhere** | Influencer | UNKNOWN | Everything | None | D1 |
| PROJKT OBJKT | **Not found anywhere** | PROJKT OBJKT | UNKNOWN | Services, pricing, positioning, logo | None | D3 |
| Higgsfield projects (9) | Higgsfield | Mixed | Names: "Photoreal Recreation," "Triple Face Composite," "God of basketball - Regular Show," etc. `recent_jobs` all empty | — | Probably earlier experiments; not inspected | Tell me which, if any, to keep |
| Local repo `/home/user/docs` | Git | None | Unmodified Mintlify starter | — | Used only as workspace for these docs | — |

## 2. Contradictions and risks found

1. **Beanie 2.0 status mismatch.** Notion PRODUCTS says "Draft / Launching next / Marketing not started / Shopify handle blank." Shopify says **ACTIVE since 2026-08-08, handle `hoshoku-2-0-beanie-orange-cream`, $75, inventory 0, made to order.** Per rules, Shopify wins. The Notion row (and the "product page live" ROADMAP item) should be reconciled, but I won't edit canon without approval.
2. **Colourway.** Shopify says Beanie 2.0 is **Orange / Cream**. Notion calls the OG **Cocoa / Cream.** No Notion page describes the 2.0's appearance. Product accuracy has to come from the Shopify master image and real photos, not from me.
3. **HOSHOKU eye/mark conflict** is 🔴 CONFLICTED. Rule: use the working lock and flag, never pick silently.
4. **Rule vs. sprint:** "don't let AI regeneration redesign a print," "copy exactly." Image models can drift logos and knit patterns. Beanie work must be reference-driven with tight QC, and wordmarks/text should be composited in Canva, not generated.
5. **Name collisions:** Higgsfield soul/element `pai` vs `5enpai`. I don't know whether either is a real-person likeness. Your brief forbids changing your appearance in source-based edits, so these are used only as supplied.
6. **Music rights** on Drive WAVs.

## 3. Higgsfield capability map (from `models_explore`, `supports_unlim: true`)

- **Image:** Soul 2.0 (fashion/UGC/character, supports `soul_id`), GPT Image 2 (text/typography, 1k/2k/4k), Nano Banana / Pro / 2, Seedream 4.5 / 5 Lite / 5 Pro, FLUX.2, Kling O1 Image.
- **Video:** Seedance 2.0 (4–15 s, up to 4K, reference-driven, start/end frames, native audio), Kling 3.0 (3–15 s, std/pro/4k), Kling 3.0 Motion Control, Gemini Omni Flash (4–10 s, 720p), Wan 2.7 (2–15 s, 720p/1080p).
- **Audio:** Seed Audio 1.0, Text-to-Speech V2, Inworld TTS, Mirelo SFX.
- Open question: which resolution/duration/mode combos the unlimited allowance actually covers. The tool says it lists them in a trailing "Unlim configs" note, which came back empty because `available:false`.

## 4. Who needs to decide what (blocking decisions)

- **D1 — Influencer identity.** Is "VANTA" an AI-influencer character you want me to treat as provisional? I have no prior conversation record of VANTA in this session's accessible sources. I will draft a **clearly labeled PROVISIONAL spec** from the brief's structure only (no invented backstory) once you paste or confirm what was discussed.
- **D2 — HOSHOKU eye/mark conflict.** Keep working lock. Confirm.
- **D3 — PROJKT OBJKT.** Need: what it sells, to whom, price points, any logo.
- **D4 — Is the unlimited promo real on your Higgsfield web UI, and for which models?**
- **D5 — Priority reorder?** See §6.

## 5. Not-yet-done reads (will do next, no approval needed)
CANON LOCK rows, Reference Library rows, Visual Language, Color System, Typography pages, the other HOSHOKU worlds page, and Drive folder contents of CONTENT DUMP / Taco.

## 6. Priority order — one evidence-based flag
Your stated order puts the influencer first. The evidence says: the influencer and PROJKT OBJKT have **zero source material**, while HOSHOKU and Beanie 2.0 have approved canon, a live product, a master image, and the $1,000/mo target. I recommend **starting generation tests on HOSHOKU identity and Beanie 2.0 (Priority 2–3) on Day 1** while the influencer spec waits on D1, and then running Priority 1 as soon as D1 lands. This isn't demoting the influencer, only unblocking it. Your call (D5).
