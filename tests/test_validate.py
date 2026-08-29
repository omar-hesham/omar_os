"""Tests for the validator's four checks."""

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
    manifest = (
        tmp_repo / "projects" / "demo" / MANIFEST_FILE
    )
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
    # Inject a broken internal link into PROJECT.md
    (proj / "PROJECT.md").write_text(
        "See [missing](nonexistent.md) and [ok](FLOW.md).\n", encoding="utf-8"
    )
    ok, report = validate_mod.validate(tmp_repo)
    assert ok is False
    assert "nonexistent.md" in report
