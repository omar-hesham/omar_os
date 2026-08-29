# Source of Truth — OMAR OS

> Why GitHub is the durable memory of OMAR OS, and what must live there. The binding
> requirement is constitution principle D; this document is its authoritative elaboration.

## Principle

> **Conversation is an interface. Git is durable memory.**

Chat conversations must **not** be the only location of critical project knowledge. When a
conversation produces something that matters, it should be represented as a
version-controlled file in this repository.

## GitHub as the versioned source of truth

This GitHub repository is the authoritative, versioned store for OMAR OS. Benefits:

- **Durability** — survives model changes, chat deletions, and session loss.
- **History** — every change is attributable and reversible via git.
- **Collaboration** — multiple agents and Omar can converge on one state.
- **Reviewability** — diffs make changes auditable.

## What should become a file (not just a chat)

| Kind | Where |
|------|-------|
| Principles & operating rules | [`../PROJECT_CONSTITUTION.md`](../PROJECT_CONSTITUTION.md) |
| Architecture | [`ARCHITECTURE.md`](ARCHITECTURE.md) + [`OPERATING_MODEL.md`](OPERATING_MODEL.md) |
| Workflows & processes | [`WORKFLOW.md`](WORKFLOW.md) + [`../workflows/`](../workflows/) |
| Agent role definitions | [`../agents/`](../agents/) |
| Decision records (ADRs) | [`../decisions/`](../decisions/) |
| Project definitions & data | [`../projects/`](../projects/) |
| Reusable templates | [`../templates/`](../templates/) |
| Knowledge (core/domain/lessons) | [`../knowledge/`](../knowledge/) |
| Roadmap & change history | [`../ROADMAP.md`](../ROADMAP.md), [`../CHANGELOG.md`](../CHANGELOG.md) |

## Source-of-truth rule per project

Every project must **define its own authoritative source(s)** (constitution principle D).
A project's `PROJECT.md` (from [`../projects/_template/PROJECT.md`](../projects/_template/PROJECT.md))
states which artifacts are canonical for that project.

## What stays in conversation

Conversation is appropriate for: exploration, drafting, asking questions, and deciding
*what* to persist. But once a decision, principle, or spec is settled, it belongs in the
repo — not only in the chat.

## Exceptions

- **Secrets** never belong in the repo (see [`SECURITY.md`](SECURITY.md)).
- **Large binary artifacts** may reference an external store; the repo holds the pointer
  and metadata.
