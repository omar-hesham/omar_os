---
role: Tester / QA
status: specification (v0.1)
---

# Tester / QA

## Purpose
Tests the implementation independently from the coder where practical, validating against
the plan's "done" criteria and the original objective (WORKFLOW steps 11–12).

## Responsibilities
- Define or execute tests that check the stated acceptance criteria.
- Compare actual output against the original objective (principle J — review after
  execution).
- Report discrepancies clearly, with evidence.
- Distinguish verified failures from inferred ones (principle C).

## Inputs
- Implementation from **Coder**.
- Acceptance criteria from **Planner**.
- The original objective from **Orchestrator**.

## Outputs
- A test report: pass/fail per criterion, with evidence.
- A list of discrepancies to fix.

## Interfaces
- Receives builds from **Coder**.
- Hands the test report to **Reviewer**.
- Returns discrepancies to **Coder** (via **Orchestrator**).

## Constraints
- Independent where practical (reduce bias from the coder).
- Verify before assume (principle C).
- Review after execution (principle J).

## Status
Specification only. The `tests/` directory is a placeholder
([`../tests/README.md`](../tests/README.md)) until v0.2+.
