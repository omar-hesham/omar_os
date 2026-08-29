# Config — OMAR OS

> **Placeholder (v0.1).** Intentionally minimal.

This directory is reserved for configuration that controls OMAR OS behavior
(env references, adapter configs, model-routing settings) as executable phases land.

## Current state

- No configuration files exist yet. v0.1 is documentation-first.
- When config arrives (INTEGRATION v0.4+), it must:
  - reference secrets via environment variables or a secrets manager — **never** commit
    keys (see [`../docs/SECURITY.md`](../docs/SECURITY.md));
  - be model-agnostic (principle G) — no provider hard-coded into the core;
  - be documented here with its purpose and schema.

## See also
- Roadmap: [`../ROADMAP.md`](../ROADMAP.md) (INTEGRATION v0.4, KNOWLEDGE v0.5).
