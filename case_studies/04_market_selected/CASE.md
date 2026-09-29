# Case 04 — Carlsberg: FinOps Operating Model Across Visibility, Governance, Forecasting and Commitments

## Why this market-selected case

The N=7 vacancy snapshot repeatedly asks for governance, forecasting, budgeting, rightsizing, showback/allocation and commitment knowledge. Carlsberg's published Azure story covers several of those capabilities in one named-company production case.

## Evidence boundary

**Primary source:** Microsoft Customer Story — Carlsberg Group increases cloud efficiency with FinOps and Azure solutions  
https://www.microsoft.com/en/customers/story/18953-carlsberg-group-azure

**Evidence grade:** A.

## SOURCE FACT

- Carlsberg began its FinOps journey after a cloud-first Azure migration to gain cost visibility and rightsize resources.
- It used Microsoft Cost Management for usage/cost data and Azure Advisor for optimization recommendations.
- The source describes rightsizing, idle-capacity elimination, storage/backup optimization and resource snoozing.
- Azure Policy is used for governance and tagging across VMs/subscriptions.
- Carlsberg describes a deliberate commitment mix based on workload stability: longer-term reservations for stable workloads, shorter terms where flexibility is needed, and Savings Plans for more dynamic/seasonal workloads.
- The source reports 40–65% compute savings from its commitment approach and 7–10% annual savings from rightsizing/storage/reservations/snoozing-related optimizations.
- Tagging by team/group, subscription and workload supports ownership transparency.
- The organization uses Cost Management APIs/exports for custom dashboards and billing-center views for application owners.
- The source explicitly connects the operating model to budgeting and forecasting without cost spikes.

## Diagnose

The challenge was not one bad resource. Carlsberg needed an operating model that worked across visibility, workload optimization, governance, accountability and commercial commitments while respecting production needs and seasonal behavior.

## Hypothesis

### OUR ANALYSIS

If cost/usage data, ownership, policy enforcement, workload optimization and commitment decisions operate as one recurring FinOps loop, then savings should be more sustainable than one-off cleanup because future waste and accountability gaps are continually surfaced.

## Finding

### SOURCE FACT

The published story shows multiple FinOps mechanisms operating together: granular cost visibility, Advisor recommendations, policy/tagging, rightsizing/snoozing, reservations/Savings Plans, forecasting/budgeting, APIs and owner-facing views.

### OUR ANALYSIS

The transferable pattern is **portfolio segmentation**. Different workloads receive different controls and pricing strategies based on stability, seasonality, criticality and ownership—not one organization-wide optimization rule.

## Solution

### SOURCE FACT

Carlsberg combined Azure-native data, recommendations, policy, tagging, Hybrid Benefit, reservations/Savings Plans and owner-facing reporting.

### OUR REPRODUCTION LAB

Create a synthetic portfolio with:

- production / dev / sandbox classes;
- workload criticality and operating schedule;
- stable vs seasonal demand;
- owner/team tags;
- monthly cost/usage;
- rightsizing/snoozing eligibility;
- reservation/Savings Plan scenario;
- budget/forecast;
- policy compliance and exceptions.

Generate a decision table that recommends **different** actions by workload pattern.

## Validation

### SOURCE FACT

The story reports named savings ranges and operating outcomes, but the public source does not expose the full raw billing dataset required for independent recomputation.

### OUR REPRODUCTION VALIDATION

The lab must separately validate:

- allocation coverage;
- forecast variance;
- policy compliance;
- technical/SLA safety of snoozing or rightsizing;
- commitment coverage/utilization;
- projected versus simulated realized savings.

## Insight

The strongest interview lesson from Carlsberg is that mature FinOps is **not a cost-cutting queue**. It is a repeated decision system linking cost data, workload behavior, governance, ownership, financial planning and architecture.

## Interview transfer

Explain why stable and seasonal workloads should not receive identical commitment strategies; how tagging feeds accountability; why budget/forecast belongs beside optimization; how dev/sandbox scheduling differs from production controls; and why policy/automation needs exceptions and workload context.

## Project mapping

- Market capabilities: governance, forecasting, budgeting, rightsizing, tagging, showback, commitments, cost visibility.
- Labs: `01_tagging`, `02_budget_alert`, `03_rightsizing`, `05_idle_compute`, `08_commitments`, `09_forecast`, `10_cicd_guardrail`.
- Power BI: executive, finance and engineering persona pages.
