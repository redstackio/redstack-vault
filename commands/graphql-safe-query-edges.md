---
data: |-
  query {
    users() {
      edges {
        node {
          email
        }
      }
    }
  }
tags:
  - graphql
  - safe-query
type: command
executor: graphql
platforms:
  - Web
id: 95dce8f0-4aca-4db8-86cb-fd640a2ed22a
created_at: '2025-12-11T06:10:40.221Z'
updated_at: '2025-12-11T06:10:40.221Z'
verified: false
validated: true
submitted: true
---
# graphql-safe-query-edges

## Command

```graphql
query {
  users() {
    edges {
      node {
        email
      }
    }
  }
}
```

## Description

This GraphQL query uses the 'edges' field, which applies proper authorization and is safe for fetching user data without bypassing controls.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `users()` | Connection to query users | Yes |
| `edges` | Field that enforces authorization | Yes |
| `email` | Attribute to fetch | No |

## Examples

### Basic Usage

```graphql
query {
  users() {
    edges {
      node {
        email
      }
    }
  }
}
```

## Expected Output

Authorized user email data, with sensitive info scrubbed.

## Related

- [[commands/graphql-vulnerable-query-nodes]]
- [[procedures/Exploit-GraphQL-Nodes-Field-for-User-Data-Leakage]]
