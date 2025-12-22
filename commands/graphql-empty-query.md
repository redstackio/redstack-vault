---
type: command
executor: bash
data: >-
  curl -X GET "$_TARGET_URL/graphql?query={}" -H "Content-Type:
  application/json"
output: null
created_at: '2023-04-06T03:55:58.757077+00:00'
updated_at: '2023-04-10T20:22:23.241265+00:00'
platforms:
  - Web
tags:
  - graphql
  - injection
  - recon
verified: true
validated: true
---

# graphql-empty-query

## Command

```bash
curl -X GET "$_TARGET_URL/graphql?query={}" -H "Content-Type: application/json"
```

## Description

Sends an empty GraphQL query to the target endpoint to test if it processes minimal inputs, helping identify active endpoints vulnerable to injection by observing response handling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Base URL of the GraphQL API (e.g., https://example.com) | Yes |
| -X GET | Use HTTP GET method | Built-in |
| -H "Content-Type: application/json" | Set JSON content type header | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://example.com/graphql?query={}" -H "Content-Type: application/json"
```

### With Proxy (e.g., Burp)

```bash
curl -X GET "https://example.com/graphql?query={}" -H "Content-Type: application/json" --proxy http://127.0.0.1:8080
```

## Expected Output

A JSON response like:

```json
{"errors":[{"message":"Must provide query string.","locations":[{"line":1,"column":1}]}]}
```

Look for any processing or additional details indicating poor input validation.

## Related

- [[Related Procedure|procedures/Identify-GraphQL-Injection-Points]]
- [[commands/graphql-schema-introspection-query]]
