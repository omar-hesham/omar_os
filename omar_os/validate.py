"""The four validator checks (stdlib only).

Checks:
  1. Internal Markdown links resolve.
  2. Classification boundary (public repo = public only; real manifests must declare).
  3. Scaffold structure (8 required files present per real project).
  4. Manifest/state schema validity.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from . import schema
from . import constants

LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)


def _slug(h: str) -> str:
    s = h.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    return re.sub(r"\s+", "-", s)


def _collect_anchors(path: Path) -> set[str]:
    anchors: set[str] = set()
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return anchors
    for line in text.splitlines():
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            anchors.add(_slug(m.group(2)))
    return anchors


def _md_files(root: Path):
    return [p for p in root.rglob("*.md")]


def check_links(root: Path) -> list[str]:
    """Return a list of broken-link problems (empty = pass)."""
    problems: list[str] = []
    files = _md_files(root)
    anchors = {p: _collect_anchors(p) for p in files}
    for f in files:
        text = FENCE_RE.sub("", f.read_text(encoding="utf-8"))
        for m in LINK_RE.finditer(text):
            target = m.group(1).strip()
            if not target:
                continue
            if target.startswith(("http://", "https://", "mailto:", "ftp://")):
                continue
            if target.startswith("#"):
                if _slug(target[1:]) not in anchors.get(f, set()):
                    problems.append(f"{f}: anchor not found: {target}")
                continue
            path_part, _, anchor_part = target.partition("#")
            if path_part == "":
                continue
            resolved = (f.parent / path_part).resolve()
            # Skip links that resolve outside the validated root: they belong to a
            # different root (e.g. a project template linking up to repo-level docs
            # like ../../docs/...). Such links are validated when the root that
            # contains their target is checked.
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                continue
            if not resolved.exists():
                problems.append(f"{f}: broken link -> {target}")
            elif anchor_part and anchor_part not in anchors.get(resolved, set()):
                problems.append(f"{f}: broken anchor {target}")
    return problems


def check_classification(projects_dir: Path, root: Path | None = None) -> list[str]:
    """Enforce ADR-0002 inside the public repo.

    * Real project manifests MUST declare classification, and it MUST be public.
    * Any *declared* classification on a document inside the public repo that is
      not `public` is a failure (covers docs/agents/workflows/etc. that choose to
      declare one). Foundation docs without a declaration are implicitly public.
    """
    problems: list[str] = []
    scan_root = (root or projects_dir.parent).resolve()

    # 1. Real project manifests (projects/, excluding _template).
    if projects_dir.is_dir():
        for proj in projects_dir.iterdir():
            if not proj.is_dir() or proj.name == "_template":
                continue
            manifest = proj / constants.MANIFEST_FILE
            if not manifest.exists():
                continue  # handled by check_scaffold/orphan checks
            try:
                data = json.loads(manifest.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                problems.append(f"{proj}: unreadable {constants.MANIFEST_FILE}")
                continue
            if "classification" not in data:
                problems.append(
                    f"{proj}: {constants.MANIFEST_FILE} missing mandatory 'classification'"
                )
                continue
            if data["classification"] != constants.PUBLIC_CLASSIFICATION:
                problems.append(
                    f"{proj}: classification {data['classification']!r} not allowed "
                    f"in public repo (must be {constants.PUBLIC_CLASSIFICATION!r})"
                )

    # 2. Any declared classification field (top-level) in scanned documents that
    #    is not `public`. We scan common doc roots but only flag an explicit,
    #    non-public declaration (implicitly-public docs are ignored).
    for sub in ("docs", "agents", "workflows", "templates", "decisions", "knowledge"):
        d = scan_root / sub
        if not d.is_dir():
            continue
        for f in d.rglob("*.md"):
            try:
                text = f.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            decl = _declared_classification(text)
            if decl is not None and decl != constants.PUBLIC_CLASSIFICATION:
                problems.append(
                    f"{f}: declared classification {decl!r} not allowed in public "
                    f"repo (must be {constants.PUBLIC_CLASSIFICATION!r})"
                )
    return problems


# A simple front-matter / inline declaration parser for `classification:`.
_CLASS_RE = re.compile(r"^\s*classification\s*:\s*[\"']?([a-zA-Z]+)[\"']?\s*$", re.MULTILINE)


def _declared_classification(text: str) -> str | None:
    """Return a top-level `classification:` value if declared, else None."""
    m = _CLASS_RE.search(text)
    if not m:
        return None
    val = m.group(1).lower()
    return val if val in constants.CLASSIFICATIONS else val


def check_scaffold(projects_dir: Path) -> list[str]:
    """Each real project must contain the 8 required files.

    A directory under ``projects/`` (excluding ``_template``) that contains any
    project artifact (``state.json`` or any of the 6 scaffold markdown files) but
    is missing ``project.json`` or any other required file is a failure — missing
    files must not be silently skipped.
    """
    problems: list[str] = []
    if not projects_dir.is_dir():
        return problems
    for proj in projects_dir.iterdir():
        if not proj.is_dir() or proj.name == "_template":
            continue
        has_any_artifact = (proj / constants.STATE_FILE).exists() or any(
            (proj / md).exists() for md in constants.SCAFFOLD_MD_FILES
        )
        if not has_any_artifact:
            continue  # an unrelated directory; not our concern
        for required in constants.REQUIRED_PROJECT_FILES:
            if not (proj / required).exists():
                problems.append(f"{proj}: missing required file {required}")
    return problems


def check_schema(projects_dir: Path) -> list[str]:
    """Every project.json / state.json must validate against the schema."""
    problems: list[str] = []
    for proj in projects_dir.iterdir():
        if not proj.is_dir() or proj.name == "_template":
            continue
        manifest = proj / constants.MANIFEST_FILE
        state = proj / constants.STATE_FILE
        if manifest.exists():
            try:
                schema.validate_project_file(manifest)
            except schema.SchemaError as exc:
                problems.append(f"{proj}: {constants.MANIFEST_FILE}: {exc}")
        if state.exists():
            try:
                schema.validate_state_file(state)
            except schema.SchemaError as exc:
                problems.append(f"{proj}: {constants.STATE_FILE}: {exc}")
    return problems


def run_checks(root: Path | None = None) -> dict[str, list[str]]:
    root = Path(root) if root else constants.PROJECTS_DIR.parent
    projects_dir = root / "projects" if root else constants.PROJECTS_DIR
    return {
        "links": check_links(root),
        "classification": check_classification(projects_dir, root),
        "scaffold": check_scaffold(projects_dir),
        "schema": check_schema(projects_dir),
    }


def format_report(results: dict[str, list[str]]) -> str:
    lines = ["OMAR OS — validation report"]
    total = 0
    for name, problems in results.items():
        total += len(problems)
        status = "PASS" if not problems else f"FAIL ({len(problems)})"
        lines.append(f"  [{status}] {name}")
        for p in problems:
            lines.append(f"        - {p}")
    lines.append(f"Overall: {'PASS' if total == 0 else f'FAIL ({total} issues)'}")
    return "\n".join(lines)


def validate(root: Path | None = None) -> tuple[bool, str]:
    results = run_checks(root)
    report = format_report(results)
    failed = any(results.values())
    return (not failed), report
