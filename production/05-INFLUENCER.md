# AI influencer — provisional specification, reference prompts, launch plan

**Status: PROVISIONAL PROPOSAL.** The name "VANTA" is **unverified**; I found no record of it in Notion, Drive, or Higgsfield. Every design choice below is *proposed by me* from your stated direction and needs your approval before it is treated as the identity. Nothing here enters ÜNDRRARE canon. Only you change canon.

## Your direction (the only fixed inputs)
- Androgynous, gender-ambiguous.
- Human-creature hybrid **or** anime-to-real-life.
- Built for virality, a recognizable identity, and eventual monetization.
- A **separate identity** that can collaborate with HOSHOKU without becoming HOSHOKU canon.

## Guardrails (so the two IPs don't merge)
- Not a rabbit, not a fox, no 50/50 split body, no seam/stitches, no diamond or X marks, no red/cyan eye pairing, no lavender/orange fur. Those belong to HOSHOKU.
- Any HOSHOKU appearance is a labeled collaboration. No shared lore claims.
- Whether the character lives inside the 5ENPAI universe is **undecided** (D7). The anime↔real transition language is approved 5ENPAI canon and can be borrowed as a *format* only.
- Disclose AI on every post using the platform's AI label. Don't present the character as a real person.

## Proposed identity (A = recommended; B = alternate)
| Field | A — "moth" lane (proposed) | B — "stag" lane (alternate) |
|---|---|---|
| Creature cue | Soft feathered antennae rising from the hairline; fine wing-vein tracery at the left temple; faint dust-like shimmer on cheekbones (subtle, ≤ light freckle density) | Small velvet antler buds; fine bark-grain tracery at the left temple |
| Silhouette (the recognition test) | Tall paired antennae + asymmetric black bob (longer on the left). Readable as a black cut-out. | Antler buds + same asymmetric bob |
| Face | Androgynous: strong brow, soft jaw, heavy-lidded eyes, neutral-to-faintly-amused resting expression | same |
| Eyes | Pale silver-grey iris, dark limbal ring (deliberately not red/cyan) | same |
| Skin | Cool, pale, matte; natural texture (pores, no plastic skin) | same |
| Hair | Black, asymmetric bob, blunt ends | same |
| Build | Slim, medium height. Gender-neutral styling. | same |
| Signature prop | One chrome ear cuff, always on the right ear | same |
| Wardrobe rules | Black base layers, one structured outer layer, no logos by default. ÜNDRRARE pieces only when product-accurate and approved. | same |
| Palette | Obsidian, bone, ash grey, chrome. One cold accent (dusty blue-violet), used sparingly. No neon. | same |
| Anime form | Same face geometry in cel-shaded line art; antennae and temple tracery preserved; used as the "from" state in transformation clips | same |
| Lighting/camera | Primary look: soft overcast key + low practical rim; 35 mm equivalent; slightly low angle for full-body; vertical 9:16 default | same |

Personality, backstory, voice, and name are **intentionally left blank**. Don't let me fill them without you. Open fields: name, pronouns, tone of voice, origin (if any), account handle, relationship to 5ENPAI.

## Reference prompts (all queue C until access is verified)
Model suggestions are from the unlimited-flagged list. Verify per model on the website first.

**IR-01 master face, front** — Soul 2.0 or Nano Banana Pro, 3:4, 2k, 4 variations
> Photoreal portrait, androgynous human-creature hybrid, front view, neutral expression. Black asymmetric blunt bob longer on the left. Two tall feathered moth antennae rising from the hairline. Fine pale wing-vein tracery at the left temple. Pale silver-grey irises with a dark outer ring. Cool pale matte skin with natural pores. Chrome ear cuff on the right ear only. Soft overcast key light, low rim light, plain mid-grey background, 35mm look. No text, no logo.

**IR-02 three-quarter left / IR-03 profile (shows antennae) / IR-04 three-quarter right** — same text with the view changed, using the best IR-01 frame as the image reference. Keep the ear cuff on the right ear in every view.

**IR-05 full body** — 3:4, same reference
> Full-length, black structured long coat over black base layers, no logos, standing, relaxed posture, slightly low camera, soft overcast light, plain background. Same face, antennae, hair, and ear cuff as the reference.

**IR-06 expression grid** — nine tiles: neutral, faint smile, amused, serious, surprised, tired, looking away, eyes closed, mid-blink. Same identity.

**IR-07 anime form** — cel-shaded line-art version of the IR-01 face geometry, same antennae/tracery, flat colour, clean ink outline.

**Identity lock steps** (after IR-01 to IR-06 are approved by you):
1. Pick 1 hero image. Create a reusable Element (instant, image-based) or train a Soul (5 to 20 approved images, about 10 min). Soul works with Soul 2.0 / Cinema only; Elements work across more models.
2. All later prompts reference that Element or Soul, not text description alone.
3. Test identity drift: generate the same identity in 3 outfits and 3 lighting setups before any video.

## Test queue (smallest set that proves the identity)
| Test | Purpose | Pass |
|---|---|---|
| IT-01 | 4 variations of IR-01 | One variation clearly matches the silhouette test |
| IT-02 | IR-02/03 from the chosen hero | Antennae and ear cuff consistent in 3 views |
| IT-03 | Hero in 3 outfits | Face stable, outfits plausible |
| IT-04 | 5-s start-frame video, one slow head turn, Seedance 2.0 or Kling 3.0 | No antenna/hair morphing, eye colour stable |
| IT-05 | Anime to real wipe, 5 s | Both forms recognisably the same |

## Three launch videos (9:16, 6 to 10 s each; concepts, not yet generated)
**LV-1 "Early Light"** — anime form fills the frame in cel-shaded line art; a slow crack of photographic texture moves left to right; the real form is revealed last at the antennae. Hook inside 1 s: the first frame is already striking (extreme close eye in anime style). Audio: single low synth swell, no speech. Purpose: establish the signature anime-to-real format.
**LV-2 "Wet Street"** — real form walks toward camera on a wet night street under sodium streetlight; small moths drift into the light behind them. Locked-off camera, slow push on last second. Purpose: silhouette and attitude, loopable.
**LV-3 "Window"** — real form looks at a shop-window reflection which shows two different silhouettes behind them for one beat (a HOSHOKU nod, labeled as collaboration tease). Needs your approval because it touches HOSHOKU IP. No lore statements. Purpose: the bridge to HOSHOKU without merging.

Each video: 3 prompt versions maximum, 2 generations each, then pick.

## Backlog of original short-form concepts (20)
1. Eyes-only reveal: five lighting setups, one iris.
2. Antennae react to a beat drop (audio-synced).
3. "Outfit of the night" three-cut transitions.
4. Anime to real, one prop at a time (ear cuff first).
5. Slow zoom out from a single moth on a sleeve to full figure.
6. "Things I'd never say" — silent subtitles over a still face.
7. Mirror reveal: reflection is the anime form.
8. Shadow on a wall shows the antennae silhouette before the character enters.
9. Rain on a bus-stop shelter, character waits, ignores camera.
10. Rooftop dawn, hair moves, antennae tilt toward the sun.
11. Elevator ride, floors count up, expression changes each floor.
12. "Pick a side" (poll) — two outfits, comment to vote.
13. 1-second beat cuts of the same face in 8 eras (clothes only).
14. Texture macro: tracery at the temple with cheek shimmer.
15. A phone-light-only scene, face lit by a screen, no text.
16. Collaboration cutaway with HOSHOKU (needs approval each time).
17. ÜNDRRARE product wearer clip (only when product-accurate and approved).
18. Trailer for a "season" of 7 posts.
19. Behind-the-scenes: the reference sheet, labeled as AI-generated.
20. Loopable ambient clip for profile banner.

## Captions and publication plan (DRAFT; nothing scheduled)
- Account: **undecided** (D7). Options: new dedicated account, or a Reels series on `@5enp.ai`. Recommendation: dedicated account, so the identity can be monetised separately.
- Cadence: 1 post per day for the first 7 days: Day 1 LV-1, Day 2 still carousel (IR-02/03/05), Day 3 LV-2, Day 4 backlog #4, Day 5 LV-3 (if approved), Day 6 poll #12, Day 7 recap.
- Caption style: short, quiet, no hype. Examples: "first light." / "no explanation yet." / "seen from the side." / "ai-generated character." Always include the AI label. No fake exclusivity.

## Measurement framework
| Stage | Metric | What it tells you |
|---|---|---|
| Hook | 3-second view rate, average % watched | Is frame 1 working? |
| Spread | Shares and saves per 1,000 views | Is it worth passing on? |
| Identity | Comments naming the character or asking "who is this" | Is it recognisable? |
| Conversion | Follows per 1,000 views; profile visits to follows | Is attention becoming audience? |
| Monetisation | Brand-inquiry DMs, link clicks, collab requests | Is there a business? |

No thresholds are claimed. After 7 posts, rank by 3-s rate and shares/1k and make more of the top two formats. Optional: Higgsfield's virality predictor on finished clips. Check its cost first.

## Questions I need answered (small)
D6 moth or stag lane, or supply your own. D7 account home and 5ENPAI relationship. D8 name (keep VANTA provisional or choose).
