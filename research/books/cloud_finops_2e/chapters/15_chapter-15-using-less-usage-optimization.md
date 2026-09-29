# Chapter 15 — Chapter 15. Using Less: Usage Optimization

> **Role:** Derived textbook source-of-truth note.  
> **Book source locator:** `OEBPS/ch15.xhtml`  
> **Source word count:** 10,797  
> **Copyright boundary:** This note records structure and derived analysis; it does not reproduce the chapter body.

## 1. Chapter Brief

_TODO — explain the chapter's purpose, scope, and why it matters to a FinOps Engineer._

## 2. Why This Chapter Matters

_TODO — connect the chapter to operational/business decisions._

## 3. Source Section Map

- Chapter 15. Using Less: Usage Optimization  `[OEBPS/ch15.xhtml]`
- The Cold Reality of Cloud Consumption  `[OEBPS/ch15.xhtml]`
      - Stories from the Cloud—Mike  `[OEBPS/ch15.xhtml]`
- Where Does Waste Come From?  `[OEBPS/ch15.xhtml]`
- Usage Reduction by Removing/Moving  `[OEBPS/ch15.xhtml]`
        - Tip  `[OEBPS/ch15.xhtml]`
- Usage Reduction by Resizing (Rightsizing)  `[OEBPS/ch15.xhtml]`
        - Tip  `[OEBPS/ch15.xhtml]`
      - Stories from the Cloud—Benjamin Coles  `[OEBPS/ch15.xhtml]`
- Common Rightsizing Mistakes  `[OEBPS/ch15.xhtml]`
- Relying on Recommendations That Use Only Averages or Peaks  `[OEBPS/ch15.xhtml]`
        - Figure 15-1. Graphs showing two CPU workloads: one has a short 90%+ peak and then remains at <10% for the rest of the hour, while the other is consistently at 20%  `[OEBPS/ch15.xhtml]`
- Failing to Rightsize Beyond Compute  `[OEBPS/ch15.xhtml]`
- Not Addressing Your Resource “Shape”  `[OEBPS/ch15.xhtml]`
- Not Simulating Performance Before Rightsizing  `[OEBPS/ch15.xhtml]`
        - Figure 15-2. Resizing based on averages will cause clipping  `[OEBPS/ch15.xhtml]`
- Hesitating Due to Reserved Instance Uncertainty  `[OEBPS/ch15.xhtml]`
- Going Beyond Compute: Tips to Control Cloud Costs  `[OEBPS/ch15.xhtml]`
- Block Storage  `[OEBPS/ch15.xhtml]`
  - Get rid of orphaned volumes  `[OEBPS/ch15.xhtml]`
        - Tip  `[OEBPS/ch15.xhtml]`
  - Focus on zero throughput or zero IOPS  `[OEBPS/ch15.xhtml]`
  - Make managing your block storage costs a priority  `[OEBPS/ch15.xhtml]`
  - Reduce the number of higher IOPS volumes  `[OEBPS/ch15.xhtml]`
  - Take advantage of elastic volumes  `[OEBPS/ch15.xhtml]`
- Object Storage  `[OEBPS/ch15.xhtml]`
  - Implement data retention policies  `[OEBPS/ch15.xhtml]`
  - Choose a storage tier/class that matches the data  `[OEBPS/ch15.xhtml]`
- Networking  `[OEBPS/ch15.xhtml]`
  - Clean up unused IP addresses  `[OEBPS/ch15.xhtml]`
  - Optimize network routes  `[OEBPS/ch15.xhtml]`
- Usage Reduction by Redesigning  `[OEBPS/ch15.xhtml]`
- Scaling  `[OEBPS/ch15.xhtml]`
- Scheduled Operations  `[OEBPS/ch15.xhtml]`
- Effects on Reserved Instances  `[OEBPS/ch15.xhtml]`
- Benefit Versus Effort  `[OEBPS/ch15.xhtml]`
- Serverless Computing  `[OEBPS/ch15.xhtml]`
- Not All Waste Is Waste  `[OEBPS/ch15.xhtml]`
        - Tip  `[OEBPS/ch15.xhtml]`
        - Tip  `[OEBPS/ch15.xhtml]`
- Maturing Usage Optimization  `[OEBPS/ch15.xhtml]`
- Advanced Workflow: Automated Opt-Out Rightsizing  `[OEBPS/ch15.xhtml]`
      - Stories from the Cloud—FinOps Community  `[OEBPS/ch15.xhtml]`
        - Figure 15-3. Schedule tracking of optimization tasks  `[OEBPS/ch15.xhtml]`
        - Figure 15-4. Automated rightsizing workflow  `[OEBPS/ch15.xhtml]`
        - Figure 15-5. Sample email notification for automated rightsizing  `[OEBPS/ch15.xhtml]`
- Tracking Savings  `[OEBPS/ch15.xhtml]`
        - Tip  `[OEBPS/ch15.xhtml]`
- Conclusion  `[OEBPS/ch15.xhtml]`

## 4. Core Concepts

_TODO — derived concept definitions, relationships, terminology, and mental models._

## 5. Detailed Explanation

_TODO — explain each major section in your own words, preserving the source's organization and intent._

## 6. Examples

_TODO — paraphrase source examples where useful, then add clearly labelled project examples._

## 7. Justification / Why the Approach Works

_TODO — why the book recommends or motivates the approach; separate source-derived rationale from project analysis._

## 8. Senior FinOps Approach

_TODO — how a senior IC should frame the decision before acting._

## 9. Step-by-Step Execution

```text
CONTEXT
→ BUSINESS QUESTION
→ DATA REQUIRED
→ HYPOTHESIS
→ ANALYSIS
→ OPTIONS
→ DECISION
→ IMPLEMENTATION
→ TECHNICAL VALIDATION
→ FINANCIAL VALIDATION
→ BUSINESS / SLA VALIDATION
→ GUARDRAIL
```

_TODO — specialize this sequence for the chapter._

## 10. Decision Rules

_TODO — when to use approach A/B, thresholds, escalation criteria, and decision ownership._

## 11. Trade-offs

_TODO — cost, performance, reliability, SLA, speed, lock-in, and organizational trade-offs._

## 12. Failure Modes / Edge Cases

_TODO — common mistakes, ambiguous cases, and conditions where the chapter's default approach may fail._

## 13. Data Required

_TODO — cost, usage, pricing, ownership, utilization, business-driver, contract, and operational data._

## 14. SQL / Python / IaC Application

_TODO — analyses and automation that belong in SQL, Python, Terraform/CI/CD, or are not applicable._

## 15. Provider Implementation

### AWS
_TODO_

### Azure
_TODO_

### Microsoft Fabric
_TODO where relevant_

### Snowflake
_TODO where relevant_

### Databricks
_TODO where relevant_

## 16. Stakeholder Perspective

- Engineering — _TODO_
- Finance — _TODO_
- Procurement — _TODO_
- Leadership / Business — _TODO_
- FinOps — _TODO_

## 17. Validation

- Technical validation — _TODO_
- Financial validation — _TODO_
- Business / SLA validation — _TODO_

## 18. KPIs

_TODO — metrics that prove progress/outcome, including denominator and grain._

## 19. Guardrails

- Preventive — _TODO_
- Detective — _TODO_
- Corrective — _TODO_

## 20. Real-World Implications

_TODO — connect to Grade A/B cases without inventing undisclosed company behavior._

## 21. FinOps Framework 2026 Reconciliation

_TODO — mark concepts as CURRENT / EVOLVED / SUPERSEDED / NEEDS RECONCILIATION._

## 22. Malaysia N=7 Market Relevance

_TODO — map only to verified vacancy signals; retain N=7 limitation._

## 23. Lab Mapping

_TODO — lab(s), synthetic fault(s), expected evidence, teardown/cost controls._

## 24. Power BI Mapping

_TODO — Diagnose → Hypothesis → Finding → Solution → Validation → Insight views/measures._

## 25. Interview Mapping

### 30-second answer
_TODO_

### 2-minute answer
_TODO_

### Senior follow-up
_TODO — WHAT / WHY / WHEN / HOW / TRADEOFF / VALIDATION / BUSINESS IMPACT._

## 26. Key Takeaways

_TODO — concise derived takeaways._

## 27. Source Locator

- EPUB file: `OEBPS/ch15.xhtml`
- Section headings and anchors are preserved above for traceability.
- Body text is intentionally not copied into this repository artifact.
