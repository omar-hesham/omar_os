# ADR-0001: OMAR OS Foundation (v0.1)

- **Status:** Accepted (ratified on merge of PR #1, 2026-08-29)
- **Date:** 2026-08-29
- **Deciders:** Omar Hesham Safwat (ratified on merge of PR #1, 2026-08-29)

## Context

Omar works across multiple AI models (ChatGPT, Codex, Claude, Gemini, Qwen, …) and wants a
**personal, model-agnostic AI Operating System** that turns his thinking method, decisions,
and accumulated knowledge into a persistent, structured system. The immediate need is a
foundation that encodes *how the system should work* before any software is built, and that
survives the replacement of any individual AI provider.

## Problem

Without a durable structure, Omar's knowledge and method live only in ephemeral chat
conversations and are tied to whichever model is current. The system needs (a) a binding
constitution of operating principles, (b) a clear architecture organized by role and
knowledge tier, (c) a defined workflow/lifecycle, (d) role specifications, (e) an ADR
system, and (f) reusable templates — all without prematurely building a multi-agent
platform.

## Decision

Establish **OMAR OS v0.1 (FOUNDATION)** as a **documentation-first** repository:

- A single binding rulebook: [`PROJECT_CONSTITUTION.md`](../PROJECT_CONSTITUTION.md)
  (principles A–L, effort-scaling, evidence hierarchy, decision traceability).
- A canonical `docs/` set: VISION, ARCHITECTURE, OPERATING_MODEL, WORKFLOW,
  KNOWLEDGE_MODEL, SOURCE_OF_TRUTH, SECURITY, glossary.
- Role-based architecture with **10 roles** (added a Security / Risk Reviewer to reconcile
  the role list with the agent specs).
- A 3-tier knowledge model (Core / Domain / Project) kept strictly separate, with a
  separate **Lessons inbox** for captured-then-promoted lessons.
- The **version-controlled repository** as the source of truth ("git is durable memory");
  GitHub is the current hosting adapter, replaceable (see ADR-0002).
- An ADR system starting with this record.
- Reusable master templates + a `_template` starter project.
- `AGENTS.md` instructing coding agents.

## Alternatives considered

- **A. Build a runtime immediately (multi-agent platform).** Rejected: violates the
  simplicity principle (L) and the "do not over-engineer / documentation-first" guidance;
  premature before the spec exists.
- **B. Store everything in chat / a notes app only.** Rejected: not durable, not
  version-controlled, not model-agnostic, fails the source-of-truth requirement.
- **C. One big monolithic spec file.** Rejected: harms navigability and single-source
  authority; the brief requires a clean directory structure.
- **D. Tie roles to specific model names.** Rejected: violates model-agnosticism (G).

## Why this option

It satisfies every stated requirement (constitution, architecture, knowledge model,
workflow, roles, ADRs, templates, roadmap) while staying minimal, local-first, and
replaceable, and it leaves room for later executable phases without rewriting the
philosophy.

## Consequences

- Positive: a durable, reviewable, model-agnostic foundation; clear ownership of concepts;
  single source of truth per concept.
- Negative / cost: no executable software yet; future phases must implement the specs.
- The constitution and role model are now stable anchors for v0.2+.

## Risks

- Spec/implementation drift: mitigated by `AGENTS.md` (update docs when behavior changes)
  and the Documentation Agent role.
- Over-documentation without execution: mitigated by the explicit phased roadmap and the
  "specification only" status labels on every non-implemented doc.
- Secrets leakage as integrations are added: mitigated by [`../docs/SECURITY.md`](../docs/SECURITY.md)
  and `.gitignore`.

## Revisit conditions

- When v0.2+ introduces a runtime, to confirm the role model still fits.
- If a new provider forces a core change (it should not, by design).
- If the 10-role model proves insufficient or redundant.

## Links

- Constitution: [`../PROJECT_CONSTITUTION.md`](../PROJECT_CONSTITUTION.md)
- Roadmap: [`../ROADMAP.md`](../ROADMAP.md)
- Architecture: [`../docs/ARCHITECTURE.md`](../docs/ARCHITECTURE.md)
- Template: [`../templates/decision-template.md`](../templates/decision-template.md)
