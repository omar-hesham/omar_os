# Projects — OMAR OS

> Per-project workspaces. Each project is a self-contained folder tracking its own
> requirements, flow, decisions, tasks, and review. The lifecycle is defined in
> [`../docs/WORKFLOW.md`](../docs/WORKFLOW.md) and
> [`../workflows/project_lifecycle.md`](../workflows/project_lifecycle.md).

## Starter

Copy [`_template/`](_template/) to create a new project:

```bash
cp -r _template my-project
```

Then fill in each file per its template.

## Structure of a project

| File | Purpose |
|------|---------|
| [`PROJECT.md`](_template/PROJECT.md) | Purpose, source of truth, owner, constraints, success criteria. |
| [`REQUIREMENTS.md`](_template/REQUIREMENTS.md) | Requirements and acceptance criteria. |
| [`FLOW.md`](_template/FLOW.md) | Logical flow / architecture (Mermaid). |
| [`DECISIONS.md`](_template/DECISIONS.md) | Project-specific decisions (link ADRs where applicable). |
| [`TASKS.md`](_template/TASKS.md) | Task list with status and dependencies. |
| [`REVIEW.md`](_template/REVIEW.md) | Review notes against the objective. |

## Rule

Each project must define its **source of truth** (constitution principle D) in its
`PROJECT.md`.

## Status

The `_template/` is the only project present in v0.1. Real projects (e.g. a Career /
Opportunity Agent) are built later, on top of this OS
([`../ROADMAP.md`](../ROADMAP.md)).
