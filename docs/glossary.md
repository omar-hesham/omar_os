# Glossary — OMAR OS

> Shared definitions so documents use the same words consistently. If a term is used
> elsewhere, it should match this definition.

| Term | Definition |
|------|------------|
| **OMAR OS** | A personal, model-agnostic AI Operating System; the persistent system for Omar's work. |
| **Model-agnostic** | Not dependent on any single AI provider; providers are interchangeable workers. |
| **Role** | A logical function in the system (e.g. Orchestrator, Architect). Distinct from a model or a person. |
| **Agent** | In this repo, usually shorthand for a *role specification* in `agents/`. Not running software in v0.1. |
| **Adapter** | Code/configuration that connects OMAR OS to a specific model, tool, or service without changing the core. |
| **Core knowledge** | Long-lived principles about how Omar works. See [`KNOWLEDGE_MODEL.md`](KNOWLEDGE_MODEL.md). |
| **Domain knowledge** | Reusable knowledge tied to an area (software, AI, marketing, …). |
| **Project knowledge** | Temporary, project-specific context. |
| **Source of truth** | The authoritative, version-controlled store — this GitHub repository. |
| **ADR** | Architecture Decision Record; a document capturing an important decision (see `decisions/`). |
| **Lifecycle** | The standard sequence of stages a project moves through (see [`WORKFLOW.md`](WORKFLOW.md)). |
| **Approval gate** | A required human checkpoint before a consequential external action (constitution principle I). |
| **Effort-scaling** | Matching analysis depth to decision importance (constitution §4). |
| **Evidence hierarchy** | The preferred order of source reliability: original → project → secondary → inference → assumption. |
| **Specification** | A description of intended behavior; not yet implemented as running software. |
| **Omar** | The human owner and final authority of OMAR OS. |
| **Constitution** | [`../PROJECT_CONSTITUTION.md`](../PROJECT_CONSTITUTION.md) — the binding rulebook. |
