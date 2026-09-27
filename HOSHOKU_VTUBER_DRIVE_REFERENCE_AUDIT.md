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
| `Everything Hoshoku` (`1U6YFByRN_Hqynda-mtBDOoYhfybKXczj`) | `shitokun05@gmail.com` (a collaborator) | **Metadata only.** The folder itself is visible (it's been viewed before), but listing its contents returned nothing — likely a permissions gap on a shared drive, not an empty folder. |

**Action needed from you:** if the collaborator's folder holds material this one doesn't, share it (or its shared-drive) directly with `dnukester10@gmail.com` so it can be enumerated. I did not treat "returned nothing" as "empty" — I don't have enough access to tell the difference.

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

## Reference matrix

| Reference | Category | What it establishes | Identity value | VTuber use | Status |
| --- | --- | --- | --- | --- | --- |
| `hoshoku_split_stitched_v2.png` | Identity, Seam | Joined rabbit/fox construction | HIGH | Primary | **REFERENCE** (filename-confirmed anchor; already mirrored into OpenArt) |
| `hoshoku_bunny_red_v2.png` | Identity, Rabbit half | Rabbit-half face/color canon | HIGH (asserted by name) | Facial construction | **REFERENCE** (not yet cross-verified against OpenArt uploads) |
| `hoshoku_fox_blue_v2.png` | Identity, Fox half | Fox-half face/color canon | HIGH (asserted by name) | Facial construction | **REFERENCE** (not yet cross-verified against OpenArt uploads) |
| `h0sh0ku_v3_01_split.png` | Identity, Seam | Possible alternate/earlier seam study | UNKNOWN | Seam | **UNKNOWN** — resolve v2 vs. v3 lineage with you |
| `h0sh0ku_v3_08_duoheart.png` | Style / Non-canonical? | Unclear | UNKNOWN | Unclear | **UNKNOWN** |
| `h0sh0ku_v3_12_handle.png` | Style | Likely branding, not character | LOW | None expected | **REFERENCE** (branding only, likely) |
| `hoshoku_yinyang.png` | Style, Identity | Symbolic brand mark | MEDIUM | Motif / theme, not pose | **REFERENCE** |
| `hoshoku_main_logo.png` | Style | Brand logo | LOW | None expected | **OBSOLETE for avatar** (brand use only) |
| `hoshoku_text_logo.png` | Style | Wordmark | LOW | None expected | **OBSOLETE for avatar** (brand use only) |
| `h0sh0ku_05_wordmark.png` | Style | Wordmark | LOW | None expected | **OBSOLETE for avatar** (brand use only) |
| `IMG_5067_Original.JPG` – `IMG_5069_Original.JPG` | Form, Face | Real-puppet photography (probable) | HIGH (if confirmed) | Face / seam / silhouette construction | **UNKNOWN** — highest-priority manual check |
| `IMG_5350.JPG`, `IMG_5351.JPG` | Form | Real-puppet photography (probable) | HIGH (if confirmed) | Silhouette / body construction | **UNKNOWN** — highest-priority manual check |
| `IMG_6052.PNG` | Form | Real-puppet photography (probable) | MEDIUM–HIGH | Construction reference | **UNKNOWN** |
| 4 UUID-named `.jpg` camera-roll photos | Form | Real-puppet photography (probable) | HIGH (if confirmed) | Construction reference | **UNKNOWN** — highest-priority manual check |
| 59 `*_n.webp` social-media pulls | Inspiration | Mood/style references from elsewhere | LOW–MEDIUM, mixed | Style inspiration only, never copied as canon | **INSPIRATION** (unclassified — needs your triage or explicit picks) |
| OpenArt Smart Shot sheets A/B (`qyJpF4p5GcEmkHTf47dg`, `gLcx9oM4nEzttNUjgQ9t`) | Identity, Humanoid? | AI-composited sheet built from `IMG_7248`–`7250` | UNKNOWN | Possible turnaround | **EXPERIMENTAL** — carried over from the OpenArt-only audit, still unreviewed |

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

## OpenArt generation decision

**Outcome: not yet — hold.** This matches your outcome A/B/C framework, landing between A and B:

- The Drive library plausibly **already answers** the core identity question (rabbit half, fox half, joined seam) through `hoshoku_bunny_red_v2.png`, `hoshoku_fox_blue_v2.png`, and `hoshoku_split_stitched_v2.png` — but that's not confirmed, because this session can't see the images.
- Committing to any generation now — including "just" a turnaround or expression sheet — would mean generating against **unconfirmed** identity references, which the resource policy's decision rule doesn't allow ("existing assets have been checked" isn't satisfied by a filename list).

**What has to happen before any generation is authorized:**

1. You (or someone who can see the images) opens `hoshoku_split_stitched_v2.png`, `hoshoku_bunny_red_v2.png`, `hoshoku_fox_blue_v2.png`, and the `IMG_5067`–`5069_Original.JPG` / `IMG_5350`/`5351.JPG` photos, and confirms: which is current canon, whether the real-puppet photos are usable, and whether `v3_01_split.png` supersedes `v2`.
2. Same for the two OpenArt Smart Shot sheets, to see whether a turnaround already exists.

**If, after that check, a gap remains** — most likely the back view, or a genuine expression/mouth sheet — **the first precise generation objective would be:**

> One OpenArt image generation: a three-panel character sheet of the joined HOSHOKU puppet (front / side / back), built from the confirmed canon references (`hoshoku_split_stitched_v2.png` + the two half-color anchors) as image references, explicitly preserving the vertical seam, each half's established eye/mark/ear details, and puppet material — matching the same construction approach already proven in the existing rabbit and fox solo character sheets (`aSAIUEPRVE85mjoFtxpk`, `d5bM8QlgvwVatnZKhxNa`).

This is deliberately **not** authorized yet — it's the candidate objective for after your visual confirmation, per outcome C (production reference missing, design already exists).

No credits were spent producing this audit.
