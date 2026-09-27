# 6. ÜNDRRARE short-form character comedy system

**Status: framework only.** The beat structure, timing and callback mechanics have to be derived from the Dante grammar (§3.1) and recall mechanism (§3.2), and neither exists yet. What *can* be fixed now is below: the brand constraints, the inputs, and the requirements the format must meet from your brief.

## 6.1 Requirements carried from the brief

The format must have all of these. How each is achieved is `PENDING_DANTE`.

| Requirement | How it's achieved |
| --- | --- |
| Short runtime | Target range from the Dante durations |
| Immediate hook | Hook function and timing from the grammar |
| Recognizable character behavior | Supplied by [`05-character-profiles.md`](05-character-profiles.md) |
| Absurd or comedic premise | Chosen per video. The premise types come from the Dante "variables" table. |
| Fast escalation | Escalation beats from the grammar |
| Concise punchline | Punchline position from the grammar |
| Recurring verbal and product callback | Mechanism from §3.2 |
| Memorable collection phrase | Built from verified on-garment text (§6.3) |
| Product visibility integrated into the story | Product-reveal rule from §3.2 |

## 6.2 Brand constraints (fixed now, from the Brand Bible)

1. **Graphics are reproduced exactly.** Each garment goes to the generator as its own reference image. AI output that redesigns the print is rejected.
2. **No overlay text on the product or the model.** Captions and supers sit clear of both.
3. **No predator/prey or hunting language** in dialogue, captions or on-screen text.
4. **Calm, non-salesy voice**, but the video still has to sell.
5. **Vocabulary:** "Archive Entry", "Artifact" and "Recovered" instead of "Collection", "Product" and "Release" in any branded caption or end card (v1.0 bible). Whether that applies to *spoken dialogue* is an open question.
6. **Tooling order:** use Canva and existing assets first. No generation credits without explicit authorization.
7. **Kept separate:** the HOSHOKU manga canon and the claymation project stay out of this system. This conflicts with the Brand Bible, which files SEEK under HOSHOKU (→ open questions).

## 6.3 Collection language: verified raw material only (Phase 6)

No slogan has been chosen, per the brief. These are the only words that physically exist on the Seek Truth and Seek Reality garments. Any callback line should be traceable to them.

| Word or phrase | Where it's printed | Notes |
| --- | --- | --- |
| `SEEK` | Front of both shirts; back arc of both | Constant across the pair |
| `TRUTH` | Seek Truth front | All caps |
| `Reality` | Seek Reality front | Title case |
| `SEEK` / `REALITY` | Back of **both** shirts, as opposing arcs | Reads differently when rotated 180° |
| `üNDRRARE` | Back arc of both shirts | Brand name, in the art's glyph style |
| `ün` / `dr` | Neck tag | ÜNDR box mark |

Plus the store-copy concepts: "One half of a pair", "The other half", "the morning after [enlightenment]", "look at what's actually there", "not stopping once you have".

The brief asks for a joke that gives the character a reason to repeat, misunderstand, challenge or reinforce SEEK TRUTH and/or REALITY. Each of those four verbs becomes a candidate callback **mode**. Which one or two the system adopts follows from what the Dante mechanism turns out to be.

| Mode | Mechanism it would need |
| --- | --- |
| Repeat | A fixed line, said at a fixed beat |
| Misunderstand | The character mis-reads the garment: wrong word, wrong orientation (§4.3 property 3), or the wrong half of the pair |
| Challenge | The character disputes the word, and the situation proves the word right |
| Reinforce | The situation ends in a moment that literally matches the word |

## 6.4 Product → character → joke mapping (deliverable 10)

Tables for mapping a product and a character to a premise:

1. **Product** (`data/products.json`): name, exact text, placement, pair relation, properties.
2. **Character** (`05-character-profiles.md`): traits, habits, reactions, deadpan register, and what to avoid.
3. **Link**: a trait from (2) is paired with a property from (1). The "Where the product can enter" rows are the starting list.
4. **Premise type**: taken from the Dante variables table (`PENDING_DANTE`).
5. **Callback mode**: one of the modes in §6.3, restricted by what §3.2 finds.
6. **Beat sheet**: filled into the grammar template from §3.1 (`PENDING_DANTE`).

A concept is valid only if every one of these checks passes:

- the callback line uses words from §6.3
- the product text is readable in at least one shot
- the character is recognizable using only the profile's canon traits
- no brand constraint from §6.2 is violated
