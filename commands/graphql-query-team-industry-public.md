---
id: 123e4567-e89b-12d3-a456-426614174004
name: graphql-query-team-industry-public
type: command
executor: bash
data: >-
  curl -X POST https://api.hackerone.com/graphql -H "Content-Type:
  application/json" -d '{"query": "query
  {team(handle:\"example-public-team\"){_id,industry}}"}'
output: '{"data":{"team":{"_id":"example-id3","industry":null}}}'
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.938Z'
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

# graphql-query-team-industry-public

## Command

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"example-public-team\"){_id,industry}}"}'
```

## Description

This command queries a public or sandboxed team handle to contrast with private queries, expecting a null 'industry' field to validate the selective disclosure mechanism.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `https://api.hackerone.com/graphql` | Endpoint | Yes |
| `-H "Content-Type: application/json"` | Header | Yes |
| `-d '{...}'` | Payload | Yes |
| `handle: \"example-public-team\"` | Public team handle | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"example-public-team\"){_id,industry}}"}'
```

### Advanced Usage

Check for null:

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query {team(handle:\"example-public-team\"){_id,industry}}"}' | jq '.data.team.industry' | grep null
```

## Expected Output

{"data":{"team":{"_id":"example-id3","industry":null}}}.

## Related

- [[commands/graphql-query-team-industry-private1]]
- [[procedures/Query-HackerOne-GraphQL-Team-Industry]]
