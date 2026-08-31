"""State read/write and stage transitions (stdlib only)."""

from __future__ import annotations

import json
from pathlib import Path

from . import schema
from .constants import (
    COMPLETE_STAGE,
    MANIFEST_FILE,
    REVIEW_STAGE,
    STATE_FILE,
    STATUS_DONE,
    STATUS_IN_PROGRESS,
    STATUS_TODO,
)
from .pathutil import project_path_for
from .schema import SchemaError, now_utc


class StateError(Exception):
    """Raised on invalid stage operations."""


def _state_path(name: str) -> Path:
    try:
        return project_path_for(name) / STATE_FILE
    except ValueError as exc:
        raise StateError(str(exc))


def read_state(name: str) -> dict:
    path = _state_path(name)
    if not path.exists():
        raise StateError(f"no state.json for project {name!r}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise StateError(f"invalid state.json for {name!r}: {exc}")


def write_state(name: str, state: dict) -> None:
    path = _state_path(name)
    path.write_text(
        json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def stage(name: str, target_stage: str, by: str = "Omar") -> dict:
    """Transition ``name`` to ``target_stage`` and append a history entry.

    Enforces:
      * target must be a legal lifecycle stage
      * complete is forbidden unless ``review`` already in history (principle J)
      * status mapping: todo -> in_progress (any non-complete) -> done (complete)
    """
    from .constants import LIFECYCLE_STAGES

    if target_stage not in LIFECYCLE_STAGES:
        raise StateError(f"unknown lifecycle stage: {target_stage!r}")

    state = read_state(name)
    history = state.get("history", [])

    # Principle-J review gate.
    if target_stage == COMPLETE_STAGE:
        if not any(h.get("stage") == REVIEW_STAGE for h in history):
            raise StateError(
                "cannot reach 'complete' before 'review' (principle J: "
                "no 'done' without review)"
            )

    history.append({"stage": target_stage, "at": now_utc(), "by": by})
    state["current_stage"] = target_stage
    state["status"] = STATUS_DONE if target_stage == COMPLETE_STAGE else STATUS_IN_PROGRESS

    # Re-validate the resulting document before writing.
    try:
        schema.validate_state(state)
    except SchemaError as exc:
        raise StateError(str(exc))

    write_state(name, state)
    return state
