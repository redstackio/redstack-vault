---
id: cmd-graphql-single-001
data: >-
  query { teams(where: { state: { _eq: soft_launched } }) { edges { node { id
  state } } } }
tags:
  - graphql
  - verification
  - secure
type: command
output: Empty teams array due to secure schema restrictions
executor: graphql
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.084Z'
verified: false
validated: true
submitted: true
---
# graphql-single-state-query

## Command

```graphql
query { teams(where: { state: { _eq: soft_launched } }) { edges { node { id state } } } }
```

## Description

This standard GraphQL query tests direct access to private 'soft_launched' team states using a single 'where' condition, which respects the secure schema and returns no results, contrasting with bypass exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| where.state._eq | Filter for 'soft_launched' state | Yes |
| edges.node.id | Retrieve team ID (if accessible) | Yes |
| edges.node.state | Retrieve state | Yes |

## Examples

### Basic Usage

```graphql
query { teams(where: { state: { _eq: soft_launched } }) { edges { node { id state } } } }
```

### Advanced Usage

Test other private states or fields.

```graphql
query { teams(where: { status: { _eq: private } }) { edges { node { id status } } } }
```

## Expected Output

{"data":{"teams":{"edges":[]}}}, an empty array confirming secure schema blocks access to hidden teams.

## Related

- [[commands/graphql-duplicate-or-query]]
- [[procedures/Exploit-GraphQL-Secure-Schema-Bypass-Using-Duplicate-Conditions]]
