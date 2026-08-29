# CORE v0.2 — Master Implementation Prompt (Project Core)

> **Purpose.** This is the authoritative implementation brief for CORE v0.2 ("Project Core").
> It is written at Foundation-level precision so a coding agent (Codex, Claude Code, Hermes,
> …) can execute it without re-deciding architecture. It is **not** an open-ended "build
> v0.2" request. Follow it exactly. Scope, schemas, acceptance criteria, tests, and git
> workflow are all specified below.
>
> **Authority.** Constitution [`PROJECT_CONSTITUTION.md`](../PROJECT_CONSTITUTION.md),
> ADR-0002 (public/private, Git ≠ GitHub, single scaffold), and ADR-0003 (this scope) are
> binding. For any conflict, the constitution + ADRs win.

---

## 1. Goal (one sentence)

Make OMAR OS **operable and verifiable** with a minimal, local-first Python package that
creates projects from the single scaffold source, represents project state, and validates
the foundation's own rules — with real automated tests.

## 2. Scope (IN)

- A Python package at `omar_os/` (importable; runnable as `python -m omar_os <cmd>`).
- **Manifest** `project.json` — versioned, declarative project metadata.
- **State** `state.json` — lifecycle stage, status, blockers, transition history.
- **CLI** with exactly **three** commands: `new-project`, `validate`, `stage`.
- **Validator** (`validate`) checking: internal Markdown links, classification boundary,
  scaffold structure, manifest/state schema.
- **Tests** (`pytest`) — the first real test suite in the repo.
- **Single scaffold source**: copies `projects/_template/` only.

## 3. Scope (OUT — do NOT build)

- No agent runtime, no orchestrator, no planner execution (that is v0.3).
- No GitHub adapter, no Codex integration, no network/cloud calls (that is v0.4).
- No knowledge database, no dashboard, no model routing, no MCP.
- No provider SDKs, no `.env`/secrets in the package.
- No fourth CLI command without a new ADR.

## 4. Architecture

```
omar_os/
├── __init__.py
├── __main__.py            # CLI entry: dispatches new-project / validate / stage
├── schema.py             # manifest + state schemas (pydantic OR stdlib dataclasses+jsonschema)
├── scaffold.py           # copies projects/_template/ -> projects/<name>/
├── state.py              # read/write state.json; stage transitions + history
├── validate.py           # the four checks (links, classification, scaffold, schema)
├── constants.py          # paths, classifications, lifecycle stages
└── ...

tests/
├── conftest.py
├── test_new_project.py
├── test_validate.py
├── test_state.py
└── test_schema.py
```

- **No external deps unless justified.** Prefer stdlib; if a schema lib is used, it must be
  installable offline (e.g. `pydantic` is acceptable; a cloud SDK is not). Keep `requirements.txt`
  minimal. If `pytest` is the only test dep, that is fine.
- **Offline + Windows paths**: all file ops use `pathlib.Path`; tests must pass on Windows
  with no network.

## 5. Data schemas

### `project.json` (manifest)
```json
{
  "schema_version": "1.0",
  "id": "kebab-case-project-id",
  "title": "Human readable title",
  "owner": "Omar",
  "effort_level": "low | medium | high",
  "classification": "public",
  "source_of_truth": ["PROJECT.md", "REQUIREMENTS.md"],
  "success_criteria": ["criterion 1", "criterion 2"],
  "created_at": "2026-08-29"
}
```
- `classification` MUST be `public` for anything committed to this public repo
  (ADR-0002 + SOURCE_OF_TRUTH). If a project is `internal`/`confidential`/`restricted`, the
  scaffold tool MUST refuse to create it inside the public repo and tell the user to use the
  private workspace.
- `effort_level` drives default required stages (see §7).

### `state.json`
```json
{
  "schema_version": "1.0",
  "current_stage": "intake",
  "status": "in_progress",
  "blockers": [],
  "history": [
    {"stage": "idea", "at": "2026-08-29T10:00:00", "by": "Omar"}
  ]
}
```
- `current_stage` ∈ the lifecycle stages from
  [`workflows/project_lifecycle.md`](../workflows/project_lifecycle.md)
  (idea, intake, problem_definition, decomposition, research, flow, logic_review,
  alternatives, decision, plan, execution, testing, review, fix, document, lessons,
  knowledge, complete).
- `status` ∈ `todo | in_progress | blocked | done`.
- `history` is append-only; every `stage` command appends an entry.

## 6. CLI commands

### `python -m omar_os new-project <name> [--effort low|medium|high] [--classification public]`
- Copies `projects/_template/` → `projects/<name>/`.
- Writes `project.json` (id=`<name>`, effort_level, classification; default `public`).
- Writes `state.json` (current_stage=`idea`, status=`todo`, empty history with one seed entry).
- **Refuses** if `<name>` already exists (no silent overwrite — principle: small reversible
  changes; protect existing work).
- **Refuses** if `--classification` is not `public` for the public repo, with a clear message
  about the private workspace.
- Prints the created path.

### `python -m omar_os validate [path]`
Runs the four checks (see §8). Exits non-zero on any failure. Prints a concise report.

### `python -m omar_os stage <project> <stage>`
- Validates the target `<stage>` is a legal lifecycle stage.
- Appends to `state.json` history and sets `current_stage`.
- **Enforces** the principle-J gate: you cannot `stage complete` unless
  `current_stage` has passed `review` (review-vs-objective) at least once for `high`/`medium`
  effort. For `low` effort, `review` is still required before `complete` (per
  `project_lifecycle.md` effort-scaling fix).

## 7. Lifecycle enforcement rules (from the foundation)
- Low-impact work may compress *analysis* stages but **must still pass `review`** before
  `complete` (no "done" without review).
- Decision stage: only `high`-effort (and architecturally important `medium`) projects
  require an ADR; `low` gets a one-line `DECISIONS.md` note. `stage` does not create ADRs; it
  only records transitions.

## 8. Validator (`validate`) — the four checks

1. **Links**: every Markdown file's internal links (a label in square brackets followed by a
   destination in parentheses) resolve to an existing relative file and, if present, a valid
   `#anchor`. Reuse the approach from the foundation review. Broken link → fail.
2. **Classification boundary**: scan `projects/` (excluding `_template`), `knowledge/`,
   `docs/`, `agents/`, `workflows/`, `templates/`, `decisions/` for any artifact whose
   declared `classification` is non-`public` while living in the public repo. Also accept a
   declared classification in `project.json` / front-matter; missing classification on a
   project manifest → fail. (Enforces ADR-0002.)
3. **Scaffold structure**: `projects/_template/` contains exactly
   `PROJECT.md, REQUIREMENTS.md, FLOW.md, DECISIONS.md, TASKS.md, REVIEW.md`; each real
   project under `projects/<name>/` contains the same set (single-source rule). Missing file
   → fail.
4. **Manifest/state schema**: every `project.json` and `state.json` validates against the
   §5 schemas; `current_stage` is a legal stage; `effort_level`/`classification` are legal
   enum values. Invalid → fail.

## 9. Acceptance criteria (all must be true for "done")

- [ ] `python -m omar_os new-project demo --effort low` creates `projects/demo/` with all 6
      scaffold files + valid `project.json` + `state.json`; exits 0.
- [ ] `new-project` refuses an existing name (exit non-zero, clear message).
- [ ] `new-project demo --classification confidential` is **refused** in the public repo
      (exit non-zero, points to private workspace).
- [ ] `python -m omar_os validate` passes on the repo after scaffolding `demo` (0 broken
      links, classification clean, scaffold intact, schemas valid).
- [ ] `validate` **fails** when a `project.json` has `classification: confidential` inside
      the public repo (proves the boundary check works).
- [ ] `validate` **fails** when a scaffold file is deleted from a project.
- [ ] `stage demo complete` is **rejected** until `demo` has reached `review` (principle J).
- [ ] `stage demo review` then `stage demo complete` succeeds (history appended both times).
- [ ] `pytest` runs offline on Windows and **all tests pass**; coverage includes the four
      validator checks + new-project refusal paths + stage gate.
- [ ] No network/cloud calls; no provider SDKs; `requirements.txt` minimal.
- [ ] `tests/README.md` placeholder is replaced by the real suite; old "no tests run" wording
      removed.

## 10. Tests (the first real suite)

Write `tests/` with `pytest`. Minimum cases (each a real assertion, not a stub):

- `test_new_project.py`: creates a project; asserts 6 files + valid JSON; refuses existing
  name; refuses non-`public` classification in public repo.
- `test_validate.py`: passes on a clean scaffolded project; fails on broken link injection,
  on a `confidential` project in public repo, on a missing scaffold file, on invalid
  `current_stage`.
- `test_state.py`: `stage` appends history; `complete` blocked before `review`; allowed
  after `review`.
- `test_schema.py`: malformed `project.json`/`state.json` are rejected by the schema loader.

Add a `conftest.py` that builds a temp copy of `projects/_template/` so tests run offline
and don't pollute the real `projects/`.

## 11. Git workflow (execute as the coding agent)

1. Branch from `main`: `core/v0.2`.
2. Coherent commits, e.g.:
   - `feat: add omar_os package skeleton (schema, constants, cli)`
   - `feat: implement new-project scaffold from single source`
   - `feat: implement state + stage transitions with review gate`
   - `feat: implement validate (links, classification, scaffold, schema)`
   - `test: add pytest suite for Project Core`
   - `docs: replace tests/README placeholder; update ROADMAP/CHANGELOG to v0.2`
3. Do **not** merge to `main` automatically. Push `core/v0.2` and open **PR #5** for review.
4. The PR must include: the package, tests, and doc updates. CI (if any) runs `pytest` +
   `python -m omar_os validate`.
5. Keep `AGENTS.md` updated if behavior changes (constitution principle: update docs when
   implementation behavior changes).

## 12. Definition of "documentation-first preserved"

The package **operates on the existing docs**; it does not replace them. `new-project` uses
`_template/`; `validate` checks the docs' own links and rules. The constitution, ADRs, and
workflows remain the single source of truth — the code enforces them.

---

## Execution hand-off

When you (the coding agent) execute this: begin on branch `core/v0.2`, follow §11, and open
**PR #5**. Do not exceed the IN scope. If you find the schema needs a change, open an ADR
(ADR-0004) rather than silently altering ADR-0003's intent.
