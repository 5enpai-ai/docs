# 3. Dante video grammar and brand-recall mechanism

**Status: derived from 9 verified reels (V01–V09).** The footage was verified by the local Codex research session, and this cloud session didn't view the media. Timing is computed by [`tools/timing_stats.py`](tools/timing_stats.py) from the transcript timestamps and detected cuts in [`data/videos/`](data/videos/).

Transcript timestamps have whole-second resolution, while cut times have hundredth-second resolution.

## 3.1 Dante video grammar (deliverable 6)

### Timed template

Ranges are **min / median / max across the 9 reels**. Functions are aligned by order, not clock time. The bands overlap between reels, but the order never changes.

| # | Function | Starts at (s) | Starts at (% runtime) | What happens | Frequency |
| --- | --- | --- | --- | --- | --- |
| 1 | **Hook**: categorical observation or stereotype about a group | 0 / 0 / 0 | 0 % | Dante speaks the topic line on the first frame. There's no logo, intro card or silence first. | 9/9 |
| 2 | **Specifics**: 2–4 escalating concrete details | 2 / 4 / 5 | ~10–20 % | A list of recognizable markers ($400 lightsaber, Kofola, Mockingjay pin). Sometimes a direct roast line caps it. | 8/9 as a separate beat. In V01 the list is packed into the hook sentence. |
| 3 | **China turn**: supplier / relative, identity, or positive China | 8 / 11 / 17 | 35 / 45 / 56 % | Gives "Chinese" a narrative reason. Most often "my supplier…" does the same thing plainly, "without making it a personality". | 9/9 (type varies, see §2.3) |
| 4 | **Tag**: "You met me at a very Chinese time in my life." | 15 / 18 / 23 | 66 / 70 / 76 % | Last joke line, spoken by Dante while the printed crewneck is visible | 9/9 |
| 5 | **CTA**: "Get yours at childrenofkhan.com. Link in bio." | 18 / 20 / 26 | 73 / 79 / 88 % | Spoken 2–3 s after the tag starts | 9/9 |
| 6 | **End card**: white-background garment/model image with www.childrenofkhan.com | see note | final seconds | Hard cut from the story set to catalog imagery | 9/9 |

Totals:

- **Runtime:** 22.8 / 25.5 / 30.1 s.
- **Shots:** 5 / 5 / 7, with an average shot of 3.8 / 5.0 / 6.0 s. The continuous voiceover carries the pace, not the cutting.
- **Close-out:** the tag, CTA and end card fill the last 6.1 / 7.2 / 8.9 s.

As a proportion, roughly: first ~⅓ of the runtime on hook and specifics, the middle ~⅓ on the China turn, and the last ~⅓ on tag → CTA → end card.

**End-card cut: open detail.** The handoff lists cut times but doesn't say which cut starts the end card.

- In every reel, the last detected cut falls **0.7–1.9 s after the CTA starts** (median 1.2 s).
- In 6/9 reels, a cut also falls between the tag and the CTA (V01, V02, V03, V05, V06, V09).

So the end card may begin before the CTA, or partway through it. That changes how we'd time ours, so I've asked for a per-cut shot label (see [08](08-open-questions.md)).

### Per-reel timing

| ID | Dur (s) | Shots | Avg shot (s) | Specifics | China turn | Tag | CTA | Last cut | Tag % | Tag→end (s) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | 22.83 | 6 | 3.80 | (in hook) | 8 | 15 | 18 | 18.70 | 66 % | 7.8 |
| V02 | 24.23 | 5 | 4.85 | 4 | 11 | 17 | 19 | 20.10 | 70 % | 7.2 |
| V03 | 24.50 | 5 | 4.90 | 5 | 13 | 17 | 19 | 20.37 | 69 % | 7.5 |
| V04 | 26.80 | 5 | 5.36 | 2 | 12 | 18 | 20 | 21.93 | 67 % | 8.8 |
| V05 | 25.90 | 5 | 5.18 | 3 | 14 | 17 | 19 | 20.23 | 66 % | 8.9 |
| V06 | 30.10 | 5 | 6.02 | 5 | 17 | 23 | 26 | 27.73 | 76 % | 7.1 |
| V07 | 28.10 | 7 | 4.01 | 2 | 11 | 21 | 24 | 25.73 | 75 % | 7.1 |
| V08 | 25.10 | 5 | 5.02 | 4 | 11 | 19 | 22 | 22.70 | 76 % | 6.1 |
| V09 | 25.50 | 5 | 5.10 | 2 | 11 | 19 | 22 | 22.80 | 75 % | 6.5 |

### Three sub-templates for the China turn

These are all the same slot, beat 3, filled three ways.

| Sub-template | Reels | Structure of beats 1–3 |
| --- | --- | --- |
| **Supplier comparison** | V01, V02, V04, V06, V08, V09 | "[Group] are / will [verdict]." → specifics (+ optional roast) → "My supplier ['s relative] [in Chinese city] does the same thing, plainly, and never made it a personality." |
| **Identity reversal** | V03, V05 | "[Nationality] will [behavior], then ask 'How did you know I'm [X]?'" → "I don't know, [sis / bro]." + specifics → "Seems cool being [X]. I wish I could be [X], but I can't, because I'm Chinese." |
| **Positive China discovery** | V07 | "Chinese [place] are the best." → enthusiastic specifics → show-and-tell of the Chinese item ("Amazing, right?") |

## 3.2 Brand-recall mechanism (deliverable 5)

### Measurements across V01–V09

| Question from the brief | Finding (9 reels) |
| --- | --- |
| What line gets repeated? | "You met me at a very Chinese time in my life." It's the same sentence printed on Dante's red crewneck. The handoff gives the verbatim spoken tag for V01. For V02–V09 it relays the identical wording as a 9/9 constant, not a per-reel transcript. |
| When does it appear? | At 15–23 s (66–76 % of runtime, median 70 %). It's always the last joke line, and never earlier in the video as a setup. |
| Setup, punchline or tag? | It works as both punchline and tag. The China turn is the setup that makes it land. It isn't the final spoken line: the CTA follows 2–3 s later. |
| Product before or after the line? | Before, during and after. The crewneck is on Dante from the first frame, visible while the tag is spoken, then isolated on the white end card. |
| Comedic register | Deadpan, absurd non-sequitur. Dante states it as though it settles the argument. The phrase itself is a twist on the *Fight Club* line "You met me at a very strange time in my life." |
| How many reinforcements per video? | Three channels: (1) spoken tag; (2) the same words printed on the chest in the same shot; (3) the garment isolated on the end card with the URL. Plus (4) the captions, which run throughout (not confirmed for the tag line specifically). |
| Does the phrase change between videos? | No variation reported: identical in all 9. What changes is the *setup* that earns it. |
| Is the repetition what makes the product memorable? | **Supported.** (a) The tag is identical to the product text. (b) It's the last joke line in 9/9. (c) It's present in every ending. |

### How the mechanism works

The formula has three parts, and all three are present in 9/9 reels:

1. **Earn it.** Each reel builds its own reason for the word "Chinese": a Chinese supplier who does the thing without the ego, a speaker who can't be British because he's Chinese, or a Chinese stationery haul. The topic changes every time, and the China turn is what bends it back toward the fixed line.
2. **Say it where it's printed.** The tag is spoken while the same sentence is visible on Dante's chest. The viewer hears and reads identical words at the same moment, so the shirt *is* the punchline.
3. **Pay it off as merchandise.** A hard cut goes to a clean white catalog image and URL, and the spoken CTA follows. The ad reads as the last beat of the joke, not an interruption, because the product was already the punchline a second earlier.

**Why the line can repeat without going stale:** it's a non-sequitur that fits *any* setup once "Chinese" has been made relevant. The variety lives entirely in the setup, and the payoff stays constant, so repeat viewers learn to anticipate it. That anticipation is the brand-recall hook.

## 3.3 Derivation method (kept for re-runs)

1. **Segment each watched video** into shots (from cut times) and lines (from transcript timestamps).
2. **Label every segment with a function**, using only what's observed.
3. **Merge labels** that describe the same function across videos. Keep a label only if it occurs in ≥ 2 videos.
4. **Align videos by function**, and record each function's start in seconds and as % of runtime.
5. **Publish ranges** as min / median / max with a frequency label. Re-run `python3 tools/timing_stats.py` whenever records are added.
