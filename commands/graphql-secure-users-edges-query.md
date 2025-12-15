---
id: cmd-uuid-001
data: >-
  curl -X POST https://target.com/graphql -H "Content-Type: application/json" -H
  "Cookie: session=your_session" -d '{"query": "query { users() { edges { node {
  email } } } }"}'
tags:
  - graphql
  - baseline
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.500Z'
verified: false
validated: true
submitted: true
---
# graphql-secure-users-edges-query

## Command

```bash
curl -X POST https://target.com/graphql -H "Content-Type: application/json" -H "Cookie: session=your_session" -d '{"query": "query { users() { edges { node { email } } } }"}'
```

## Description

This command sends a GraphQL query using the 'edges' field on users() to demonstrate the authorized path, where attribute-level scrubbing is applied, typically returning limited or no sensitive data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method for GraphQL queries | Yes |
| `-H "Content-Type: application/json"` | Sets JSON payload format | Yes |
| `-H "Cookie: session=your_session"` | Provides authentication cookie | Yes |
| `-d '{...}'` | JSON-encoded query payload | Yes |
| `users() { edges { node { email } } }` | Queries users via edges, targeting email field | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/graphql -H "Content-Type: application/json" -H "Cookie: session=your_session" -d '{"query": "query { users() { edges { node { email } } } }"}'
```

### Advanced Usage

```bash
curl -X POST https://target.com/graphql -H "Content-Type: application/json" -H "Cookie: session=your_session" --data-urlencode 'query { users(first: 10) { edges { node { email username } } } }'
```

## Expected Output

JSON response like {"data":{"users":{"edges":[{"node":{"email":null}}]}}}, showing scrubbed or null values for sensitive fields due to authorization.

## Related

- [[commands/graphql-vulnerable-users-nodes-query]]
- [[procedures/Bypass-GraphQL-Authorization-Using-Nodes-Field-on-Users]]
