# Generation access and credit-safe queues

Status: **nothing here is verified.** The connector metadata and the website can disagree, so the website decides. Until you verify, every generative task sits in queue **C** and nothing is submitted.

## What the connector actually told me
- Balance: 1,200 credits, Plus plan, one private workspace.
- `models_explore` flags 14 models `supports_unlim` and reports `unlim.available: false`. Per your note, that is not proof either way.
- A read-only AI-influencer **quote** (no job created, nothing submitted) priced one character sheet at **1.125 credits** and returned **no free-generation count**. So the free pool is unknown, not zero.
- Kling's own account has 0 credits. Kling models are reachable only via Higgsfield.

## The four queues
| Queue | Meaning | What goes in | Rule |
|---|---|---|---|
| **U** Eligible Unlimited | Website shows "Unlimited" for that exact model + resolution + duration + mode | Nothing yet | Move a row here only after you confirm it in the UI |
| **F** Free-generation pool | Website shows a free-gen counter for that surface | Nothing yet | Record the counter and expiry before use |
| **C** Credit-consuming | Anything not confirmed U or F | All generative rows (default) | Needs your explicit approval with an exact cost quote |
| **P** Prep, no generation credits | Writing, indexing, planning, layout in Canva, Drive organisation | Copy, calendars, prompts, shot lists, agency docs | Safe to do now. Caveat: Canva/Adobe/Higgsfield *edit* tools (background removal, upscale, reframe) may cost credits. Verify each before use. |

## Your verification sheet (website only; do not generate)
For each model, write what the generate page shows. Fill in the blanks and send it back.

| Model | Shows "Unlimited"? (Y/N) | Resolution covered | Duration covered | Mode covered (std/pro/4k) | Free-gen counter | Expires (date, time, zone) |
|---|---|---|---|---|---|---|
| Soul 2.0 | | 1.5k / 2k | n/a | | | |
| Nano Banana Pro | | 1k / 2k / 4k | n/a | | | |
| Nano Banana 2 | | | n/a | | | |
| GPT Image 2 | | 1k / 2k / 4k + quality tier | n/a | | | |
| Seedream 5 Pro / 4.5 | | | n/a | | | |
| FLUX.2 | | | n/a | | | |
| Seedance 2.0 | | 480p–4k | 4–15 s | | | |
| Kling 3.0 | | | 3–15 s | std / pro / 4k | | |
| Kling 3.0 Motion Control | | | | std / pro | | |
| Wan 2.7 | | 720p / 1080p | 2–15 s | | | |
| Gemini Omni Flash | | 720p | 4–10 s | | | |
| Character sheet / AI Influencer builder | | | | | | |

Also record: does the credit meter change after one *preview*? (Do not submit to find out. Read the price shown on the button.)

## Pre-flight rule for every generation
1. Row is in U or F, or you have approved the exact credit cost in writing.
2. The price on the button is 0 (or the approved amount).
3. Reference files cited. Prompt matches the board row.
4. After the run, log result, credits before/after, and any failure in `03-FAILURE-LOG.md` (created on first failure).
