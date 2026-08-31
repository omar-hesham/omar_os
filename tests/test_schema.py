"""Tests for schema validation (malformed manifests / state rejected)."""

from __future__ import annotations

import json

import pytest

from omar_os import schema
from omar_os.schema import SchemaError

from conftest import make_project


def test_valid_manifest_and_state_pass():
    m = schema.build_manifest("demo", "Demo", "Omar", "low", "public")
    s = schema.build_state("demo", "Omar")
    schema.validate_project(m)
    schema.validate_state(s)


def test_missing_required_key_fails():
    with pytest.raises(SchemaError):
        schema.validate_project({"id": "x"})  # missing most keys
    with pytest.raises(SchemaError):
        schema.validate_state({"current_stage": "idea"})  # missing keys


def test_bad_enum_fails():
    m = schema.build_manifest("demo", "Demo", "Omar", "low", "public")
    m["effort_level"] = "huge"
    with pytest.raises(SchemaError):
        schema.validate_project(m)
    m2 = schema.build_manifest("demo", "Demo", "Omar", "low", "public")
    m2["classification"] = "topsecret"
    with pytest.raises(SchemaError):
        schema.validate_project(m2)


def test_bad_type_fails():
    m = schema.build_manifest("demo", "Demo", "Omar", "low", "public")
    m["success_criteria"] = "not-a-list"
    with pytest.raises(SchemaError):
        schema.validate_project(m)
