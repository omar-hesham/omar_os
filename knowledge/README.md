# Knowledge — OMAR OS

> The **three-tier knowledge store** (Core / Domain / Project) plus a **Lessons inbox**.
> The model is authoritative in [`docs/KNOWLEDGE_MODEL.md`](../docs/KNOWLEDGE_MODEL.md).
> This file is the entry point.

## Tiers (the three knowledge stores)

| Tier | Folder | What goes here | Changes |
|------|--------|----------------|---------|
| **Core** | [`core/`](core/) | Long-lived principles: methodology, operating principles, stable preferences, quality standards, decision rules. | Rarely; deliberate + ADR-backed. |
| **Domain** | [`domains/`](domains/) | Reusable knowledge per area (software, AI, marketing, research, thesis, real estate, …). | As areas mature. |
| **Project** | [`../projects/`](../projects/) | Temporary, project-specific context (requirements, decisions, customer info, data). | Per project. |

## Lessons inbox (NOT a tier)

[`lessons/`](lessons/) is a **capture/promotion queue**, not a fourth tier. Raw lessons land
here, then the Knowledge Curator promotes them into Core / Domain / Project. Nothing should
live permanently in `lessons/`.

## Rules

- **Do not contaminate core knowledge with short-lived project detail.**
- Promote lessons: Lessons → Project → Domain → Core (via the Knowledge Curator role).
- Classify sensitive knowledge: confidential/restricted material belongs in a **private
  workspace**, never a public repo (see [`../docs/SECURITY.md`](../docs/SECURITY.md)).
- Store knowledge as version-controlled Markdown. No DB in v0.1 (see ROADMAP KNOWLEDGE v0.5).

## Status

Folders are intentionally seeded with `.gitkeep` and README only. Content grows as projects
complete.
