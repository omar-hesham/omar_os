"""Tests for new-project scaffolding, path-safety, and classification refusal."""

from __future__ import annotations

import json

import pytest

from omar_os import scaffold
from omar_os.scaffold import ScaffoldError
from omar_os.constants import MANIFEST_FILE, STATE_FILE, SCAFFOLD_MD_FILES

from conftest import make_project


def test_new_project_creates_8_files(tmp_repo):
    dest = make_project(tmp_repo, "demo", effort="low")
    # 6 markdown + 2 json
    for md in SCAFFOLD_MD_FILES:
        assert (dest / md).exists(), f"missing {md}"
    assert (dest / MANIFEST_FILE).exists()
    assert (dest / STATE_FILE).exists()
    manifest = json.loads((dest / MANIFEST_FILE).read_text(encoding="utf-8"))
    state = json.loads((dest / STATE_FILE).read_text(encoding="utf-8"))
    assert manifest["classification"] == "public"
    assert state["status"] == "todo"
    assert len(state["history"]) == 1
    assert state["history"][0]["stage"] == "idea"


def test_new_project_refuses_existing(tmp_repo):
    make_project(tmp_repo, "demo")
    with pytest.raises(ScaffoldError):
        make_project(tmp_repo, "demo")


def test_new_project_refuses_non_public(tmp_repo):
    with pytest.raises(ScaffoldError):
        make_project(tmp_repo, "secret", classification="confidential")


def test_new_project_refuses_traversal_names(tmp_repo):
    for bad in ("../escape", "a/b", "a..b", ".hidden", "Bad Name", "a--b", "-x", "X"):
        with pytest.raises(ScaffoldError):
            make_project(tmp_repo, bad)


def test_new_project_extra_files_allowed(tmp_repo):
    dest = make_project(tmp_repo, "demo", extra_files=["notes.txt", "src/main.py"])
    assert (dest / "notes.txt").exists()
    assert (dest / "src" / "main.py").exists()
