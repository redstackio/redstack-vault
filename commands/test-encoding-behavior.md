---
data: >-
  query { node(id: "gid://hackerone/PaymentsLibrary::Payment/%3fsomething%26") {
  ... on User { id } } }
tags:
  - encoding
  - testing
type: command
output: >-
  HTTP GET /payments/?something&.json (actual); expected
  /payments/%3fsomething%26.json
executor: graphql
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.598Z'
id: 3bc873b5-4fd9-407a-b4bd-f0c5b76f0fc3
verified: false
validated: true
submitted: true
---
# test-encoding-behavior

## Command

```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/%3fsomething%26") { ... on User { id } } }
```

## Description

Tests ActiveResource's decoding without re-encoding to expose the injection root cause.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| id | Encoded test string | Yes |

## Examples

### Basic Usage

```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/%3fsomething%26") { ... on User { id } } }
```

## Expected Output

Decoded path injection, not escaped.

## Related

- [[commands/inject-query-parameters]]
- [[procedures/Inject-Query-Parameters-via-Global-ID]]
