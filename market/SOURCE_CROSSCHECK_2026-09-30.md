# Checkpoint 1 Source Cross-Check — 2026-09-30

## Purpose

This pass was added after the first census build to explicitly cross-check major public job sources rather than relying only on broad web discovery. The objective is to distinguish a missing platform listing from an actually inactive requisition.

## Source hierarchy

For current-status decisions, evidence is interpreted in this order:

1. official employer careers / ATS;
2. direct employer LinkedIn requisition;
3. major job boards such as JobStreet and Indeed;
4. recruiter or regional job-board posting;
5. search-engine/indexed mirror used only as supporting evidence.

Absence from a lower-priority platform does not invalidate a live higher-priority requisition. Conflicting sources are recorded rather than silently reconciled.

## Dedicated platform pass

### JobStreet Malaysia

The exact-title pass surfaced the canonical ExxonMobil and NTT DATA FinOps Engineer roles. NTT DATA also appeared under two employer-name renderings with materially identical text; those are treated as one requisition, not two vacancies.

### Indeed Malaysia

The exact-title/employer pass confirmed ExxonMobil and Xsolla. Indeed currently shows a Coforge `FinOps Analyst (Hybrid Infrastructure)` role, but the direct LinkedIn Coforge requisition `4445718197` remains a separate live `FinOps Engineer` role and therefore remains canonical.

### Google Careers / Google-indexed search

Google Careers is Google's own employer career portal, not a universal job-board source. No Google-owned Malaysia `FinOps Engineer` vacancy was found. Broad Google-indexed/public-web discovery was still used to find and cross-check employer, recruiter and regional job-board pages.

## Canonical cross-source matrix

| ID | Company | Exact-title source | JobStreet | Indeed | Official/direct employer source | Cross-check result |
|---|---|---|---|---|---|---|
| MY-FE-0001 | ExxonMobil | Official ExxonMobil Careers | Confirmed | Confirmed | Confirmed official careers page | Strongly confirmed |
| MY-FE-0002 | NTT DATA Services | NTT DATA careers / JobStreet | Confirmed | Not surfaced in dedicated pass | Direct NTT careers URL retained in evidence | Confirmed; JobStreet independently corroborates |
| MY-FE-0003 | Xsolla | Xsolla Lever Careers | Not surfaced in dedicated pass | Confirmed | Confirmed official Lever/careers page | Strongly confirmed |
| MY-FE-0006 | International SOS | Direct-employer LinkedIn requisition | Not surfaced | Not surfaced | Public International SOS Malaysia careers list did not surface the role during recheck | Conflicting visibility; LinkedIn evidence retained and conflict documented |
| MY-FE-0007 | Coforge | Direct LinkedIn job ID 4445718197 | Not surfaced | Different `FinOps Analyst` requisition surfaced | LinkedIn requisition remained live with Apply and exact title | Confirmed as a distinct exact-title requisition |
| MY-FE-0008 | Encora | Regional job-board listing | Not surfaced | Not surfaced | No accessible employer ATS page found in this pass | Confirmed through current regional listing; medium evidence strength |
| MY-FE-0009 | Softenger | Current regional listing + Softenger recruiter signal | Not surfaced | Not surfaced | Softenger careers confirms Malaysia hiring locations but does not expose the exact role list | Confirmed through current recruiter/listing evidence; medium evidence strength |

## Non-canonical audit records

- `MY-FE-0004` JobScoper remains excluded as a duplicate/syndicated representation of the International SOS underlying role.
- `MY-FE-0005` Net2Source remains excluded because the verified postings were no longer accepting applications.

## Interpretation

The dedicated JobStreet, Indeed and Google/Google-indexed pass did not reveal a hidden population approaching 50 unique qualifying vacancies. It mainly corroborated existing canonical roles, exposed duplicate employer-name renderings, and highlighted source-visibility differences between platforms.

The canonical population therefore remains `N = 7` for this snapshot. The census must not be inflated by counting the same requisition once per platform or by replacing the locked exact-title rule with adjacent FinOps titles.
