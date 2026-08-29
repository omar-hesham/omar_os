# Changelog — OMAR OS

All notable changes to this repository are documented here, in reverse chronological order.
Format inspired by Keep a Changelog. For the plan behind these entries, see
[`ROADMAP.md`](ROADMAP.md). For decision rationale, see [`decisions/`](decisions/).

## [0.1.1] — 2026-08-29 — Foundation review corrections

Correction pass resolving the pre-merge review findings (shipped via PR #1, then ratified
on merge to `main`). Still **documentation-first**; no executable software added.

### Changed (correctness fixes)
- **Public/private data boundary** (merge blocker): added mandatory data classification
  (`public | internal | confidential | restricted`) in `docs/SOURCE_OF_TRUTH.md` and
  `docs/SECURITY.md`; confidential/restricted data (PII, customer info, contracts, thesis
  material, financial) must live in a **private workspace**, never the public repo.
  Formalized in **ADR-0002**.
- **Git ≠ GitHub**: source of truth is now "the version-controlled repository"; GitHub is the
  *current hosting adapter* (replaceable). Fixed in `docs/ARCHITECTURE.md`,
  `docs/SOURCE_OF_TRUTH.md`, `decisions/ADR-0001`.
- **Three-tier knowledge model corrected**: tiers are **Core / Domain / Project**; "Lessons"
  is now an **inbox/promotion queue**, not a tier. Fixed in `docs/ARCHITECTURE.md`,
  `docs/KNOWLEDGE_MODEL.md`, `knowledge/README.md`, `knowledge/lessons/README.md`, ADR-0001.
- **Constitution status**: `PROJECT_CONSTITUTION.md` and `ADR-0001` were set to
  **Draft/Proposed** during review; they are now **Adopted/Accepted** (ratified on merge of
  PR #1, 2026-08-29). See 0.1.2.
- **Evidence hierarchy**: stated once (principle E in the constitution); duplicate listing
  removed.
- **Verify-before-assume**: "label *every* claim" relaxed to "label *material* claims"
  (those affecting a decision); applied in constitution, `research_workflow.md`.
- **Workflow logic**: Review node no longer forks ambiguously to Execution + Fix + Document;
  it routes discrepancy → Fix/Iterate → Execution, pass → Document. Low-impact work still
  requires a review-vs-objective step (constitution principle J).
- **Decision workflow**: clarified ADRs are for *important* decisions only; separated record
  types (ADR vs project decision vs approval record) to prevent ADR bloat.

### Added
- `decisions/ADR-0002-public-private-split.md` — public core / private workspace, Git ≠
  GitHub, single scaffold source.
- `templates/project-template.md` is now a **pointer** to `projects/_template/` (single
  scaffold source; removes the prior duplication/drift).

### Notes / open items
- **LICENSE: not yet added.** Pending decision (see ROADMAP).
- **File naming**: repo mixes kebab-case and snake_case; a normalization is a future cleanup
  (do not block merge). AGENTS.md naming rule to be reconciled later.
- Constitution and ADRs are **Adopted/Accepted** (ratified on merge of PR #1, 2026-08-29).

## [0.1.2] — 2026-08-29 — Post-merge consistency (PR #2)

Finalizes statuses and closes residual contradictions flagged after PR #1 merged.

### Changed
- **Statuses finalized**: `PROJECT_CONSTITUTION.md` → **Adopted**; `ADR-0001` and `ADR-0002`
  → **Accepted** (ratified on merge of PR #1).
- **Git ≠ GitHub (remaining spots)**: removed "GitHub is the source of truth" wording from
  `PROJECT_CONSTITUTION.md` §7, `README.md` (high-level architecture), and `docs/ARCHITECTURE.md`
  (diagram node + "Source of Truth" line). Unified phrasing: *version-controlled repository;
  GitHub = current replaceable hosting adapter*.
- **Classification contract corrected** (`docs/SOURCE_OF_TRUTH.md`, `docs/SECURITY.md`):
  - `public` is the **default** for core-repo paths; sensitive classes must be explicitly
    labelled.
  - `internal` is explicitly a labelled, non-sensitive class (not silently "safe").
  - `confidential` → private version-controlled workspace; `restricted` (incl. financial
    records) → secure/encrypted private store; `credentials` (API keys/passwords/tokens) →
    secrets manager. **Financial records are not credentials** — they do not go to a secrets
    manager.
  - Added `## 2b. Classification` to `projects/_template/PROJECT.md` so every project manifest
    declares its classification.
- **Workflow contradictions fixed** (`workflows/project_lifecycle.md`):
  - Decision stage: important/hard-to-reverse decisions get an ADR; trivial choices get a
    one-line `DECISIONS.md` note (not an ADR every time).
  - Effort scaling: low-impact work may compress analysis but **must still pass stage 13
    (Review vs objective)** before "done".
- **Decision routing** (`workflows/decision_workflow.md`, `README.md`): consequential external
  actions are **approval records**, not ADRs; ADRs are for important system-level decisions.
- **Scaffold ownership clarified**: `templates/README.md` and `projects/_template/PROJECT.md`
  now state `_template/` is the **single source** and `project-template.md` is only a pointer.
- Removed "pre-merge" wording from this changelog.

### Notes / open items
- Still **no executable software** (intended for v0.1).
- LICENSE pending (see ROADMAP).
- With PR #2, Foundation v0.1 is considered **approved and complete**; CORE v0.2 may begin.

## [0.1.0] — 2026-08-29 — FOUNDATION

Documentation-first foundation of OMAR OS. **No executable software yet**; everything is a
specification.

### Added
- `PROJECT_CONSTITUTION.md` — binding operating principles (A–L), effort-scaling, evidence
  hierarchy, decision traceability.
- `AGENTS.md` — instructions for coding agents.
- `README.md` — professional entry point (replaces placeholder).
- `docs/` — VISION, ARCHITECTURE, OPERATING_MODEL, WORKFLOW, KNOWLEDGE_MODEL,
  SOURCE_OF_TRUTH, SECURITY, glossary.
- `agents/` — 10 role specifications (orchestrator, architect, researcher, planner, coder,
  tester, reviewer, documentation, knowledge_curator, security_risk).
- `workflows/` — project_lifecycle, decision_workflow, research_workflow, software_delivery.
- `knowledge/` — three-tier store (core / domain / project) + lessons inbox, with READMEs.
- `projects/_template/` — starter project (PROJECT, REQUIREMENTS, FLOW, DECISIONS, TASKS,
  REVIEW).
- `decisions/` — ADR-0001 (foundation) + README.
- `templates/` — decision, workflow, agent, review, postmortem (+ project pointer).
- `config/`, `scripts/`, `tests/` — intentional placeholders with READMEs.
- `.gitignore` — excludes secrets and local artifacts.

### Notes / open items
- The 10th role (Security / Risk Reviewer) was added to reconcile the role list in
  `docs/ARCHITECTURE.md` with the agent specs; recorded in ADR-0001.

## [Unreleased]
- LICENSE decision (pending).
- v0.2 Project Core: ADR-0002-driven — `new-project` / `validate` / `stage` CLI, single
  scaffold source, `project.json` + `state.json`, classification enforcement.
