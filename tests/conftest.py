"""Pytest fixtures for OMAR OS Project Core tests.

Builds a temporary copy of ``projects/_template/`` so the suite runs offline
and never pollutes the real ``projects/`` directory.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from omar_os.constants import PROJECTS_DIR, TEMPLATE_DIR

# A standalone template dir inside the temp repo root (mirrors projects/_template).
TEMPLATE_MD = (
    "PROJECT.md",
    "REQUIREMENTS.md",
    "FLOW.md",
    "DECISIONS.md",
    "TASKS.md",
    "REVIEW.md",
)


@pytest.fixture()
def tmp_repo(tmp_path: Path):
    """Create a temp repo root mirroring the real one (so template links resolve).

    Deep-copies the real repository (excluding ``.git``) so the validator's link
    check sees a faithful environment. Then replaces ``projects/`` with a temp
    template so ``make_project`` can scaffold without touching the real repo.
    Tests never modify the real repository.
    """
    repo_root = PROJECTS_DIR.parent
    # Copy everything except .git and the live projects/ dir.
    for item in repo_root.iterdir():
        if item.name in (".git", "projects"):
            continue
        dest = tmp_path / item.name
        if item.is_dir():
            shutil.copytree(item, dest)
        else:
            shutil.copy2(item, dest)

    projects = tmp_path / "projects"
    if projects.exists():
        shutil.rmtree(projects)
    template = projects / "_template"
    template.mkdir(parents=True)
    for md in TEMPLATE_MD:
        (template / md).write_text(f"# {md}\n", encoding="utf-8")
    return tmp_path


def make_project(
    tmp_repo: Path,
    name: str,
    classification: str = "public",
    effort: str = "low",
    extra_files: list[str] | None = None,
) -> Path:
    """Scaffold a project under tmp_repo/projects/<name> using the package."""
    from omar_os import scaffold
    import omar_os.constants as C
    import omar_os.pathutil as PU

    orig_projects = C.PROJECTS_DIR
    orig_template = C.TEMPLATE_DIR
    orig_scaffold_template = scaffold.TEMPLATE_DIR
    orig_pu_projects = PU.PROJECTS_DIR
    C.PROJECTS_DIR = tmp_repo / "projects"
    C.TEMPLATE_DIR = tmp_repo / "projects" / "_template"
    scaffold.TEMPLATE_DIR = tmp_repo / "projects" / "_template"
    PU.PROJECTS_DIR = tmp_repo / "projects"
    try:
        dest = scaffold.new_project(
            name=name, owner="Omar", effort_level=effort, classification=classification
        )
    finally:
        C.PROJECTS_DIR = orig_projects
        C.TEMPLATE_DIR = orig_template
        scaffold.TEMPLATE_DIR = orig_scaffold_template
        PU.PROJECTS_DIR = orig_pu_projects

    if extra_files:
        for ef in extra_files:
            p = dest / ef
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text("extra\n", encoding="utf-8")
    return dest
