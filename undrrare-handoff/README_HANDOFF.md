# ÜNDRRARE — Master Handoff Index

**Package built:** 2026-09-04
**Built by:** Claude (Claude Code, remote session), read-only pass
**For:** a receiving Claude Max account with zero prior conversation history

---

## ⚠️ READ THIS BEFORE ANYTHING ELSE

This package was assembled under two hard limitations. Both change how you must
read every other document here.

**1. There was NO conversation history available to the session that wrote this.**
The owner asked for conversation context to be recovered and preserved. That was
not possible — the authoring session began with the handoff request as its first
message and had no prior turns to draw on. **Nothing in this package is a
recovered memory of a past conversation.** Everything here was derived from
primary sources inspected live (see below). Where a document says something is
unrecoverable, that is literal, not hedging.

**2. The ÜNDRRARE Shopify theme Git repository was NOT accessible.**
The authoring session had access to exactly one repo — `5enpai-ai/docs`, an
untouched Mintlify starter kit unrelated to ÜNDRRARE. The real theme code was
read through the **Shopify Admin API (read-only)** instead, which is why this
package can describe the live theme files accurately but cannot describe the
repo's branches, commits, or its two most important documents (`CLAUDE.md` and
`PHASE_3_DISCOVERY.md`, both referenced repeatedly by the theme's own code).

### What was actually inspected (all read-only, nothing modified)

| Source | Status |
|---|---|
| Shopify store `undrrare.shop` — shop info, 68 products, 8 collections, 4 menus, 4 pages, 1 blog, file library | ✅ read live |
| Live MAIN theme `undrrare-theme-phase2-f661bce` — full file list + key file contents | ✅ read live |
| Development theme `Development (912126-penguin)` — the newest work | ✅ read live |
| Brand voice files (`undr-hoshoku-voice` skill + references) | ✅ read in full |
| Audience persona file (`undr-audience.md`) | ✅ read in full |
| ÜNDRRARE theme Git repo (branches, commits, `CLAUDE.md`, `PHASE_3_DISCOVERY.md`) | ❌ not accessible |
| Prior conversation history | ❌ did not exist |

---

## Recommended reading order

| # | Document | Read when |
|---|---|---|
| 1 | **[00_START_HERE.md](00_START_HERE.md)** | First. Always. Orientation + the single most important state summary. |
| 2 | **[09_AGENT_PROTOCOL.md](09_AGENT_PROTOCOL.md)** | Second — read before you touch anything. How to work on this project. |
| 3 | **[06_GUARDRAILS.md](06_GUARDRAILS.md)** | Third. What must not break. Short; read it fully. |
| 4 | **[03_TECHNICAL_STATE.md](03_TECHNICAL_STATE.md)** | Before any code decision. Separates confirmed / planned / incomplete / deprecated. |
| 5 | **[02_WEBSITE_ARCHITECTURE.md](02_WEBSITE_ARCHITECTURE.md)** | Before any homepage or template work. |
| 6 | **[08_SHOPIFY_CONTENT_MAP.md](08_SHOPIFY_CONTENT_MAP.md)** | Before anything touching products, collections, or links. Contains live-broken references. |
| 7 | **[01_BRAND_AND_DESIGN_DNA.md](01_BRAND_AND_DESIGN_DNA.md)** | Before any creative, copy, or visual decision. |
| 8 | **[05_NEXT_TASKS.md](05_NEXT_TASKS.md)** | When you're ready to pick up work. Prioritized P0→P3. |
| 9 | **[04_PHASE_HISTORY.md](04_PHASE_HISTORY.md)** | For context on why things are the way they are. |
| 10 | **[10_DECISION_LOG.md](10_DECISION_LOG.md)** | To avoid re-litigating settled decisions. |
| 11 | **[07_ASSET_INVENTORY.md](07_ASSET_INVENTORY.md)** | Before any asset or media work. |

## Full file list

- `README_HANDOFF.md` — this index
- `00_START_HERE.md` — master orientation
- `01_BRAND_AND_DESIGN_DNA.md` — brand + design source of truth
- `02_WEBSITE_ARCHITECTURE.md` — site architecture as actually built
- `03_TECHNICAL_STATE.md` — technical audit (confirmed/planned/incomplete/deprecated)
- `04_PHASE_HISTORY.md` — phase timeline and reasoning
- `05_NEXT_TASKS.md` — prioritized open task queue
- `06_GUARDRAILS.md` — do-not-break list
- `07_ASSET_INVENTORY.md` — asset inventory
- `08_SHOPIFY_CONTENT_MAP.md` — Shopify data/content map
- `09_AGENT_PROTOCOL.md` — agent operating protocol + reporting format
- `10_DECISION_LOG.md` — decision log

## The first three things you must do

1. **Get the theme Git repo.** Ask the owner for access. Then read `CLAUDE.md`
   and `PHASE_3_DISCOVERY.md` in it — they are the project's real governing
   documents and this package is a substitute for neither.
2. **Read the live code before trusting this package.** See
   `09_AGENT_PROTOCOL.md` rule 4.
3. **Ask the owner to fill the conversation-history gaps** listed at the end of
   `00_START_HERE.md`.
