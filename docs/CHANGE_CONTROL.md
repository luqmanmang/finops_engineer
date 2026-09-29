# Change Control

The project Source of Truth governs scope and standards.

Every material change should record:

```text
what changed
why
source/evidence
impact on curriculum
impact on labs
impact on repo
```

Do not silently change:

- vacancy inclusion criteria
- case-study evidence standard
- cloud scope
- validation standard
- dashboard priority
- definition of realized savings
- completion gates

## Recorded changes

### 2026-09-30 — Checkpoint 1 live census ingestion

- **What changed:** Added live Malaysia census records; added OCI as a market-observed cloud taxonomy signal; clarified syndication de-duplication; changed raw vacancy storage from preserving long vacancy prose to preserving source facts while paraphrasing long prose.
- **Why:** An active NTT DATA vacancy explicitly requires AWS + OCI, so omitting OCI would undercount observed market demand. Public-repository research should also avoid copying full job descriptions and should not multiply-count obvious syndications.
- **Source/evidence:** Active postings checked on 2026-09-30 from ExxonMobil Careers, NTT DATA Careers, Xsolla Lever Careers, LinkedIn JobScoper and LinkedIn Net2Source.
- **Curriculum/lab impact:** None yet. Market capture may include technologies outside the locked hands-on platform scope; curriculum weighting remains blocked until the census is assessed.
- **Repo impact:** Taxonomy/schema-derived columns and cloud-frequency logic must include OCI; raw/evidence records remain auditable and source-linked.
### 2026-09-30 — Census classifier calibration

- **What changed:** Added explicit certification-demand taxonomy/output and calibrated source-backed stakeholder wording for Finance, Engineering, Product/Business and Procurement.
- **Why:** The first deterministic build undercounted stakeholder collaboration and left certification demand as a placeholder even though active vacancies explicitly disclose both.
- **Impact:** `certification_frequency.csv` becomes a generated market artifact; stakeholder and certification tables now derive from the same audited raw records as other frequencies.

