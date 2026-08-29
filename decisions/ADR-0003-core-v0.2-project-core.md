# ADR-0003: CORE v0.2 — "Project Core" vertical slice

- **Status:** Accepted (ratified on merge of PR #4, 2026-08-29)
- **Date:** 2026-08-29
- **Deciders:** Omar Hesham Safwat (ratified on approval/merge)
- **Supersedes / relates:** Refines ADR-0002 (public/private split, Git ≠ GitHub, single
  scaffold source). Implements the CORE v0.2 roadmap item.

## Context

Foundation v0.1 is merged and approved (PR #1–#3). It is documentation-only. The next step
is to turn OMAR OS from a doc set into a **minimal, operable core** without over-building.
The independent review concluded the correct v0.2 scope is a single vertical slice —
"Project Core" — not a multi-agent runtime.

The slice must honor the constraints already established: model-agnostic, local-first,
no cloud, no provider SDKs, public repo holds only `public` classification, and
`projects/_template/` is the single scaffold source.

## Problem

How should v0.2 make the foundation operable while staying minimal, testable, and
consistent with the constitution and ADR-0002?

## Decision

Build **CORE v0.2 "Project Core"** as a small Python package (`omar_os/`) that:

1. Defines a **machine-readable project manifest** (`project.json`) and a separate
   **state file** (`state.json`).
2. Provides a **local CLI** (`python -m omar_os <command>`) with exactly three commands:
   `new-project`, `validate`, `stage`.
3. Ships a **repeatable validator** (`validate`) covering: links, classification boundary,
   scaffold structure, and manifest/state schema.
4. Ships **real automated tests** (`pytest`) — the first executable tests in the repo.
5. Uses **`projects/_template/` as the single scaffold source** (no duplication).

Explicitly **out of scope** for v0.2: agent runtime, GitHub adapter, orchestrator, planner
implementation, knowledge database, dashboard, model routing, any network/cloud call.

## Alternatives considered

- **A. Build the orchestrator + agent runtime now (v0.3 scope pulled forward).** Rejected:
  violates "small, testable, local-first" and the simplicity principle (L); premature.
- **B. Start with the GitHub adapter (v0.4).** Rejected: depends on external services;
  contradicts local-first and the not-yet-established manifest.
- **C. No schema, just a scaffolding script.** Rejected: without a manifest/state and a
  validator, the foundation's "git is durable memory" and classification rules can't be
  enforced, and drift returns.

## Why this option

It is the smallest slice that makes the foundation *operable* and *verifiable*: it enforces
the classification boundary and single-source scaffold the reviews fought hard to establish,
and it gives OMAR OS its first real, runnable, tested software — without coupling to any
provider or service.

## Consequences

- Positive: operable core; enforced classification + scaffold rules; first real test suite;
  foundation becomes a working tool, not just docs.
- The CLI is the seam future phases (v0.3 orchestrator, v0.4 adapters) plug into.
- `validate` can later become a CI check.

## Risks

- Over-scoping the CLI (adding commands beyond the three). Mitigated: ADR restricts to
  `new-project` / `validate` / `stage`; anything else needs a new ADR.
- Tests claiming coverage they don't have. Mitigated: tests must actually run and assert;
  `tests/README.md` placeholder is replaced by a real suite.

## Revisit conditions

- When v0.3 begins (orchestrator/planner) — confirm the CLI seam fits.
- If a fourth CLI command is needed — requires a new ADR.
- If the manifest schema needs breaking changes.

## Links

- Foundation: [`ADR-0001-omar-os-foundation.md`](ADR-0001-omar-os-foundation.md)
- Public/private split: [`ADR-0002-public-private-split.md`](ADR-0002-public-private-split.md)
- Master prompt: [`../docs/CORE_V0.2_MASTER_PROMPT.md`](../docs/CORE_V0.2_MASTER_PROMPT.md)
- Roadmap: [`../ROADMAP.md`](../ROADMAP.md) (CORE v0.2)
- Single scaffold source: [`../projects/_template/`](../projects/_template/)
