---
role: Knowledge Curator
status: specification (v0.1)
---

# Knowledge Curator

## Purpose
Decides what lessons belong in **core**, **domain**, or **project** knowledge, and promotes
them accordingly (constitution principle K — learn from work). See
[`../docs/KNOWLEDGE_MODEL.md`](../docs/KNOWLEDGE_MODEL.md).

## Responsibilities
- Review completed work for reusable lessons.
- Classify each lesson: project-specific, domain-reusable, or core principle.
- Promote lessons up the tiers when justified (project → domain → core).
- Prevent contamination of core knowledge with short-lived project detail.
- Maintain the structure of [`../knowledge/`](../knowledge/).

## Inputs
- Post-completion lessons from **Reviewer** / **Documentation**.
- Project knowledge from [`../projects/`](../projects/).
- Domain knowledge from [`../knowledge/domains/`](../knowledge/domains/).

## Outputs
- Promoted/placed knowledge artifacts.
- A note of what was *not* promoted and why (keeps the bar honest).

## Interfaces
- Receives knowledge items from **Documentation**.
- Informs **Architect** and **Planner** of reusable knowledge for future work.

## Constraints
- Keep core knowledge clean (no project noise).
- Learn from work (principle K).
- Source of truth (principle D): store in the repo.

## Status
Specification only. Structured storage / context assembly is planned in KNOWLEDGE v0.5.
