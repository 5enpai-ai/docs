# HOSHOKU Vol 1: handoff for continuing locally

Written 2026-10-14. Everything below is in this repo on branch `claude/hoshoku-volume-1-audit-jdy64c` (`5enpai-ai/docs`). Start a local Claude Code session here and tell it: **"Read `drafts/HOSHOKU-HANDOFF.md` and continue."**

## 1. Set up on your computer

```bash
git clone https://github.com/5enpai-ai/docs.git
cd docs
git checkout claude/hoshoku-volume-1-audit-jdy64c
bash drafts/hoshoku-vol1-vertical/pipeline/setup_local.sh   # needs Python 3; downloads the 52 panels, renders, slices (0 credits)
claude                                                      # start Claude Code in this folder
```

- **Connectors:** the local session needs the **Canva** and **OpenArt** connectors (and **Notion** / **Google Drive** for canon sources). If you sign in to Claude Code with the same claude.ai account, check they appear with `/mcp`.
- **Why local:** the cloud session can't open `webtoons.com` or OpenArt's CDN, and its storage is wiped when it ends. On your machine you can open the published Webtoon episode and compare it directly.

## 2. Hard rules (carry these into every session)

1. **Manga only.** The claymation/stop-motion project is completely separate: never canon, origin, inspiration, continuity or visual reference. The Pai stitching origin is **not canon**.
2. **OpenArt credits are for the HOSHOKU manga only.** Balance: **6,227** (8,507 at start; 57 jobs × 40 = 2,280 spent).
3. **Position A is locked:** Bunni/rabbit LEFT, red eye, black diamond/teardrop. Renard/fox RIGHT, cyan-blue eye, black X scar and small fang.
4. **Don't invent** lore, dialogue, story beats or explanations. Transcribe only. Mark UNRESOLVED / OBSERVED / UNVERIFIED. Keep canon separate from adaptation.
5. **Original Canva designs stay untouched.** Read or test only in draft transactions, and always cancel them. The vertical edition is kept separate.
6. **No generation** until the source/continuity gate passes. No generation past the mirror scene (14d) until the Chapter 2 beats exist.

## 3. Where things stand

| Item | Status |
|---|---|
| Vertical Ch. 1 + Ch. 2 opening (to 14d) | 52 panels generated, 55 Webtoon slices. **Ch. 1 lock SUSPENDED** (2026-10-09). |
| Why suspended | The edition was built only from the art **placed on** Canva pages 1–14. The Canva `Hoshoku` folder has 21 unplaced images; 7 of them have no equivalent on any page. The published Webtoon may also have panels that aren't in Canva at all. |
| Approved decisions | Broly-voice captions are the final caption layer. Broly hair = approved sheet everywhere. 3c = closed cloud, "Just… breathe.", left unclassified. 14a number blank. 14c dark charcoal crew-neck. BROLY name tape removed. 2c recruit = source look, unassigned. |
| Canva vertical folder | `FAHWQyQJp9s`: cover + parts 01–10 (02/03/10 are the "(LOCKED)" versions). Old ones in `Superseded (pre-lock)` (`FAHWRNtpWN0`). **Do not combine the parts** without explicit approval. |
| Chapter 2 | On hold after 14d. The groundwork is ready: `drafts/hoshoku-ch2-groundwork.md`. |

## 4. Next task (start here)

**Chapter 1 completeness check.** It needs D'nuke's input, and it spends no credits.

1. Open the published Webtoon Ch. 1 episode and list every panel in order.
2. Compare that list with `drafts/hoshoku-ch1-ch2-continuity-script.md` (Canva pages 1–12) and `reference/unplaced_canva_art.jpg`.
3. For each missing panel, record where it goes and its source (a Canva image ID from `reference/canva_hoshoku_folder_images.tsv`, or a Webtoon-only screenshot).
4. Add the new panels to the continuity script using its per-panel format, and put them through the same source checks.
5. **Only then** recreate the missing panels: about 40 credits each, nano-banana-pro image2image at 2K, with the source panel plus `reference/gen_refs/` and the Broly sheet as references. Then re-render, re-slice, and update the Canva folder (parts only, no merge).

The 7 candidates in group A of `unplaced_canva_art.jpg`:

- p_20 (a): hospital room, masked staff
- p_20 (b): POV of ceiling lights
- p_21 (a): Broly in a hospital bed, gown
- p_22: Broly faces a dark capped figure
- Image to Image-1767524494000 (1): hospital room with staff
- Image to Image-1767530090000: syringe/IV close-up
- Image to Image-1767454600000: courtyard, stumbling

## 5. Map of files

| Path | What |
|---|---|
| `drafts/hoshoku-volume-1-audit.md` | Audit, canon decisions (A), story as built (B), open questions (E) |
| `drafts/hoshoku-ch1-ch2-continuity-script.md` | Panel-by-panel as-built script, hair/props ledgers, flags |
| `drafts/hoshoku-ch2-groundwork.md` | Ch. 2 beat intake sheet, open threads T1–T20, canon questions Q1–Q7 |
| `drafts/hoshoku-vol1-vertical/README.md` | Vertical edition: status, gates, lettering system, script table, credits |
| `…/webtoon_upload/` | Current 55 slices (pre-completeness-check) |
| `…/source_panels/` | Crops of the original Canva panels (`1a`–`14d`), used as references |
| `…/reference/` | Broly consistency sheet, before/after sheets, unplaced-art sheet, Canva folder image list, `gen_refs/` |
| `…/pipeline/` | `build.py` + `letter.py` (render), `slice.py` (Webtoon/Canva cuts), `mkspec.py` → `spec_full.json` (lettering positions), `panel_sources.json` (generated panel URLs), `source_refs.json` (uploaded source refs), `setup_local.sh`, fonts in `f/` |

**Key IDs**

- Canva originals:
  - `DAG9IhSY4Xo`: manga, pages 1–19
  - `DAHR7QwZmf8`: tall pages
  - `DAHR7ZC2IKs`: lettering style guide
- Canva folders:
  - `FAHM5-EhqDY`: Hoshoku
  - `FAHWQyQJp9s`: Vertical Edition
- OpenArt project: `SSv9vVVoeJgYuglRoCHK`

## 6. Notes for the pipeline

- **Render:** `python3 build.py spec_full.json out/ep_full.png`. Set `HOSHOKU_SOURCE_CAPTIONS=1` to drop the caption bodies.
- **Adding a panel:**
  1. Save the new art as `gen/v_<id>.png`.
  2. Add its URL to `panel_sources.json`.
  3. Insert a `P('<id>', [...letters])` entry at the right spot in `mkspec.py`, then run `python3 mkspec.py`.
  4. Rebuild and run `slice.py`.
- **Canva upload route used so far:** upload the PNG to OpenArt storage, then use Canva `upload-asset-from-url`, then `move-item-to-folder`. Locally, you can also drag the parts into Canva by hand.
