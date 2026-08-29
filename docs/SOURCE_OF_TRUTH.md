# Source of Truth — OMAR OS

> Why a version-controlled repository is the durable memory of OMAR OS, and what must live
> there. The binding requirement is constitution principle D; this document is its
> authoritative elaboration.

## Principle

> **Conversation is an interface. Git is durable memory.**

Chat conversations must **not** be the only location of critical project knowledge. When a
conversation produces something that matters, it should be represented as a
version-controlled file in the repository.

## Repository as the source of truth

The **version-controlled repository** is the authoritative, versioned store for OMAR OS.
GitHub is the *current hosting adapter* and is replaceable — the architecture does not
depend on GitHub specifically (see [`ARCHITECTURE.md`](ARCHITECTURE.md)). Benefits of using
a version-controlled repo:

- **Durability** — survives model changes, chat deletions, and session loss.
- **History** — every change is attributable and reversible via git.
- **Collaboration** — multiple agents and Omar can converge on one state.
- **Reviewability** — diffs make changes auditable.

## Data classification (required)

The public `omar-os` repository is the **public core**; a separate **private workspace**
holds sensitive material. Classification governs *where* an artifact lives. Core repository
paths default to `public`; anything sensitive is kept out of the public repo.

| Class | Examples | Where it lives |
|-------|----------|---------------|
| **public** | code, principles, architecture, workflows, templates, ADRs | public core repo (default) |
| **internal** | working drafts, non-sensitive project notes | public core repo **or** private workspace — must carry an explicit `internal` label; not assumed safe, just non-sensitive |
| **confidential** | customer information, contracts, academic/thesis material, business data, PII | **private version-controlled workspace** (separate private repo or local directory) |
| **restricted** | financial records, personal sensitive data | **approved secure / encrypted private store** (e.g. encrypted volume, private repo with restricted access) |
| **credentials** | API keys, passwords, tokens | **secrets manager only** — never in git |

> **Rules:**
> - `public` is the default for anything already in this repo; `internal/confidential/restricted`
>   artifacts must be **explicitly labelled** and placed per the table above.
> - Confidential and restricted material **must not** be committed to the public repo — store
>   it in the private workspace and reference it by pointer/metadata only.
> - **Financial records are not credentials** — they go to the secure private store, *not* a
>   secrets manager (only API keys/passwords/tokens go to a secrets manager).
> - See [`SECURITY.md`](SECURITY.md) and ADR-0002 for enforcement.

## What should become a file (not just a chat)

| Kind | Where |
|------|-------|
| Principles & operating rules (public) | [`../PROJECT_CONSTITUTION.md`](../PROJECT_CONSTITUTION.md) |
| Architecture (public) | [`ARCHITECTURE.md`](ARCHITECTURE.md) + [`OPERATING_MODEL.md`](OPERATING_MODEL.md) |
| Workflows & processes (public) | [`WORKFLOW.md`](WORKFLOW.md) + [`../workflows/`](../workflows/) |
| Agent role definitions (public) | [`../agents/`](../agents/) |
| Decision records (public) | [`../decisions/`](../decisions/) |
| Project definitions & data (**classified**) | [`../projects/`](../projects/) — or private workspace if confidential |
| Reusable templates (public) | [`../templates/`](../templates/) |
| Knowledge (public parts) | [`../knowledge/`](../knowledge/) — confidential parts in private workspace |
| Roadmap & change history (public) | [`../ROADMAP.md`](../ROADMAP.md), [`../CHANGELOG.md`](../CHANGELOG.md) |

## Source-of-truth rule per project

Every project must **define its own authoritative source(s)** and its classification
(constitution principles D and I). A project's `PROJECT.md`
(from [`../projects/_template/PROJECT.md`](../projects/_template/PROJECT.md)) states which
artifacts are canonical and at what classification.

## What stays in conversation

Conversation is appropriate for: exploration, drafting, asking questions, and deciding
*what* to persist. But once a decision, principle, or spec is settled, it belongs in the
repo (or private workspace) — not only in the chat.

## Exceptions

- **Secrets** never belong in the repo (see [`SECURITY.md`](SECURITY.md)).
- **Confidential / restricted data** (PII, customer info, thesis material, contracts) belong
  in a private workspace, never a public repo.
- **Large binary artifacts** may reference an external store; the repo holds the pointer
  and metadata.
