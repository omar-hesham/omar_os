# Roadmap — OMAR OS

> Phased plan from **FOUNDATION** to **AUTOMATION**. v0.1 (this release) is documentation;
> later phases build the executable system. Each phase should remain small, testable,
> local-first, and replaceable. Phase sequencing may be refined by architecture review, but
> the philosophy (constitution) is stable.

## Philosophy of phasing

1. **Documentation-first, then executable.** The constitution comes before code.
2. **Small, testable, local-first, replaceable.** The first software core must be minimal.
3. **Model-agnostic.** No phase may hard-code a provider (principle G).
4. **Source of truth.** Every phase keeps knowledge in version-controlled files.

## FOUNDATION — v0.1  ✅ (this release)

- [x] Project constitution (`PROJECT_CONSTITUTION.md`)
- [x] Vision & architecture (`docs/`)
- [x] Knowledge model (3 tiers)
- [x] Workflow & lifecycle specification
- [x] Agent role definitions (10 roles)
- [x] ADR system + ADR-0001
- [x] Project & reusable templates
- [x] `AGENTS.md` for coding agents

**Exit criteria:** a new engineer or AI agent can understand the system and where each
concept lives.

## CORE — v0.2

- [ ] Structured **project manifest** (machine-readable project metadata)
- [ ] **Local project-creation tool** (scaffold from `projects/_template/`)
- [ ] **Workflow / state representation** (track lifecycle stage per project)
- [ ] **Validation** (manifest schema, link checks, structure checks)
- [ ] First real tests in `tests/`

**Intent:** make the documentation *operable* locally without external services.

## CORE — v0.3

- [ ] **Agent interface** (a contract a role implementation must satisfy)
- [ ] **Orchestrator** (drives the lifecycle)
- [ ] **Planner / executor separation** (thinking vs execution, per `docs/OPERATING_MODEL.md`)
- [ ] Role implementations begin (initially one model performing several roles)

**Intent:** the roles stop being pure specs and start being invocable.

## INTEGRATION — v0.4

- [ ] **GitHub adapter** (read/write issues, decisions, docs)
- [ ] **Local execution adapter** (run code/tests/git locally)
- [ ] **Codex workflow** (local agent performs coder/tester roles)
- [ ] **MCP / tool adapters** foundation

**Intent:** connect the core to durable storage and execution without coupling.

## KNOWLEDGE — v0.5

- [ ] **Structured knowledge storage** (beyond folders, still local)
- [ ] **Lesson promotion** automation (project → domain → core)
- [ ] **Context assembly** (compile relevant knowledge for a task)

**Intent:** turn captured lessons into reusable, retrieved context.

## AUTOMATION — v0.6+

- [ ] **External integrations** (job portals, CRMs, calendars — e.g. the Career /
      Opportunity Agent built *on top of* OMAR OS)
- [ ] **Scheduling** (deferred/dated work)
- [ ] **Monitoring** (health, drift, review reminders)
- [ ] **Approval gates** (human-in-the-loop enforcement, principle I)
- [ ] **Dashboard / API** (view and drive the system)
- [ ] **Model routing** (choose worker per task, still provider-agnostic)

## Open questions influencing the roadmap

- **LICENSE:** which license fits a personal OS? Pending decision (not in v0.1).
- **Storage:** folders now; structured store in v0.5 — which format?
- **First real project:** likely the Career / Opportunity Agent; built on the OS, not in
  the core.
- **Public/private split (decided in ADR-0002):** the public core repo holds only
  `public`/`internal` artifacts; confidential/restricted data goes to a private workspace.
  v0.2 `validate` should enforce this boundary.
- **File naming:** the repo mixes kebab-case and snake_case; a one-time normalization is a
  future cleanup and does not block merge.

See also: [`PROJECT_CONSTITUTION.md`](PROJECT_CONSTITUTION.md),
[`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md), [`CHANGELOG.md`](CHANGELOG.md).
