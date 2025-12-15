---
id: proc-compare-graphql-results-001
name: Compare-Query-Results-for-Discrepancies
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.236Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - comparison
  - discrepancy
  - inference
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Compare-Query-Results-for-Discrepancies

## Summary

This procedure manually compares the results from baseline and Jira-sorted GraphQL queries to identify discrepancies in total_count and report listings, enabling inference of Jira ticket associations.

## Description

After executing both queries, review the JSON responses side-by-side. Differences in total_count or the presence of additional/duplicated reports in the jira_status sort indicate backend inclusion of Jira-linked reports. This side-channel leak exposes workflow details, such as which vulnerabilities are escalated to Jira, without direct access.

## Requirements

1. JSON outputs from prior queries saved (e.g., baseline.json and jira.json)
2. Text editor or diff tool (e.g., vimdiff, jq for parsing)
3. Understanding of report fields like title, substate

## Defense

Defensive measures and detection strategies:

- Ensure consistent total_count regardless of order_by to avoid side-channels
- Implement query normalization and logging for comparison patterns
- Train teams to avoid mixing restricted data in public APIs

## Objectives

1. Identify count and listing differences
2. Infer Jira usage on specific reports
3. Document leaked workflow information

## Instructions

### Step 1: Manual Review and Comparison

**Context**: Load both query responses and compare total_count, then inspect nodes for extras or reordering tied to null Jira fields.

**Command** (No specific command; use manual or tool-based diff):
```bash
# Example using jq to extract counts
jq '.data.reports.total_count' baseline.json
jq '.data.reports.total_count' jira.json

# Diff nodes if parsed
jq '.data.reports.nodes[] | {title, jira_escalation_state}' baseline.json > baseline_nodes.txt
jq '.data.reports.nodes[] | {title, jira_escalation_state}' jira.json > jira_nodes.txt
diff baseline_nodes.txt jira_nodes.txt
```

> Comparison reveals higher count in jira.json and additional reports with null jira_escalation_state, confirming inference.

### Step 2: Analyze for Inference

**Context**: Note reports unique to jira_status sort as likely Jira-linked.

> Cross-reference titles/usernames to map inferred statuses.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[comparison]]
- [[discrepancy]]
- [[inference]]
