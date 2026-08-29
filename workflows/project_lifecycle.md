---
workflow: Project Lifecycle
status: specification (v0.1)
---

# Project Lifecycle Workflow

Detailed companion to the lifecycle in [`../docs/WORKFLOW.md`](../docs/WORKFLOW.md).

## Stages

| # | Stage | Key actions | Gate / output |
|---|-------|-------------|---------------|
| 1 | **Idea** | Capture the seed. | Idea note. |
| 2 | **Intake** | Clarify scope, constraints, owner. | Intake record. |
| 3 | **Problem definition** | State the problem precisely. | Problem statement. |
| 4 | **Decomposition** | Break into components (Architect). | Component list. |
| 5 | **Research / evidence** | Gather sources (Researcher). | Evidence summary. |
| 6 | **Flow / system logic** | Draw the flow with branches/gates. | Mermaid flow. |
| 7 | **Logic review** | Review before building. | Review note → may loop to 3. |
| 8 | **Alternatives** | Enumerate options. | Alternatives list. |
| 9 | **Decision** | Choose + record *why* (ADR). | [`../decisions/`](../decisions/) entry. |
| 10 | **Implementation plan** | Work packages (Planner). | TASKS. |
| 11 | **Execution** | Implement (Coder). | Artifacts + commits. |
| 12 | **Testing** | Validate vs criteria (Tester). | Test report. |
| 13 | **Review vs objective** | Fitness check (Reviewer). | Verdict → may loop to 11. |
| 14 | **Fix / iterate** | Resolve discrepancies. | Updates. |
| 15 | **Document** | Update docs + changelog. | Docs. |
| 16 | **Lessons learned** | Capture reusables. | Lesson notes. |
| 17 | **Knowledge update** | Promote to knowledge tiers. | [`../knowledge/`](../knowledge/) entries. |
| 18 | **Complete** | Close the project. | Done. |

## Effort scaling

Not every project needs all 18 stages. Apply the effort-scaling rule
([`../docs/WORKFLOW.md`](../docs/WORKFLOW.md) §3): low-impact work may stop after stage 9–11;
high-impact work runs the full sequence with an ADR and postmortem.

## Feedback loops

- Logic review (7) → problem definition (3).
- Alternatives (8) → decomposition (4).
- Review (13) → execution (11).
