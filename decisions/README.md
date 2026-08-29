# Decisions — Architecture Decision Records (ADRs)

> Important decisions are recorded here as **Architecture Decision Records**. This
> implements constitution principle F (decision traceability) and §12 (ADR system).

## What belongs here

Any **important or hard-to-reverse** decision:
- Architecture changes
- Tool / provider / model selection
- Process or workflow changes
- Consequential external actions (with the approval gate, principle I)

## Convention

- Filename: `ADR-<4-digit number>-<short-slug>.md` (e.g. `ADR-0001-omar-os-foundation.md`).
- Number sequentially from `ADR-0001`.
- Use [`../templates/decision-template.md`](../templates/decision-template.md).
- Link the ADR from the relevant doc (architecture, project, roadmap).
- Status values: `Proposed`, `Accepted`, `Deprecated`, `Superseded`.

## Existing records

| ADR | Title | Status |
|-----|-------|--------|
| [`ADR-0001-omar-os-foundation.md`](ADR-0001-omar-os-foundation.md) | OMAR OS foundation (v0.1) | Proposed → Accepted on approval/merge |
| [`ADR-0002-public-private-split.md`](ADR-0002-public-private-split.md) | Public core / private workspace; Git ≠ GitHub; single scaffold source | Proposed |
