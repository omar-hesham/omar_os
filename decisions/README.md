# Decisions — Architecture Decision Records (ADRs)

> Important decisions are recorded here as **Architecture Decision Records**. This
> implements constitution principle F (decision traceability) and the ADR system defined in
> [`../PROJECT_CONSTITUTION.md`](../PROJECT_CONSTITUTION.md) §6 (Decision Traceability).

## What belongs here

ADRs record **important or hard-to-reverse *system-level* decisions** only:

- Architecture changes
- Tool / provider / model selection
- Process or workflow changes

> **Not here:** project-specific choices go in a project's `DECISIONS.md`; consequential
> external actions (job applications, external messages, production changes, data deletion,
> financial actions) are **approval records**, not ADRs (constitution principle I). See
> [`../docs/SECURITY.md`](../docs/SECURITY.md).

## Convention

- Filename: `ADR-<4-digit number>-<short-slug>.md` (e.g. `ADR-0001-omar-os-foundation.md`).
- Number sequentially from `ADR-0001`.
- Use [`../templates/decision-template.md`](../templates/decision-template.md).
- Link the ADR from the relevant doc (architecture, project, roadmap).
- Status values: `Proposed`, `Accepted`, `Deprecated`, `Superseded`.

## Existing records

| ADR | Title | Status |
|-----|-------|--------|
| [`ADR-0001-omar-os-foundation.md`](ADR-0001-omar-os-foundation.md) | OMAR OS foundation (v0.1) | Accepted (ratified 2026-08-29) |
| [`ADR-0002-public-private-split.md`](ADR-0002-public-private-split.md) | Public core / private workspace; Git ≠ GitHub; single scaffold source | Accepted (ratified 2026-08-29) |
