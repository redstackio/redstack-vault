---
data: >-
  curl 'https://gitlab.domain.com/api/graphql' -H 'Content-Type:
  application/json' -H 'Authorization: Bearer <TOKEN>' --data '{"query":"query
  {\nprojects{\n nodes{\n id\n name\n }\n}\n}\n"}'
tags:
  - graphql
  - projects
type: command
output: List of projects including private/internal ones
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.446Z'
id: fd167d92-722e-485a-a404-d3e188c0af24
verified: false
validated: true
submitted: true
---
# curl-graphql-projects-query

## Command

```bash
curl 'https://gitlab.domain.com/api/graphql' -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' --data '{"query":"query {\nprojects{\n nodes{\n id\n name\n }\n}\n}\n"}'
```

## Description

Queries all projects via GraphQL, useful for data access in bypass scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--data` | Projects query | Yes |
| `-H 'Authorization: Bearer <TOKEN>'` | Token | Yes |

## Examples

### Basic Usage

```bash
curl 'https://gitlab.domain.com/api/graphql' -H 'Content-Type: application/json' -H 'Authorization: Bearer <TOKEN>' --data '{"query":"query {\nprojects{\n nodes{\n id\n name\n }\n}\n}\n"}'
```

## Expected Output

Array of project nodes with IDs and names.

## Related

- [[commands/curl-graphql-currentuser-query]]
- [[procedures/Query-GraphQL-API-with-Deactivated-Token]]
