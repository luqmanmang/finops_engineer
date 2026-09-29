# FinOps Engineer Field Lab

Portfolio + learning repository for a Data Engineering → FinOps Engineering transition.

## Repository flow

```text
Vacancy sources
  → market/raw
  → market/evidence
  → validation gates
  → canonical vacancy dataset
  → skill/capability frequency outputs
  → docs/MARKET_ANALYSIS.md
  → knowledge map + textbook notes + case studies
  → JD learning coverage system
  → labs + Power BI
  → interview evidence
```

## Core rules

- Malaysia vacancy census targets active roles whose job title contains the contiguous phrase `FinOps Engineer`.
- Do not pad the dataset with related job titles if the verified population is smaller than the target.
- Keep source facts, analysis, and reproduction labs separate.
- Keep potential, projected, and realized savings separate.
- Every optimization lab must validate cost, technical, and business/SLA impact where applicable.
- Learning coverage is not the same as hands-on mastery, production experience or an earned certification.

## Learning path

The repository now uses a three-volume learning model:

```text
VOLUME 1 — Zero-to-Production Beginner Guide
  fundamentals → billing → allocation → budget/forecast → RCA → optimization

VOLUME 2 — JD Coverage Handbook
  multi-cloud → Terraform/API/shells → vendor tools → vendor management
  → AI token economics → TCO/ROI → security/audit → stakeholder/project delivery

VOLUME 3 — Certification & Interview Transfer
  FOCP/cloud/security/Power BI signals → answer structures → honesty rules
```

Key files:

- `research/books/cloud_finops_2e/BOOK_SOURCE_OF_TRUTH.md` — 27-chapter textbook-layer inventory.
- `docs/KNOWLEDGE_MAP.md` — market → Framework → book → implementation → lab/interview mapping.
- `docs/VOLUME_2_JD_COVERAGE_HANDBOOK.md` — literal N=7 JD coverage beyond the beginner core.
- `docs/VOLUME_3_CERTIFICATION_INTERVIEW_TRANSFER.md` — certification and interview bridge.
- `learning/JD_COVERAGE_MATRIX.csv` — machine-readable coverage for every positive taxonomy field in the canonical JD matrix.
- `learning/JD_SUPPLEMENTAL_TERMS.json` — named tools and edge topics from raw JD evidence.
- `tests/test_jd_learning_coverage.py` — regression gate preventing silent JD-learning gaps.

The current coverage gate checks **learning representation**, not completed hands-on proof. Later labs must still demonstrate implementation and validation.

## Market census commands

```bash
make market-check   # validate raw + evidence without writing derived outputs
make market-build   # rebuild canonical datasets, frequencies, QA report and market analysis
make test           # run unit tests, including book + JD-learning coverage gates
```

Python 3.12+ is recommended. The market census builder uses only the Python standard library.

## Vacancy ingestion contract

Every candidate vacancy uses the same ID in both locations:

```text
market/raw/MY-FE-0001.json
market/evidence/MY-FE-0001.json
```

A record reaches the canonical population only when all gates pass:

```text
valid raw record
+ matching evidence record
+ active vacancy
+ exact contiguous title phrase "FinOps Engineer"
+ Malaysia scope verified
+ matching URL/source
+ unique vacancy ID and URL
= canonical record
```

See `docs/VACANCY_INGESTION_CONTRACT.md` for the full workflow.

## Main areas

- `market/` — vacancy census, raw evidence, canonical datasets, derived matrices and frequencies.
- `learning/` — machine-readable JD coverage and named-tool/edge-topic coverage.
- `docs/` — analysis, knowledge map, JD handbook, certification/interview transfer, KPI dictionary, decision trees, guardrails and source register.
- `research/` — framework, textbook layer, provider documentation and published company cases.
- `case_studies/` — deep case-study work.
- `labs/` — reproducible FinOps experiments.
- `data/` — lab/project data lifecycle: raw → bronze → silver → gold.
- `sql/`, `python/`, `terraform/`, `bash/`, `powershell/` — implementation artifacts by language/tool.
- `powerbi/`, `tableau/` — dashboard artifacts.
- `evidence/` — baselines, experiments, validation outputs and screenshots.
- `interview/` — question bank, scenarios and answer cards.
