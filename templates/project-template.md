<!--
Single source of truth for project scaffolding: projects/_template/.
This file is now a POINTER only — do not maintain a second copy of the PROJECT.md body here.
To start a project: copy the whole projects/_template/ folder (see projects/README.md).
-->
# Project template — see `projects/_template/`

> **This is a pointer, not a second scaffold.** The canonical, copy-ready project
> starter lives in **[`../projects/_template/`](../projects/_template/)** (its `PROJECT.md`
> plus `REQUIREMENTS.md`, `FLOW.md`, `DECISIONS.md`, `TASKS.md`, `REVIEW.md`).

## How to create a project

```bash
cp -r projects/_template projects/<your-project>
# then fill in each file; the same-folder links (REQUIREMENTS.md, etc.) resolve correctly
```

## Why a pointer instead of a duplicate

Maintaining the PROJECT.md body in *both* `templates/project-template.md` and
`projects/_template/PROJECT.md` caused drift. The `_template/` folder is the single source;
this file only explains how to use it. (Decision recorded in ADR-0002.)
