"""Path-safety helpers shared by new-project and stage (stdlib pathlib only).

All containment checks use ``Path.resolve()`` + ``is_relative_to()`` — never
``os.path.normpath`` (per the CORE v0.2 Master Implementation Prompt, §4).
"""

from __future__ import annotations

import re
from pathlib import Path

from .constants import KEBAB_CASE_RE, PROJECTS_DIR

# Project id must be a single path segment, kebab-case.
_ID_BAD_CHARS = ("/", "\\", ".", "..")


def is_safe_project_id(name: str) -> bool:
    """True if ``name`` is a single kebab-case path segment."""
    if not name:
        return False
    if name in (".", ".."):
        return False
    if any(ch in name for ch in ("/", "\\")):
        return False
    if name.startswith(".") or name.endswith("."):
        return False
    return bool(re.match(KEBAB_CASE_RE, name))


def project_path_for(name: str) -> Path:
    """Return the resolved absolute path for ``projects/<name>/``.

    Raises ``ValueError`` if the name is unsafe or the resolved destination would
    escape ``PROJECTS_DIR``. Computed with ``Path.resolve()`` /
    ``is_relative_to()`` only.
    """
    if not is_safe_project_id(name):
        raise ValueError(
            f"unsafe project id: {name!r} "
            "(must be kebab-case, single path segment, no slashes/dots)"
        )
    resolved_projects = PROJECTS_DIR.resolve()
    # Build candidate inside PROJECTS_DIR and resolve it.
    candidate = (resolved_projects / name).resolve()
    try:
        candidate.relative_to(resolved_projects)
    except ValueError:
        raise ValueError(
            f"project destination escapes projects/: {name!r}"
        )
    return candidate


def is_inside_projects(path: Path) -> bool:
    """True if ``path`` resolves to a location strictly inside PROJECTS_DIR."""
    resolved_projects = PROJECTS_DIR.resolve()
    try:
        Path(path).resolve().relative_to(resolved_projects)
        return True
    except ValueError:
        return False
