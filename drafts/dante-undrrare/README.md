# Luca Maxim Dante → ÜNDRRARE content system

Research and systems-design workspace. Nothing here is published: the `drafts/` folder is excluded from the Mintlify build by `.mintignore`.

## Status as of 2026-09-27

| Phase | Status | Why |
| --- | --- | --- |
| 1. Source collection | **Blocked: 0 videos watched** | The session's network policy blocks every video host (youtube.com, tiktok.com, instagram.com, x.com, knowyourmeme.com, archive.org). Only web-search result titles and URLs could be seen. Your Google Drive and Notion have no copies of the Dante videos. Higgsfield video analysis could read YouTube links, but the account has 0 credits, and you didn't authorize spending. |
| 2. Dante format database | **Pending Phase 1** | Constants, variables and frequency need watched videos. The empty coding sheet is ready. |
| 3. Video grammar | **Pending Phase 1** | Not derived. I didn't assume a structure. |
| 4. Brand-recall mechanism | **Pending Phase 1** | Not analyzed. Search results name a recurring line; it's recorded as a lead to verify, not as evidence. |
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
- [`schema/video-record.schema.json`](schema/video-record.schema.json): one record per watched Dante video (the Phase 1 fields)
- [`schema/concept.schema.json`](schema/concept.schema.json): generator input and output
- [`tools/collect_dante.sh`](tools/collect_dante.sh): runs Phase 1 once video hosts are reachable (download, scene frames, transcript)

## Unblocking Phase 1

Pick any one of these:

1. **Allow the hosts** in the cloud environment's network settings (environment menu → **Edit** → **Network access**): `youtube.com`, `*.googlevideo.com`, `*.ytimg.com`, `tiktok.com`, `*.tiktokcdn.com`, `instagram.com`, `*.cdninstagram.com`, and `huggingface.co` for the transcription model. Then run `tools/collect_dante.sh`.
2. **Put the videos in Google Drive** (screen recordings or downloads) and share the folder. Drive is reachable from this session.
3. **Authorize Higgsfield video analysis** on YouTube links. Credits are at 0, so this also needs a top-up.

## Ground rules followed

- No Dante dialogue, beat, timing or shot is described anywhere in this workspace, because none was watched.
- Product facts come only from Shopify and the Printify print files. Anything I couldn't read is marked `UNVERIFIED`.
- No HOSHOKU manga canon, no claymation material, no generation credits spent, nothing published.
