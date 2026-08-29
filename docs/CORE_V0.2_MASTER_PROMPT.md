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
├── schema.py             # manifest + state schemas (stdlib dataclasses + inline validation)
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

- **Zero runtime dependencies.** Use only the Python standard library at runtime:
  `json`, `datetime`, `pathlib`, `argparse`, `re`. **Do not** introduce `jsonschema` or
  `pydantic` as runtime dependencies — schema validation in v0.2 is performed with a small
  stdlib check (required keys present, enums in allowed sets, types correct). `pytest` is the
  only acceptable *test* dependency. Keep `requirements.txt` minimal or empty.
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
  "created_at": "2026-08-29T10:00:00Z"
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
    {"stage": "idea", "at": "2026-08-29T10:00:00Z", "by": "Omar"}
  ]
}
```
- **Timestamps are RFC3339 UTC** (suffix `Z`), e.g. `2026-08-29T10:00:00Z`. Generate them
  with `datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")` (stdlib). No local-time or
  naive datetimes.
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
- Writes `state.json` (current_stage=`idea`, status=`todo`, `history` seeded with one entry
  `{stage: idea, at: <RFC3339 UTC>, by: <owner>}`).
- **Refuses** if `<name>` already exists (no silent overwrite — principle: small reversible
  changes; protect existing work).
- **Refuses** if `--classification` is not `public` for the public repo, with a clear message
  about the private workspace.
- **Path-safety (explicit, all must hold or the command refuses):**
  - `<name>` must be a **single path segment** — no slashes (`/` or `\`), no `..`, no `.`,
    no absolute path, no leading/trailing separators.
  - `<name>` must match **kebab-case**: `^[a-z0-9]+(-[a-z0-9]+)*$` (lowercase letters,
    digits, single hyphens, no consecutive hyphens, no leading/trailing hyphen).
  - The final destination `projects/<name>/` must resolve to a path **strictly inside**
    `projects/` after normalization (reject anything that escapes, e.g. `../`, absolute
    paths). Compute `os.path.normpath` and assert the result is under `projects/`.
- Prints the created path.

### `python -m omar_os validate [path]`
Runs the four checks (see §8). Exits non-zero on any failure. Prints a concise report.

### `python -m omar_os stage <project> <stage>`
- **Path-safety on `<project>`** (same rules as `new-project`): `<project>` must be a single
  kebab-case path segment (no slashes, `.`, `..`, absolute paths); its resolved location must
  stay strictly inside `projects/`. Anything else is refused before any file is written.
- Validates `<stage>` is a **legal lifecycle stage** (the closed set from
  [`workflows/project_lifecycle.md`](../workflows/project_lifecycle.md): idea, intake,
  problem_definition, decomposition, research, flow, logic_review, alternatives, decision,
  plan, execution, testing, review, fix, document, lessons, knowledge, complete).
- Appends a history entry and sets `current_stage = <stage>`.
- **Status mapping:** the project's `status` field follows this simple rule —
  - created via `new-project` → `todo`;
  - any `stage` call to a **non-`complete`** stage → `in_progress`;
  - `stage complete` (when allowed) → `done`.
- **Enforces the principle-J review gate:** `stage complete` is **rejected** unless the
  project's `history` already contains a `review` entry (review-vs-objective occurred at
  least once). This applies to **all effort levels** — low/medium/high must all pass review
  before `complete` (per `project_lifecycle.md` effort-scaling fix: no "done" without review).
- **No complex workflow engine.** v0.2 permits transition to any known stage in any order
  except the `complete` gate above. A full transition graph / legal-edge matrix is **deferred
  to v0.3** — do not build it now.

## 7. Lifecycle enforcement rules (from the foundation)
- Low-impact work may compress *analysis* stages but **must still pass `review`** before
  `complete` (no "done" without review).
- **ADR routing is by decision type, not project size** (constitution §6 + `decisions/README.md`):
  ADRs record important/hard-to-reverse **system-level** decisions. Whether a project is
  `low`/`medium`/`high` effort does **not** change that rule. Within a project, `DECISIONS.md`
  records project-specific choices (a one-line note for trivial choices, a fuller entry for
  consequential ones). `stage` does not create ADRs; it only records stage transitions.

## 8. Validator (`validate`) — the four checks

1. **Links**: every Markdown file's internal links (a label in square brackets followed by a
   destination in parentheses) resolve to an existing relative file and, if present, a valid
   `#anchor`. Reuse the approach from the foundation review. Broken link → fail.
2. **Classification boundary** (enforces ADR-0002):
   - **Real project manifests are mandatory**: every `projects/<name>/project.json` MUST
     declare `classification` explicitly (no default/implicit value).
   - **Inside the public repo, `classification` must be `public`.** Any declaration of
     `internal` / `confidential` / `restricted` (or missing `classification`) on an artifact
     living in the public repo is a **validation failure**.
   - The foundation docs themselves are treated as **implicitly `public`** unless a file
     explicitly declares otherwise; validators must not require a `classification` field on
     existing foundation Markdown (only on real `projects/<name>/project.json` manifests and
     on any artifact that chooses to declare one).
   - Scan surface: `projects/` (excluding `_template`), `knowledge/`, `docs/`, `agents/`,
     `workflows/`, `templates/`, `decisions/`. A declared non-`public` classification inside
     the public repo → fail.
3. **Scaffold structure** (single-source rule):
   - `projects/_template/` contains **exactly the 6 markdown files**:
     `PROJECT.md, REQUIREMENTS.md, FLOW.md, DECISIONS.md, TASKS.md, REVIEW.md`.
   - A **real** project under `projects/<name>/` must contain those **same 6 markdown files
     PLUS `project.json` and `state.json`** (8 files total). The two JSON manifests are added
     by `new-project`; they are not part of `_template/`. Missing file → fail.
4. **Manifest/state schema**: every `project.json` and `state.json` validates against the
   §5 schemas; `current_stage` is a legal stage; `effort_level`/`classification` are legal
   enum values. Invalid → fail.

## 9. Acceptance criteria (all must be true for "done")

- [ ] `python -m omar_os new-project demo --effort low` creates `projects/demo/` containing
      the 6 template markdown files (`PROJECT.md, REQUIREMENTS.md, FLOW.md, DECISIONS.md,
      TASKS.md, REVIEW.md`) **plus** `project.json` (classification `public`) and `state.json`
      (current_stage `idea`, status `todo`, one seeded history entry); exits 0.
- [ ] `new-project` **refuses an existing name** (exit non-zero, clear message).
- [ ] `new-project` **path-safety**: refuses `../x`, absolute paths, names with slashes or
      `.`/`..`, and any non-kebab-case id (e.g. `Bad Name`, `a--b`, `-x`); and refuses any
      name whose normalized destination escapes `projects/`.
- [ ] `new-project demo --classification confidential` is **refused** in the public repo
      (exit non-zero, points to private workspace).
- [ ] `python -m omar_os validate` passes on the repo after scaffolding `demo` (0 broken
      links, classification clean, scaffold intact, schemas valid).
- [ ] `validate` **fails** when a `project.json` has `classification: confidential` inside
      the public repo (proves the boundary check works).
- [ ] `validate` **fails** when a scaffold file is deleted from a project.
- [ ] `validate` **fails** when a `projects/<name>/project.json` has **no `classification`**
      field (mandatory on real manifests).
- [ ] `stage demo complete` is **rejected** until `demo` history contains a `review` entry
      (principle J; applies to all effort levels).
- [ ] `stage demo review` then `stage demo complete` succeeds; status transitions
      `todo` → `in_progress` (at first non-complete stage) → `done` (at complete); history
      appended each time.
- [ ] `pytest` runs offline on Windows and **all tests pass**; coverage includes the four
      validator checks + new-project refusal/security paths + stage gate + RFC3339 timestamps.
- [ ] **Zero runtime dependencies** — only Python stdlib (`json`, `datetime`, `pathlib`,
      `argparse`, `re`); no `jsonschema`/`pydantic` at runtime. `pytest` is the only test dep.
- [ ] `tests/README.md` placeholder is replaced by the real suite; old "no tests run" wording
      removed.
- [ ] The implementation PR **updates `README.md`** so it no longer claims "no executable
      software" — documents `omar_os` package, the three commands, and CORE v0.2 status.

## 10. Tests (the first real suite)

Write `tests/` with `pytest`. Minimum cases (each a real assertion, not a stub):

- `test_new_project.py`: creates a project; asserts the 6 template markdown files **plus**
  `project.json` (classification `public`, status `todo`) and `state.json` exist (8 files
  total) with valid JSON; refuses existing name; refuses non-`public` classification in
  public repo; **refuses path-unsafe names** (`../x`, absolute, slashes, `.`/`..`, and
  non-kebab-case ids) and any name whose destination escapes `projects/`.
- `test_validate.py`: passes on a clean scaffolded project (6 md + 2 json); fails on broken
  link injection, on a `confidential` project in public repo, on a missing scaffold file
  (any of the 6 md or the 2 json), on invalid `current_stage`, and on a real manifest
  **missing `classification`**.
- `test_state.py`: `stage` appends history and sets `current_stage`; status transitions
  `todo` → `in_progress` (first non-complete stage) → `done` (complete); `complete` blocked
  before a `review` entry exists; allowed after `review`; timestamps are RFC3339 UTC.
- `test_schema.py`: malformed `project.json`/`state.json` are rejected by the stdlib schema
  check (missing required keys, bad enum, wrong type).

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
   - `docs: replace tests/README placeholder; update ROADMAP/CHANGELOG/README for CORE v0.2`
3. Do **not** merge to `main` automatically. Push `core/v0.2` and open a PR (the PR number is
   assigned by GitHub — **do not hard-code a PR number** in the docs or commits) for review.
4. The PR must include: the package, tests, and doc updates. CI (if any) runs `pytest` +
   `python -m omar_os validate`.
5. **Update `README.md`** in the same PR: after v0.2 lands, the statement that OMAR OS has
   "no executable software" is no longer true — document the new `omar_os` package, the three
   CLI commands, and the CORE v0.2 status. Keep README accurate (constitution principle:
   update docs when implementation behavior changes).
6. Keep `AGENTS.md` updated if behavior changes (constitution principle: update docs when
   implementation behavior changes).

## 12. Definition of "documentation-first preserved"

The package **operates on the existing docs**; it does not replace them. `new-project` uses
`_template/`; `validate` checks the docs' own links and rules. The constitution, ADRs, and
workflows remain the single source of truth — the code enforces them.

---

## Execution hand-off

When you (the coding agent) execute this: begin on branch `core/v0.2`, follow §11, and open
**a PR** (do not hard-code the number). Do not exceed the IN scope. If you find the schema
needs a change, open an ADR (ADR-0004) rather than silently altering ADR-0003's intent.
