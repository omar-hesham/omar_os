---
workflow: Research
status: specification (v0.1)
---

# Research Workflow

Evidence gathering per the evidence hierarchy (constitution principle E) and the
verify-before-assume rule (principle C). Implements the Researcher role
([`../agents/researcher.md`](../agents/researcher.md)).

## Steps

1. **Define questions** — what must be known to decide or build?
2. **Search by tier**, preferring higher tiers (this is the *procedural application* of
   constitution principle E; the canonical order is defined once in the constitution, not
   re-stated as authority here):
   1. Original / official source
   2. Project source data / documentation
   3. Reputable secondary source
   4. Inference
   5. Assumption
3. **Evaluate reliability** and cite the authoritative source.
4. **Label material claims**: *verified fact* / *inference* / *assumption* / *opinion* —
   at minimum for claims that affect a decision.
5. **Flag gaps** where verification is not reasonably possible.
6. **Summarize** with citations and confidence labels.
7. **Promote** reusables to knowledge (Knowledge Curator).

## Output

An evidence summary that the Architect and Planner can rely on, with explicit confidence so
no one mistakes an assumption for a verified fact.

## Status

Specification only. Automated research/retrieval is future (ROADMAP v0.6+).
