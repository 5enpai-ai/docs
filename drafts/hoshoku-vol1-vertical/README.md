# HOSHOKU Vol 1 "Flashback": Vertical Edition, Ch. 1 + Ch. 2 opening

A vertical webtoon recreation of the existing manga (Canva `DAG9IhSY4Xo`, pages 1–14).

- **Source:** the original project is the reference and the guide. The story is unchanged.
- **Manga only.** No claymation material is used anywhere.

## Decisions applied (D'nuke, 2026-09-26)

| Topic | Decision |
|---|---|
| Format | 800 px wide vertical scroll. Every original panel is recomposed as a tall or insert panel. |
| Broly's hair | **Approved sheet everywhere:** pink-and-blonde ombré locs (sandy roots, pink ends) on every panel. This replaces the original's short-twist and long-loc switches. |
| HOSHOKU | Position A is locked. HOSHOKU does not appear in any Ch. 1–2 panel; this matches the original, where he appears only in the emblem. |
| Captions | Captions are rewritten in **Broly's own wry voice** in HOSHOKU-styled boxes. The original caption *information* (day, time, place) is kept as the mono header on each box. |
| Dialogue / SFX | Carried over word for word from the original (see flags). No new dialogue or story beats were added. |
| Tall pages 16–19 of the original | Not used as a source. They changed settings (ENLIST neon, indoor pool, drill instructor). The recreation follows the published spreads. |

## Deliverables

| What | Where |
|---|---|
| **Webtoon upload slices:** 55 JPGs at 800×1280, in reading order | `webtoon_upload/hoshoku_v1_ch1-2_001.jpg` … `_055.jpg` |
| Half-res preview of the whole strip | `preview_half_res.jpg` |
| Broly consistency sheet (turnaround, heads, 6 expressions) | `reference/broly_consistency_sheet_v1.jpg` |
| Canva: 11 tall parts (cover + parts 01–10) | Canva folder **HOSHOKU Vol 1 — Vertical Edition** (`FAHWQyQJp9s`), inside `Hoshoku` |
| OpenArt: all panels, references, and the sheet | OpenArt project **HOSHOKU Manga Vol 1** (`SSv9vVVoeJgYuglRoCHK`) |
| Full-resolution panel URLs, keyed by original panel ID | `pipeline/panel_sources.json` |
| Lettering and assembly pipeline (re-runnable) | `pipeline/` (see below) |

The original Canva designs were **not modified**.

## Lettering system

| Element | Look |
|---|---|
| **HOSHOKU caption** | Bone `#F5F0E8` box with a black border. **Crimson left edge**, **Renard-blue right edge**, cross-stitched seam along the top, split-emblem tag on the corner. Mono header in crimson (the original info). Hand-scrawl body in black (Broly's voice). |
| Broly speech | Style-guide bubble: plain white, thick black border, one clipped corner. |
| Other speakers | Round white bubble with a thin border. |
| Thought | Soft cloud, dot trail, muted grey-blue `#555577` italic, in parentheses (per the style guide). |
| Shouts | White spiky burst, heavy black type. |
| SFX | Big hits: crimson with white outline (BANG!). Ambient: bold white caps (SPLASH!, HUFF, CLACK, TSS). |
| Room tone | Faint grey italic lowercase (beep…, drip…). |

Fonts are **placeholders** that follow the agreed direction: condensed SFX, rounded-sans dialogue. No brand family has been chosen yet in Notion.

- Anton (SFX)
- Nunito (dialogue)
- Permanent Marker (caption voice)
- Space Mono (caption headers)

All four are OFL-licensed, from `@fontsource`.

## Vertical script: captions and lettering

Captions are **PROPOSED** (Broly's voice). Everything else is carried over from the original.

| Panel | Lettering |
|---|---|
| Title card | HOSHOKU / VOL. 1 — FLASHBACK / CH. 1 — RECRUITMENT DAY |
| 1a | (no text) |
| 1b | Broly: "No turning back now." |
| 1c | CAPTION `BOOTCAMP // DAY 8`: *Legs: gone. Pride: leaving.* Off-panel shout: "Keep moving…" |
| 2a | CAPTION `DAY 8 >> DAY 34`: *Same drills. Newer bruises.* Thought: "(Breathe. Don't panic.)" SFX SPLASH! |
| 2b | Thought: "(No excuses.)" Off-panel shout: "MOVE!" |
| 2c | Off-panel shout: "FASTER!!" |
| 2d | Off-panel shout: "AGAIN!!" HUFF ×3. Broly: "Just… one more round." |
| 2e | CLACK, BANG!. Off-panel shout: "Eyes forward. Squeeze—" ⚠ |
| 3a | CAPTION `BOOTCAMP // DAY 8`: *Lights out. My head didn't get the memo.* Broly: "Can't… slow down…" ⚠ |
| 3b | CAPTION `02:13 AM // COURTYARD`: *Needed air. Any air.* |
| 3c | Thought: "(Just… breathe.)" ⚠ |
| 3d | Broly: "…I'm gonna—" |
| 3e | Off-panel (the arm's owner): "Whoa! Easy—" |
| 4a | CAPTION `PRE-BLACKOUT`: *Last thing I remember clearly.* TSS. Off-panel: "Hold still." |
| 4b–4c | beep…, drip… (fading) |
| Black | · · · · · · |
| 5b | CAPTION `DAY: UNKNOWN // LOCATION: UNKNOWN`: *Me: …also unknown.* "ngh…" |
| 5c | Broly: "Where… am I…?" |
| 6a | CAPTION `MILITARY MEDICAL WING`: *Too clean. Too quiet.* |
| 6b–12 | No lettering (as in the original). ALARM appears on the screens in 10b. |
| End card | END OF CH. 1 / FLASHBACK |
| Title card | HOSHOKU / VOL. 1 — FLASHBACK / CH. 2 |
| 13a–13e, 14a | No lettering |
| 14b / 14c / 14d | In-world numbers **#007 / #614 / #389** (as in the original) |
| End card | TO BE CONTINUED |

### Flags

1. **2e:** the range line uses the published reading "Eyes forward. Squeeze—" (UNVERIFIED from a small thumbnail). The Aug-2026 tall page used "Two forward squads—". **Confirm which one.**
2. **3a:** the second half of "slow down…" was hidden under a caption in the original. It's restored as "down…" (UNVERIFIED).
3. **3c:** the original shape was cloud-like with no dot trail, so the thought-vs-speech call is UNVERIFIED. It's lettered as a thought.
4. **14a:** the original's tiny "#…" number is illegible, so it's **omitted** rather than guessed.
5. **2b:** the generated art added a **"BROLY" name tape** on the uniform (not in the original). Keep it, or I'll fix it (~40 credits).
6. **2c:** the recruit's identity is ambiguous in the original. The generated art has pink-toned hair, so it reads as Broly.
7. **9d:** invented vial labels ("VACCINE", "MEDICINE") appeared and were removed with an edit pass (blank labels now).
8. **14c:** Broly is shirtless at the sink (the original shows a dark top). Minor.
9. **Captions:** all caption *bodies* are new copy in Broly's voice (PROPOSED). The headers keep the original information.

## Credits

| Item | Jobs | Credits |
|---|---:|---:|
| Broly consistency sheet | 1 | 40 |
| Panels: pilot (8) + remaining (44) | 52 | 2,080 |
| 9d label fix | 1 | 40 |
| **Total** | **54** | **2,160** |

- Balance: 8,507 → **6,347**.
- Model: Nano Banana Pro i2i at 2K, 40 credits each.
- Title and end cards, black beats, lettering, and assembly were done locally: 0 credits.

## Re-running the assembly (0 credits)

`pipeline/build.py spec_full.json out.png` renders the strip from `panel_sources.json` images (downloaded as `gen/v_<id>.png`). It expects:

- fonts in `f/`, via `npm pack @fontsource/{anton,nunito,permanent-marker,space-mono}`
- `split_v2.png`, the Drive split emblem, alongside

Edit `spec_full.json` to move or reword any bubble, then re-render. No regeneration needed.

## Next

- Assemble the Canva parts into one Canva design (needs your OK before I save edits in Canva).
- Resolve the flags above.
- Story beats for Ch. 2 after the mirror scene: the continuation is blocked on your beats (E in the audit). Nothing past page 14 has been generated.
