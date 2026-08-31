# Changelog — OMAR OS

All notable changes to this repository are documented here, in reverse chronological order.
Format inspired by Keep a Changelog. For the plan behind these entries, see
[`ROADMAP.md`](ROADMAP.md). For decision rationale, see [`decisions/`](decisions/).

## [0.2.0] — 2026-08-29 — CORE v0.2 Project Core implemented (PR #5)

The first executable slice of OMAR OS (per ADR-0003, ratified by PR #4).

### Added
- `omar_os/` Python package (stdlib only — `json`, `datetime`, `pathlib`, `argparse`,
  `re`, `dataclasses`; no `jsonschema`/`pydantic` at runtime):
  - `constants.py` — paths, classifications, lifecycle stages, kebab-case rule.
  - `schema.py` — `project.json` / `state.json` schemas + inline stdlib validation.
  - `pathutil.py` — shared path-safety (`Path.resolve()` + `is_relative_to()`, never
    `os.path.normpath`).
  - `scaffold.py` — `new-project` copies the single source `projects/_template/`.
  - `state.py` — `stage` transitions with the principle-J review gate + status mapping.
  - `validate.py` — four checks: links, classification boundary, scaffold structure, schema.
  - `__main__.py` — CLI: `new-project` / `validate` / `stage`.
- `tests/` — first real `pytest` suite (`conftest.py` + 4 test modules) replacing the
  placeholder; runs offline via a temp copy of the repo.
- `docs/CORE_V0.2_MASTER_PROMPT.md` — the Master Implementation Prompt that drove this.

### Behavior
- `new-project` refuses existing names, non-`public` classification in the public repo,
  and path-unsafe ids (`../`, absolute, slashes, non-kebab-case).
- `stage complete` is rejected until `review` is in history (principle J).
- `validate` enforces the public-repo classification boundary and 8-file scaffold presence.

### Notes
- LICENSE still pending (see ROADMAP).

### Hardening (from the same PR #5, after review)
Closed six attack-test blockers and added regression tests (suite now 30 tests, all
passing offline on Windows); all within the ADR-0003 scope:
- Validator scans **declared** `classification` in any repo document (project md, docs,
  agents, workflows, templates, decisions, knowledge) and fails non-`public` declarations
  in the public repo (ADR-0002). Prose mentioning classification is not mistaken for a
  declaration, and code-fence examples are ignored.
- A project missing `project.json` / `state.json` / any scaffold file **fails** (a bare
  `project.json` no longer silently passes the 8-file check).
- Malformed JSON in `project.json` / `state.json` yields a structured validation failure
  (no crash).
- Schema hardened: `schema_version` must equal `1.0`; `at` timestamps must match RFC3339
  UTC (`YYYY-MM-DDThh:mm:ssZ`); `source_of_truth` / `success_criteria` / `blockers` must be
  string lists; history `stage`/`at`/`by` are strictly validated.
- `stage <project>` with a traversal/unsafe id raises a clean `StateError` (no traceback).
- `new-project` refuses an incomplete single-source template.
- Test fixture corrected to actually use its temp template copy.

## [0.1.2] — 2026-08-29 — Post-merge consistency (PR #2)

Finalizes statuses and closes residual contradictions flagged after PR #1 merged.

### Changed
- **Statuses finalized**: `PROJECT_CONSTITUTION.md` → **Adopted**; `ADR-0001` and `ADR-0002`
  → **Accepted** (ratified on merge of PR #1).
- **Git ≠ GitHub (remaining spots)**: removed "GitHub is the source of truth" wording from
  `PROJECT_CONSTITUTION.md` §7, `README.md` (high-level architecture), and `docs/ARCHITECTURE.md`
  (diagram node + "Source of Truth" line). Unified phrasing: *version-controlled repository;
  GitHub = current replaceable hosting adapter*.
- **Classification taxonomy unified** (`docs/SOURCE_OF_TRUTH.md`, `docs/SECURITY.md`,
  `decisions/ADR-0002`, `projects/_template/PROJECT.md`): four classes only —
  `public | internal | confidential | restricted`. `credentials` (API keys/passwords/tokens)
  are a *type* of **restricted** data → secrets manager, **not** a fifth class. Only `public`
  is allowed in the public repo; `internal`/`confidential`/`restricted` live in the private
  workspace / secure store.
- **Workflow contradictions fixed** (`workflows/project_lifecycle.md`):
  - Decision stage: important/hard-to-reverse decisions get an ADR; trivial choices get a
    one-line `DECISIONS.md` note (not an ADR every time).
  - Effort scaling: low-impact work may compress analysis but **must still pass stage 13
    (Review vs objective)** before "done".
- **Decision routing** (`decisions/README.md`, `workflows/decision_workflow.md`, `README.md`,
  `PROJECT_CONSTITUTION.md` §6): separated record types — ADRs for important *system-level*
  decisions; project decisions in `DECISIONS.md`; consequential external actions as
  **approval records**, not ADRs. Fixed the dangling `§12` reference (now §6) and the
  malformed ADR index table.
- **Scaffold ownership clarified**: `templates/README.md` and `projects/_template/PROJECT.md`
  now state `_template/` is the **single source** and `project-template.md` is only a pointer.
- Removed "pre-merge" wording from this changelog; reordered entries reverse-chronologically.

### Notes / open items
- Still **no executable software** (intended for v0.1).
- LICENSE pending (see ROADMAP).
- With PR #2, Foundation v0.1 is considered **approved and complete**; CORE v0.2 may begin.

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
