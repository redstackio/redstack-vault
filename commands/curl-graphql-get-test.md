---
id: cmd-998457-graphql-get
data: 'curl -X GET "https://target.com/graphql?query={__schema{types{name}}}" -v'
tags:
  - graphql
  - test
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:42.840Z'
verified: false
validated: true
submitted: true
---
# curl-graphql-get-test

## Command

```bash
curl -X GET "https://target.com/graphql?query={__schema{types{name}}}" -v
```

## Description

This command tests if a GraphQL endpoint accepts GET requests by performing an introspection query, revealing the schema and confirming CSRF bypass potential.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `query=...` | GraphQL query parameter | Yes |
| `-v` | Verbose output for headers | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://target.com/graphql?query={__schema{types{name}}}" -v
```

### Advanced Usage

```bash
curl -X GET "https://target.com/graphql?query={mutation{test}{id}}" -H "Cookie: session=abc" -v
```

## Expected Output

Successful response: JSON with schema types, e.g., {"data":{"__schema":{"types":[{"name":"User"},...]}}}, no method error.

## Related

- [[Related Procedure: Exploit-GraphQL-CSrf-Bypass-via-GET]]
