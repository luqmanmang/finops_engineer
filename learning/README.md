# Learning Coverage System

This directory is the machine-readable bridge between the verified Malaysia FinOps Engineer market snapshot and the learning artifacts in this repository.

## Three-volume learning model

```text
VOLUME 1 — Zero-to-Production Beginner Guide
  fundamentals → billing → allocation → budget/forecast → RCA → optimization

VOLUME 2 — JD Coverage Handbook
  multi-cloud → Terraform/API/shells → vendor tools → vendor management
  → AI token economics → TCO/ROI → security/audit → stakeholder/project delivery

VOLUME 3 — Certification & Interview Transfer
  FOCP/cloud/security/Power BI signals → answer structures → honesty rules
```

## Machine-readable artifacts

### `JD_COVERAGE_MATRIX.csv`

One row for every positive taxonomy requirement in `market/vacancy_skill_matrix.csv`.

The matrix separates:
- learning depth,
- theory/explanation/example/step-by-step representation,
- lab/proof path,
- dashboard relevance,
- interview transfer,
- learning status.

`COMPLETE` means the requirement is represented in the learning system. It does **not** mean production mastery, an earned certification, or completed hands-on evidence.

### `JD_SUPPLEMENTAL_TERMS.json`

Tracks named tools and JD-specific edge topics that do not have dedicated columns in the canonical skill matrix, for example CloudHealth, Apptio/Cloudability, Flexera, Finout, Kubecost, BigQuery, AI token cost management, TCO/ROI, Spot, Helm/GitOps, PMP/PRINCE2 and Agile/Scrum.

Each term must remain traceable to at least one canonical raw vacancy and to a teaching artifact.

## Regression gate

`tests/test_jd_learning_coverage.py` fails when:

- a positive `vacancy_skill_matrix.csv` field has no coverage row;
- the stored observed count drifts from the canonical matrix;
- theory/explanation/example/step-by-step/interview representation disappears;
- a declared artifact does not exist;
- a supplemental named term cannot be found in its declared raw vacancy source;
- a supplemental named term disappears from Volume 2;
- certification requirements stop mapping to Volume 3.

## Coverage vs proof

Do not collapse these two concepts:

```text
LEARNING REPRESENTATION
"I understand and can explain the requirement"

HANDS-ON PROOF
"I built/tested/validated the requirement in a reproducible artifact"
```

The next project phase should increase hands-on proof coverage without weakening the market evidence boundary.
