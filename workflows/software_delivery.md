---
workflow: Software Delivery
status: specification (v0.1)
---

# Software Delivery Workflow

Plan → code → test → review → release, specialized from the project lifecycle
([`project_lifecycle.md`](project_lifecycle.md)) for software work. Implements the Coder,
Tester, and Reviewer roles.

## Stages

1. **Plan** (Planner): work packages with acceptance criteria; flag approval gates.
2. **Implement** (Coder): small, reversible commits; follow [`../AGENTS.md`](../AGENTS.md);
   raise an ADR for architecture changes.
3. **Test** (Tester / QA): validate against acceptance criteria; compare to objective.
4. **Review** (Reviewer): fitness-for-purpose, not just "it runs"; confirm decisions logged.
5. **Release / integrate**: merge per git workflow; update docs and changelog.
6. **Lessons**: capture reusables (Knowledge Curator).

## Quality gates

- No secrets committed (principle I / [`../docs/SECURITY.md`](../docs/SECURITY.md)).
- Tests pass (when a suite exists — placeholder in v0.1, see
  [`../tests/README.md`](../tests/README.md)).
- Docs updated when behavior changes.
- Consequential external actions gated by Omar (principle H/I).

## Status

Specification only. The local execution adapter and GitHub adapter that make this
automatable are planned in INTEGRATION v0.4 ([`../ROADMAP.md`](../ROADMAP.md)).
