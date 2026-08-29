# Tests — OMAR OS

> **Placeholder (v0.1).** Intentionally minimal.

Reserved for automated tests of OMAR OS software as it is built (CORE v0.2+). In v0.1 the
system is documentation; there is nothing executable to test yet.

## Current state

- No test suite exists. Any claim of "tests passing" would be fabricated — none run.
- The `tests/` directory exists so the structure is ready and so tooling (CI) can be wired
  later without restructuring.

## When tests arrive
- Validate the project manifest schema (CORE v0.2).
- Validate workflow/state representations.
- Validate templates and ADR numbering.
- Independent testing is preferred (Tester / QA role,
  [`../agents/tester.md`](../agents/tester.md)).

## See also
- Roadmap: [`../ROADMAP.md`](../ROADMAP.md) (CORE v0.2, CORE v0.3).
- Workflow: [`../workflows/software_delivery.md`](../workflows/software_delivery.md).
