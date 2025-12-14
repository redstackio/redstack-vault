---
id: cmd-query-deprecated-team
data: >-
  curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json"
  -d '{"query": "query
  {team(handle:\"security\"){id,_id,about,base_bounty,bug_count}}"}' -o
  team_data.json
tags:
  - graphql
  - deprecated
type: command
output: >-
  {"data": {"team": {"id": "Z2lkOi8vaGFja2Vyb25lL1RlYW0vMTM=", "_id": "13",
  "about": "Vulnerability disclosure should be safe, transparent, and
  rewarding.", "base_bounty": 500, "bug_count": 236 }}}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.423Z'
verified: false
validated: true
submitted: true
---
# query-deprecated-team-node

## Command

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"security\"){id,_id,about,base_bounty,bug_count}}"}' -o team_data.json
```

## Description

Queries a deprecated GraphQL root node 'team' to fetch details using a specific handle, exposing internal data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `handle:\"security\"` | Team identifier in the query | Yes |
| Fields: id,_id,about,base_bounty,bug_count | Specific fields to retrieve | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"security\"){id,_id}}"}'
```

### Advanced Usage

Query multiple fields as shown.

## Expected Output

{"data": {"team": {"id": "Z2lkOi8vaGFja2Vyb25lL1RlYW0vMTM=", "_id": "13", "about": "Vulnerability disclosure should be safe, transparent, and rewarding.", "base_bounty": 500, "bug_count": 236 }}}

## Related

- [[commands/graphql-introspection-query]]
- [[procedures/Query-Deprecated-Root-Nodes]]
