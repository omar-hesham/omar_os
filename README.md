# OMAR OS

> A personal, **model-agnostic AI Operating System** — turning the way Omar thinks,
> decides, builds, and learns into a persistent, structured system that works with
> *any* AI model or execution tool.

**Current stage:** 🧱 CORE v0.2 — *Project Core (first executable slice).* The repository
contains the constitution, architecture, knowledge model, role and workflow
specifications, project/ADR templates, **and a minimal, local-first Python package**
(`omar_os`) that scaffolds projects, represents project state, and validates the
foundation's own rules. Roles/agents beyond v0.2 are still specifications.

> **Try it locally:** `python -m omar_os new-project <name>` scaffolds a project from the
> single source; `python -m omar_os validate` checks links, classification boundary,
> scaffold structure, and manifest/state schema; `python -m omar_os stage <project> <stage>`
> records lifecycle transitions (enforcing the principle-J review gate). See
> [`docs/CORE_V0.2_MASTER_PROMPT.md`](docs/CORE_V0.2_MASTER_PROMPT.md).

---

## What OMAR OS is

OMAR OS is **not** a chatbot, a prompt collection, or an automation script. It is an
operating system for Omar's work: a durable, version-controlled body of principles,
knowledge, workflows, agent-role definitions, and decisions.

The central idea:

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

## Why it exists

Individual AI models are ephemeral and interchangeable. If ChatGPT, Codex, Claude, Gemini,
Qwen, or any other model is replaced, the system must keep working. OMAR OS makes Omar's
thinking method, standards, and accumulated knowledge survive provider churn by storing
them as durable, version-controlled files rather than only inside chat conversations.

See [`docs/VISION.md`](docs/VISION.md) for the full motivation.

## Core philosophy

The philosophy is encoded as a small set of **non-negotiable operating principles**
(analyze before execution, verify before assume, model-agnostic, human authority, learn
from work, simplicity, and others) plus an **effort-scaling rule**: the depth of analysis
is proportional to the importance of the decision.

These are binding and live in one canonical place:

➡️ **[`PROJECT_CONSTITUTION.md`](PROJECT_CONSTITUTION.md)**

## High-level architecture

OMAR OS is organized around **roles** (not model names) and **layers** (thinking vs
execution), with **three knowledge tiers** (core / domain / project) kept strictly
separate. The **version-controlled repository** is the durable source of truth (GitHub is
the current, replaceable hosting adapter); adapters for specific models, tools, and
services are interchangeable.

```
┌─────────────────────────────────────────────┐
│  Omar (human authority + approval gates)     │
├─────────────────────────────────────────────┤
│  Thinking / Orchestration  (model-agnostic)  │  roles: orchestrator, architect,
│   - analysis, decomposition, review          │         researcher, planner, reviewer
├─────────────────────────────────────────────┤
│  Execution (interchangeable adapters)        │  local Codex, GitHub, browsers,
│   - coding, testing, git, automation         │         MCP tools, cloud services
├─────────────────────────────────────────────┤
│  Knowledge (3 tiers, version-controlled)      │  core / domain / project
│   + a Lessons inbox (promotion queue)         │
├─────────────────────────────────────────────┤
│  Source of Truth: version-controlled repo    │  docs, decisions, projects, config
│   (GitHub = current hosting adapter)          │  git = durable memory
└─────────────────────────────────────────────┘
```

Full detail: ➡️ **[`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)** and
**[`docs/OPERATING_MODEL.md`](docs/OPERATING_MODEL.md)**.

## Project lifecycle

Every project moves through a consistent lifecycle, with feedback loops:

```
IDEA → INTAKE → PROBLEM DEFINITION → DECOMPOSITION → RESEARCH/EVIDENCE
 → FLOW/LOGIC → LOGIC REVIEW → ALTERNATIVES → DECISION → PLAN
 → EXECUTION → TESTING → REVIEW vs OBJECTIVE → FIX/ITERATE
 → DOCUMENT → LESSONS → KNOWLEDGE UPDATE → COMPLETE
```

See ➡️ **[`docs/WORKFLOW.md`](docs/WORKFLOW.md)** for diagrams and the detailed steps.

## How AI agents should work with this repo

Coding agents (Codex, Claude Code, Hermes, etc.) are governed by:

➡️ **[`AGENTS.md`](AGENTS.md)**

In short: read the constitution first, inspect before changing, do not silently change
architecture, record important decisions as ADRs, verify before claiming success, and
never put secrets in the repo.

## Repository structure

```
omar_os/
├── README.md                      # this file (entry point)
├── AGENTS.md                      # instructions for coding agents
├── PROJECT_CONSTITUTION.md        # binding operating principles (canonical)
├── ROADMAP.md                     # phased plan FOUNDATION → AUTOMATION
├── CHANGELOG.md                   # human-readable change history
├── .gitignore
│
├── docs/                          # the canonical system documentation
│   ├── VISION.md  ARCHITECTURE.md  OPERATING_MODEL.md
│   ├── WORKFLOW.md  KNOWLEDGE_MODEL.md  SOURCE_OF_TRUTH.md
│   ├── SECURITY.md  glossary.md
│
├── agents/                        # role SPECIFICATIONS (not running agents)
│   ├── orchestrator.md  architect.md  researcher.md  planner.md
│   ├── coder.md  tester.md  reviewer.md  documentation.md
│   ├── knowledge_curator.md  security_risk.md
│
├── workflows/                     # process specifications
│   ├── project_lifecycle.md  decision_workflow.md
│   ├── research_workflow.md  software_delivery.md
│
├── knowledge/                     # three-tier store (core / domain / project)
│   ├── core/  domains/  lessons/   # lessons/ = promotion inbox, not a tier
│
├── projects/                      # per-project workspaces
│   └── _template/                 # starter project (PROJECT/REQUIREMENTS/FLOW/
│                                  #   DECISIONS/TASKS/REVIEW)
│
├── decisions/                     # Architecture Decision Records (ADRs)
│   └── ADR-0001-omar-os-foundation.md
│
├── templates/                     # reusable master templates
│   ├── project-template.md  decision-template.md  workflow-template.md
│   ├── agent-template.md  review-template.md  postmortem-template.md
│
├── config/  scripts/  tests/      # intentional placeholders (see their READMEs)
```

> **LICENSE:** Not yet added. A decision is pending on the appropriate license. See
> `CHANGELOG.md` and the roadmap. Do not assume distribution terms.

## Getting started (contributors & agents)

1. Read [`README.md`](README.md) (this file), then [`PROJECT_CONSTITUTION.md`](PROJECT_CONSTITUTION.md).
2. Read [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) and [`docs/WORKFLOW.md`](docs/WORKFLOW.md).
3. For any change, follow [`AGENTS.md`](AGENTS.md).
4. For a new project, **use the tool** (preferred): `python -m omar_os new-project <name>`
   scaffolds from [`projects/_template/`](projects/_template/) and writes `project.json` +
   `state.json`. (You may also copy the template manually and add the two JSON files.)
5. After changes, run `python -m omar_os validate` to check links, classification boundary,
   scaffold structure, and manifest/state schema.
6. For any **important or hard-to-reverse** decision, open an ADR using [`templates/decision-template.md`](templates/decision-template.md). Trivial choices get a one-line note in the relevant doc or project `DECISIONS.md`; consequential external actions get an **approval record**, not an ADR (see [`docs/SECURITY.md`](docs/SECURITY.md)).

## Roadmap summary

| Phase | Theme | Headline items |
|-------|-------|----------------|
| **v0.1** | FOUNDATION | constitution, architecture, knowledge model, workflows, agent roles, ADRs, templates ✅ |
| **v0.2** | CORE | **Project Core** ✅ — `omar_os` package: `project.json`/`state.json`, `new-project` / `validate` / `stage` CLI, four-check validator, `pytest` suite (ADR-0003) |
| **v0.3** | CORE | agent interface, orchestrator, planner/executor separation |
| **v0.4** | INTEGRATION | GitHub adapter, local execution adapter, Codex workflow |
| **v0.5** | KNOWLEDGE | structured knowledge storage, lesson promotion, context assembly |
| **v0.6+** | AUTOMATION | external integrations, scheduling, monitoring, approval gates, dashboard/API |

Full plan and rationale: ➡️ **[`ROADMAP.md`](ROADMAP.md)**.

## Status & honesty note

OMAR OS is in **active, phased development**. Foundation v0.1 (documentation) and CORE
v0.2 (the `omar_os` Project Core package) are implemented and tested. Roles/agents, the
GitHub adapter, knowledge services, and automation (v0.3+) remain **specifications** until
their phases land. Do not treat any role, agent, or capability described here as running
code unless its phase's commit says otherwise — see `ROADMAP.md`.

---

*OMAR OS — the persistent system. Models are workers; this is the operating system.*
