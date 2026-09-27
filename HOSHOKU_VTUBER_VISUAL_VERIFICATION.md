# HOSHOKU VTuber — visual verification queue

Companion to `HOSHOKU_VTUBER_DRIVE_REFERENCE_AUDIT.md` and `HOSHOKU_VTUBER_STATE.md`.

<Warning>
Nothing in this document is a visual claim. This session cannot view image pixels — not from the OpenArt CDN (network-blocked) and not from Google Drive (`read_file_content` only extracts text/OCR, which returns nothing for photos or flat design PNGs). Every entry below exists because metadata alone can't answer the question it names. Only a human (or a tool/session with real image access) can close these out.
</Warning>

This list contains **only** the assets where seeing the actual image would change a production decision — not the full 96-file Drive inventory, and not the 59-file inspiration bucket. See the Drive audit for those.

---

## Priority 1 — must see

These block the most decisions. Open these first.

### 1. `hoshoku_split_stitched_v2.png`
**Drive ID:** `1X8DAomebEfiHe4EwtLmiBVYco_OMh8pf`

- **Why we need to see it:** It's named as the primary joined-character identity anchor and is the file OpenArt's own upload library mirrors by filename.
- **Question it answers:** Does this provide a sufficiently clean joined-character facial/body reference to build a humanoid manifestation from?
- **Outcome A:** Yes, it's clean and current → adopt as the primary identity anchor; skip identity generation entirely.
- **Outcome B:** No — it's a scene composite, low-res, outdated, or superseded by `h0sh0ku_v3_01_split.png` → determine precisely what's missing before any generation is considered.

### 2. `hoshoku_bunny_red_v2.png`
**Drive ID:** `1UX-KFtjWbGxjeFpnxxPGQHUb5EowhgNK`

- **Why we need to see it:** Named as the canon rabbit-half reference, but not cross-matched to anything already used in OpenArt — it may be an unused, sharper reference.
- **Question it answers:** Does this establish the rabbit half's face (red eye, ear, mark, proportions) clearly enough to build from?
- **Outcome A:** Yes → use as the rabbit-half construction reference; more valuable than the existing OpenArt rabbit sheet if sharper or more current.
- **Outcome B:** No, or it duplicates what OpenArt already has → drop it from the reference pack, rely on the existing OpenArt rabbit character sheet (`aSAIUEPRVE85mjoFtxpk`) instead.

### 3. `hoshoku_fox_blue_v2.png`
**Drive ID:** `12w37fXSaZA3yZWDq_lYU55sLdyDzR3mL`

- **Why we need to see it:** Same situation as #2, for the fox half.
- **Question it answers:** Does this establish the fox half's face (blue eye, ear, mark, proportions) clearly enough to build from?
- **Outcome A:** Yes → use as the fox-half construction reference.
- **Outcome B:** No, or duplicates OpenArt's existing fox sheet (`d5bM8QlgvwVatnZKhxNa`) → drop it, rely on the existing one.

### 4. OpenArt Smart Shot sheet A — `qyJpF4p5GcEmkHTf47dg`
**OpenArt history ID:** `DNhP2jtg7z3k57P2NeSp` · 1536×1024, generated 2026-09-04

- **Why we need to see it:** It's an auto-composited "character sheet" built from `IMG_7248`–`7250`. It might already be a usable joined-character turnaround — which would mean skipping a generation entirely.
- **Question it answers:** Is this a clean, multi-angle, production-usable joined-HOSHOKU reference, or a rough/single-angle scene image?
- **Outcome A:** It's clean and multi-angle → treat as a candidate turnaround; likely satisfies part of the "production views" requirement with zero new credits spent.
- **Outcome B:** It's messy, single-angle, or anatomically inconsistent (Smart Shot auto-composites are not guaranteed clean) → discard as a production reference, but keep on file as a design study.

### 5. OpenArt Smart Shot sheet B — `gLcx9oM4nEzttNUjgQ9t`
**OpenArt history ID:** `KXPjxKAuQuD5gBKGuAsm` · 1536×1024, generated 2026-09-04

- **Why we need to see it:** Same lineage as #4, an earlier run — may be better or worse than sheet A.
- **Question it answers:** Same as #4, plus: does A or B look more usable, if both exist?
- **Outcome A:** One or both are usable → pick the stronger one (or both, for different angles) as a candidate turnaround.
- **Outcome B:** Neither is usable → both remain candidate design studies only, not production references.

---

## Priority 2 — possibly important

These matter if Priority 1 leaves the identity anchors unconfirmed, or if the real-puppet photos turn out to be the stronger reference.

### 6–8. `IMG_5067_Original.JPG`, `IMG_5068_Original.JPG`, `IMG_5069_Original.JPG`
**Drive IDs:** `1rqiZZTdbEymnLeP0oHPxLIKophG4FE2y`, `1dggG_oMKWMpSQHUiy70ks0qJIoEfRv5-`, `1tWVKNh8Bf2IEFee-hBBmgLcLvERVkuGO`

- **Why we need to see them:** Filename pattern (`_Original`, sequential numbering) strongly suggests real photos of the physical puppet — the actual object, not an interpretation of it. If true, this is the highest-fidelity reference available for seam/material/proportion.
- **Question they answer:** Are these genuinely photos of the physical HOSHOKU puppet, and if so, do any show the face/seam clearly?
- **Outcome A:** Yes, and at least one is a clean face/seam shot → this becomes the primary ground-truth reference for both 2D and 3D work, potentially outranking every AI-generated reference.
- **Outcome B:** No (they're something else — set photos, unrelated puppet photos, blurry/unusable) → drop from the reference pack.

### 9–10. `IMG_5350.JPG`, `IMG_5351.JPG`
**Drive IDs:** `17wWszSWZGLC3vEjPhjNkQoDSSI5_Icn5`, `1LYJrK69Vjfkvzb2Qe4ci1k-J8rypPZJN`

- **Why we need to see them:** Same real-photo hypothesis as #6–8, different capture batch — may show a different angle (side/back), which is the single clearest gap in the whole library.
- **Question they answer:** Do these show an angle (side or back) that no other reference shows?
- **Outcome A:** Yes → this may close the "no back view found anywhere" gap without any generation at all.
- **Outcome B:** No, they duplicate the front-facing angle already seen elsewhere → gap remains open.

---

## Additional assets worth flagging (lower priority, name-driven)

| File | Why it might matter | What seeing it would resolve |
| --- | --- | --- |
| `h0sh0ku_v3_01_split.png` (`1ODNEf65ECHS0-ND0iJm7WoXrfmFprbIf`) | Possible alternate or newer "split" identity study than `hoshoku_split_stitched_v2.png` | Whether `v3` supersedes `v2` as canon — changes which anchor is primary |
| `h0sh0ku_v3_08_duoheart.png` (`1X4Ou1BdKFiclH-CVO6oI-c1yB-odReAo`) | Name doesn't map to any known anchor or brand term | Whether this is a HOSHOKU pose/motif study (possibly relevant to a humanoid pose) or unrelated |
| `IMG_6052.PNG` (`1R5LLJFkwCE1emjtylYacs3qntAa5ECbw`) | Same real-photo hypothesis, later batch | Whether it adds a new angle or duplicates existing ones |
| 4 UUID-named camera-roll `.jpg` files (`4CCC6E23…`, `14E4CAB4…`, `D61A0780…`, and the duplicate-ID entry) | Same real-photo hypothesis | Same as above |

Nothing from the 59-file inspiration bucket is queued here — per the Drive audit, none of it is asserted by filename to be HOSHOKU-original, so opening it doesn't resolve a production decision the way the files above would. If you know specific ones matter, name them and they'll be added here with their own entry.

---

## The questionnaire

Once you've opened the Priority 1 (and, if needed, Priority 2) files, these 10 questions cover everything this audit needs back. Answer only what you can from what you saw — "didn't check" is a valid answer for any of these.

1. **Which joined-HOSHOKU image should be the primary identity anchor** — `hoshoku_split_stitched_v2.png`, `h0sh0ku_v3_01_split.png`, one of the real-puppet photos, one of the Smart Shot sheets, or something else entirely?
2. **Does an existing reference establish the face clearly enough** (both halves) to build from, or does a new reference need to be generated first?
3. **Does an existing reference establish the seam clearly enough** (path, width, material) to build from?
4. **Does any existing reference show how the seam interacts with the mouth** — or is this confirmed to be a genuine open gap?
5. **Do any existing images (Drive or OpenArt) provide a usable humanoid direction**, even a rough one — or is humanoid form entirely undesigned?
6. **Which existing style should inform the humanoid manifestation** — the claymation/puppet aesthetic already used throughout OpenArt, the real-photo puppet texture, something from the inspiration bucket, or a new direction?
7. **What clothing/outfit direction is appropriate** for the humanoid form — none identified yet, so this is your call to originate, not something to find in the library.
8. **Are the two existing Smart Shot sheets usable as production references**, usable only as design studies, or not usable at all?
9. **Does the mouth need to cross the seam as one system, or read as visually divided** between the two halves — based on what you saw, not a default assumption?
10. **Is a new OpenArt generation actually required**, and if so, which branch of the decision tree in the Drive audit applies (identity gap, humanoid-design gap, turnaround gap, or expression/mouth gap)?

---

No image content was viewed to produce this document. No credits were spent. No generation has been made or scheduled.
