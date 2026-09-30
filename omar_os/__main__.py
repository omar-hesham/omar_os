"""CLI entry point for ``python -m omar_os``.

Dispatches: new-project, validate, stage. Stdlib + argparse only.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import scaffold, state, validate as validate_mod
from .scaffold import ScaffoldError
from .state import StateError


def _cmd_new_project(args) -> int:
    try:
        dest = scaffold.new_project(
            name=args.name,
            owner=args.owner,
            effort_level=args.effort,
            classification=args.classification,
        )
    except ScaffoldError as exc:
        print(f"✗ error: {exc}", file=sys.stderr)
        return 1
    print(f"✓ created project: {dest}")
    return 0


def _cmd_validate(args) -> int:
    root = Path(args.path) if args.path else None
    ok, report = validate_mod.validate(root)
    print(report)
    return 0 if ok else 1


def _cmd_stage(args) -> int:
    try:
        new_state = state.stage(args.project, args.stage, by=args.by)
    except StateError as exc:
        print(f"✗ error: {exc}", file=sys.stderr)
        return 1
    print(
        f"✓ staged {args.project}: current_stage={new_state['current_stage']} "
        f"status={new_state['status']}"
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    from .constants import LIFECYCLE_STAGES
    parser = argparse.ArgumentParser(
        prog="omar_os", description="OMAR OS Project Core (v0.2)"
    )
    sub = parser.add_subparsers(dest="command", required=True, metavar="COMMAND")

    p_new = sub.add_parser("new-project", help="scaffold a new project")
    p_new.add_argument("name", help="name of the project to create (kebab-case)")
    p_new.add_argument("--owner", default="Omar", help="owner of the project")
    p_new.add_argument("--effort", choices=["low", "medium", "high"], default="low", help="expected effort level: %(choices)s", metavar="EFFORT")
    p_new.add_argument(
        "--classification",
        default="public",
        help="must be 'public' for the public repo (ADR-0002)",
    )
    p_new.set_defaults(func=_cmd_new_project)

    p_val = sub.add_parser("validate", help="run the four validation checks")
    p_val.add_argument("path", nargs="?", default=None, help="root to validate")
    p_val.set_defaults(func=_cmd_validate)

    p_stage = sub.add_parser("stage", help="transition a project lifecycle stage")
    p_stage.add_argument("project", help="name of the project to update")
    p_stage.add_argument("stage", choices=LIFECYCLE_STAGES, help="target lifecycle stage: %(choices)s", metavar="STAGE")
    p_stage.add_argument("--by", default="Omar", help="person or agent making the change")
    p_stage.set_defaults(func=_cmd_stage)

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    # Print help if no arguments are provided
    if (argv is None and len(sys.argv) == 1) or (argv is not None and len(argv) == 0):
        parser.print_help(sys.stderr)
        return 1

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
