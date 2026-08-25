---
name: prd-analysis
description: Analyze a PRD and produce business questions, metrics, funnels, and a draft tracking-point table for user review. Use as the analysis stage before a DRD is generated.
---

# PRD analysis

Create `outputs/<requirement>/analysis.md` with the following sections:

1. Business goal
2. Scope and user flow
3. Analysis questions
4. Metrics or funnel
5. Tracking-point draft
6. Open questions and assumptions

## Tracking-point draft

Use this table:

| # | Behavior | Trigger | Proposed event | Properties | Platform | Purpose | Evidence |
|---|---|---|---|---|---|---|---|

Rules:

- Each row must answer at least one analysis question.
- The trigger must be observable and testable.
- Prefer reusing a semantically equivalent event or property when local metadata proves equivalence.
- Do not treat a similar name as proof of equivalent meaning.
- Do not create a property that repeats information already encoded in the event name.
- Keep client actions separate from server-confirmed outcomes.
- Group multiple fields that describe one business object into a structured object when that improves consistency.
- Mark unsupported details as `TBD`; never invent them.

## Naming

When the local project uses a six-segment convention, compose:

```text
{app}_{domain}_{page}_{module}_{element}_{action}
```

Use the configured missing-segment value when a segment does not apply. New names must come from the local naming taxonomy or be clearly marked as proposed additions.

## Finish condition

Present the draft and stop. Ask for explicit confirmation or corrections. Do not invoke `drd-builder` yet.
