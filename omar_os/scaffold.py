"""Scaffold operations: copy the single source template into a new project.

Stdlib only. Uses pathlib; never os.path.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from . import schema
from .constants import (
    MANIFEST_FILE,
    PUBLIC_CLASSIFICATION,
    SCAFFOLD_MD_FILES,
    STATE_FILE,
    TEMPLATE_DIR,
)
from .pathutil import project_path_for


class ScaffoldError(Exception):
    """Raised on scaffold failure (e.g. name exists, non-public classification)."""


def new_project(
    name: str,
    owner: str = "Omar",
    effort_level: str = "low",
    classification: str = PUBLIC_CLASSIFICATION,
    title: str | None = None,
) -> Path:
    """Create ``projects/<name>/`` from the single template source.

    Writes project.json + state.json. Refuses if the name exists, if the
    classification is not ``public`` (public repo rule, ADR-0002), or if the
    project id is unsafe (path traversal / non-kebab-case).
    """
    # Path-safety: also rejects non-kebab-case / traversal before any write.
    try:
        dest = project_path_for(name)
    except ValueError as exc:
        raise ScaffoldError(str(exc))

    if dest.exists():
        raise ScaffoldError(
            f"project already exists: {name!r} (refusing to overwrite)"
        )

    if classification != PUBLIC_CLASSIFICATION:
        raise ScaffoldError(
            f"classification {classification!r} is not allowed in the public repo; "
            f"use the private workspace for {classification!r} projects"
        )

    # Copy the 6 markdown templates (single-source rule).
    dest.mkdir(parents=True)
    for md in SCAFFOLD_MD_FILES:
        src = TEMPLATE_DIR / md
        if src.exists():
            shutil.copyfile(src, dest / md)

    # Write the two JSON manifests (not part of the template).
    manifest = schema.build_manifest(
        project_id=name,
        title=title or name,
        owner=owner,
        effort_level=effort_level,
        classification=classification,
    )
    state = schema.build_state(project_id=name, owner=owner)
    (dest / MANIFEST_FILE).write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (dest / STATE_FILE).write_text(
        json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return dest
