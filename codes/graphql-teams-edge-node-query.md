---
id: 12909128-cc78-4403-8ce4-9fa073cf905f
name: graphql-teams-edge-node-query
type: code
language: json
verified: true
created_at: '2023-04-06T03:55:58.816363+00:00'
updated_at: '2023-04-10T20:22:23.649352+00:00'
platforms:
  - Web
tags:
  - graphql
  - payload
  - data-extraction
validated: true
---

# graphql-teams-edge-node-query

## Code

```json
{
  "query": "query {
    teams{
      total_count,edges{
        node{
          id,_id,about,handle,state
        }
      }
    }
  }"
} 
```

## Description

This JSON payload contains a GraphQL query that targets the 'teams' object, using 'total_count' for overview and 'edges' with 'node' to extract detailed fields from connected team entities. It is designed for data extraction in vulnerable GraphQL APIs, allowing traversal of the schema to pull sensitive information like internal IDs and states without authentication checks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| teams | The root query object (replace with other types like 'users' if needed) | teams |
| total_count | Field for total item count | total_count |
| edges | Pagination wrapper for nodes | edges |
| node | Individual data object | node |
| id, _id, about, handle, state | Specific fields to extract (customize based on schema) | id, _id, about, handle, state |

## Usage

Embed this payload in an HTTP POST request to the GraphQL endpoint using tools like curl or Burp Suite. For example, in a procedure like [[procedures/GraphQL-Edge-Node-Data-Extraction]], substitute into the -d flag of curl-send-graphql-query. Modify fields based on schema introspection to target other objects. Use in red team engagements to simulate data leaks via over-permissive APIs.

## Detection

- Log analysis for GraphQL queries with deep nesting or unexpected fields like '_id' or 'state'.
- WAF rules matching JSON payloads with 'edges' and 'node' patterns.
- Anomalous data volumes in API responses or queries without auth tokens.
- Schema monitoring tools alerting on access to internal fields.

## Related

- [[procedures/GraphQL-Edge-Node-Data-Extraction]] (procedure using this code)
- [[tools/cURL]] (tool for delivery)
