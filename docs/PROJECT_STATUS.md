# Project Status

## Locked / implemented

- repository architecture
- vacancy population contract
- raw/evidence separation
- vacancy ID contract
- deterministic vacancy classifier
- active/inactive and duplicate-underlying-vacancy gates
- canonical dataset builder
- derived frequency outputs
- certification-demand frequency output
- quality report contract
- unit-test suite
- GitHub Actions workflow definition
- practitioner-signal artifacts
- recommendation quality gate
- RACI working model
- operating cadence working model
- research questions
- market-to-knowledge mapping contract
- recurring-capability coverage test
- populated canonical source register

## Checkpoint 1 — Vacancy Census

```text
STATUS: COMPLETE / CURRENT VERIFIED PUBLIC SNAPSHOT N = 7
Snapshot date: 2026-09-30
Target requested: up to 50 active Malaysia exact-title FinOps Engineer vacancies
Raw candidate records: 9
Evidence records: 9
Verified active unique exact-title population: 7
Rejected/non-canonical: 2
  - 1 active duplicate/syndication
  - 1 inactive posting
Coverage: 7 / 50
```

The seven canonical opportunities are ExxonMobil, NTT DATA Services, Xsolla, International SOS, Coforge, Encora and Softenger.

The requested 50 is an upper target, not a quota. The project does not pad the census with mirrors, inactive roles, adjacent titles, non-Malaysia roles or fabricated records. Search and cross-source reasoning are recorded in `market/CENSUS_SEARCH_NOTES.md` and `market/SOURCE_CROSSCHECK_2026-09-30.md`.

Because N = 7, one vacancy moves a frequency by approximately 14.29 percentage points. Frequency tables are observed snapshot evidence, not a precise estimate of the entire Malaysia labour market.

## Checkpoint 2 — Market-to-Knowledge Mapping

```text
STATUS: COMPLETE FOR N = 7 SNAPSHOT
Recurring capability rule: market count >= 2
Recurring capabilities: 16
Framework mapped: 16 / 16
Book concept/chapter mapped: 16 / 16
Official implementation path mapped: 16 / 16
Resume capability/gap mapped: 16 / 16
Lab/interview proof path mapped: 16 / 16
Mapping coverage: 100%
```

Artifacts:

- `market/market_to_knowledge_mapping.csv`
- `docs/KNOWLEDGE_MAP.md`
- `docs/MARKET_INTERPRETATION.md`
- `tests/test_market_knowledge_map.py`

The 100% figure means **mapping coverage of recurring market capabilities**, not hands-on mastery or full project completion. Later hands-on, validation, dashboard and interview gates remain separate.

Primary learning gaps identified from the versioned resume comparison are forecasting, technology budgeting, chargeback, commitment portfolio strategy, FinOps-specific governance/financial controls, procurement/vendor collaboration, realized-savings validation and FOCUS-style multi-cloud normalization.

## Checkpoint 3 — Source Register

```text
STATUS: COMPLETE FOR CURRENT MAPPING BASELINE
```

`docs/SOURCE_REGISTER.md` now includes the current FinOps Framework and high-priority capability pages, Cloud FinOps 2nd Edition with its 2023 limitation, official AWS/Azure/Fabric/Snowflake/Databricks implementation guidance, and Grade A production anchors for ExxonMobil, Arm, BP and Vocus.

Evidence grades and source limitations are explicit. Grade D practitioner discussion remains hypothesis/failure-mode input only.

## CI state

GitHub-hosted Actions on `luqmanmang/finops_engineer` are operational. `Market Census Quality` runs all `test_*.py` files, including the market-to-knowledge coverage tests added in Checkpoint 2.

## Next gate

**Checkpoint 4 — Canonical Topic Research.**

For each high-priority topic, assemble and reconcile:

```text
current FinOps Framework
+ official implementation guidance
+ real named-company case where available
+ supporting engineering source
→ repeated pattern
→ decision tree
→ lab requirement
```

Start with the highest market-frequency / weakest-resume-proof topics: governance, forecasting, budgeting, chargeback/showback, rightsizing and commitment/rate optimization.
