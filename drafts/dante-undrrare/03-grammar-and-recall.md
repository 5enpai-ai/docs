# 3. Dante video grammar and brand-recall mechanism

**Status: 1 verified video (V01).** The grammar needs a function to appear in ≥ 2 videos, so no timeline can be published yet. §3.3 records V01's structure and recall measurements as a single observation. It is not a template.

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
| Is the repetition what makes the product memorable? | Evidence only: (a) phrase text is identical to or on the product; (b) the phrase is the last line of the joke (the last line before any CTA); (c) the phrase is present in the endings of most videos. It's a conclusion only if all three hold, and otherwise it's reported as undetermined. |

### Leads to test (from search summaries)

- The recurring line may be "You met me at a very Chinese time in my life" (see [`01-source-inventory.md`](01-source-inventory.md) §1.4). Confirmed in V01 (see §3.3)..
- The same text may be printed on the shirt.

If both are confirmed, the questions to answer from footage are these:

- Is the line spoken while the garment text is visible, so the viewer hears and reads the same words at once?
- Does the joke build a situation that "earns" the line? In other words, does the line work as the answer to the scene?
- Is the line identical every time, so it works as a catchphrase, or does the setup change around a fixed line?

These questions frame what gets measured. They are not findings.

## 3.3 V01 "Gym guys": single-video observation

Source: [`data/videos/V01-gym-guys.json`](data/videos/V01-gym-guys.json), inspected by the local session. We don't have timestamps yet, so the beats are in order only.

### Beat order as observed

1. Stereotype list (the hook), delivered as fast voiceover from the first moment
2. Contrast figure: "My supplier in Guangdong…"
3. Deadpan superiority payoff that resolves into the recurring line
4. Recurring line, spoken while the garment print is readable
5. Hard cut to a clean catalog / product-model shot
6. CTA plus link in bio (the final line)

### Recall measurements (from §3.2)

| Question | V01 |
| --- | --- |
| What line is repeated? | "You met me at a very Chinese time in my life." |
| When? | Beat 4 of 6, after the payoff and before the product shot. Timestamp not relayed. |
| Setup, punchline or tag? | Both the punchline and the tag. The Guangdong contrast sets up a reason for "Chinese", and the line then closes the bit. |
| Product before or after the line? | Worn before and during. The garment text is readable *while* the line is spoken, and the dedicated product shot comes *after*. |
| Comedic register | Deadpan / absurdist. A calm assertion of superiority, with no reaction beat described. |
| Reinforcements | At least 3 channels: spoken, printed on the garment, then the isolated product shot. Whether the lower-third captions also show the line isn't stated. |
| Variation across videos | Can't be assessed from one video |
| Is repetition what makes the product memorable? | **Undetermined.** Condition (a) is met: the phrase text is on the product. Condition (b) is met: it's the last line before the CTA. Condition (c), present across most endings, needs more videos. The final line is the CTA, not the phrase. |

### What V01 shows about the mechanism (one video, not yet a rule)

- **The joke gives the product line a reason to exist.** The Guangdong contrast is what makes "Chinese" land, so the garment copy works as the answer to the scene rather than an add-on.
- **Hearing and reading happen at once.** The spoken line and the printed copy are identical and coincide on screen.
- **The ad follows through on the punchline.** The cut to the catalog shot and the CTA come immediately after, so the sell reads as the last beat of the joke.

These three become rules only if later videos repeat them.
