"""Tests for the validator's four checks, including attack/regression cases."""

from __future__ import annotations

import json

import pytest

from omar_os import validate as validate_mod
from omar_os.constants import MANIFEST_FILE, STATE_FILE

from conftest import make_project


def test_validate_passes_on_clean_project(tmp_repo):
    make_project(tmp_repo, "demo")
    ok, _ = validate_mod.validate(tmp_repo)
    assert ok is True


def test_validate_fails_confidential_in_public(tmp_repo):
    make_project(tmp_repo, "demo", classification="public")
    manifest = tmp_repo / "projects" / "demo" / MANIFEST_FILE
    data = json.loads(manifest.read_text(encoding="utf-8"))
    data["classification"] = "confidential"
    manifest.write_text(json.dumps(data), encoding="utf-8")
    ok, report = validate_mod.validate(tmp_repo)
    assert ok is False
    assert "classification" in report


def test_validate_fails_missing_scaffold_file(tmp_repo):
    make_project(tmp_repo, "demo")
    (tmp_repo / "projects" / "demo" / "FLOW.md").unlink()
    ok, report = validate_mod.validate(tmp_repo)
    assert ok is False
    assert "FLOW.md" in report


def test_validate_fails_missing_classification(tmp_repo):
    make_project(tmp_repo, "demo")
    manifest = tmp_repo / "projects" / "demo" / MANIFEST_FILE
    data = json.loads(manifest.read_text(encoding="utf-8"))
    del data["classification"]
    manifest.write_text(json.dumps(data), encoding="utf-8")
    ok, report = validate_mod.validate(tmp_repo)
    assert ok is False
    assert "classification" in report


def test_validate_fails_invalid_current_stage(tmp_repo):
    make_project(tmp_repo, "demo")
    state = tmp_repo / "projects" / "demo" / STATE_FILE
    data = json.loads(state.read_text(encoding="utf-8"))
    data["current_stage"] = "not_a_stage"
    state.write_text(json.dumps(data), encoding="utf-8")
    ok, report = validate_mod.validate(tmp_repo)
    assert ok is False
    assert "state.json" in report


def test_validate_detects_broken_link(tmp_repo):
    make_project(tmp_repo, "demo")
    proj = tmp_repo / "projects" / "demo"
    (proj / "PROJECT.md").write_text(
        "See [missing](nonexistent.md) and [ok](FLOW.md).\n", encoding="utf-8"
    )
    ok, report = validate_mod.validate(tmp_repo)
    assert ok is False
    assert "nonexistent.md" in report


# --- Regression: deleted project.json must NOT silently pass ----------------
def test_validate_fails_when_project_json_deleted(tmp_repo):
    make_project(tmp_repo, "demo")
    (tmp_repo / "projects" / "demo" / MANIFEST_FILE).unlink()
    ok, report = validate_mod.validate(tmp_repo)
    assert ok is False
    assert "project.json" in report


# --- Regression: malformed JSON must fail cleanly, not crash -----------------
def test_validate_handles_malformed_project_json(tmp_repo):
    make_project(tmp_repo, "demo")
    (tmp_repo / "projects" / "demo" / MANIFEST_FILE).write_text(
        "{not valid json", encoding="utf-8"
    )
    ok, report = validate_mod.validate(tmp_repo)
    assert ok is False
    assert "invalid JSON" in report


def test_validate_handles_malformed_state_json(tmp_repo):
    make_project(tmp_repo, "demo")
    (tmp_repo / "projects" / "demo" / STATE_FILE).write_text(
        "{not valid json", encoding="utf-8"
    )
    ok, report = validate_mod.validate(tmp_repo)
    assert ok is False
    assert "invalid JSON" in report


# --- Regression: declared non-public classification outside manifests --------
def test_validate_fails_declared_classification_in_docs(tmp_repo):
    # A doc under the scanned surface declaring confidential must fail.
    bad = tmp_repo / "docs" / "secret-notes.md"
    bad.parent.mkdir(parents=True, exist_ok=True)
    bad.write_text("classification: confidential\n\nSome notes.\n", encoding="utf-8")
    ok, report = validate_mod.validate(tmp_repo)
    assert ok is False
    assert "secret-notes.md" in report


def test_validate_ignores_implicit_public_docs(tmp_repo):
    # A doc with no classification declaration must NOT be flagged.
    ok_doc = tmp_repo / "docs" / "normal.md"
    ok_doc.parent.mkdir(parents=True, exist_ok=True)
    ok_doc.write_text("# Normal\n\nNo classification here.\n", encoding="utf-8")
    make_project(tmp_repo, "demo")
    ok, _ = validate_mod.validate(tmp_repo)
    assert ok is True


# --- Regression: invalid history entries must be rejected --------------------
def test_validate_fails_bad_history_stage(tmp_repo):
    make_project(tmp_repo, "demo")
    state = tmp_repo / "projects" / "demo" / STATE_FILE
    data = json.loads(state.read_text(encoding="utf-8"))
    data["history"].append({"stage": "bogus", "at": "2026-08-29T10:00:00Z", "by": "Omar"})
    state.write_text(json.dumps(data), encoding="utf-8")
    ok, report = validate_mod.validate(tmp_repo)
    assert ok is False
    assert "history" in report


def test_validate_fails_numeric_timestamp(tmp_repo):
    make_project(tmp_repo, "demo")
    state = tmp_repo / "projects" / "demo" / STATE_FILE
    data = json.loads(state.read_text(encoding="utf-8"))
    data["history"].append({"stage": "review", "at": 1234567890, "by": "Omar"})
    state.write_text(json.dumps(data), encoding="utf-8")
    ok, report = validate_mod.validate(tmp_repo)
    assert ok is False
    assert "history" in report


def test_validate_fails_null_by(tmp_repo):
    make_project(tmp_repo, "demo")
    state = tmp_repo / "projects" / "demo" / STATE_FILE
    data = json.loads(state.read_text(encoding="utf-8"))
    data["history"].append({"stage": "review", "at": "2026-08-29T10:00:00Z", "by": None})
    state.write_text(json.dumps(data), encoding="utf-8")
    ok, report = validate_mod.validate(tmp_repo)
    assert ok is False
    assert "history" in report
