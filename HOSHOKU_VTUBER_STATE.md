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
| OpenArt project: HOSHOKU Manga Vol 1 | Vertical webtoon recreation of Vol 1 "Flashback" (manga only) |
| Meshy | Not yet checked — confirm the account or workspace is still accessible |
| Local HOSHOKU assets | Not yet inventoried in this repository |

---

## Existing asset inventory

Candidates to check **before** any new VTuber generation. Only the first 50 entries of each OpenArt project were reviewed; both projects have more history (`hasMore: true`). Page further back before generating anything new.

### Character references (default project)

| Asset | OpenArt history ID | Model | Notes |
| --- | --- | --- | --- |
| Joined Hoshoku puppet composite (rabbit half left, red eye; fox half right, blue eye; vertical stitch) | `kbkkHUkmNCxLXmWtSSAE` | Nano Banana Pro | Strongest existing "joined HOSHOKU" reference |
| Rabbit puppet character sheet | `R8nfMQROHreJMkHNe96k` | Nano Banana 2 | Original sheet |
| Rabbit puppet character sheet, seam removed | `aSAIUEPRVE85mjoFtxpk` | Nano Banana 2 | Corrected version of the sheet above |
| Fox puppet character sheet | `d5bM8QlgvwVatnZKhxNa` | Nano Banana 2 | |
| Pai claymation character sheet | `T78wEiHSOJpg9glrUzDi` | Nano Banana Pro | Built from real-person references |
| Pai character sheet, outfit change | `7vwEeoPbNzrLRtYAUiy4` | Nano Banana Pro | |
| HOSHOKU handmade title card | `2YqDGbWiXjbdweFCwXxG` | Nano Banana 2 | Branding, not avatar source |

### Uploaded references

| Upload | Upload ID | Notes |
| --- | --- | --- |
| `hoshoku_split_stitched_v2.png` | `6K8E2jClPXqI5hMDQczU` | Split/stitched HOSHOKU reference — review as a likely avatar source |
| `IMG_7248`–`IMG_7250`, `IMG_7307`–`IMG_7310`, `IMG_7348`, `IMG_7349`, `IMG_7357` | various | Not yet reviewed |

### Motion references (default project)

Many Kling 3 Omni stop-motion clips (12 fps puppet movement) from 2026-09-24 and 2026-09-25, plus one MiniMax H3 Max clip (`ZdL3sUBphhBqJv6qCoxS`). These can be studied for movement and expression before paying for new motion studies.

### Gap analysis

- Every existing character asset is in **stop-motion puppet / claymation** style. None is a **humanoid HOSHOKU** reference, and none has clean 2D VTuber source art, front/side/back turnarounds, or expression and mouth sheets.
- Decide which HOSHOKU manifestation the VTuber should be (puppet or humanoid) before any generation. That decision defines the first genuinely missing asset.

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

### OpenArt inventory audit — 2026-09-27

- **Purpose:** Satisfy the "check existing assets first" rule before any VTuber generation
- **Tool:** OpenArt MCP (read-only: account, projects, uploads, generation history)
- **Input:** Both OpenArt projects and the upload library
- **Output:** Existing asset inventory and gap analysis above
- **Status:** PASS (partial — only the latest 50 generations per project were reviewed)
- **Reuse:** Inventory only; no new asset
- **Credit impact:** None
- **Next step:** Choose the VTuber manifestation (puppet or humanoid), check Meshy access, then define the first missing asset against the decision rule
