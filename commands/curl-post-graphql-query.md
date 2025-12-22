---
id: 29d9a26d-2b02-4f28-a54f-f3e4d96a2d66
name: curl-post-graphql-query
type: command
executor: bash
data: 'curl -X POST $_ENDPOINT -H "Content-Type: application/json" -d ''$_PAYLOAD'''
output: null
created_at: '2023-04-06T03:55:58.926424+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - web
  - graphql
  - injection
verified: true
validated: true
---

# curl-post-graphql-query

## Command

```bash
curl -X POST $_ENDPOINT -H "Content-Type: application/json" -d '$_PAYLOAD'
```

## Description

This command sends a POST request to a GraphQL endpoint with a JSON payload containing a query. It is used to test or exploit GraphQL APIs by submitting custom queries, such as those with injection payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ENDPOINT | The GraphQL endpoint URL (e.g., https://target.com/graphql) | Yes |
| $_PAYLOAD | The JSON payload string, including the escaped GraphQL query | Yes |
| -X POST | Specifies the HTTP method as POST | Built-in |
| -H "Content-Type: application/json" | Sets the request header for JSON data | Built-in |
| -d | Passes the data payload in the request body | Built-in |

## Examples

### Basic Usage

```bash
curl -X POST https://example.com/graphql -H "Content-Type: application/json" -d '{"query": "query { hello }"}'
```

### Advanced Usage

For complex escaped payloads:

```bash
curl -X POST https://target.com/graphql -H "Content-Type: application/json" --data-raw '{"query": "query { doctors(options: \"{\\\"limit\\\": 1}\", search: \\"{}\\") { id } }"}'
```

## Expected Output

A JSON response from the GraphQL server, such as {"data":{"doctors":[{"id":"123"}]}} on success, or an error like {"errors":[{"message":"Parse error"}]} on failure. Look for leaked data in the 'data' field.

## Related

- [[procedures/GraphQL-Injection-for-NoSQL-Exploitation]]
- [[tools/cURL]]
