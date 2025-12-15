---
id: proc-graphql-baseline-query-001
name: Query-Reports-Ordered-by-ID
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.239Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - graphql
  - query
  - baseline
commands:
  - '[[commands/graphql-query-reports-by-id]]'
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Query-Reports-Ordered-by-ID

## Summary

This procedure queries HackerOne's GraphQL API for reports on a specific team, ordered by the 'id' field, to establish a baseline count and listing of accessible reports without triggering Jira-related data exposure.

## Description

In the context of testing access controls in HackerOne's API, this step fetches reports filtered by team handle and sorted ascending by ID. It retrieves total_count and detailed nodes, confirming what an unauthorized user can normally see. This serves as the control for comparing against restricted field sorts, revealing discrepancies due to improper backend JOINs on Jira data.

## Requirements

1. Authenticated HackerOne user session (without Jira access)
2. Knowledge of a test team handle
3. Access to GraphQL endpoint via HTTP client

## Defense

Defensive measures and detection strategies:

- Implement field-level authorization in GraphQL resolvers to block sorting on restricted fields like jira_status
- Monitor API queries for unusual order_by parameters and log discrepancies in response counts
- Use rate limiting on GraphQL queries to prevent enumeration attempts

## Objectives

1. Retrieve baseline report data for a team
2. Verify absence of Jira fields in response
3. Prepare for comparison with restricted sorts

## Instructions

### Step 1: Execute Baseline GraphQL Query

**Context**: Send a POST request to the GraphQL endpoint with the baseline query to fetch reports ordered by ID.

**Command** ([[commands/graphql-query-reports-by-id]]):
```bash
curl -X POST https://api.hackerone.com/graphql \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ reports(where: {team: {handle: {_eq: \"team_handle\"}}}, order_by: {direction: ASC, field: id}) { total_count nodes { substate jira_escalation_state jira_escalation_last_state_change_at created_at disclosed_at extracted_report_data { hosts } title url team { handle } reporter { username } } } }"}'
```

> This command authenticates and queries for reports, expecting a JSON response with total_count and nodes array showing standard report details, all Jira fields null.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/graphql-query-reports-by-id]]

## Tools Used


## Tags

- [[graphql]]
- [[query]]
- [[baseline]]
