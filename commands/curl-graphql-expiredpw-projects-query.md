---
data: >-
  curl --request POST --url https://gitlab.domain.com/api/graphql --header
  'Authorization: Bearer <TOKEN>' --header 'Content-Type: application/json'
  --data '{"query":"query {\n projects{\n nodes{\n id\n name\n }\n }\n}"}'
tags:
  - graphql
  - expired-password
type: command
output: 'List of all projects, no errors'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.414Z'
id: c22d68bc-1ee8-476a-970f-0399054a8a47
verified: false
validated: true
submitted: true
---
# curl-graphql-expiredpw-projects-query

## Command

```bash
curl --request POST --url https://gitlab.domain.com/api/graphql --header 'Authorization: Bearer <TOKEN>' --header 'Content-Type: application/json' --data '{"query":"query {\n projects{\n nodes{\n id\n name\n }\n }\n}"}'
```

## Description

Queries projects via GraphQL with expired password token, bypassing restriction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--data` | Projects query | Yes |
| `-H 'Authorization: Bearer <TOKEN>'` | Token | Yes |
| `--request POST` | HTTP method | Yes |

## Examples

### Basic Usage

```bash
curl --request POST --url https://gitlab.domain.com/api/graphql --header 'Authorization: Bearer <TOKEN>' --header 'Content-Type: application/json' --data '{"query":"query {\n projects{\n nodes{\n id\n name\n }\n }\n}"}'
```

## Expected Output

Projects list JSON.

## Related

- [[commands/curl-rest-expiredpw-block]]
- [[procedures/Bypass-Additional-Restrictions-via-GraphQL]]
