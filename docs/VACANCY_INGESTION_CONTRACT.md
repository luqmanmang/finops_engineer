# Vacancy Ingestion Contract

## Purpose

Create one repeatable path from a live Malaysia FinOps Engineer vacancy to auditable market datasets.

## Lifecycle

```text
DISCOVER
  ↓
ASSIGN IMMUTABLE ID
  ↓
CAPTURE SOURCE-DERIVED FIELDS
  ↓
VERIFY ACTIVE + TITLE + MALAYSIA SCOPE
  ↓
RUN VALIDATION
  ↓
CLASSIFY SKILLS/CAPABILITIES
  ↓
CANONICAL POPULATION
  ↓
AGGREGATE FREQUENCIES
  ↓
MARKET ANALYSIS
```

## Step 1 — Assign ID

Use the next unused ID, for example `MY-FE-0001`. ID behaves like a primary key and must never be recycled for another vacancy.

## Step 2 — Raw record

Copy `market/templates/vacancy_record.template.json` to `market/raw/MY-FE-0001.json`.

Populate source-derived facts. Preserve exact names, technologies, qualifications and short evidence phrases, but paraphrase long copyrighted vacancy prose before committing it to the public repository. Keep source facts separate from interpretation.

Where the same underlying vacancy is syndicated across multiple job boards or recruiter URLs, keep one canonical vacancy record when employer, role, location and materially identical description indicate the same opening. Record the chosen source URL and avoid inflating market frequency with duplicate syndications.

## Step 3 — Evidence record

Copy `market/templates/evidence_record.template.json` to `market/evidence/MY-FE-0001.json`.

Record the verification timestamp and evidence for active status, exact title, and Malaysia scope.

## Step 4 — Pre-build validation

```bash
make market-check
```

Fix hard contract failures before building derived outputs.

## Step 5 — Deterministic classification

The builder scans the four source-text fields against `market/schemas/signal_taxonomy.json`. A keyword match creates a candidate signal. Use `manual_overrides` only to document a source-backed correction to deterministic classification; do not silently hand-edit generated CSV columns.

## Step 6 — Eligibility gate

Canonical inclusion requires all of the following:

```text
raw.active_status = true
AND evidence.active_status = true
AND raw.job_title contains contiguous "FinOps Engineer"
AND evidence.title_verified = true
AND evidence.malaysia_verified = true
AND raw.job_url = evidence.job_url
AND raw.source = evidence.source
AND vacancy_id unique
AND job_url unique
```

Related titles are valid research leads but are not canonical census members.

## Step 7 — Build

```bash
make market-build
```

Generated outputs include the canonical CSV/JSON, skill matrix, FinOps capability, cloud, platform, language, BI-tool, industry and seniority frequencies, the quality report and `docs/MARKET_ANALYSIS.md`.

## Step 8 — Review QA report

Never quote the requested target as though it were observed market size. Report exactly:

```text
Target population requested: 50
Verified active exact-title population: N
Coverage achieved: N / 50
```

## Source fact vs derived analysis

### Source fact

Title, employer, location, source URL, active-state evidence and source-backed technologies/requirements.

### Deterministic derived signal

Keyword-classified fields such as `terraform = true` or `rightsizing = true`.

### Human analysis

Why the market signal matters, interview-risk interpretation, learning priority and resume gap.

Do not collapse these three layers into one.

## Change control

When a vacancy expires later, do not delete its historical ID. Update/recheck the research record according to the study methodology. The canonical active census should always represent the intended collection snapshot, while source history remains traceable in Git.
