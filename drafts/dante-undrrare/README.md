# Luca Maxim Dante → ÜNDRRARE content system

Research and systems-design workspace. Nothing here is published: the `drafts/` folder is excluded from the Mintlify build by `.mintignore`.

## Status as of 2026-09-27

| Phase | Status | Why |
| --- | --- | --- |
| 1. Source collection | **9 verified (V01–V09)** | The local Codex research session verified the reels through the user's logged-in Instagram (@lucamaxiim) and relayed structured records here. This cloud session can't reach video hosts. Music and SFX are still UNVERIFIED. |
| 2. Dante format database | **Done for the 9-reel sample** | 11 constants, and variables with frequencies. |
| 3. Video grammar | **Done: timed template** | Computed min / median / max timings for 6 functions, plus 3 variants of the China turn |
| 4. Brand-recall mechanism | **Done: supported 9/9** | The tag is identical to the garment print, is spoken as the last joke line while visible, and is paid off by the catalog end card and CTA. |
| 5. ÜNDRRARE translation | **Partial** | Brand constraints and inputs are documented. The beat structure waits on Phase 3. |
| 6. Collection language | **Partial** | The verified on-garment text is documented, including a rotational SEEK / REALITY back graphic. No slogan chosen, as you asked. |
| 7. Character application | **Draft done** | Built from each character's canon. Only the "where SEEK TRUTH / REALITY enters" part depends on the Dante findings. |
| 8. Product identity mapping | **Done for the two named products** | Taken from Shopify (source of truth) and the Printify print files, which I inspected. |
| 9. Automation spec | **Draft v0** | Input and output schema are defined. Slots that depend on Dante findings are marked `PENDING_DANTE`. |

## Deliverable index

| # | Deliverable | File |
| --- | --- | --- |
| 1 | Source inventory | [`01-source-inventory.md`](01-source-inventory.md) |
| 2 | Video-by-video breakdown | [`02-dante-format-database.md`](02-dante-format-database.md) §1 |
| 3 | Recurring format | [`02-dante-format-database.md`](02-dante-format-database.md) §2 |
| 4 | Variable components | [`02-dante-format-database.md`](02-dante-format-database.md) §3 |
| 5 | Brand-recall mechanism | [`03-grammar-and-recall.md`](03-grammar-and-recall.md) §2 |
| 6 | Dante video grammar | [`03-grammar-and-recall.md`](03-grammar-and-recall.md) §1 |
| 7 | ÜNDRRARE translation | [`06-undrrare-system.md`](06-undrrare-system.md) |
| 8 | Killua application | [`05-character-profiles.md`](05-character-profiles.md) §1 |
| 9 | Zero Two application | [`05-character-profiles.md`](05-character-profiles.md) §2 |
| 10 | Product → character → joke system | [`04-product-identity-map.md`](04-product-identity-map.md) + [`06-undrrare-system.md`](06-undrrare-system.md) §4 |
| 11 | Automation spec | [`07-automation-spec.md`](07-automation-spec.md) + [`schema/`](schema/) |
| 12 | Open questions | [`08-open-questions.md`](08-open-questions.md) |

Supporting files:

- [`data/products.json`](data/products.json): machine-readable product records
- [`data/videos/`](data/videos/): one verified record per watched Dante video (V01–V09)
- [`tools/timing_stats.py`](tools/timing_stats.py): recomputes the timing grammar from the records
- [`tools/build_records_v01_v09.py`](tools/build_records_v01_v09.py): encodes the V01–V09 handoff as records
- [`schema/video-record.schema.json`](schema/video-record.schema.json): one record per watched Dante video (the Phase 1 fields)
- [`schema/concept.schema.json`](schema/concept.schema.json): generator input and output
- [`tools/collect_dante.sh`](tools/collect_dante.sh): runs Phase 1 once video hosts are reachable (download, scene frames, transcript)

## How footage gets in

- **Primary route:** the local Codex session reads reels through the user's logged-in Instagram browser. It downloads Instagram's separate signed video and audio streams, merges them, samples frames and transcribes locally.
- **Storage:** media and raw analysis live only at `/Volumes/lacie/watch-work/luca-dante/<reel-folder>/`, on the external drive, never the internal one. This repo holds only the structured records (`data/videos/*.json`).
- **Unverified candidates:** a candidate stays **UNVERIFIABLE** until its footage and audio have been inspected.
- **Tools:** use OpenArt, not Higgsfield, for any later *authorized* generation or video analysis. No generation credits are spent during research.
- `tools/collect_dante.sh` is a fallback, for a machine that has network access to the video hosts.

## Ground rules followed

- No Dante dialogue, beat, timing or shot is described anywhere in this workspace, because none was watched.
- Product facts come only from Shopify and the Printify print files. Anything I couldn't read is marked `UNVERIFIED`.
- No HOSHOKU manga canon, no claymation material, no generation credits spent, nothing published. Higgsfield is not used.
