# 09 — Agent Operating Protocol

**This is the most important document in the package after `00_START_HERE.md`.
The sixteen rules below are the owner's own, given verbatim in the handoff
brief. Follow them.**

---

## The sixteen rules

### 1. Read `00_START_HERE.md` first.
Before anything else, every session. It carries the state summary and the honest
account of what is and isn't known.

### 2. Read the remaining documents before making architectural decisions.
Small fixes don't require the whole package. **Architectural decisions do** — and
that includes anything touching the world-token system, the homepage section
structure, the boot/hub components, or how worlds are scoped. At minimum read
`03_TECHNICAL_STATE.md`, `02_WEBSITE_ARCHITECTURE.md`, and `06_GUARDRAILS.md`
first.

### 3. Inspect the actual repository before assuming anything.
Get the theme repo (`05_NEXT_TASKS.md` P0-1) and read `CLAUDE.md` and
`PHASE_3_DISCOVERY.md`. Then read the specific files you're about to change,
including the comments — this codebase's comments carry the reasoning, the bugs
already hit, and the measurements taken.

### 4. Never trust documentation over the current code when they conflict.
**The code wins. Always.** This package is a snapshot taken on 2026-09-04 without
repo access. When you find a conflict: follow the code, then **correct this
package** and say so in your report.

### 5. Preserve the established brand direction.
The palettes, the two-voice separation, the motion register, the copy rules —
these are approved decisions, not defaults awaiting improvement.
`01_BRAND_AND_DESIGN_DNA.md` distinguishes what's established from what's a
recommendation. Respect the line.

### 6. Do not make unnecessary redesigns.
If the task is "fix a broken link," fix the broken link. Do not restyle the
section while you're in there. Unrequested visual change is a violation, not
initiative.

### 7. Do not replace working systems simply because another implementation is technically possible.
Specifically: the `--world-*` token indirection, the progressive-enhancement
model, and the Horizon base. All three would be replaceable with something
"cleaner" and all three would lose real value. See `06_GUARDRAILS.md` §8 for what
was already decided against.

### 8. Prefer small, reversible changes.
The existing work is additive by design — new capability arrives as opt-in
settings that render byte-identically when unset. Match that. One change, verify,
then the next.

### 9. Test desktop / mobile / tablet when relevant.
The breakpoint convention is **749px**. **Tablet (750–1024px) has never been
verified** — the World Hub's `auto-fit / minmax(14rem, 1fr)` produces some column
count there that nobody has looked at. Also test the **no-JS path** and
**`prefers-reduced-motion`**, both of which are load-bearing here.

### 10. Keep Shopify catalog/content changes separate from theme work.
Products, prices, statuses, inventory, collections, template assignment, pages,
and menus are a **separate workstream with separate approval**. Never bundle a
catalog change into a theme deploy. When a task needs both (e.g. the HOSHOKU
template), do them as two deliberate steps and say which is which.

### 11. Before major creative-direction changes, stop and request approval.
Palette changes, new motion, new copy in a brand-facing surface, world-switching
UI, generated assets, product storytelling rewrites. There is already unapproved
copy sitting in a dev template flagged "PENDING APPROVAL" — that's the standard.

### 12. Maintain a structured changelog after each work session.
Use the reporting format below. Keep a running log (in the theme repo, alongside
`CLAUDE.md`) so the next session — or the next agent — can pick up cleanly.

### 13. Never claim something is complete without verifying it.
"Verified" means you looked at the result: rendered the page, checked computed
styles, confirmed the link resolves, saw the product appear. **Not** "the edit
applied without error." This codebase's failure mode is *silent* — see rule 16's
context and `06_GUARDRAILS.md` §9. Nothing errored when three sections rendered
completely the wrong color on the live site.

### 14. Never silently remove existing functionality.
If a change drops a behavior — even one that looks vestigial — say so explicitly
and get agreement. Several things here look vestigial and are not (the doubled
class, the `.shopify-section` qualifier, the `body ` prefix).

### 15. Never overwrite approved assets without documenting why.
The beanie photography, the approved palettes, and the live product copy are
approved material. If something must be replaced, record what, why, and what it
replaced.

### 16. When uncertain, flag the uncertainty instead of guessing.
This project's whole value is that it isn't generic. A confident guess that turns
out generic is worse than a question. Say "I don't know" and ask.

---

## Standard reporting format

**Use this at the end of every work session.** All six headings, every time —
including empty ones, because an empty **ISSUES** section is information.

```
COMPLETED
- What was actually finished, in plain terms.

CHANGED
- Every file touched, with what changed in it.
- Every Shopify object touched (marked clearly as a catalog change).

VERIFIED
- What you actually checked, and how.
- Breakpoints tested. Browsers/devices used.
- What you did NOT verify, stated plainly.

ISSUES
- Anything broken, blocked, or discovered along the way.
- Anything in the handoff package that turned out wrong (rule 4).

DECISIONS NEEDED
- Questions only the owner can answer, each with enough context to answer
  without scrolling back, and a recommendation where you have one.

NEXT RECOMMENDED TASK
- One task. Why it's next. What it depends on.
```

### Notes on using it well

- **VERIFIED is the section people skip and the one that matters most here.**
  Write what you looked at, not what you assume followed. If you didn't check
  mobile, write "mobile not checked."
- **CHANGED must distinguish theme changes from catalog changes** (rule 10). They
  have different risk, different approval, and different rollback.
- **DECISIONS NEEDED should be answerable in one reply.** Give the option set and
  the tradeoff, not an open-ended question.
- **NEXT RECOMMENDED TASK is one task**, not a list. `05_NEXT_TASKS.md` is the
  list.

---

## Session checklist

**Starting:**
1. Read `00_START_HERE.md`.
2. Confirm you have the theme repo, `CLAUDE.md`, and `PHASE_3_DISCOVERY.md`.
3. Check the live vs Development theme state — it was diverged as of 2026-09-04.
4. Read the specific files you'll touch, comments included.

**Working:**
5. One small change at a time.
6. Additive over destructive.
7. Verify visually, not just by absence of error.
8. Stop and ask at any creative-direction fork.

**Finishing:**
9. Report in the format above.
10. Update the changelog.
11. Correct anything in this package that the code proved wrong.
12. Name the one next task.

---

## A note on this project's specific failure mode

Nearly every bug recorded in this codebase's history **failed silently**. Nothing
threw. The site looked fine and was wrong:

- three sections rendered in entirely the wrong palette on the live site
- a world object scrolled to itself instead of its destination
- a CSS rule vanished because of a `*/` inside a comment
- two collection CTAs point at collections that don't exist — **still live today**

The discipline that follows: **verify by looking.** Render the page. Inspect
computed styles. Click the link. "The change applied" is not evidence that the
change worked.
