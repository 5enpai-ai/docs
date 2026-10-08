# Production board v0.2 (supersedes v0.1)

**Queue:** U = verified unlimited, F = verified free pool, C = credit-consuming (needs your approval + quote), P = prep, no generation credits. Nothing is U or F until you verify on the website (`03-GENERATION-ACCESS.md`).
**Who:** ME = I can finish it, YOU-HF = you operate Higgsfield manually, YOU-OK = needs your decision.
**Status:** READY (can start now), PREPPED (my part done, waiting on you), BLOCKED(reason).

Execution order per your instruction: 1 tracker, 2 influencer, 3 HOSHOKU references, 4 Beanie 2.0, 5 5ENPAI, 6 PROJKT OBJKT. All run in parallel on the prep side.

| ID | Brand | Deliverable | Who | Queue | Refs / inputs | Target model (verify) | Format | Tests | Status | Output / doc |
|---|---|---|---|---|---|---|---|---|---|---|
| X-01 | All | Audit + tracker | ME | P | — | — | md | — | DONE | `00`, `02`, `03` |
| I-01 | Influencer | Provisional spec (moth/stag lane) | ME | P | Your direction | — | md | — | PREPPED (needs D6–D8) | `05-INFLUENCER.md` |
| I-02 | Influencer | Reference prompts IR-01..07 | ME | P | I-01 | — | prompts | — | PREPPED | `05` |
| I-03 | Influencer | Master ref sheet generation | YOU-HF | C | I-02 | Soul 2.0 / Nano Banana Pro | 3:4 | IT-01..03 | BLOCKED(access check, D6) | Drive `/Sprint/Influencer/` (not created) |
| I-04 | Influencer | Identity lock (Element or Soul) | YOU-HF | C | Approved hero | Soul 2.0 | — | — | BLOCKED(I-03) | — |
| I-05 | Influencer | 3 launch videos | YOU-HF | C | I-04 | Seedance 2.0 / Kling 3.0 | 9:16, 6–10 s | IT-04/05 | BLOCKED(I-04) | `05` LV-1..3 |
| I-06 | Influencer | 20-concept backlog, captions, measurement plan | ME | P | I-01 | — | md | — | DONE | `05` |
| H-01 | HOSHOKU | Reference recovery | YOU-OK | P | Drive candidates | — | — | — | PREPPED (your selection) | `04`, `11` |
| H-02 | HOSHOKU | Controlled identity tests HT-01..03 | YOU-HF | C | H-01 anchor | Nano Banana Pro / Seedream 5 Pro | 9:16 | 3 | BLOCKED(H-01, access) | `07` |
| H-03 | HOSHOKU | Motion concepts (6) | YOU-HF | C | H-02 pass | Seedance 2.0 / Kling 3.0 | 9:16, 5 s | HT-04 | BLOCKED(H-02) | `07` |
| H-04 | HOSHOKU | Repeatable formats and dialogue | ME | P | Canva Style Guide | — | md | — | DONE (voice DRAFT) | `07` |
| B-01 | ÜNDRRARE | Beanie shot list, prompts, copy | ME | P | Shopify facts | — | md | — | DONE | `06` |
| B-02 | ÜNDRRARE | Real beanie photos selected | YOU-OK | P | CONTENT DUMP / Photo gallery | — | — | — | PREPPED (your file picks) | `11` |
| B-03 | ÜNDRRARE | AI motion/background plates | YOU-HF | C | B-02 | Seedance 2.0 / Nano Banana Pro | 9:16 / 3:4 | — | BLOCKED(B-02, access) | `06` |
| B-04 | ÜNDRRARE | Made-to-order lead time | YOU-OK | P | — | — | — | — | BLOCKED(D11) | — |
| F-01 | 5ENPAI | Content kit (templates, captions) | ME | P | Palette names | — | Canva | — | PREPPED (fonts D9, hexes D12) | `08` |
| F-02 | 5ENPAI | Reality→anime test on your clip | YOU-HF | C | Your clip | Seedance 2.0 / Kling 3.0 MC | 9:16 | 1 | BLOCKED(clip, access) | `08` |
| P-01 | PROJKT OBJKT | Positioning, service copy, outreach drafts | ME | P | Your definition | — | md | — | DONE (placeholders) | `09` |
| P-02 | PROJKT OBJKT | Service graphics, rate card | ME | P | Brand basics D14 | — | Canva | — | BLOCKED(logo/colours/fonts) | `09` |
| X-02 | All | Calendar | ME | P | — | — | md | — | DONE (draft) | `10` |
| X-03 | All | Failure log | ME | P | — | — | md | — | Created on first failure | `03-FAILURE-LOG.md` |

## Rules
- No row moves to U or F without your website confirmation.
- No publish, no store edits, no source overwrites, no paid credits without explicit approval and a quote.
- Cite the reference used on every generation. Log every failure with cause.
- Final wordmarks and copy are composited in Canva; generation never draws text on products.
