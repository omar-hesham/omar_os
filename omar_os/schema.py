"""Manifest / state schema validation (stdlib only, no jsonschema/pydantic).

Defines the required shape of ``project.json`` and ``state.json`` and a small
inline validator. Also exposes helpers to build the default documents written
by ``new-project``.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from .constants import (
    CLASSIFICATIONS,
    COMPLETE_STAGE,
    DEFAULT_EFFORT,
    EFFORT_LEVELS,
    KEBAB_CASE_RE,
    LIFECYCLE_STAGES,
    PUBLIC_CLASSIFICATION,
    REVIEW_STAGE,
    SCHEMA_VERSION,
    STATUSES,
    STATE_FILE,
    MANIFEST_FILE,
)

import re


def now_utc() -> str:
    """RFC3339 UTC timestamp, e.g. 2026-08-29T10:00:00Z."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class SchemaError(Exception):
    """Raised when a manifest or state document is invalid."""


# --- Required-key definitions ------------------------------------------------
PROJECT_REQUIRED = {
    "schema_version": str,
    "id": str,
    "title": str,
    "owner": str,
    "effort_level": str,
    "classification": str,
    "source_of_truth": list,
    "success_criteria": list,
    "created_at": str,
}

STATE_REQUIRED = {
    "schema_version": str,
    "current_stage": str,
    "status": str,
    "blockers": list,
    "history": list,
}


def _check_required(data: dict, required: dict, doc_name: str) -> None:
    if not isinstance(data, dict):
        raise SchemaError(f"{doc_name} must be a JSON object")
    for key, expected_type in required.items():
        if key not in data:
            raise SchemaError(f"{doc_name} missing required key: {key}")
        if not isinstance(data[key], expected_type):
            raise SchemaError(
                f"{doc_name}.{key} must be of type {expected_type.__name__}"
            )


def _check_enum(value: str, allowed, field_name: str, doc_name: str) -> None:
    if value not in allowed:
        raise SchemaError(
            f"{doc_name}.{field_name} must be one of {list(allowed)}; got {value!r}"
        )


def validate_project(data: dict) -> None:
    """Validate a project.json manifest. Raises SchemaError on failure."""
    _check_required(data, PROJECT_REQUIRED, MANIFEST_FILE)
    _check_enum(data["effort_level"], EFFORT_LEVELS, "effort_level", MANIFEST_FILE)
    _check_enum(
        data["classification"], CLASSIFICATIONS, "classification", MANIFEST_FILE
    )
    if not re.match(KEBAB_CASE_RE, data["id"]):
        raise SchemaError(f"{MANIFEST_FILE}.id must be kebab-case; got {data['id']!r}")


def validate_state(data: dict) -> None:
    """Validate a state.json document. Raises SchemaError on failure."""
    _check_required(data, STATE_REQUIRED, STATE_FILE)
    _check_enum(data["current_stage"], LIFECYCLE_STAGES, "current_stage", STATE_FILE)
    _check_enum(data["status"], STATUSES, "status", STATE_FILE)
    # history entries must be dicts with stage/at/by, each well-typed.
    for i, entry in enumerate(data["history"]):
        if not isinstance(entry, dict):
            raise SchemaError(f"{STATE_FILE}.history[{i}] must be an object")
        for k in ("stage", "at", "by"):
            if k not in entry:
                raise SchemaError(f"{STATE_FILE}.history[{i}] missing key: {k}")
        if not isinstance(entry["stage"], str) or entry["stage"] not in LIFECYCLE_STAGES:
            raise SchemaError(
                f"{STATE_FILE}.history[{i}].stage must be a legal stage; "
                f"got {entry['stage']!r}"
            )
        if not isinstance(entry["at"], str) or not entry["at"]:
            raise SchemaError(
                f"{STATE_FILE}.history[{i}].at must be a non-empty RFC3339 string; "
                f"got {entry['at']!r}"
            )
        if not isinstance(entry["by"], str) or not entry["by"]:
            raise SchemaError(
                f"{STATE_FILE}.history[{i}].by must be a non-empty string; "
                f"got {entry['by']!r}"
            )


def validate_project_file(path) -> None:
    from pathlib import Path

    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SchemaError(f"{MANIFEST_FILE}: invalid JSON: {exc}") from exc
    validate_project(data)


def validate_state_file(path) -> None:
    from pathlib import Path

    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SchemaError(f"{STATE_FILE}: invalid JSON: {exc}") from exc
    validate_state(data)


# --- Document builders -------------------------------------------------------
def build_manifest(
    project_id: str,
    title: str,
    owner: str,
    effort_level: str = DEFAULT_EFFORT,
    classification: str = PUBLIC_CLASSIFICATION,
    source_of_truth=None,
    success_criteria=None,
) -> dict:
    return {
        "schema_version": SCHEMA_VERSION,
        "id": project_id,
        "title": title,
        "owner": owner,
        "effort_level": effort_level,
        "classification": classification,
        "source_of_truth": source_of_truth or ["PROJECT.md", "REQUIREMENTS.md"],
        "success_criteria": success_criteria or [],
        "created_at": now_utc(),
    }


def build_state(project_id: str, owner: str) -> dict:
    return {
        "schema_version": SCHEMA_VERSION,
        "current_stage": "idea",
        "status": "todo",
        "blockers": [],
        "history": [
            {"stage": "idea", "at": now_utc(), "by": owner or project_id}
        ],
    }
