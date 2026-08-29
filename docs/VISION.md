# Vision — OMAR OS

> **Why** OMAR OS exists and **what** it aspires to be. The binding rules that govern it
> live in [`../PROJECT_CONSTITUTION.md`](../PROJECT_CONSTITUTION.md); the structure lives in
> [`ARCHITECTURE.md`](ARCHITECTURE.md). This document is motivational and directional.

## The problem

Omar works with many AI models — ChatGPT, Codex, Claude, Gemini, Qwen, and others — plus
automation tools, repositories, and services. Two risks follow:

1. **Knowledge evaporates.** Hard-won thinking, decisions, and lessons live only inside
   chat conversations, which are poor long-term memory.
2. **Vendor lock-in of the mind.** If a model is replaced, the accumulated method and
   context vanish with it.

## The thesis

Make Omar's way of working **persistent and portable**. Store principles, knowledge,
workflows, agent roles, and decisions as version-controlled files. Then any model or tool
can plug in and operate on the same durable system.

```
Omar
  ↓  Principles / Knowledge / Preferences
  ↓  Analysis & Decision System
  ↓  Workflow Orchestrator
  ↓  Specialized AI Agents (roles, not fixed models)
  ↓  Execution Tools
  ↓  Artifacts / Code / Documents / Decisions
  ↓  Review / Learning
  ↺  back into the knowledge system
```

**AI models are replaceable workers. OMAR OS is the persistent system.**

## What it is (and is not)

| It **is** | It is **not** |
|-----------|---------------|
| A model-agnostic operating system for Omar's work | A single chatbot |
| A durable, version-controlled body of knowledge & rules | A prompt collection |
| A framework of roles, workflows, and decisions | An automation script |
| An evolving system (docs now, software later) | A finished product |

## How Omar thinks (summary)

The operating method is a disciplined loop: capture → analyze → decompose → model the flow
→ review logic → enumerate alternatives → decide (and record why) → execute → test → review
against the objective → document → learn. The full, canonical version is in
[`WORKFLOW.md`](WORKFLOW.md); the effort-scaling rule (depth ∝ importance) is in
[`../PROJECT_CONSTITUTION.md`](../PROJECT_CONSTITUTION.md).

## Long-term capabilities (aspirational — NOT built yet)

These are **future capabilities** to leave room for. They are explicitly deferred; nothing
here is implemented in v0.1.

- structured project intake and automatic decomposition
- Mermaid flowchart generation from problem descriptions
- planning, task dependencies, and agent assignment
- approval gates and execution logs
- decision logs and artifact management
- test/review loops and long-term knowledge
- model routing; GitHub integration; local Codex execution
- MCP / tool adapters; external integrations (job portals, CRMs, etc.)
- a user dashboard, scheduling, and monitoring

The first real-world use case likely to be built *on top of* OMAR OS is a **Career /
Opportunity Agent** (discover, score, and prepare applications, with human approval before
external submission). It is a *project built on the OS*, not the core architecture. See
[`ROADMAP.md`](../ROADMAP.md).

## Guiding constraints

- **Model-agnostic:** no workflow depends on one provider (principle G).
- **Human authority:** Omar decides consequential matters (principle H).
- **Simplicity:** the simplest architecture that satisfies the need (principle L).
- **Documentation-first, then executable:** start with the constitution; evolve into
  small, testable, local-first, replaceable software.

## Next

- Structure: [`ARCHITECTURE.md`](ARCHITECTURE.md)
- Operation: [`OPERATING_MODEL.md`](OPERATING_MODEL.md), [`WORKFLOW.md`](WORKFLOW.md)
- Knowledge: [`KNOWLEDGE_MODEL.md`](KNOWLEDGE_MODEL.md)
- Durability: [`SOURCE_OF_TRUTH.md`](SOURCE_OF_TRUTH.md)
- Safety: [`SECURITY.md`](SECURITY.md)
- Plan: [`../ROADMAP.md`](../ROADMAP.md)
