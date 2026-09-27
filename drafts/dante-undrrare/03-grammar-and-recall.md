# 3. Dante video grammar and brand-recall mechanism

**Status: not derived.** Both sections require watched videos. Writing a timeline or a mechanism now would mean assuming the structure, which the brief rules out. This file defines exactly how each one gets derived, so the result is reproducible and can be checked against the videos.

## 3.1 Grammar derivation method (deliverable 6)

1. **Segment each watched video** into shots, using scene-cut timestamps from `tools/collect_dante.sh`, and into lines, using transcript timestamps.
2. **Label every segment with a function, choosing only from what's observed.** Start with an open label set and don't reuse the example list in the brief. For each segment record what happens (action or line), who drives it, and whether the product or phrase is on screen or spoken.
3. **Merge labels** that describe the same function across videos. Keep a label only if it occurs in ≥ 2 videos.
4. **Align videos by function**, not by clock time. For each function, record its start and end as absolute seconds and as a percentage of runtime.
5. **Publish the timeline** as ranges: min–max across videos, plus the median. Every function carries its frequency label from [`02-dante-format-database.md`](02-dante-format-database.md) §2.4. Optional functions stay marked optional.

Output format (filled only after step 5):

| Order | Function | Start (s) min–median–max | End (s) min–median–max | Frequency | Notes |
| --- | --- | --- | --- | --- | --- |
| — | — | — | — | — | — |

## 3.2 Brand-recall mechanism (deliverable 5)

Each question in the brief maps to one measurement, taken per video and then compared across videos.

| Question from the brief | Measurement |
| --- | --- |
| What line gets repeated? | Exact transcript text for every occurrence, verbatim. Variants are kept separate. |
| When does it appear? | Timestamp and % of runtime for each occurrence |
| Setup, punchline, tag, or all three? | Beat function of the segment where it occurs (from §3.1) |
| Product shown before or after the line? | Product first-on-screen time compared with line time. Also: is the text on the garment readable in-shot at that moment? |
| Comedic register | Delivery label per occurrence: deadpan / sincere / ironic / absurd / shouted / other. Include voice tone and the reaction shot, if any. |
| How many reinforcements? | Count of verbal + on-garment + on-screen-text occurrences per video |
| Does the phrase change between videos? | Diff of the variants across videos |
| Is the repetition what makes the product memorable? | Evidence only: (a) phrase text is identical to or on the product; (b) the phrase is the final line; (c) the phrase is present in the endings of most videos. It's a conclusion only if all three hold, and otherwise it's reported as undetermined. |

### Leads to test (from search summaries, unverified)

- The recurring line may be "You met me at a very Chinese time in my life" (see [`01-source-inventory.md`](01-source-inventory.md) §1.3).
- The same text may be printed on the shirt.

If both are confirmed, the questions to answer from footage are these:

- Is the line spoken while the garment text is visible, so the viewer hears and reads the same words at once?
- Does the joke build a situation that "earns" the line? In other words, does the line work as the answer to the scene?
- Is the line identical every time, so it works as a catchphrase, or does the setup change around a fixed line?

These questions frame what gets measured. They are not findings.
