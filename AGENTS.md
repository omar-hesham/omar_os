# AGENTS.md — Instructions for Coding Agents

> This file is read automatically by coding agents (Codex, Claude Code, Hermes, etc.)
> working inside the OMAR OS repository. It is the operational contract between a human
> or orchestrator and any AI that edits this codebase.

**First, read [`PROJECT_CONSTITUTION.md`](PROJECT_CONSTITUTION.md).** It is the binding
rulebook. When in doubt, the constitution wins.

OMAR OS is a **model-agnostic personal AI Operating System**. You are a replaceable worker;
the persistent system is the repository, its constitution, knowledge, and decisions — not
any single model. See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) and
[`README.md`](README.md) for orientation.

---

## 1. Before you change anything

1. **Inspect the repository first.** Understand the current structure, existing
   architecture, and prior decisions before proposing changes.
2. **Read the constitution** ([`PROJECT_CONSTITUTION.md`](PROJECT_CONSTITUTION.md)).
3. **Read relevant decisions** in [`decisions/`](decisions/) — an ADR may already have
   resolved the question you are about to raise.
4. **Understand the problem** before implementing it. Principle A
   (*analyze before execution*) applies to you.

## 2. Working with architecture

- **Do not silently change architecture.** The structure in
  [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) is intentional.
- For any **important** architecture change, create or update an **ADR** in
  [`decisions/`](decisions/) using [`templates/decision-template.md`](templates/decision-template.md).
- Prefer **small, reversible changes**. Avoid large, irreversible rewrites without prior
  agreement and an ADR.
- Preserve compatibility unless a change is intentionally breaking — and if it is,
  document it in the ADR and the [`CHANGELOG.md`](CHANGELOG.md).

## 3. Quality and verification

- **Run relevant tests** before claiming done. (In v0.1 the test suite is a placeholder;
  see [`tests/README.md`](tests/README.md). Do not invent passing tests.)
- **Do not claim success without verification.** State what you actually did and what you
  actually observed.
- Distinguish *verified fact*, *inference*, *assumption*, and *opinion* (principle C).
- Keep commits **coherent**: one logical change per commit, with a clear message.

## 4. Documentation and knowledge

- **Update documentation when implementation behavior changes.** Stale docs are bugs.
- Avoid duplicated documentation. Each concept has **one primary authoritative location**
  (the constitution, an architecture doc, or a decision); other docs *link* to it.
- **Document assumptions** explicitly when you cannot verify something.
- Lessons worth keeping should move into [`knowledge/`](knowledge/) (see
  [`docs/KNOWLEDGE_MODEL.md`](docs/KNOWLEDGE_MODEL.md)), not be rediscovered each time.

## 5. Safety and respect

- **Never overwrite meaningful user work** without justification and, for consequential
  changes, an approval gate (principles H and I).
- **Never put secrets or API keys** in the repository. See [`docs/SECURITY.md`](docs/SECURITY.md).
- Treat other agents' work and configs with respect; do not edit files owned by other
  agents unless explicitly asked.

## 6. Reporting

- **Report blockers explicitly.** If you cannot proceed, say so — do not fabricate output
  or pretend a feature exists.
- Distinguish clearly between what is **implemented** and what is **specified but not yet
  built**.
- Leave the repository in a coherent state: consistent docs, working links, no dangling
  references.

## 7. Conventions

- Use **Markdown** for all docs. Use **relative links** between documents.
- Use **Mermaid** for diagrams where it aids understanding.
- Use consistent naming (kebab-case for files, `UPPERCASE` for root constants).
- Mark intentionally deferred work with a `TODO` and a link to the relevant
  [`ROADMAP.md`](ROADMAP.md) item.

---

*This file is part of the OMAR OS foundation (v0.1). It is documentation, not running
software; the workflows it describes are specifications until a later phase implements them.*
