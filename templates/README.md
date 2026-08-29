# Templates — OMAR OS

> Reusable **master templates**. Use these to create new decisions, workflows, agent specs,
> reviews, and postmortems. The directory [`../projects/_template/`](../projects/_template/)
> is the **single source of truth for project scaffolding** (its `PROJECT.md` plus
> `REQUIREMENTS.md`, `FLOW.md`, `DECISIONS.md`, `TASKS.md`, `REVIEW.md`).
> `project-template.md` in this folder is a **pointer** to that scaffold, not a second copy.

## Contents

| Template | Use for |
|----------|---------|
| [`project-template.md`](project-template.md) | A new project workspace. |
| [`decision-template.md`](decision-template.md) | An Architecture Decision Record (ADR). |
| [`workflow-template.md`](workflow-template.md) | A new workflow document. |
| [`agent-template.md`](agent-template.md) | A new agent role specification. |
| [`review-template.md`](review-template.md) | A review verdict note. |
| [`postmortem-template.md`](postmortem-template.md) | A post-implementation review. |

## Convention

- Templates are filled in, not edited in place. Copy the content into the target location.
- Keep required fields consistent with the constitution
  ([`../PROJECT_CONSTITUTION.md`](../PROJECT_CONSTITUTION.md)).
- Prefer relative links to canonical docs over duplicating their content.
