# FinOps Knowledge Map

## Purpose

This map reconciles the verified Malaysia `FinOps Engineer` market snapshot with the current FinOps Framework, *Cloud FinOps, 2nd Edition*, official provider implementation guidance, the learner's versioned resume, reproduction labs, and interview transfer.

The required chain is:

```text
VACANCY REQUIREMENT
→ FINOPS FRAMEWORK CAPABILITY
→ BOOK CHAPTER / CONCEPT
→ OFFICIAL PROVIDER IMPLEMENTATION
→ RESUME CAPABILITY / GAP
→ REAL CASE / PATTERN
→ DECISION TREE
→ LAB
→ SQL / PYTHON / IaC
→ POWER BI
→ INTERVIEW
```

## Evidence boundary

- Market snapshot date: **2026-09-30**.
- Verified active exact-title population: **N = 7**.
- One vacancy changes a frequency by about **14.29 percentage points**.
- Market percentages below describe this observed snapshot only; they are not presented as precise estimates of the entire Malaysia labour market.
- The current FinOps Framework is authoritative for current taxonomy. The 2023 textbook is used for conceptual depth and is explicitly subordinate where terminology has evolved.
- Resume status is based on the versioned `MASTER_RESUME_Raja_Luqman.md` retrieved for this checkpoint, not on unversioned conversational memory.
- `strong`, `partial`, and `gap` describe evidence already present in the resume; they do **not** claim mastery.

## Current FinOps Framework reconciliation

The current Framework organizes capabilities under four outcome domains:

1. **Understand Usage & Cost** — Data Ingestion, Allocation, Reporting & Analytics, Anomaly Management.
2. **Quantify Business Value** — Planning & Estimating, Forecasting, Budgeting, KPIs & Benchmarking, Unit Economics.
3. **Optimize Usage & Cost** — Architecting & Workload Placement, Usage Optimization, Rate Optimization, Licensing & SaaS, Sustainability.
4. **Manage the FinOps Practice** — Executive Strategy Alignment, FinOps Practice Operations, Governance, Policy & Risk, Education & Enablement, Invoicing & Chargeback, Assessment, Automation, Tools & Services, Intersecting Disciplines.

Do not force older Inform/Optimize/Operate chapter labels into capability names when the current Framework has a more specific capability. The phases remain useful as an iterative operating loop, while the domains/capabilities are the current taxonomy used by this map.

## Market-weighted learning tiers

### P0 — Deep: recurring in at least 5 of 7 vacancies

| Requirement | Market | Current Framework | Book backbone | Resume evidence | Required outcome |
|---|---:|---|---|---|---|
| Governance | 7/7 | Manage the FinOps Practice → Governance, Policy & Risk | Ch 7, 20, 21, 24 | Partial | Build policy, risk, ownership, exception, guardrail and review-cadence reasoning specific to technology spend |
| Forecasting | 6/7 | Quantify Business Value → Forecasting | Ch 13 | Gap | Forecast spend from historical cost plus business drivers, quantify variance and reforecast deliberately |
| Budgeting | 5/7 | Quantify Business Value → Budgeting | Ch 13, 20 | Gap | Separate budget from forecast; implement thresholds, alerts, ownership, escalation and corrective action |
| Chargeback | 5/7 | Manage the FinOps Practice → Invoicing & Chargeback; Understand → Allocation | Ch 11 | Gap | Reconcile provider bill, allocate shared cost, produce accountable billing and explain fairness/tradeoffs |
| Rightsizing | 5/7 | Optimize Usage & Cost → Usage Optimization | Ch 15 | Partial | Validate utilization, seasonality and SLA before change; prove financial result after implementation |
| Showback | 5/7 | Reporting & Analytics + Invoicing & Chargeback | Ch 8, 11 | Partial | Turn strong Power BI skill into ownership-aware technology-cost transparency and action workflows |

### P1 — Strong: recurring in 3–4 of 7 vacancies

| Requirement | Market | Framework | Book | Resume evidence | Required outcome |
|---|---:|---|---|---|---|
| Allocation | 4/7 | Allocation | Ch 11 | Partial | Account/subscription/tag/business hierarchy, shared-cost rules, allocation coverage KPI |
| Cost visibility | 4/7 | Data Ingestion + Reporting & Analytics | Ch 5, 8, 10 | Partial | Billing grain, effective/amortized cost, freshness, reconciliation, multi-cloud ownership dimensions |
| Reserved Instances | 4/7 | Rate Optimization | Ch 16–18 | Gap | Coverage/utilization, break-even, term risk, expiry and approval controls |
| Tagging | 4/7 | Allocation | Ch 12 | Partial | Required keys, inheritance, policy-as-code, exceptions and quality KPI |
| Anomaly management | 3/7 | Anomaly Management | Ch 10, 21, 22 | Partial | Cost baseline, materiality threshold, usage-vs-rate RCA, owner routing and validation loop |
| Savings Plans | 3/7 | Rate Optimization | Ch 16–18 | Gap | Eligible stable usage, lookback sensitivity, coverage/utilization, lock-in risk and comparable-post-period validation |

### P2 — Working/Strong: recurring in 2 of 7 vacancies

| Requirement | Market | Framework | Book | Resume evidence | Required outcome |
|---|---:|---|---|---|---|
| Cost analysis | 2/7 | Reporting & Analytics | Ch 5, 8, 10 | Strong | Transfer SQL/Python/RCA strength to provider billing semantics and FinOps KPIs |
| Procurement | 2/7 | Rate Optimization + Intersecting Disciplines + Governance | Ch 3, 16, 18, 20, 24 | Gap | Commercial alternatives, break-even, lock-in, approval owner and contract-risk reasoning |
| Unit economics | 2/7 | Unit Economics | Ch 22, 26 | Partial | Cost per business outcome; distinguish total-cost growth from improving unit economics |
| Vendor management | 2/7 | Governance, Policy & Risk + Rate Optimization + Intersecting Disciplines | Ch 3, 16, 18, 20 | Gap | Renewal/obligation tracking, pricing alternatives, vendor risk and realized-value review |

Machine-readable detail is in `market/market_to_knowledge_mapping.csv`.

## Knowledge coverage calculation

The recurring-responsibility denominator is every canonical FinOps capability with `count >= 2` in `market/finops_capability_frequency.csv`.

```text
Recurring market capabilities: 16
Mapped to current Framework: 16
Mapped to textbook concept/chapter: 16
Mapped to implementation path: 16
Mapped to resume capability/gap: 16
Mapped to lab or portfolio proof path: 16
Checkpoint 2 mapping coverage: 16 / 16 = 100%
```

This satisfies the **mapping** coverage target for recurring responsibilities. It does **not** mean the later hands-on, validation, dashboard and interview gates are already complete.

## Resume-to-market analysis

### Strong transfer assets already evidenced

- Python, PySpark/Pandas and SQL.
- AWS and Azure engineering.
- Terraform and GitHub Actions CI/CD.
- Power BI with advanced DAX/Power Query and governed security.
- ETL/ELT, dimensional modelling, reconciliation, data quality and observability.
- Production-style RCA and multi-million-row data work.
- Snowflake, Databricks and Microsoft Fabric.
- Cost-adjacent platform controls such as Snowflake auto-suspend / credit quota concepts and workload optimization.

### Partial transfer — technical base exists, FinOps operating proof is missing

- Governance → translate data/CI governance into technology-spend policy, exception and financial-risk controls.
- Rightsizing → translate performance tuning into utilization + SLA + cost decisioning.
- Cost visibility → translate pipelines/BI into cloud billing ingestion, effective/amortized cost and reconciliation.
- Allocation/tagging → translate dimensional/governance skills into ownership and shared-cost models.
- Showback → translate Power BI into accountable team/product cost views and action workflows.
- Anomaly management → translate monitoring/RCA into cost-specific materiality, routing and financial validation.
- Unit economics → translate business analytics into technology cost per product/transaction/business outcome.

### Highest-priority gaps to build

1. Forecasting and forecast variance.
2. Technology budgeting and escalation controls.
3. Chargeback and provider-invoice reconciliation.
4. Commitment portfolio management: RIs/Savings Plans, coverage/utilization, term risk and break-even.
5. FinOps-specific governance, policy, risk, exception and operating cadence.
6. Procurement/vendor/commercial collaboration.
7. Potential vs projected vs realized savings and comparable post-change billing validation.
8. FOCUS-style multi-cloud normalization and shared cost ownership.

## Interview-risk analysis

The most dangerous interview areas are where **market frequency is high but resume evidence is weak**:

| Risk area | Why it is risky | Proof required in this project |
|---|---|---|
| Forecasting | 6/7 demand; direct resume gap | Python/SQL forecast lab, variance analysis, Power BI forecast vs actual |
| Budgeting | 5/7 demand; direct resume gap | budget/alert lab with owner, threshold, escalation and action evidence |
| Chargeback | 5/7 demand; direct resume gap | allocation model that reconciles to source total and handles shared/unallocated cost |
| Governance | 7/7 demand; only partial FinOps evidence | policy/guardrail catalogue, CI/CD control, exception path, compliance KPI |
| Rightsizing | 5/7 demand; partial | utilization evidence, workload owner approval, SLA guardrail, rollback and realized outcome |
| Commitment strategy | RI 4/7 + SP 3/7; gap | modeled commitment decision; no real commitment purchase required |
| Showback/allocation | 5/7 + 4/7; partial | Gold ownership model + Power BI engineering/finance/leadership views |
| Cost anomaly/RCA | 3/7; partial | cost anomaly → isolate scope/service/resource/owner → cause → action → validation |

## Provider implementation matrix

| Capability family | AWS | Azure | Fabric | Snowflake | Databricks |
|---|---|---|---|---|---|
| Cost visibility / data | CUR/cost-management datasets and Cost Explorer-family analysis | Cost Management exports/views | Capacity Metrics / enterprise capacity views | Account usage and cost-management views | `system.billing.usage` and billing system tables |
| Allocation / showback / chargeback | Cost allocation tags and account hierarchy | Cost allocation rules, tags and billing scopes | Chargeback app pattern where applicable | Tags/resource attribution where available | Custom tags + billing system tables |
| Budgets / controls | Budget alerts and cost controls | Budgets and cost alerts | Capacity sizing/monitoring | Budgets and resource monitors | Account/workspace budgets and usage monitoring where available |
| Rightsizing / usage | Cost Optimization Hub/right-sizing recommendations | Advisor/cost optimization patterns | Capacity optimization | Warehouse sizing, auto-suspend and query/workload controls | Cluster/serverless workload optimization plus billing evidence |
| Commitments / rate | RI and Savings Plans analysis | Reservations/savings plan concepts | Capacity commitment/economic decision where applicable | Contract/credit economics are organization-specific | Contract/DBU economics are organization-specific |
| Anomaly / RCA | Cost Anomaly Detection | Cost alerts/anomaly capabilities | Capacity Metrics investigation | Usage/cost views + monitors | Billing tables + tags + workload metadata |

Provider recommendation is **input evidence**, never automatic authorization to change production. Every recommendation must pass workload owner, business/SLA, financial and rollback checks.

## Tool-depth decisions from N=7

- **Power BI — primary/deep:** 5/7. It remains the required primary dashboard.
- **Python — deep:** 4/7 and a strong existing skill; use for ingestion, anomaly analysis, forecast automation and evidence generation.
- **SQL — deep:** explicit in 3/7 but foundational to billing analysis and existing resume strength.
- **Terraform / CI/CD / automation — strong:** each appears materially and directly supports preventive guardrails.
- **API / Excel / Kubernetes — working depth:** useful but not the center of the learning path.
- **Tableau — secondary:** 3/7, but Source of Truth requires it only after Power BI is complete.
- **Bash — working:** low explicit frequency; useful operationally.
- **PowerShell — light:** only 1/7.
- **Bicep — defer:** 0/7 in this snapshot.

## Cloud/platform scope decision

Observed vacancy evidence contains AWS 7/7, Azure 5/7, OCI 4/7 and GCP 3/7. The locked project scope remains AWS + Azure + Fabric + Snowflake + Databricks. Therefore:

- AWS: deep hands-on.
- Azure: strong hands-on.
- OCI: awareness sufficient for interpreting market requirements; no large OCI lab is added by this checkpoint.
- GCP: awareness sufficient for cross-cloud terminology; no GCP-focused learning path is added.
- Fabric/Snowflake/Databricks: retained because they are locked project platforms and already evidenced in the resume, even though this N=7 vacancy snapshot does not name them frequently.

Changing hands-on cloud scope requires explicit change control; market observation alone does not silently rewrite the project architecture.

## Real-case anchors

The case layer remains separate from our reproduction labs.

- **ExxonMobil / AWS OLA** — rightsizing, licensing/storage/database optimization analysis and post-analysis validation pattern.
- **Arm / AWS** — semiconductor EDA, Spot and commitment-aware cost/performance tradeoff.
- **BP / Azure** — cloud governance and cost-management operating controls.
- **Vocus / AWS** — architecture/automation pattern with published cost reduction.
- Other verified seed cases from the Source of Truth remain candidates for Checkpoints 4–6 and must preserve SOURCE FACT vs OUR ANALYSIS vs OUR REPRODUCTION LAB boundaries.

No company architecture or behavior is inferred when a source does not disclose it.

## Lab mapping

| Lab | Primary market capability proof |
|---|---|
| `01_tagging` | allocation, tagging, showback foundation, governance |
| `02_budget_alert` | budgeting, anomaly/detective control, escalation |
| `03_rightsizing` | usage optimization / rightsizing with SLA guardrail |
| `04_incremental_vs_full` | unit economics, architecture cost tradeoff, workload efficiency |
| `05_idle_compute` | usage optimization / corrective governance |
| `06_storage_lifecycle` | usage optimization, lifecycle policy |
| `07_transfer` | architecture cost tradeoff / egress reasoning |
| `08_commitments` | RIs, Savings Plans, rate optimization, procurement/vendor risk |
| `09_forecast` | forecasting, variance, budget relationship |
| `10_cicd_guardrail` | governance, preventive policy-as-code, exception workflow |

All commitment labs are modeled unless safe credits/trials make real execution appropriate. Do not buy commitments merely to demonstrate the concept.

## Senior decision loop

Every critical topic should be practiced through the same decision contract:

```text
CONTEXT
→ SYMPTOM
→ SCOPE
→ OWNER
→ DATA
→ HYPOTHESIS
→ RCA
→ OPTIONS
→ ACTION
→ VERIFY TECHNICAL
→ VERIFY FINANCIAL
→ VERIFY BUSINESS / SLA
→ REALIZED OUTCOME
→ GUARDRAIL
```

This prevents the common failure mode of jumping from a cost spike directly to a tool recommendation.

## Checkpoint 2 conclusion

**Checkpoint 2 — Market-to-Knowledge Mapping: COMPLETE for the N=7 snapshot.**

- 16/16 recurring market capabilities are reconciled.
- Current Framework mappings are explicit.
- Book mappings are explicit and subordinate to the current Framework.
- Official implementation paths are explicit.
- Resume transfer/gap status is explicit.
- Lab/interview proof paths are explicit.
- Mapping coverage = **100% of recurring capabilities in the current verified snapshot**.

Next source-of-truth execution gate: populate and validate the source register, then perform canonical topic research with 3–4 strong sources per high-priority topic.
