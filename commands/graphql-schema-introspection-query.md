---
type: command
executor: bash
data: >-
  curl -X GET "$_TARGET_URL/graphql?query={__schema{types{name}}}" -H
  "Content-Type: application/json"
output: null
created_at: '2023-04-06T03:55:58.757034+00:00'
updated_at: '2023-04-10T20:22:23.241265+00:00'
platforms:
  - Web
tags:
  - graphql
  - introspection
  - recon
verified: true
validated: true
---

# graphql-schema-introspection-query

## Command

```bash
curl -X GET "$_TARGET_URL/graphql?query={__schema{types{name}}}" -H "Content-Type: application/json"
```

## Description

Performs a GraphQL introspection query to retrieve schema type names, revealing API structure and potential injection targets if introspection is not disabled.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Base URL of the GraphQL API | Yes |
| -X GET | HTTP GET method | Built-in |
| -H "Content-Type: application/json" | JSON header | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://example.com/graphql?query={__schema{types{name}}}" -H "Content-Type: application/json"
```

### POST Variant

```bash
curl -X POST "$_TARGET_URL/graphql" -H "Content-Type: application/json" -d '{"query":"{__schema{types{name}}}"}'
```

## Expected Output

JSON with schema data:

```json
{"data":{"__schema":{"types":[{"name":"Query"},{"name":"User"},... ]}}}
```

Empty or error if protected; detailed types indicate exposure.

## Related

- [[Related Procedure|procedures/Identify-GraphQL-Injection-Points]]
- [[commands/graphql-empty-query]]
