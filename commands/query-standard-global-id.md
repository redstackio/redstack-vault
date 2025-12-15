---
data: >-
  query { node(id: "gid://hackerone/PaymentsLibrary::Payment/1") { ... on User {
  id } } }
tags:
  - graphql
  - recon
type: command
output: 'HTTP GET /payments/1; returns User ID if successful, but mismatches type'
executor: graphql
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.610Z'
id: 177940ec-2c8e-4c11-b0da-8aaaca2991a5
verified: false
validated: true
submitted: true
---
# query-standard-global-id

## Command

```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/1") { ... on User { id } } }
```

## Description

Queries the GraphQL node for a Payment by standard global ID, triggering an ActiveResource find call to the backend to demonstrate normal translation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| id | Global ID in format gid://hackerone/PaymentsLibrary::Payment/[ID] | Yes |

## Examples

### Basic Usage

```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/1") { ... on User { id } } }
```

### Advanced Usage

Use with introspection to explore types.

## Expected Output

Backend HTTP GET /payments/1; GraphQL response with type mismatch error, but confirms request routing.

## Related

- [[commands/query-non-integer-id]]
- [[procedures/Test-GraphQL-Node-Interface]]
