# 7. Automation spec (draft v0)

This spec turns one input record into one video concept. The input and output shapes are fixed now. Every field that depends on the Dante analysis has the literal value `PENDING_DANTE` in the schema, and the generator must refuse to run while any of those remain.

Machine-readable versions: [`schema/concept.schema.json`](schema/concept.schema.json) (generator input and output) and [`schema/video-record.schema.json`](schema/video-record.schema.json) (research record).

## 7.1 Pipeline

```
CHARACTER            ← 05-character-profiles.md (id, canon traits, avoid-list)
  ↓
PRODUCT              ← data/products.json (exact text, placements, pair)
  ↓
COLLECTION           ← Ü-002 // SEEK (fixed while this is the target)
  ↓
CHARACTER TRAIT      ← one trait id from the character profile
  ↓
PRODUCT PROPERTY     ← one property id from products.json (§4.3)
  ↓
COMEDIC PREMISE      ← premise type from the Dante variables table   [PENDING_DANTE]
  ↓
BEATS                ← grammar template, one entry per function      [PENDING_DANTE]
  ↓
PRODUCT REVEAL       ← reveal rule from the recall mechanism         [PENDING_DANTE]
  ↓
CALLBACK LINE        ← built only from verified garment words (§6.3)
  ↓
BRAND TAG / ENDING   ← ending structure from the grammar             [PENDING_DANTE]
  ↓
VALIDATION           ← checks in 06-undrrare-system.md §6.4
```

Your conceptual chain went straight from premise to escalation. I kept escalation *inside* BEATS rather than as a fixed stage, because whether escalation is its own stage in the Dante videos is something the analysis has to show.

## 7.2 Input record

```json
{
  "character_id": "killua | zero_two",
  "product_id": "u002-seek-truth-oversized | u002-seek-reality-oversized",
  "colorway": "White | Black | Natural",
  "trait_id": "string (from the character profile)",
  "product_property_id": "pair | front_back_split | rotational_back | casing | seek_constant",
  "premise_type": "PENDING_DANTE",
  "callback_mode": "repeat | misunderstand | challenge | reinforce (subset allowed by §3.2)",
  "batch_seed": "string (for reproducibility)"
}
```

## 7.3 Output record

```json
{
  "concept_id": "string",
  "inputs": { "...": "echo of the input record" },
  "runtime_target_s": "PENDING_DANTE",
  "beats": [
    {
      "function": "PENDING_DANTE (label from the grammar)",
      "start_s": 0,
      "end_s": 0,
      "shot": "framing / camera",
      "action": "string",
      "dialogue": [{ "speaker": "string", "line": "string" }],
      "product_visibility": "none | partial | text_readable",
      "on_screen_text": "string | null (never over the product or model)"
    }
  ],
  "callback": {
    "line": "string — must use only §6.3 words",
    "occurrences": [{ "beat_index": 0, "channel": "spoken | garment | caption" }]
  },
  "ending": "PENDING_DANTE",
  "render_notes": {
    "garment_reference_images": ["one per garment, exact print"],
    "style": "PENDING_DANTE (render style from Dante analysis)",
    "voice": "PENDING_DANTE"
  },
  "validation": {
    "callback_uses_verified_words": true,
    "product_text_readable_in_a_shot": true,
    "character_canon_only": true,
    "no_hunting_or_predator_language": true,
    "no_text_over_product_or_model": true,
    "no_sexualized_framing": true
  }
}
```

## 7.4 Batch rules

- **Batch size:** each batch is a grid of *character × product × trait × property*, with one concept per cell.
- **Near-duplicates:** no two concepts in a batch may share the same `premise_type` and `trait_id`.
- **Callback wording:** it stays identical across a batch *only if* §3.2 finds identical wording in the Dante videos. If it finds variation, the allowed variants are listed and rotated.
- **No auto-generation:** the output is a text concept only. Rendering video is a separate, manually authorized step, because it spends credits. That step runs on **OpenArt**, not Higgsfield.
