---
data: >-
  curl -X POST $ENDPOINT -H "Content-Type: application/json" -d '{"query":
  "query { __schema { queryType { name } mutationType { name } types { name
  description } } }"}'
tags:
  - graphql
  - recon
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.684Z'
id: e3aff058-4676-41d3-88cf-8b8ccf6713d6
verified: false
validated: true
submitted: true
---
# graphql-introspect

## Command

```bash
curl -X POST $ENDPOINT -H "Content-Type: application/json" -d '{"query": "query { __schema { queryType { name } mutationType { name } types { name description } } }"}'
```

## Description

Sends a GraphQL introspection query to retrieve the API schema, listing types, queries, and mutations for reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $ENDPOINT | Target GraphQL URL (e.g., https://example.com/graphql) | Yes |
| -H | Header for JSON content type | Yes |
| -d | Query payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://tng-api.watsons.com.my/graphql -H "Content-Type: application/json" -d '{"query": "query { __schema { types { name } } }"}'
```

### Advanced Usage

```bash
curl -X POST https://tng-api.watsons.com.my/graphql -H "Content-Type: application/json" -d '{"query": "query { __schema { mutationType { fields { name args { name type { name } } } } } }"}'
```

## Expected Output

JSON object with schema details, e.g., {"data":{"__schema":{"types":[{"name":"Query"},{"name":"Mutation"},... ]}}}

## Related

- [[Related Procedure: Enumerate-GraphQL-Endpoint-and-Introspection]]
