---
data: >-
  query { node(id: "gid://hackerone/PaymentsLibrary::Payment/something") { ...
  on User { id } } }
tags:
  - graphql
  - testing
type: command
output: HTTP GET /payments/something; no exception raised
executor: graphql
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.608Z'
id: edeef19c-f12f-4a7e-9780-0e677eb7f55c
verified: false
validated: true
submitted: true
---
# query-non-integer-id

## Command

```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/something") { ... on User { id } } }
```

## Description

Tests the GraphQL node with a non-integer ID to illustrate ActiveResource's lack of strict validation or encoding.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| id | Invalid string ID | Yes |

## Examples

### Basic Usage

```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/something") { ... on User { id } } }
```

## Expected Output

Backend HTTP GET /payments/something without errors, showing tolerance for malformed IDs.

## Related

- [[commands/query-standard-global-id]]
- [[procedures/Test-GraphQL-Node-Interface]]
