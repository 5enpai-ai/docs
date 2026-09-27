# HOSHOKU VTuber — production state

Working log for the HOSHOKU VTuber pipeline. Governed by the generation resource policy (`hoshoku/vtuber-resource-policy.mdx`).

Record every meaningful OpenArt or Meshy operation in the **Operations log** below, newest first.

---

## Resource status

Snapshot taken 2026-09-27 through the OpenArt MCP (read-only, no credits spent).

| Resource | Status |
| --- | --- |
| OpenArt account | Plus plan, 6,227 credits |
| OpenArt project: Personal Project (default) | Stop-motion / claymation HOSHOKU work (puppets, sets, video tests) |
| OpenArt project: HOSHOKU Manga Vol 1 | Vertical webtoon recreation of Vol 1 "Flashback" (manga only). Not an avatar source. |
| Meshy | Not yet checked — confirm the account or workspace is still accessible |
| Local HOSHOKU assets | Not yet inventoried in this repository |

---

## Avatar subject (decided 2026-09-27)

The VTuber is **HOSHOKU, the joined half-rabbit / half-fox stitched puppet**:

- Rabbit half on the **left**: white/cream fur, red button eye, black teardrop mark, pink nose, single floppy ear
- Fox half on the **right**: burnt-orange fur, blue button eye, black X mark, black nose, single pointed ear
- One **vertical** stitched seam down the center of the face and body (never horizontal)
- Handmade felt / fur / burlap puppet material with black thread and bone-shaped accents

Out of scope as avatar sources: Broly and all other *HOSHOKU Manga Vol 1* webtoon panels, and Pai (the mad-scientist puppet). Those assets belong to the manga and the stop-motion short, not the VTuber.

---

## Existing asset inventory

Candidates to check **before** any new VTuber generation. The default project's full history has been reviewed (100 entries). The manga project was skipped because it holds no HOSHOKU avatar material.

### Joined HOSHOKU (primary)

| Asset | OpenArt ID | Type | Notes |
| --- | --- | --- | --- |
| Original HOSHOKU character references | uploads `l8NTrOPw1CZvi6sSvi9E`, `gfO0vUIYGz09VYd66cK4`, `FUdeyXVw6YY17k80eiFy` (`IMG_7248`–`IMG_7250`) | Upload | The source design. Used as character refs for every Smart Shot run. |
| Split/stitched reference v2 | upload `6K8E2jClPXqI5hMDQczU` | Upload | Newest joined-HOSHOKU reference (2026-09-25). Likely the strongest avatar source. |
| Smart Shot character sheet A | creation `qyJpF4p5GcEmkHTf47dg` (history `DNhP2jtg7z3k57P2NeSp`) | Image 1536x1024 | Auto-generated sheet from `IMG_7248`–`7250`. Needs visual review. |
| Smart Shot character sheet B | creation `gLcx9oM4nEzttNUjgQ9t` (history `KXPjxKAuQuD5gBKGuAsm`) | Image 1536x1024 | Same as above, earlier run. Needs visual review. |
| Joined puppet in restraint chair | history `kbkkHUkmNCxLXmWtSSAE` | Image | Scene composite, not a clean sheet. Face/eye reference only. |
| Stitching insert frames | uploads `nrOL6SJXgj1eAXS9RdYi`, `0JkTYaVQzxHba4K2wAVk` (`IMG_7307`, `IMG_7308`) | Upload | Top-down joined head. Useful face reference. |

### Separate halves (secondary)

| Asset | OpenArt history ID | Notes |
| --- | --- | --- |
| Rabbit puppet character sheet, seam removed | `aSAIUEPRVE85mjoFtxpk` | Front / side / limp poses. Whole rabbit, not the joined character. |
| Fox puppet character sheet | `d5bM8QlgvwVatnZKhxNa` | Front / side / limp poses. Whole fox. |

These define each half's materials and details. They are not the avatar itself.

### Motion references

| Asset | OpenArt history ID | What it shows |
| --- | --- | --- |
| Stitch-together + eyes open (6 s) | `DNhP2jtg7z3k57P2NeSp` | Joining, spark, rabbit eye then fox eye opening, one expression change |
| Stitch-together + eyes open (4 s) | `KXPjxKAuQuD5gBKGuAsm` | Shorter version of the above |
| Seam closing insert (3 s) | `wAWwBP1eJPSwokLZs5qT` | Vertical seam closing between `IMG_7307` and `IMG_7308` |
| Stop-motion clips, 2026-09-24/25 | multiple Kling 3 Omni | 12 fps puppet movement. Study for blink / head-turn timing. |

Existing clips already answer "how do HOSHOKU's eyes open, and how does the expression change?" Don't pay for a new video test on that question.

### Gap analysis for the joined HOSHOKU VTuber

| Need | Status |
| --- | --- |
| Canonical design reference | **Likely covered.** Upload `6K8E2jClPXqI5hMDQczU` plus `IMG_7248`–`7250`. |
| Front / side / back turnaround of the *joined* character | **Unconfirmed.** Smart Shot sheets A/B may cover it; review them first. No back view found. |
| Expression sheet (each half's eye states: open, closed, blink, X-stitched) | **Missing** |
| Mouth-shape sheet (visemes: closed, A, I, U, E, O) | **Missing** |
| Clean 2D layered source art for Live2D | **Missing** |
| 3D reference for Meshy | **Missing.** A confirmed front/side turnaround would double as this. |

Design question to settle before the mouth sheet: the stitched seam runs through the mouth. Decide whether the mouth opens across the seam as one mouth, or each half has its own mouth.

---

## Operations log

Template (copy for each operation):

```markdown
### Asset name

- **Purpose:** Why it exists
- **Tool:** OpenArt / Meshy / other
- **Input:** Reference assets
- **Output:** Generated or exported asset
- **Status:** PASS / FAIL / NEEDS REVISION
- **Reuse:** Can this become a canonical production asset?
- **Credit impact:** Known / estimated / unknown
- **Next step:** What consumes this asset next?
```

### Avatar subject decision + full default-project audit — 2026-09-27

- **Purpose:** Lock the avatar subject and finish the existing-asset check
- **Tool:** OpenArt MCP (read-only, full default-project history)
- **Input:** User decision: the VTuber is the joined half-rabbit / half-fox HOSHOKU, not Broly or Pai
- **Output:** Avatar subject, joined-HOSHOKU inventory, and gap analysis above
- **Status:** PASS
- **Reuse:** Inventory only; no new asset
- **Credit impact:** None
- **Next step:** Visually review Smart Shot sheets A/B and upload `6K8E2jClPXqI5hMDQczU` in OpenArt (the session's network policy blocks the OpenArt CDN). If a sheet shows a clean joined front/side view, promote it as canonical. Otherwise the first justified generation is one joined-HOSHOKU front/side/back turnaround from those references.

### OpenArt inventory audit — 2026-09-27

- **Purpose:** Satisfy the "check existing assets first" rule before any VTuber generation
- **Tool:** OpenArt MCP (read-only: account, projects, uploads, generation history)
- **Input:** Both OpenArt projects and the upload library
- **Output:** Existing asset inventory and gap analysis above
- **Status:** PASS (partial — only the latest 50 generations per project were reviewed)
- **Reuse:** Inventory only; no new asset
- **Credit impact:** None
- **Next step:** Superseded by the entry above
