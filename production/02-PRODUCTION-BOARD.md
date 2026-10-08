# Seven-day production board (v0.1, 2026-10-08)

**Who does it:** `ME` = I can finish it directly (writing/indexing/planning). `YOU-HF` = you operate Higgsfield manually. `YOU-OK` = needs your approval first.
**Status key:** READY, BLOCKED(reason), TODO.
Aspect ratios follow approved 3:4 / 9:16 / 4:3 for Instagram; HOSHOKU art is recomposed vertical. Model names are those exposed as unlimited-capable; **verify each in the UI (Action 1).**
Output location convention: Drive `/Sprint-Oct26/<brand>/<ID>_<v#>.ext` (not yet created; `YOU-OK`).

| ID | Pri | Brand | Deliverable | Who | Refs required | Model | Format | Variations | Consistency requirements | QC criteria | Status | Purpose |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I-00 | 1 | Influencer | Identity spec (provisional) | ME | Prior VANTA discussion (not on file) | — | doc | — | Unknown fields left blank | No invented backstory | BLOCKED(D1) | Source of truth |
| I-01 | 1 | Influencer | Master face/body ref sheet | YOU-HF | I-00 | Soul 2.0 → train Soul (5–20 images) | 3:4 | 8 | Same face across angles | 3 of 4 views recognisably identical | BLOCKED(D1) | Identity anchor |
| I-02 | 1 | Influencer | 3 launch videos, 9:16 | YOU-HF | I-01 | Seedance 2.0 / Kling 3.0 | 9:16, 5–8 s | 3 per video | Face, hair, wardrobe stable | No face drift at 5 s | BLOCKED(I-01) | Launch |
| I-03 | 1 | Influencer | 30 short-form concepts + captions + measurement plan | ME | I-00 | — | doc | — | — | Each has hook, shot, caption | BLOCKED(D1) | Backlog |
| H-01 | 2 | HOSHOKU | Identity re-test vs expression sheet | YOU-HF | 12-expression sheet file | Nano Banana Pro / Seedream 5 Pro | 3:4 | 4 | 50/50 split, seam, stitches, anthro muzzle; red eye + diamond (Bunni), cyan eye + X (Renard) per working lock | Matches sheet; no human face | BLOCKED(file, D2) | Anchor |
| H-02 | 2 | HOSHOKU | Motion concepts: ear flick, seam reveal, split-eye blink (5 s loops) | YOU-HF | Best H-01 frame as start image | Seedance 2.0 / Kling 3.0 | 9:16, 5 s | 2 each | Colours and marks unchanged | No morphing of seam/marks | BLOCKED(H-01) | Reusable Reels |
| H-03 | 2 | HOSHOKU | Dual-mood format: Bunni (sad) / Renard (cocky) split-screen caption series | ME (concept), YOU-HF (gen) | H-01 | Image + Canva lettering | 4:3, 3:4 | 6 | Red/blue lettering rule | Lettering follows Canva guide | TODO | Repeatable format |
| H-04 | 2 | HOSHOKU | Webtoon-vertical recomposition tests | YOU-HF | Canva Chapter 1 panels | Seedream 5 Pro | 9:16 | 3 | Do not alter lore | No new story beats | TODO | Webtoon promo |
| B-01 | 3 | ÜNDRRARE | Beanie 2.0 hero editorial, flat/ghost | YOU-HF | Shopify master + 3 real photos | Nano Banana Pro | 3:4 | 4 | Orange/cream split, ears, seam match master exactly | Overlay-ready, no text on product | READY after Action 4 | Sales |
| B-02 | 3 | ÜNDRRARE | Beanie 2.0 on-model editorial (3 looks) | YOU-HF | Same + model ref (D1 or real person) | Soul 2.0 | 3:4 | 4 per look | Garment unchanged | Hat accurate, face not distorted | BLOCKED(model choice) | Sales |
| B-03 | 3 | ÜNDRRARE | 5-s product reel (slow orbit, ear detail) | YOU-HF | Best B-01 | Seedance 2.0 | 9:16, 5 s | 2 | No pattern drift | Knit texture stable | BLOCKED(B-01) | Reels, ads |
| B-04 | 3 | ÜNDRRARE | Beanie 2.0 copy (unique, calm, archive tags, no predator/prey) | ME | Shopify description | — | doc | 3 options | Do not reuse OG copy | Follows Brand Rules | READY | Product page, IG |
| B-05 | 3 | ÜNDRRARE | OG vs 2.0 "origin file" comparison post | ME + Canva | Shopify images | — | 3:4 carousel | 1 | Prices from Shopify only | Prices match live | READY | Upsell |
| B-06 | 3 | ÜNDRRARE | Made-to-order lead-time messaging | ME | **Lead time unknown** | — | doc | — | — | Ask D'nuke | BLOCKED(YOU-OK) | Conversion |
| F-01 | 4 | 5ENPAI | Creator visual system (palette, lower-thirds, cover templates) | ME + Canva | Approved transition language (reality/anime/distortion/return) | — | 3:4, 9:16 | — | Do not alter your face | No generated likeness of you | TODO | Brand |
| F-02 | 4 | 5ENPAI | Reality→anime transition test using *your supplied footage* | YOU-HF | A clip you supply | Seedance 2.0 / Kling 3.0 Motion Control | 9:16 | 2 | Source unchanged except style per approved rules | Face preserved | BLOCKED(footage) | Creator content |
| P-01 | 5 | PROJKT OBJKT | Positioning + outreach creative | ME | Services/pricing/logo | — | doc | — | — | — | BLOCKED(D3) | Agency |
| X-01 | All | All | Calendar, captions, publication sequence | ME | — | — | doc | — | Approved voice | — | TODO | Publishing |
| X-02 | All | All | Dashboard + handoff doc (single file) | ME | — | — | md | — | — | — | In progress (this folder) | Handoff |

## Rules this board enforces
- No publish, no store edits, no source overwrite, no paid credits without your explicit OK.
- Cite the approved reference used on every row.
- Generation order inside a day: image test → motion test → final. Failures logged in `03-FAILURE-LOG.md`.
- Final copy and wordmarks are composited in Canva, not generated.

## Prompt starters (to refine after reference files are confirmed)
- **B-01:** "Product photo of the hat in the attached reference image, unchanged: split orange and cream knit, long bunny ears, visible stitched centre seam. Soft studio light, neutral background, 3:4. No text, no logos added, do not redesign the hat."
- **H-01:** "Anthropomorphic rabbit-fox fusion, anthro muzzle and skull, body split exactly 50/50 down the centre with a visible surgical-stitch seam, stitches at shoulders/wrists/knees, dark grey shorts. Left: pale lavender fur, floppy ear with pink inner, red iris, black diamond scar. Right: orange-brown fur, pointed black-tipped ear, cyan-blue iris, black X scar, small fang. Rough dry-brush ink, cel-shaded. Match the attached expression sheet." (Uses only approved traits; flag the eye/mark conflict in the log.)
- **H-02/B-03 motion:** "Start from the attached frame. 5 seconds. Only [one action]. Camera locked off. Do not change colours, markings, or garment pattern."
