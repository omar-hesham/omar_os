# tests/

The first real automated test suite for OMAR OS (introduced in CORE v0.2).

Run with:

```bash
pytest
```

## Layout

- `conftest.py` — builds a temp copy of `projects/_template/` so tests run offline
  and never touch the real `projects/` directory.
- `test_new_project.py` — scaffolding, path-safety, classification refusal.
- `test_validate.py` — the four validator checks (links, classification,
  scaffold structure, schema).
- `test_state.py` — `stage` transitions, status mapping, the principle-J review
  gate, and path-traversal refusal.
- `test_schema.py` — manifest/state schema validation.

## Scope

These tests cover the CORE v0.2 "Project Core" slice only: the `omar_os` package,
the `new-project` / `validate` / `stage` commands, and the four validator checks.
Agent runtime, GitHub adapter, and knowledge services are later phases (see
`ROADMAP.md`) and are **not** exercised here.
