---
name: drd-builder
description: Convert an explicitly approved tracking-point draft into a DRD JSON file and validate it against the repository schema. Use only after the user confirms the draft.
---

# DRD builder

## Preconditions

Continue only when the user has explicitly approved the tracking-point draft. If approval is absent or ambiguous, return to `prd-analysis` and ask for confirmation.

## Output

Create `outputs/<requirement>/<requirement>-drd.json` that conforms to `schemas/drd.schema.json`.

For every event, include:

- stable event name and human-readable description
- trigger, valid condition, counting rule, and boundary behavior
- reporting platforms
- implementation owner when known
- properties with type, requirement, description, privacy classification, and example
- legacy mapping only when verified by local metadata
- source references back to the approved draft

Use fictional values for illustrative examples. Do not include real user data, credentials, internal links, document tokens, or unrelated business information.

## Validation

Run:

```bash
python3 scripts/validate_drd.py "outputs/<requirement>/<requirement>-drd.json"
```

Fix every validation error before delivery. Then report the local DRD path, event count, and any remaining `TBD` items.

## Consistency checks

- The DRD event set matches the approved draft.
- Property types and examples agree.
- Required properties have a clear reason.
- Client actions and server outcomes are not merged into one event.
- No private configuration or knowledge-base content is copied into the output.
