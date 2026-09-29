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
- Cloud FinOps 2e derived textbook layer: 27 / 27 chapters
- permanent 27-chapter completion regression gate
- machine-readable JD learning coverage matrix
- named-tool / edge-topic JD registry
- JD-learning regression gate

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

The 100% figure means **mapping coverage of recurring market capabilities**, not hands-on mastery or full project completion.

Primary learning gaps identified from the versioned resume comparison were forecasting, technology budgeting, chargeback, commitment portfolio strategy, FinOps-specific governance/financial controls, procurement/vendor collaboration, realized-savings validation and FOCUS-style multi-cloud normalization.

## Checkpoint 3 — Source Register

```text
STATUS: COMPLETE FOR CURRENT MAPPING BASELINE
```

`docs/SOURCE_REGISTER.md` includes the current FinOps Framework and high-priority capability pages, Cloud FinOps 2nd Edition with its 2023 limitation, official AWS/Azure/Fabric/Snowflake/Databricks implementation guidance, and Grade A production anchors.

Evidence grades and source limitations are explicit. Grade D practitioner discussion remains hypothesis/failure-mode input only.

## Textbook Layer — Cloud FinOps 2nd Edition

```text
STATUS: COMPLETE DERIVED LEARNING LAYER
Chapters indexed: 27 / 27
Chapter notes completed: 27 / 27
Source locators present: 27 / 27
Completion regression gate: ENABLED
```

Artifacts:

- `research/books/cloud_finops_2e/BOOK_SOURCE_OF_TRUTH.md`
- `research/books/cloud_finops_2e/chapters/*.md`
- `tests/test_book_source_structure.py`

The current FinOps Framework remains authoritative for current taxonomy. The 2023 textbook layer provides conceptual depth and is reconciled where terminology evolved.

## JD Learning Coverage Layer

```text
STATUS: COMPLETE FOR LEARNING REPRESENTATION / N = 7 SNAPSHOT
Positive taxonomy requirements in canonical JD matrix: 48
Coverage rows: 48 / 48
Required representation per row:
  theory + explanation + example + step-by-step + interview
Supplemental named-tool / edge-topic terms: 24
Supplemental terms traceable to raw vacancy evidence: required by CI
```

Artifacts:

- `learning/JD_COVERAGE_MATRIX.csv`
- `learning/JD_SUPPLEMENTAL_TERMS.json`
- `learning/README.md`
- `docs/VOLUME_2_JD_COVERAGE_HANDBOOK.md`
- `docs/VOLUME_3_CERTIFICATION_INTERVIEW_TRANSFER.md`
- `tests/test_jd_learning_coverage.py`

The JD layer closes the learning-representation gaps found after auditing the beginner guide. It explicitly covers multi-cloud vocabulary, OCI/GCP working depth, Terraform, APIs, Bash/PowerShell, Tableau/Excel, Kubernetes, enterprise FinOps tools, vendor management, procurement/commercial collaboration, Spot, AI token economics, TCO/ROI, financial modelling, security/audit, stakeholder delivery and certification/interview transfer.

### Important interpretation

`COMPLETE` in `JD_COVERAGE_MATRIX.csv` means:

```text
the requirement is represented in the learning system
```

It does **not** mean:

```text
production mastery
or completed hands-on proof
or an earned certification
or realized financial impact
```

Those are separate evidence gates.

## CI state

GitHub-hosted Actions on `luqmanmang/finops_engineer` are operational. `Market Census Quality` runs all `test_*.py` files, including:

- market census quality gates;
- market-to-knowledge coverage;
- 27/27 textbook-note completion;
- JD learning coverage and supplemental source traceability.

## Next gate

**Hands-on proof coverage.**

Convert learning representation into reproducible evidence, prioritizing:

```text
AWS + Azure billing/cost pipeline
→ normalized Gold FinOps model
→ ownership/allocation reconciliation
→ Power BI persona views
→ forecast + budget variance
→ anomaly/RCA
→ rightsizing with SLA guardrail
→ RI/Savings Plan commitment model
→ Terraform/CI-CD cost guardrail
→ vendor/renewal commercial model
→ OCI/GCP normalization sample
→ interview scenario evidence
```

The next coverage metric should measure `hands_on_proof`, not repeat the already-complete learning-representation score.
