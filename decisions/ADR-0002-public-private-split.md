# ADR-0002: Public Core / Private Workspace split, Git ≠ GitHub, single scaffold source

- **Status:** Accepted (ratified on merge of PR #1, 2026-08-29)
- **Date:** 2026-08-29
- **Deciders:** Omar Hesham Safwat (recorded; binding on approval/merge)
- **Supersedes / relates:** Refines ADR-0001 (foundation). Addresses the pre-merge review
  findings on data boundary, source-of-truth wording, and scaffold duplication.

## Context

The v0.1 foundation was built with the repository assumed to be the single store for all
knowledge. The pre-merge review (and the public status of `omar-hesham/omar_os`) surfaced
three correctness problems:

1. **Public/private data boundary missing.** Docs direct *customer information* and
   *project data* into `projects/`, while `SECURITY.md` excludes only *secrets*, not PII,
   contracts, academic/thesis material, or business data. A public repo cannot hold those.
2. **Git and GitHub conflated.** "GitHub is the source of truth" was hard-coded even though
   the GitHub adapter is explicitly deferred to v0.4 and not implemented.
3. **Two sources for one scaffold.** `templates/project-template.md` duplicated
   `projects/_template/PROJECT.md`, causing drift and links that break after copying.

## Problem

How should OMAR OS separate public, durable system knowledge from private/sensitive
personal data, without coupling the architecture to one hosting provider, and without
maintaining duplicate scaffolds?

## Decision

1. **Two-store model.**
   - **Public core repository** (`omar-os`): code, constitution, architecture, workflows,
     agent specs, templates, ADRs, roadmap, non-sensitive project *definitions*.
   - **Private workspace** (separate private repo or local directory, not public): personal
     knowledge (Core/Domain that is private), confidential project data, PII, customer
     info, contracts, academic/thesis material, financial data.
2. **Source of truth = version-controlled repository + declared authoritative sources.**
   GitHub is the *current hosting adapter* and is replaceable; the architecture must not
   depend on GitHub. The deferred GitHub adapter (v0.4) is one of several possible hosts.
3. **Data classification is mandatory.** Every artifact carries a class:
   `public | internal | confidential | restricted`. Confidential/restricted never enter a
   public repo. (See [`../docs/SOURCE_OF_TRUTH.md`](../docs/SOURCE_OF_TRUTH.md).)
4. **Single scaffold source.** `projects/_template/` is the only copy-ready project
   starter. `templates/project-template.md` becomes a pointer to it. `new-project` (v0.2)
   copies `_template/` only.

## Alternatives considered

- **A. Keep everything in the public repo.** Rejected: leaks PII/contracts/thesis material;
  violates the new data-classification requirement.
- **B. Make the whole repo private.** Rejected: OMAR OS is meant to be a reusable,
  shareable system skeleton; the public core is valuable and the private parts can live
  separately.
- **C. Hard-code GitHub as the source of truth.** Rejected: contradicts model-agnosticism
  (principle G) and the deferred GitHub adapter; couples the constitution to a vendor.
- **D. Keep both scaffold copies.** Rejected: already caused drift; single source is
  simpler (principle L).

## Why this option

It closes the data-boundary merge blocker, decouples Git from GitHub while keeping "git is
durable memory" intact, and removes a duplication source — all without rewriting the
philosophy or over-engineering.

## Consequences

- Positive: a safe public/private boundary; vendor-agnostic source of truth; no scaffold
  drift.
- The private workspace needs its own lightweight governance (classification, location) —
  documented in `SOURCE_OF_TRUTH.md`; tooling can enforce it in v0.2 (`validate`).
- `projects/` in the public repo holds only non-confidential project *definitions*;
  sensitive project data references the private workspace by pointer.

## Risks

- Forgetting to classify an artifact and committing confidential data to public — mitigated
  by the mandatory classification rule and a planned `validate` check (v0.2) that refuses
  confidential-classed content in the public repo.
- Private workspace falling out of sync — mitigated by treating it as its own versioned
  store with the same "git is durable memory" discipline.

## Revisit conditions

- When the v0.4 GitHub adapter lands (confirm it still treats GitHub as one adapter).
- If a different host (GitLab, self-hosted) is adopted.
- If the private workspace needs its own ADR for governance.

## Links

- Foundation: [`ADR-0001-omar-os-foundation.md`](ADR-0001-omar-os-foundation.md)
- Source of truth (updated): [`../docs/SOURCE_OF_TRUTH.md`](../docs/SOURCE_OF_TRUTH.md)
- Security: [`../docs/SECURITY.md`](../docs/SECURITY.md)
- Roadmap: [`../ROADMAP.md`](../ROADMAP.md) (v0.2 Project Core)
