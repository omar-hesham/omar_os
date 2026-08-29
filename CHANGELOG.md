# Changelog — OMAR OS

All notable changes to this repository are documented here, in reverse chronological order.
Format inspired by Keep a Changelog. For the plan behind these entries, see
[`ROADMAP.md`](ROADMAP.md). For decision rationale, see [`decisions/`](decisions/).

## [0.1.0] — 2026-08-29 — FOUNDATION (current)

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
- `knowledge/` — three-tier store (core / domains / lessons) with READMEs.
- `projects/_template/` — starter project (PROJECT, REQUIREMENTS, FLOW, DECISIONS, TASKS,
  REVIEW).
- `decisions/` — ADR-0001 (foundation) + README.
- `templates/` — project, decision, workflow, agent, review, postmortem.
- `config/`, `scripts/`, `tests/` — intentional placeholders with READMEs.
- `.gitignore` — excludes secrets and local artifacts.

### Notes / open items
- **LICENSE: not yet added.** A decision on the appropriate license is pending (see
  ROADMAP). Do not assume distribution terms.
- The 10th role (Security / Risk Reviewer) was added to reconcile the role list in
  `docs/ARCHITECTURE.md` with the agent specs; recorded in ADR-0001.

## [Unreleased]
- LICENSE decision (pending).
- v0.2: structured project manifest, local project-creation tool, workflow/state
  representation, validation.
