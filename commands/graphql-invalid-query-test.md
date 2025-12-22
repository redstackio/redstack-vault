---
type: command
executor: bash
data: >-
  curl -X GET "$_TARGET_URL/graphql?query={thisdefinitelydoesnotexist}" -H
  "Content-Type: application/json"
output: null
created_at: '2023-04-06T03:55:58.757165+00:00'
updated_at: '2023-04-10T20:22:23.241265+00:00'
platforms:
  - Web
tags:
  - graphql
  - error-testing
  - injection
verified: true
validated: true
---

# graphql-invalid-query-test

## Command

```bash
curl -X GET "$_TARGET_URL/graphql?query={thisdefinitelydoesnotexist}" -H "Content-Type: application/json"
```

## Description

Tests the GraphQL endpoint with an invalid query to analyze error responses for verbose details that could aid in crafting injection payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Target GraphQL API URL | Yes |
| -X GET | HTTP GET | Built-in |
| -H "Content-Type: application/json" | JSON header | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://example.com/graphql?query={thisdefinitelydoesnotexist}" -H "Content-Type: application/json"
```

### With Silent Output

```bash
curl -s -X GET "$_TARGET_URL/graphql?query={thisdefinitelydoesnotexist}" -H "Content-Type: application/json" | jq .
```

## Expected Output

Error JSON:

```json
{"errors":[{"message":"Cannot query field \"thisdefinitelydoesnotexist\" on type \"Query\".","locations":[{"line":1,"column":2}]}]}
```

Verbose messages (e.g., stack traces) signal injection risk.

## Related

- [[Related Procedure|procedures/Identify-GraphQL-Injection-Points]]
- [[commands/graphql-schema-introspection-query]]
