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
holds sensitive material. Classification governs *where* an artifact lives.

**Taxonomy (four classes):** `public | internal | confidential | restricted`.

> **`credentials` is a data *type*, not a fifth class.** Credentials (API keys, passwords,
> tokens) are classified **`restricted`** and stored in a **secrets manager** — they are
> never committed to git and are not tracked as a separate classification.

| Class | Examples | Where it lives |
|-------|----------|---------------|
| **public** | code, principles, architecture, workflows, templates, ADRs | public core repo (default; the *only* class allowed in the public repo) |
| **internal** | working drafts, non-sensitive project notes | **private workspace** — explicitly labelled; not for the public repo |
| **confidential** | customer information, contracts, academic/thesis material, business data, PII | **private version-controlled workspace** |
| **restricted** | financial records, personal sensitive data, **credentials** (API keys/passwords/tokens) | **approved secure/encrypted store** — credentials specifically go to a **secrets manager** |

> **Rules:**
> - Only **`public`** is allowed in the public core repo. `internal`/`confidential`/`restricted`
>   must live in the private workspace / secure store.
> - `internal` is an explicitly-labelled, non-sensitive class — it belongs in the private
>   workspace, not the public repo (a future `validate` can treat any non-`public` class in
>   the public repo as a hard error).
> - Confidential and restricted material is referenced from the public repo by
>   pointer/metadata only.
> - **Credentials are `restricted` → secrets manager**; financial/personal records are
>   `restricted` → secure store. Neither goes in git.
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
