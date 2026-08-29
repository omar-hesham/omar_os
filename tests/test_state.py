"""Tests for stage transitions, status mapping, review gate, and path-safety."""

from __future__ import annotations

import json

import pytest

from omar_os import state
from omar_os.state import StateError
from omar_os.constants import STATE_FILE

from conftest import make_project


def _patch_paths(tmp_repo, monkeypatch):
    import omar_os.constants as C
    import omar_os.pathutil as PU
    import omar_os.scaffold as S

    monkeypatch.setattr(C, "PROJECTS_DIR", tmp_repo / "projects")
    monkeypatch.setattr(C, "TEMPLATE_DIR", tmp_repo / "projects" / "_template")
    monkeypatch.setattr(PU, "PROJECTS_DIR", tmp_repo / "projects")
    monkeypatch.setattr(S, "TEMPLATE_DIR", tmp_repo / "projects" / "_template")


def test_stage_appends_history_and_sets_status(tmp_repo, monkeypatch):
    _patch_paths(tmp_repo, monkeypatch)
    make_project(tmp_repo, "demo")
    st = state.stage("demo", "intake")
    assert st["current_stage"] == "intake"
    assert st["status"] == "in_progress"
    assert len(st["history"]) == 2


def test_complete_blocked_before_review(tmp_repo, monkeypatch):
    _patch_paths(tmp_repo, monkeypatch)
    make_project(tmp_repo, "demo")
    state.stage("demo", "intake")
    with pytest.raises(StateError):
        state.stage("demo", "complete")


def test_complete_allowed_after_review(tmp_repo, monkeypatch):
    _patch_paths(tmp_repo, monkeypatch)
    make_project(tmp_repo, "demo")
    state.stage("demo", "research")
    state.stage("demo", "review")
    st = state.stage("demo", "complete")
    assert st["current_stage"] == "complete"
    assert st["status"] == "done"


def test_stage_rejects_path_traversal_cleanly(tmp_repo, monkeypatch):
    _patch_paths(tmp_repo, monkeypatch)
    make_project(tmp_repo, "demo")
    # Must raise StateError (clean message), not an unhandled traceback.
    with pytest.raises(StateError):
        state.stage("../escape", "review")
    with pytest.raises(StateError):
        state.stage("/abs/path", "review")


def test_stage_rejects_unknown_stage(tmp_repo, monkeypatch):
    _patch_paths(tmp_repo, monkeypatch)
    make_project(tmp_repo, "demo")
    with pytest.raises(StateError):
        state.stage("demo", "not_a_stage")


# --- Regression: malformed history must be rejected, not crash --------------
def test_stage_rejects_bad_history(tmp_repo, monkeypatch):
    _patch_paths(tmp_repo, monkeypatch)
    make_project(tmp_repo, "demo")
    state_file = tmp_repo / "projects" / "demo" / STATE_FILE
    data = json.loads(state_file.read_text(encoding="utf-8"))
    data["history"].append({"stage": "bogus", "at": "2026-08-29T10:00:00Z", "by": "Omar"})
    state_file.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(StateError):
        state.stage("demo", "review")
