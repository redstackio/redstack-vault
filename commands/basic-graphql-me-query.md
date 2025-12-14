---
id: cmd-basic-graphql-me
data: >-
  curl -X POST https://api.hackerone.com/graphql -H "Content-Type:
  application/json" -H "Authorization: Bearer YOUR_TOKEN" -d '{"query": "query {
  me { id } }"}'
tags:
  - graphql
  - auth-test
  - curl
type: command
output: '{"data":{"me":{"id":"123"}}}'
executor: bash
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.556Z'
verified: false
validated: true
submitted: true
---
# basic-graphql-me-query

## Command

```bash
curl -X POST https://api.hackerone.com/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"query": "query { me { id } }"}'
```

## Description

This command tests authentication and connectivity to the HackerOne GraphQL API by querying the current user's ID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP POST method | Yes |
| `-H "Content-Type: application/json"` | JSON header | Yes |
| `-H "Authorization: Bearer YOUR_TOKEN"` | Auth token | Yes |
| `-d '{...}'` | Query payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query { me { id } }"}'
```

### With Auth

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN" -d '{"query": "query { me { id name } }"}'
```

## Expected Output

{"data":{"me":{"id":"123"}}} or null if unauthenticated.

## Related

- [[Related Procedure: Prepare GraphQL Client for HackerOne API]]
