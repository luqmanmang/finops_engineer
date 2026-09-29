# Chapter 17 — Chapter 17. Understanding Commitment-Based Discounts

> **Role:** Derived textbook source-of-truth note.  
> **Book source locator:** `OEBPS/ch17.xhtml`  
> **Source word count:** 9,732  
> **Source boundary:** The owned 2023 EPUB is paraphrased. Provider mechanics must be rechecked against current official documentation before implementation.

## 1. Chapter Brief

This chapter explains commitment-based discount mechanics across major cloud providers: scope, term, payment model, size flexibility, conversion/cancellation, sharing, account affinity, and the difference between resource-based and spend-based constructs.

## 2. Why This Chapter Matters

Commitments can produce large rate reductions, but an incorrect purchase can lock in spend after a workload changes. A senior FinOps Engineer therefore needs to understand what the instrument actually covers, who receives the benefit, who carries the cost, and what happens when architecture or demand changes.

## 3. Source Section Map

- Commitment-Based Discount Basics `[OEBPS/ch17.xhtml]`
- Compute Instance Size Flexibility `[OEBPS/ch17.xhtml]`
- Conversions and Cancellations `[OEBPS/ch17.xhtml]`
- AWS Reserved Instances / Savings Plans `[OEBPS/ch17.xhtml]`
- Member Account Affinity / Sharing `[OEBPS/ch17.xhtml]`
- Azure Reservations / Savings Plans `[OEBPS/ch17.xhtml]`
- Google CUDs / Flexible CUDs `[OEBPS/ch17.xhtml]`

## 4. Core Concepts

- A commitment discount is a pricing instrument, not a resource.
- **Coverage** asks how much eligible usage is discounted; **utilization** asks how much purchased commitment is actually consumed.
- Narrower scope can increase discount depth but usually increases stranded-risk.
- Spend-based constructs are typically more flexible than narrowly resource-based constructs, but eligibility still matters.
- Size flexibility, sharing, region/family/OS constraints, conversion rights and cancellation rules differ by provider and product.
- Central ownership is useful because isolated account-level purchasing can fragment demand and hide enterprise risk.

## 5. Detailed Explanation

### SOURCE-DERIVED

The chapter compares the mechanics of the large-provider programs and repeatedly shows that apparently similar commitment products are not equivalent. The practical lesson is to understand eligibility, scope and benefit application before purchase.

### PROJECT EXPLANATION

For this repo, every commitment object should be modeled with explicit fields: provider, product, service, scope, region, family, term, start/end, payment type, eligible usage, sharing rule, flexibility, owner and current effective benefit. This turns commercial constructs into auditable data rather than tribal knowledge.

## 6. Examples

- A regional resource-specific commitment can become underutilized after migration to another architecture.
- A broader spend-based plan may accept more eligible compute shapes, reducing stranded-risk while still requiring enough eligible spend.
- A centrally purchased commitment may benefit multiple linked accounts; internal showback/chargeback still needs a rule for allocating both commitment cost and savings.

## 7. Justification

Headline discount is not realized value. Real value depends on eligible usage continuing to exist. Modeling eligibility and sharing is therefore necessary to explain why a portfolio can show high “discount percentage” while still wasting money.

## 8. Senior FinOps Approach

1. Inventory every commitment and its exact terms.
2. Build an eligibility matrix by provider/service/region/family/license/scope.
3. Normalize actual usage to the same dimensions.
4. Calculate hourly/daily coverage, utilization, unused commitment cost and effective savings.
5. Overlay planned migrations, rightsizing and decommissions.
6. Define purchase authority, benefit sharing, renewal and expiry ownership.
7. Monitor continuously and rebalance where the product allows it.

## 9. Step-by-Step Execution

```text
INVENTORY
→ ELIGIBILITY MODEL
→ NORMALIZED USAGE
→ COVERAGE + UTILIZATION
→ ARCHITECTURE ROADMAP
→ RISK SCENARIOS
→ PURCHASE / HOLD / EXCHANGE DECISION
→ COST ALLOCATION
→ CONTINUOUS MONITORING
→ RENEW / REBALANCE / EXPIRE
```

## 10. Decision Rules

- Prefer broader/flexible constructs when architecture volatility is high.
- Prefer narrower constructs only when stable demand and scope are strongly evidenced.
- Never assume similarly named AWS/Azure/GCP constructs behave the same.
- Do not purchase against peak usage; identify stable eligible baseline.
- Block new purchases when known rightsizing/decommission work would invalidate the baseline.

## 11. Trade-offs

| Choice | Benefit | Risk |
|---|---|---|
| Narrow resource commitment | stronger rate potential | stranded if architecture changes |
| Broad spend commitment | flexibility | may offer different discount depth |
| Long term | higher potential discount | longer lock-in |
| Central portfolio | economies of scale | needs fair internal allocation |
| On-demand | flexibility | higher rate |

## 12. Failure Modes / Edge Cases

- Confusing coverage with utilization.
- Ignoring sharing/account-affinity settings.
- Treating commitment as if it “moves with” a workload automatically.
- Missing OS/license eligibility.
- No expiry/renewal owner.
- Counting negotiated discount and commitment benefit twice.
- Using historical peak as stable baseline.

## 13. Data Required

- commitment inventory and terms
- eligible usage by hour/day
- provider/account/subscription/project hierarchy
- normalized instance/compute attributes
- amortized/effective cost
- sharing configuration
- renewal/expiry dates
- architecture roadmap and forecast

## 14. SQL / Python / IaC Application

- **SQL:** map usage to eligibility, calculate coverage/utilization and unused cost.
- **Python:** provider-specific eligibility logic, scenario stress tests, expiry alerts and portfolio simulation.
- **IaC/CI:** expose planned architecture changes early; do not hard-code commercial purchases into deployment automation without governance.

## 15. Provider Implementation

The 2023 book contains detailed AWS, Azure and Google mechanics, but those mechanics are time-sensitive. Use the chapter as the conceptual model and validate current official product rules before any purchase. For Fabric/Snowflake/Databricks, apply the same portfolio principles to committed capacity/spend constructs where supported.

## 16. Stakeholder Perspective

- Engineering: future usage and architecture flexibility.
- Finance: cash/expense view and forecast.
- Procurement: commercial terms and negotiations.
- Leadership: risk appetite and strategic provider direction.
- FinOps: centralized model, recommendation and monitoring.

## 17. Validation

Technical: eligible workload behavior remains as expected.  
Financial: effective savings and unused commitment reconcile to billing.  
Business: flexibility retained at an acceptable risk level.

## 18. KPIs

- commitment coverage %
- commitment utilization %
- unused commitment cost
- effective savings rate
- on-demand spillover
- days to expiry
- stranded commitment exposure

## 19. Guardrails

Preventive: purchase thresholds, architecture-change review, minimum utilization assumptions.  
Detective: low-utilization/expiry/drift alerts.  
Corrective: exchange/rebalance/stop renewal where product rules allow.

## 20. Real-World Implications

Only use published cases for facts they disclose. Keep provider-program mechanics separate from company-specific production evidence.

## 21. FinOps Framework 2026 Reconciliation

**EVOLVED.** The old standalone commitment-management capability is now represented inside the current **Rate Optimization** capability. The mechanics remain important, but commitments are now explicitly treated as one rate lever alongside negotiated discounts, Spot and other pricing mechanisms.

## 22. Malaysia N=7 Market Relevance

Supports recurring requirements around reservations/commitments, rate optimization, vendor/procurement collaboration and governance. With N=7, frequency is a prioritization signal only.

## 23. Lab Mapping

Create hourly eligible usage plus multiple commitment objects with different scopes. Calculate coverage, utilization, unused cost and realized savings. Inject a migration that strands one instrument and a sharing-policy change that moves the benefit.

## 24. Power BI Mapping

Portfolio dashboard: coverage, utilization, unused cost, on-demand spill, expiry ladder, owner/account/service drill-through and stranded-risk alerts.

## 25. Interview Mapping

### 30-second answer

I treat commitments as pricing instruments, not infrastructure. I model exactly what each instrument can cover, map actual usage to that eligibility, track both coverage and utilization, and stress-test architecture changes before purchase. I manage expiry and benefit allocation centrally and validate realized savings rather than quoting headline discounts.

### 2-minute structure

`WHAT → PRODUCT MECHANICS → ELIGIBILITY → DATA → RISK → PURCHASE → MONITOR → VALIDATE`

### Senior follow-up

Be ready to explain why 95% coverage can still be bad if utilization is poor, and why a smaller/flexible purchase can create more business value than maximizing headline discount.

## 26. Key Takeaways

- Commitment value depends on eligibility and continued demand.
- Coverage and utilization answer different questions.
- Provider constructs must not be treated as equivalent.
- Architecture roadmap is part of the purchase decision.
- Portfolio monitoring continues after purchase.

## 27. Source Locator

- EPUB: `OEBPS/ch17.xhtml`
- Current Framework mapping is based on 2026 FinOps Foundation guidance, not attributed to the 2023 book.
