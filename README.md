# F85 | Agentic Climate Science | L3 Gold Standard | v1.0

A governed multi-agent reference system for climate evidence synthesis, model comparison, scenario analysis, uncertainty reasoning, attribution review, reproducibility, and qualified human scientific reporting.

## Research pipeline

- Problem formulation
- Data and provenance review
- Climate modeling
- Uncertainty analysis
- Scientific review

## Gold-standard research integrity

F85 is fail closed. Research release requires reviewed problem definition, data provenance, model assumptions, scenario definitions, uncertainty, attribution, reproducibility, and explicit qualified human approval.

Release is blocked for missing data provenance, invalid model assumptions, scenario mismatch, uncharacterized material uncertainty, attribution overclaiming, unsupported causal claims, reproducibility gaps, or unresolved contradictory evidence.

The reference system cannot fabricate evidence, hide uncertainty, claim certain attribution beyond the evidence, make binding policy mandates, or exercise autonomous scientific or policy authority.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

The behavioral verification layer includes eight direct climate-science governance tests and a 10-scenario held-out suite.
