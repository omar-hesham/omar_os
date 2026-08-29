# Knowledge — OMAR OS

> The **three-tier knowledge store**. The model (tiers + promotion) is authoritative in
> [`docs/KNOWLEDGE_MODEL.md`](../docs/KNOWLEDGE_MODEL.md). This file is the entry point.

## Tiers

| Tier | Folder | What goes here | Changes |
|------|--------|----------------|---------|
| **Core** | [`core/`](core/) | Long-lived principles: methodology, operating principles, stable preferences, quality standards, decision rules. | Rarely; deliberate + ADR-backed. |
| **Domain** | [`domains/`](domains/) | Reusable knowledge per area (software, AI, marketing, research, thesis, real estate, …). | As areas mature. |
| **Lessons** | [`lessons/`](lessons/) | Captured lessons learned, awaiting promotion to domain/core. | Per completed project. |

## Rules

- **Do not contaminate core knowledge with short-lived project detail.**
- Promote lessons upward (project → domain → core) via the Knowledge Curator role.
- Store knowledge as version-controlled Markdown. No DB in v0.1 (see ROADMAP KNOWLEDGE v0.5).

## Status

Folders are intentionally seeded with `.gitkeep` and README only. Content grows as projects
complete.
