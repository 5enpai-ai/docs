# HOSHOKU VTuber — Drive reference audit

Companion to `HOSHOKU_VTUBER_STATE.md`. This audit treats the Google Drive **Everything Hoshoku** folder as the visual source of truth, ahead of OpenArt's own generation history.

Subject: **HOSHOKU, the joined half-rabbit / half-fox stitched puppet.** Broly, the *HOSHOKU Manga Vol 1* webtoon panels, and Pai are out of scope as avatar identity sources — see `hoshoku/vtuber-resource-policy.mdx` and the prior state-log entry.

<Warning>
**A hard limitation, stated up front:** this session cannot view image pixels. The OpenArt CDN is blocked by this environment's network policy (confirmed by a failed download attempt), and Google Drive's `read_file_content` tool only extracts text/OCR — for a photo or a flat design PNG with no embedded text, it returns empty content. Every classification below comes from **filenames, folder placement, upload lineage, and the descriptive prompt text already on record from OpenArt** (from the prior audit), not from looking at the images. Anything marked `UNKNOWN` needs a human to actually open the file. Treat "CONFIRMED" claims below as filename/lineage confidence, not visual confirmation.
</Warning>

## Where the library lives

Two Drive folders are both named "Everything Hoshoku":

| Folder | Owner | Access |
| --- | --- | --- |
| `Everything Hoshoku` (`1bp0DKbIhD1p8APHaAsTeKrT8oF3FhPuw`) | `dnukester10@gmail.com` (the user) | **Full access.** 96 files enumerated below. |
| `Everything Hoshoku` (`1U6YFByRN_Hqynda-mtBDOoYhfybKXczj`) | `shitokun05@gmail.com` (a collaborator) | `EXTERNAL_REFERENCE_FOLDER_UNVERIFIED` |

**`EXTERNAL_REFERENCE_FOLDER_UNVERIFIED` — exact status:** the folder object itself is visible to this session (its metadata returns, and `viewedByMeTime` shows it has been opened by this account before), but a `parentId` search against it returns zero results — not an error, just nothing. That's consistent with either an empty folder or a permissions gap on a shared drive (`0ANRsyPb4ZNNfUk9PVA`) where this account can see the folder exists but can't list its children. This session cannot tell which. Its contents are therefore unknown, not "assumed irrelevant" — they haven't been ruled out as materially relevant to the avatar design. No action is being requested here; this is a record of what's blocked and why, for you to weigh against how much you already know is in that folder.

The accessible folder is **flat** (no subfolders) with 96 files, fully enumerated (two pages, no more after that).

## Reference categories found

### 1. Identity references — canonical design anchors

These are the only files whose names directly assert canonical HOSHOKU identity, and they match the naming scheme you gave as anchors.

| File | Drive ID | Category | What it likely establishes | OpenArt cross-reference |
| --- | --- | --- | --- | --- |
| `hoshoku_split_stitched_v2.png` | `1X8DAomebEfiHe4EwtLmiBVYco_OMh8pf` (newer, 2026-09-03) / `1Z2AsRMKfNGEnjVXiGP1Xi_NSVFZd9prY` (older dup, 2026-08-26) | Identity, Seam | Joined rabbit/fox construction — the primary character anchor | **Matches by filename** the upload `hoshoku_split_stitched_v2.png` (`6K8E2jClPXqI5hMDQczU`) already in OpenArt's upload library. Drive is confirmed as the source; OpenArt holds a copy. |
| `hoshoku_bunny_red_v2.png` | `1UX-KFtjWbGxjeFpnxxPGQHUb5EowhgNK` | Identity, Rabbit half | Rabbit-half face/color canon (red eye) | **No filename match** in OpenArt's upload list. Not yet imported into OpenArt under this name. |
| `hoshoku_fox_blue_v2.png` | `12w37fXSaZA3yZWDq_lYU55sLdyDzR3mL` | Identity, Fox half | Fox-half face/color canon (blue eye) | **No filename match** in OpenArt's upload list. Not yet imported into OpenArt under this name. |

<Note>
**Finding:** `hoshoku_bunny_red_v2.png` and `hoshoku_fox_blue_v2.png` are named as deliberate per-half canon references ("_v2", color-coded) but were **not** found among OpenArt's existing uploads (`IMG_7248`–`7250` etc.). If those `IMG_` uploads are actually renamed copies of these two files, that needs confirming by hash or visual match — I can't do that here. If they're different images, these two Drive files are unused, higher-priority identity references that should be brought into OpenArt before any new generation, since they may be sharper than what's already there.
</Note>

### 2. Style / brand references — identity, not necessarily avatar-usable

| File | Drive ID | Category | Notes |
| --- | --- | --- | --- |
| `hoshoku_yinyang.png` | `1ehRPaFzLJ2BU3DSbXZzy9Lqx5646cQyN` | Style, Identity | Likely a symbolic/branding mark (yin-yang framing fits the "two halves, one whole" theme) — probably brand asset, not a character pose |
| `hoshoku_main_logo.png` | `1TvJNrEQlcR6_HEMuiUpvhRrw2k_juzH2` (+ dup `1nbCPVNae9qtDFI9upP2naP0sdHPGWx-3`) | Style | Brand logo, not avatar source |
| `hoshoku_text_logo.png` | `1XBikBOY-pzfKBDBC6eQ2FnvzISuQBA6F` (+ dup `1HLZCzrqDkJVXyWg4iMpA3FMgam33pK6Y`) | Style | Wordmark, not avatar source |
| `h0sh0ku_05_wordmark.png` | `1_7R6qKb03F7sum6P17x5PK0T7xIvveUw` | Style | Another wordmark variant |
| `h0sh0ku_v3_01_split.png` | `1ODNEf65ECHS0-ND0iJm7WoXrfmFprbIf` | Identity, Seam | Name suggests another "split" identity study — possibly an earlier or alternate take on the seam concept than `hoshoku_split_stitched_v2.png`. Needs visual comparison to know which is canon. |
| `h0sh0ku_v3_08_duoheart.png` | `1X4Ou1BdKFiclH-CVO6oI-c1yB-odReAo` | Style, Non-canonical / inspiration | "Duoheart" — unclear if this is a HOSHOKU pose/motif study or a separate concept. Flag as **UNKNOWN** pending visual review. |
| `h0sh0ku_v3_12_handle.png` | `1Vh1-Z8cePqoais_EvRg6ojb29sSpRj7O` | Style | "Handle" — likely a social-media handle/branding graphic, not character art |

The `h0sh0ku_v3_*` naming (zero for "o") is a distinct series from the `hoshoku_*_v2` series — worth asking you whether `v3` supersedes `v2`, since that changes which file is canonical.

### 3. Form / physical references — probable ground-truth photos

These filenames (`_Original`, sequential `IMG_` numbers, bare UUID camera-roll names) strongly suggest **photos of the real handmade puppet**, not AI generations. If true, this is the single strongest form/silhouette reference available, since it's not an interpretation — it's the object itself.

| File | Drive ID | Category | Notes |
| --- | --- | --- | --- |
| `IMG_5067_Original.JPG` | `1rqiZZTdbEymnLeP0oHPxLIKophG4FE2y` | Form, Face | Likely a real-puppet photo |
| `IMG_5068_Original.JPG` | `1dggG_oMKWMpSQHUiy70ks0qJIoEfRv5-` | Form, Face | Likely a real-puppet photo |
| `IMG_5069_Original.JPG` | `1tWVKNh8Bf2IEFee-hBBmgLcLvERVkuGO` | Form, Face | Likely a real-puppet photo |
| `IMG_5350.JPG` | `17wWszSWZGLC3vEjPhjNkQoDSSI5_Icn5` | Form | Likely a real-puppet photo |
| `IMG_5351.JPG` | `1LYJrK69Vjfkvzb2Qe4ci1k-J8rypPZJN` | Form | Likely a real-puppet photo |
| `IMG_6052.PNG` | `1R5LLJFkwCE1emjtylYacs3qntAa5ECbw` | Form | Likely a real-puppet photo (later batch than the 5000s) |
| `42B9C08B-1B98-405E-851B-49098E5B0ECA.jpg` | `19APE_dUlZssKhPFvvSYuOonpgAHri0EA`... | Form | Camera-roll UUID name — likely a real-puppet photo |
| `14E4CAB4-7ABB-4F10-B1C8-40D7926208D9.jpg` | `1LGM3EJiWcsgN50bOdDVBAPUAKqseSAon` | Form | Camera-roll UUID name — likely a real-puppet photo |
| `4CCC6E23-1C9F-4A34-B879-C82CF44174DB.jpg` | `19APE_dUlZssKhPFvvSYuOonpgAHri0EA` | Form | Camera-roll UUID name — likely a real-puppet photo |
| `D61A0780-1C7D-49C7-9391-94ECF9F0188F.jpg` | `1FI4LI8n4OD0sD5kmx1IY8xH68MMI4RTS` | Form | Camera-roll UUID name — likely a real-puppet photo |

<Warning>
**This is the category most worth your time to open manually.** If these are photos of the physical puppet, they are the highest-value form/silhouette/seam/proportion reference in the whole library — stronger than any AI generation, because they show what the seam, ears, and materials actually do on a real object. I cannot confirm this from filenames alone.
</Warning>

### 4. Non-canonical / inspiration — moodboard pulls

**59 unique files** (some uploaded twice, once on 2026-08-26 and again on 2026-09-03/04) follow the pattern `<digits>_<digits>_<digits>_n.webp` — the standard filename Facebook/Instagram CDN gives to a saved image from a post. This is a social-media moodboard dump, not original HOSHOKU art.

These are **not itemized individually** in this audit — cataloguing 59 unverifiable inspiration images by hand would be its own large task and isn't the minimum-effort path the resource policy calls for. What matters:

- Treat this whole batch as **INSPIRATION**, not canon, per your instruction not to flatten style diversity into one thing — these may be exactly the "diverse styles sharing HOSHOKU identity traits" you mentioned finding before, but confirming that requires opening them.
- If you already know which of these mattered most (e.g. a specific style you want the VTuber to borrow from), name them and I'll pull just those into the reference pack instead of guessing from filenames.

## Full non-visual asset metadata

Every column below is metadata: filename, ID, dates, folder location, upload lineage, and (for OpenArt items) the text prompt actually submitted. **None of it is a visual claim.** "Relationship to known anchors" and "classification" are inferred from naming/lineage patterns, not from seeing the image. The "useful for" flags mark what the asset *would plausibly serve if its content matches its name/prompt* — they are hypotheses to verify, not confirmations.

### Drive — identity-asserting files

| Filename | OpenArt ID | Drive ID | Upload date | Source | Prompt | Relationship to anchors | Classification | Useful for |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `hoshoku_split_stitched_v2.png` | Mirrored as upload `6K8E2jClPXqI5hMDQczU` (filename match) | `1X8DAomebEfiHe4EwtLmiBVYco_OMh8pf` (+ dup `1Z2AsRMKfNGEnjVXiGP1Xi_NSVFZd9prY`) | 2026-09-03 (dup 2026-08-26) | User-owned Drive folder | N/A (static image, not an OpenArt generation) | **Is** a named anchor | Reference (asserted original) | Identity, 2D, 3D, Seam |
| `hoshoku_bunny_red_v2.png` | None found | `1UX-KFtjWbGxjeFpnxxPGQHUb5EowhgNK` | 2026-09-03 | User-owned Drive folder | N/A | **Is** a named anchor; not cross-matched to any OpenArt upload | Reference (asserted original) | Identity, 2D, 3D |
| `hoshoku_fox_blue_v2.png` | None found | `12w37fXSaZA3yZWDq_lYU55sLdyDzR3mL` | 2026-09-03 | User-owned Drive folder | N/A | **Is** a named anchor; not cross-matched to any OpenArt upload | Reference (asserted original) | Identity, 2D, 3D |
| `h0sh0ku_v3_01_split.png` | None found | `1ODNEf65ECHS0-ND0iJm7WoXrfmFprbIf` | 2026-09-03 | User-owned Drive folder | N/A | Name implies a second, differently-versioned "split" study — unresolved v2/v3 lineage vs. `hoshoku_split_stitched_v2.png` | Unknown (reference or superseded draft) | Identity, Seam (pending) |

### Drive — brand/style files (name implies non-character)

| Filename | OpenArt ID | Drive ID | Upload date | Source | Prompt | Relationship to anchors | Classification | Useful for |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `hoshoku_yinyang.png` | None found | `1ehRPaFzLJ2BU3DSbXZzy9Lqx5646cQyN` | 2026-09-04 | User-owned Drive folder | N/A | Independent brand mark, thematically linked ("two halves") | Reference (brand) | Style (theme only) |
| `hoshoku_main_logo.png` | None found | `1TvJNrEQlcR6_HEMuiUpvhRrw2k_juzH2` (+ dup) | 2026-09-03 (dup 2026-08-26) | User-owned Drive folder | N/A | Independent, logo naming | Reference (brand) | None expected |
| `hoshoku_text_logo.png` | None found | `1XBikBOY-pzfKBDBC6eQ2FnvzISuQBA6F` (+ dup) | 2026-09-03 (dup 2026-08-26) | User-owned Drive folder | N/A | Independent, wordmark naming | Reference (brand) | None expected |
| `h0sh0ku_05_wordmark.png` | None found | `1_7R6qKb03F7sum6P17x5PK0T7xIvveUw` | 2026-09-03 | User-owned Drive folder | N/A | Independent, wordmark naming | Reference (brand) | None expected |
| `h0sh0ku_v3_08_duoheart.png` | None found | `1X4Ou1BdKFiclH-CVO6oI-c1yB-odReAo` | 2026-09-03 | User-owned Drive folder | N/A | Unclear — name doesn't map to any known anchor or brand term | Unknown | Unknown — flag for review |
| `h0sh0ku_v3_12_handle.png` | None found | `1Vh1-Z8cePqoais_EvRg6ojb29sSpRj7O` | 2026-09-03 | User-owned Drive folder | N/A | "Handle" suggests a social-media username graphic | Reference (brand, probable) | None expected |

### Drive — probable real-puppet photography

| Filename | OpenArt ID | Drive ID | Upload date | Source | Prompt | Relationship to anchors | Classification | Useful for |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `IMG_5067_Original.JPG` | None found | `1rqiZZTdbEymnLeP0oHPxLIKophG4FE2y` | 2026-08-26 | User-owned Drive folder | N/A | Not named as a HOSHOKU anchor; "_Original" + sequential `IMG_` numbering is the pattern camera apps use for source photos | Original (probable, unverified) | Identity, 2D, 3D, Expression |
| `IMG_5068_Original.JPG` | None found | `1dggG_oMKWMpSQHUiy70ks0qJIoEfRv5-` | 2026-08-26 | User-owned Drive folder | N/A | Same pattern as above | Original (probable, unverified) | Identity, 2D, 3D, Expression |
| `IMG_5069_Original.JPG` | None found | `1tWVKNh8Bf2IEFee-hBBmgLcLvERVkuGO` | 2026-08-26 | User-owned Drive folder | N/A | Same pattern as above | Original (probable, unverified) | Identity, 2D, 3D, Expression |
| `IMG_5350.JPG` | None found | `17wWszSWZGLC3vEjPhjNkQoDSSI5_Icn5` | 2026-09-03 | User-owned Drive folder | N/A | Same pattern, later batch | Original (probable, unverified) | Identity, 3D |
| `IMG_5351.JPG` | None found | `1LYJrK69Vjfkvzb2Qe4ci1k-J8rypPZJN` | 2026-09-03 | User-owned Drive folder | N/A | Same pattern, later batch | Original (probable, unverified) | Identity, 3D |
| `IMG_6052.PNG` | None found | `1R5LLJFkwCE1emjtylYacs3qntAa5ECbw` | 2026-08-26 | User-owned Drive folder | N/A | Same pattern, later numbering | Original (probable, unverified) | Identity, 3D |
| `4CCC6E23-1C9F-4A34-B879-C82CF44174DB.jpg` | None found | `19APE_dUlZssKhPFvvSYuOonpgAHri0EA` | 2026-09-03 | User-owned Drive folder | N/A | Bare camera-roll UUID naming — typical of an unedited phone photo | Original (probable, unverified) | Identity, 3D |
| `14E4CAB4-7ABB-4F10-B1C8-40D7926208D9.jpg` | None found | `1LGM3EJiWcsgN50bOdDVBAPUAKqseSAon` | 2026-09-03 | User-owned Drive folder | N/A | Same pattern | Original (probable, unverified) | Identity, 3D |
| `D61A0780-1C7D-49C7-9391-94ECF9F0188F.jpg` | None found | `1FI4LI8n4OD0sD5kmx1IY8xH68MMI4RTS` | 2026-09-03 | User-owned Drive folder | N/A | Same pattern | Original (probable, unverified) | Identity, 3D |

### OpenArt — joined-HOSHOKU-relevant generations (previously catalogued, carried forward)

| Asset | OpenArt ID | Drive location | Upload/created date | Source/project | Prompt (verbatim excerpt) | Relationship to anchors | Classification | Useful for |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Smart Shot character sheet A | `qyJpF4p5GcEmkHTf47dg` (history `DNhP2jtg7z3k57P2NeSp`) | N/A (OpenArt only) | 2026-09-04 | OpenArt Personal Project, Smart Shot feature | Auto-composed from `IMG_7248`–`7250` character references; scene description built the joined-stitching sequence | Built **from** OpenArt uploads, not confirmed to derive from the Drive anchors above | Candidate reference — **not a confirmed turnaround** | 2D, possibly 3D, Identity (pending review) |
| Smart Shot character sheet B | `gLcx9oM4nEzttNUjgQ9t` (history `KXPjxKAuQuD5gBKGuAsm`) | N/A (OpenArt only) | 2026-09-04 | OpenArt Personal Project, Smart Shot feature | Same lineage as sheet A, earlier run | Same as above | Candidate reference — **not a confirmed turnaround** | 2D, possibly 3D, Identity (pending review) |
| Joined puppet in restraint chair | `kbkkHUkmNCxLXmWtSSAE` | N/A | 2026-09-24 | OpenArt Personal Project | "Compose the joined Hoshoku puppet (rabbit half left with red eye, fox half right with blue eye, vertical stitched seam down the center...)" — full prompt on record | Explicitly describes the joined design in text; scene composite, not a clean sheet | Reference (scene composite) | Face, Expression (partial — eyelid device, not blink) |
| Rabbit puppet sheet, seam removed | `aSAIUEPRVE85mjoFtxpk` | N/A | 2026-09-23 | OpenArt Personal Project | Edits a prior rabbit sheet to remove a center seam, preserving face/eye/mark/ear/joint-stitch details per the prompt | Solo-rabbit construction reference, not the joined character | Reference | 2D construction detail (rabbit half only) |
| Fox puppet sheet | `d5bM8QlgvwVatnZKhxNa` | N/A | 2026-09-23 | OpenArt Personal Project | Full independent-fox-puppet character sheet, three panels, described in detail in the prompt | Solo-fox construction reference, not the joined character | Reference | 2D construction detail (fox half only) |
| Stitching + eyes-open video (6s) | `DNhP2jtg7z3k57P2NeSp` | N/A | 2026-09-24 | OpenArt Personal Project, Smart Shot video | Describes two separate halves being stitched together, a spark, then rabbit-eye-first, fox-eye-second opening and one expression change | Directly depicts (per prompt text) the joined character's eye behavior | Reference (motion) | Motion, Expression |
| Stitching + eyes-open video (4s) | `KXPjxKAuQuD5gBKGuAsm` | N/A | 2026-09-24 | OpenArt Personal Project, Smart Shot video | Shorter version of the same beat sequence | Same as above | Reference (motion) | Motion, Expression |
| Seam-closing insert (3s) | `wAWwBP1eJPSwokLZs5qT` | N/A | 2026-09-23 | OpenArt Personal Project, image-to-video | Prompt explicitly specifies the seam stays **vertical at all times, down the center of the face** while closing | Directly documents seam orientation, in text | Reference (motion) | Motion, Seam |

### Inspiration bucket (not itemized)

| Group | Count | Drive location | Upload dates | Classification | Useful for |
| --- | --- | --- | --- | --- | --- |
| `*_n.webp` social-media pulls (Facebook/Instagram CDN naming) | 59 unique files (some duplicated across two upload batches) | User-owned Drive folder | 2026-08-26 and 2026-09-03/04 | Inspiration (asserted by filename pattern, not content) | Style (unconfirmed which, if any) |

Not broken out per-file for the reasons given earlier: without pixel access, a per-file row would just repeat "unknown" 59 times and add no decision-relevant information. If you can name specific files from this batch that matter, I'll add them as their own rows with full metadata.

### Second Drive folder

| Item | Status |
| --- | --- |
| `Everything Hoshoku` (`1U6YFByRN_Hqynda-mtBDOoYhfybKXczj`, owned by `shitokun05@gmail.com`) | `EXTERNAL_REFERENCE_FOLDER_UNVERIFIED` — see "Where the library lives" above for the exact access gap |

## VTuber reference pack (proposed, pending your confirmation)

The smallest useful group, **contingent on you confirming the `UNKNOWN` rows above**:

- **Identity:** `hoshoku_split_stitched_v2.png`
- **Rabbit half:** `hoshoku_bunny_red_v2.png`
- **Fox half:** `hoshoku_fox_blue_v2.png`
- **Seam:** `hoshoku_split_stitched_v2.png` (primary) + `h0sh0ku_v3_01_split.png` (if it turns out to be a distinct, useful seam study rather than a duplicate)
- **Face:** whichever of `IMG_5067`–`IMG_5069_Original.JPG` / `IMG_5350`/`5351.JPG` turns out to be a clean face shot, once opened
- **Expression:** none found yet in Drive — this still relies on the OpenArt motion clips logged in `HOSHOKU_VTUBER_STATE.md`
- **Style:** a small, deliberately chosen subset of the 59 inspiration pulls — needs your picks, not a guess
- **Humanoid:** none found — no Drive reference shows a humanoid interpretation
- **Clothing:** none found — no outfit/accessory references identified in Drive by name or category

I did not finalize this pack because three of its slots depend on `UNKNOWN` rows only you (or a sighted pass over the files) can resolve.

## The 12 questions

1. **What does the rabbit half's face look like?** Not visually confirmed. `hoshoku_bunny_red_v2.png` is named as the canon rabbit reference; the `IMG_5067`–`5069_Original.JPG` photos may show the real puppet's face. Needs opening.
2. **What does the fox half's face look like?** Same situation — `hoshoku_fox_blue_v2.png` is the named canon reference, unconfirmed visually.
3. **How does the center seam behave on a face?** `hoshoku_split_stitched_v2.png` is named exactly for this. OpenArt's own prompt text (from the prior audit) already describes it in words: a **vertical** seam, never horizontal, running down the center of the face and body. That's a text description from a generation prompt, not a visual confirmation of the Drive file's content — but it's the best evidence available right now.
4. **How do the eyes behave when blinking/closing?** Not answered by any Drive filename. The OpenArt motion clips already logged (`DNhP2jtg7z3k57P2NeSp`, `KXPjxKAuQuD5gBKGuAsm`) describe rabbit-eye-first-then-fox-eye opening in text form. No Drive blink reference found.
5. **What happens to the seam around the mouth?** **Not answered by any source yet.** No Drive file names a mouth-specific study, and no OpenArt prompt describes the seam crossing the mouth. This is the single most-unsolved question in the whole audit.
6. **Are there references where the face becomes more humanoid?** No. Nothing in the Drive filenames or the OpenArt inventory suggests a humanoid take exists yet.
7. **Are there references that establish humanoid proportions?** No.
8. **Are there useful clothing/outfit references?** No HOSHOKU-specific outfit reference was found. (Pai's outfit change exists in OpenArt, but Pai is out of scope for HOSHOKU's identity per your instruction.)
9. **Are there references useful for a front-facing VTuber bust?** Possibly the real-puppet photos, if one is a clean front-on face shot — unconfirmed. Possibly OpenArt Smart Shot sheet A or B — also unconfirmed.
10. **Are there references useful for side/back construction?** No back-view reference was found anywhere, Drive or OpenArt. This remains the clearest total gap.
11. **Are there references useful for facial expressions?** Only the OpenArt motion clips (text-described, not visually confirmed here).
12. **Are there references useful for mouth construction?** None found in either library.

## Humanoid design invariants — what must survive the form change

The target is a **humanoid HOSHOKU**, not "a generic anime human." Nothing here invents new canon; it restates, as a checklist, the traits already established by name and by OpenArt prompt text (not yet visually confirmed) that a humanoid design must preserve to still read as HOSHOKU:

| Trait | Source | Status |
| --- | --- | --- |
| Rabbit half on the **left** | User's own description; consistent with `hoshoku_bunny_red_v2.png` naming and every OpenArt prompt reviewed | Established by description/naming, not yet visually confirmed |
| Fox half on the **right** | Same | Established by description/naming, not yet visually confirmed |
| Red eye on the rabbit half | User's description; OpenArt prompts consistently specify "red eye" for the rabbit side | Established by description, not yet visually confirmed |
| Blue eye on the fox half | User's description; OpenArt prompts consistently specify "blue eye" for the fox side | Established by description, not yet visually confirmed |
| A single **vertical** center seam/stitching, never horizontal | Explicit in multiple OpenArt prompts (e.g. `wAWwBP1eJPSwokLZs5qT`: "the seam stays VERTICAL at all times") | Established by prompt text, not yet visually confirmed |
| Overall HOSHOKU silhouette (two-halved, stitched-together creature) | User's description | Established by description, not yet visually confirmed |
| Distinctive facial construction (floppy ear vs. pointed ear, teardrop mark vs. X mark, per prompt text) | OpenArt prompts for the solo rabbit/fox sheets | Established by prompt text, not yet visually confirmed |

**What is explicitly not being decided here:** how these traits map onto a bipedal/humanoid body, what proportions that body has, or what the mouth does at the seam. Those are open questions in the visual verification queue and questionnaire below, not resolved by this checklist.

## Mouth question — evidence, not a decision

Per your instruction, no mouth design decision is being made here. What the evidence actually shows:

- The seam is established (by OpenArt prompt text, not yet by Drive visual confirmation) as **strictly vertical**, running through the center of the face.
- No source — Drive or OpenArt — shows or describes the seam's relationship to an open or talking mouth. Every existing eyes-opening reference stops at the eyes; none of the reviewed prompts mention the mouth at all.
- This means the mouth-across-the-seam question isn't answered by existing material yet. It looks like a genuine gap, not something already solved and overlooked.

## Requirements already solved without generation

- Canon identity anchor (joined character): **likely solved** — `hoshoku_split_stitched_v2.png`, pending you confirming it's the current version over `h0sh0ku_v3_01_split.png`.
- Per-half color/identity reference: **likely solved** — `hoshoku_bunny_red_v2.png` / `hoshoku_fox_blue_v2.png`, pending cross-check against what OpenArt already used.
- "How does HOSHOKU wake up / change expression" motion question: **solved**, already in OpenArt (from the prior audit).

## Requirements that genuinely remain unsolved

- Face detail, confirmed visually (rabbit half, fox half)
- Seam-through-mouth behavior — no evidence anywhere
- Any expression sheet beyond the two motion clips
- Any mouth-shape / viseme reference
- Front/side/**back** turnaround of the joined character — still no back view found in either library
- Any humanoid interpretation or proportion reference
- Any clothing/accessory reference

## OpenArt generation decision — decision tree, not a preset outcome

**Status: HOLD. No generation is authorized by this audit, and none is assumed to be the next step.** The old framing (default to "generate a front/side/back turnaround") has been replaced with a tree, because the right generation — if any is needed at all — depends entirely on what your visual review finds. Preserving OpenArt credits for the actual production pipeline (2D and/or 3D) matters more than guessing now.

```
Is the joined-HOSHOKU identity (rabbit half, fox half, seam) already
clearly established by a confirmed reference?
│
├─ YES, and a humanoid form also already exists somewhere in the library
│   → Generate NOTHING. Move straight to production (turnaround/expression
│     sheets from the existing humanoid design).
│
├─ YES on identity, but NO humanoid form exists anywhere
│   → The first generation (if any) is a HUMANOID DESIGN generation:
│     one image translating the confirmed identity onto a body, holding
│     the invariants above fixed. Not a turnaround yet — the design itself.
│
├─ Humanoid design exists (from a prior step or found in review), but
│   production views (front/side/back) are missing
│   → Generate a turnaround from the confirmed humanoid design.
│
├─ Turnaround exists, but expressions/mouth states are missing
│   → Generate an expression/mouth sheet from the confirmed turnaround.
│
└─ Several of the above are missing at once
    → Prefer ONE generation that covers as many as it can cleanly
      (e.g. a turnaround that already includes 2-3 key expressions),
      provided the result stays clean and controllable enough for
      downstream Live2D/3D work. Do not chase "one generation solves
      everything" at the cost of a messy, unusable result.
```

**What determines which branch applies:** the answers in `HOSHOKU_VTUBER_VISUAL_VERIFICATION.md` and the questionnaire it contains — specifically Q1–Q5 and Q10 there. Until those are answered, this tree cannot be resolved to a single next action, and none is being chosen preemptively.

No credits were spent producing this audit.
