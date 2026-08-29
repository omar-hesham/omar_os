# Agents — OMAR OS Roles

> This directory defines the **logical roles** of OMAR OS. Each file is a **role
> specification**, *not* running software. In v0.1 one model may perform several roles;
> the roles are stable even as models change.

## Why roles, not model names

OMAR OS is model-agnostic (constitution principle G). We describe *what function* is
needed, not *which model* performs it. This keeps the system working when any provider is
replaced. See [`../docs/ARCHITECTURE.md`](../docs/ARCHITECTURE.md) for the role map.

## The ten roles

| # | Role | File |
|---|------|------|
| 1 | Orchestrator | [`orchestrator.md`](orchestrator.md) |
| 2 | Architect | [`architect.md`](architect.md) |
| 3 | Researcher | [`researcher.md`](researcher.md) |
| 4 | Planner | [`planner.md`](planner.md) |
| 5 | Coder | [`coder.md`](coder.md) |
| 6 | Tester / QA | [`tester.md`](tester.md) |
| 7 | Reviewer | [`reviewer.md`](reviewer.md) |
| 8 | Documentation Agent | [`documentation.md`](documentation.md) |
| 9 | Knowledge Curator | [`knowledge_curator.md`](knowledge_curator.md) |
| 10 | Security / Risk Reviewer | [`security_risk.md`](security_risk.md) |

## How to read a role file

Each role file describes: **purpose**, **responsibilities**, **inputs**, **outputs**,
**interfaces** (which roles it hands off to), **constraints** (which constitution
principles bind it), and **status**. New roles should follow
[`../templates/agent-template.md`](../templates/agent-template.md).

## Caveats

- These are **specifications**. No agent code exists in v0.1 (see
  [`../ROADMAP.md`](../ROADMAP.md), CORE v0.3 for the agent interface).
- Do not assume a role is autonomous or that roles are isolated processes. The workflow in
  [`../docs/WORKFLOW.md`](../docs/WORKFLOW.md) defines how they sequence.
