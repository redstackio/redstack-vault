---
id: cmd-graphql-baseline-001
name: graphql-query-reports-by-id
type: command
executor: bash
data: >-
  curl -X POST https://api.hackerone.com/graphql -H "Authorization: Bearer
  YOUR_TOKEN" -H "Content-Type: application/json" -d '{"query": "{
  reports(where: {team: {handle: {_eq: \"team_handle\"}}}, order_by: {direction:
  ASC, field: id}) { total_count nodes { substate jira_escalation_state
  jira_escalation_last_state_change_at created_at disclosed_at
  extracted_report_data { hosts } title url team { handle } reporter { username
  } } } }"}'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.234Z'
platforms:
  - Web
tags:
  - graphql
  - query
verified: false
validated: true
submitted: true
---

# graphql-query-reports-by-id

## Command

```bash
curl -X POST https://api.hackerone.com/graphql \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ reports(where: {team: {handle: {_eq: \"team_handle\"}}}, order_by: {direction: ASC, field: id}) { total_count nodes { substate jira_escalation_state jira_escalation_last_state_change_at created_at disclosed_at extracted_report_data { hosts } title url team { handle } reporter { username } } } }"}'
```

## Description

This command sends a GraphQL query to HackerOne's API to fetch reports for a team, ordered by ID ascending, establishing a baseline for access control testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `YOUR_TOKEN` | Authentication bearer token | Yes |
| `team_handle` | Handle of the target team (e.g., redacted as ██████) | Yes |
| `where` | Filter clause for team equality | Yes |
| `order_by` | Sorting by id ASC | Yes |
| `total_count` | Field to retrieve matching report count | Yes |
| `nodes` | Array of report objects with specified fields | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api.hackerone.com/graphql -H "Authorization: Bearer token123" -H "Content-Type: application/json" -d '{"query": "{ reports(where: {team: {handle: {_eq: \"test-team\"}}}, order_by: {direction: ASC, field: id}) { total_count nodes { title } } }"}'
```

### Advanced Usage

Include full fields as in the data for detailed report info.

## Expected Output

JSON response like: {"data":{"reports":{"total_count":10,"nodes":[{"title":"Report 1","jira_escalation_state":null},...]}}}

## Related

- [[commands/graphql-query-reports-by-jira-status]]
- [[procedures/Query-Reports-Ordered-by-ID]]
