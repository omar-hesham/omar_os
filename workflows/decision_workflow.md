---
workflow: Decision
status: specification (v0.1)
---

# Decision Workflow

How OMAR OS makes and records important decisions. Implements constitution principle F
(decision traceability) and the ADR system defined in [`../PROJECT_CONSTITUTION.md`](../PROJECT_CONSTITUTION.md) §6.

## When to use

Use a formal decision (ADR) for anything **important or hard to reverse** at the *system*
level: architecture changes, tool/provider selection, process changes. For
**trivial choices**, a sentence in the relevant doc suffices. **Not every project-lifecycle
decision needs an ADR** — see record-types note below.

> **Consequential external actions** (job applications, external messages, production
> changes, data deletion, financial actions) are handled by **approval records**, not ADRs
> (constitution principle I). See the *Record types* section.

## Steps

1. **Frame** the decision: what is being decided and why now?
2. **Gather context** (problem, constraints, stakeholders).
3. **Enumerate alternatives** — at least the status quo and one real alternative.
4. **Compare** using evidence, cost, complexity, risk, reversibility, expected value.
5. **Decide** and record *why* this option.
6. **Record tradeoffs and consequences** (intended and foreseeable).
7. **File the ADR** in [`../decisions/`](../decisions/) using
   [`../templates/decision-template.md`](../templates/decision-template.md).
8. **Link** the ADR from the relevant doc (architecture, project, roadmap).
9. **Set revisit conditions** — when should this decision be re-examined?

## Required ADR fields

- Status, Date, Context, Problem, Decision, Alternatives considered, Why this option,
  Consequences, Risks, Revisit conditions.

(See [`../decisions/ADR-0001-omar-os-foundation.md`](../decisions/ADR-0001-omar-os-foundation.md)
for a worked example and [`../templates/decision-template.md`](../templates/decision-template.md).)

## Record types (kept distinct)

OMAR OS uses **separate record types**; do not mix them in one file:

- **Architecture Decision Records (ADRs)** — in `decisions/`, for important/hard-to-reverse
  *system* decisions (architecture, tooling, process). Use the full template.
- **Project decisions** — in a project's `DECISIONS.md`, for project-specific choices. Link
  an ADR when the choice has system-wide weight.
- **Approval records** — human sign-off on consequential external actions (principle I);
  captured where the action is tracked (e.g. project `TASKS.md` gate), not as an ADR.

This separation prevents ADR bloat and keeps approval evidence auditable.

Consequential decisions require Omar's approval (principle H) and, for external actions, an
approval gate (principle I). See [`../docs/SECURITY.md`](../docs/SECURITY.md).
