# OMAR OS — Project Constitution

**Status:** Adopted — Foundation v0.1
**Date adopted:** 2026-08-29
**Owner:** Omar Hesham Safwat
**Amendment process:** Any change to this document requires an Architecture Decision Record (ADR). See [`decisions/ADR-0001-omar-os-foundation.md`](decisions/ADR-0001-omar-os-foundation.md) and the ADR template ([`templates/decision-template.md`](templates/decision-template.md)).

> This is the **binding rulebook** for OMAR OS. It is the authoritative home for the
> non-negotiable operating principles, the effort-scaling rule, the evidence
> hierarchy, and the decision-traceability requirement.
>
> - *Why* OMAR OS exists → see [`docs/VISION.md`](docs/VISION.md).
> - *How* the system is structured → see [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).
> - *How* work is performed → see [`docs/WORKFLOW.md`](docs/WORKFLOW.md) and [`docs/OPERATING_MODEL.md`](docs/OPERATING_MODEL.md).
> - *What* counts as truth → see [`docs/SOURCE_OF_TRUTH.md`](docs/SOURCE_OF_TRUTH.md).
> - *How* knowledge is organized → see [`docs/KNOWLEDGE_MODEL.md`](docs/KNOWLEDGE_MODEL.md).
> - *Security, secrets, and human gates* → see [`docs/SECURITY.md`](docs/SECURITY.md).

---

## 1. Purpose of this document

OMAR OS is a personal, **model-agnostic AI Operating System**. AI models and tools are
replaceable workers; this constitution and the knowledge it governs are the persistent
system. This document encodes the rules that must hold regardless of which model, agent,
or integration is currently in use.

If any other document in this repository appears to conflict with a principle stated
here, **this document wins** until an ADR explicitly amends it.

## 2. Scope

These rules apply to:

- Every change made to this repository.
- Every AI agent (orchestrator, architect, coder, etc.) operating on Omar's behalf.
- Every project, workflow, and decision recorded in OMAR OS.

## 3. Non-negotiable Operating Principles

These principles are constitutional. They are the single canonical statement of OMAR OS's
operating rules; other documents reference them rather than re-stating them.

| # | Principle | Rule |
|---|-----------|------|
| **A** | **Analyze before execution** | Do not begin implementing a significant task until the problem is understood. |
| **B** | **Flow before complex implementation** | For complex work, create a logical flow or architecture before coding. |
| **C** | **Verify before assume** | Verify what can reasonably be verified. Label every claim as *verified fact*, *inference*, *assumption*, or *opinion/recommendation*. |
| **D** | **Source of truth** | Every project must define its authoritative source(s). |
| **E** | **Evidence hierarchy** | Prefer, in order: (1) original/official source, (2) project source data/docs, (3) reputable secondary source, (4) inference, (5) assumption. |
| **F** | **Decision traceability** | Important decisions must record decision, date, context, alternatives, reason, tradeoffs, and consequences. |
| **G** | **Model agnostic** | No fundamental workflow may depend on a single AI provider. |
| **H** | **Human authority** | Omar is the final authority for important or consequential decisions. |
| **I** | **Human-in-the-loop gates** | External actions with meaningful consequences must support approval gates. |
| **J** | **Review after execution** | Completion is not the end; compare output to the intended result. |
| **K** | **Learn from work** | Reusable lessons move into knowledge/workflow/templates rather than being rediscovered. |
| **L** | **Simplicity** | Prefer the simplest architecture capable of satisfying the requirement. |

### Elaboration

- **A — Analyze before execution.** Analysis is a prerequisite, not a delay. For low-impact
  work a sentence of analysis suffices; for high-impact work use the full decomposition in
  [`docs/WORKFLOW.md`](docs/WORKFLOW.md).
- **C — Verify before assume.** Uncertainty is allowed; *undisclosed* uncertainty is not.
  Always separate what is known from what is guessed.
- **E — Evidence hierarchy.** When sources conflict, the higher tier wins unless a lower
  tier is demonstrably more current and relevant.
- **G — Model agnostic.** Adapters and integrations are interchangeable. The orchestration
  logic must not hard-code a provider. See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).
- **H / I — Human authority & gates.** External, consequential actions (job applications,
  external messages, production changes, data deletion, financial actions) require explicit
  human approval. See [`docs/SECURITY.md`](docs/SECURITY.md).
- **K — Learn from work.** Every completed project should ask: *what here is reusable?*

## 4. Effort-Scaling Principle

The depth of analysis must be **proportional to the importance** of the decision. This is the
single canonical definition; [`docs/WORKFLOW.md`](docs/WORKFLOW.md) shows how it is applied.

| Impact | Required depth |
|--------|---------------|
| **Low** | Quick analysis → decision → validation. |
| **Medium** | Structured analysis → alternatives → execution → review. |
| **High / expensive / hard to reverse** | Full decomposition → evidence collection → flowchart → alternatives → risk analysis → decision record → implementation plan → testing → review → postmortem. |

**Do not over-engineer trivial tasks.**

## 5. Evidence Hierarchy (canonical order)

1. Original / official source
2. Project source data / documentation
3. Reputable secondary source
4. Inference
5. Assumption

## 6. Decision Traceability (required fields for important decisions)

Every important decision record must capture:

- **Decision**
- **Date**
- **Context**
- **Alternatives considered**
- **Reason**
- **Tradeoffs**
- **Consequences**

Captured as ADRs in [`decisions/`](decisions/) using [`templates/decision-template.md`](templates/decision-template.md).

## 7. Source of Truth

GitHub (this repository) is the versioned source of truth. Conversation is an interface;
git is durable memory. Critical project knowledge must eventually be represented as
version-controlled files. See [`docs/SOURCE_OF_TRUTH.md`](docs/SOURCE_OF_TRUTH.md).

## 8. Model-Agnostic Guarantee

No fundamental workflow depends on one AI provider. Current examples of *replaceable
workers* include ChatGPT, Codex, Claude, Gemini, and Qwen — none is required. Future
adapters (local models, browsers, cloud services, MCP tools) must plug in without
rewriting the core philosophy. See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## 9. Amendment

Changes to this constitution are made through an ADR and a coherent commit. The
constitution may evolve, but the *philosophy* (principles A–L, model-agnosticism, human
authority) is intended to be stable across provider and tool changes.

## 10. See also

- [`docs/VISION.md`](docs/VISION.md) — why OMAR OS exists
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — system structure
- [`docs/OPERATING_MODEL.md`](docs/OPERATING_MODEL.md) — thinking vs execution
- [`docs/WORKFLOW.md`](docs/WORKFLOW.md) — the process
- [`docs/KNOWLEDGE_MODEL.md`](docs/KNOWLEDGE_MODEL.md) — knowledge tiers
- [`docs/SOURCE_OF_TRUTH.md`](docs/SOURCE_OF_TRUTH.md) — durable memory
- [`docs/SECURITY.md`](docs/SECURITY.md) — secrets and gates
- [`AGENTS.md`](AGENTS.md) — instructions for coding agents
- [`ROADMAP.md`](ROADMAP.md) — phased plan
