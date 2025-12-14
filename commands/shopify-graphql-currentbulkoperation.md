---
id: cmd-uuid-3
data: >-
  curl -X POST
  'https://yourstore.myshopify.com/admin/internal/web/graphql/core?operation=LoginNotificationsRead'
  -H 'Content-Type: application/json' -H 'Cookie: _shopify_s=session;
  _shopify_y=session' -d '{"query":"query { currentBulkOperation { id }
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
updated_at: '2025-12-14T17:25:53.518Z'
verified: false
validated: true
submitted: true
---
# shopify-graphql-currentbulkoperation

## Command

```bash
curl -X POST 'https://yourstore.myshopify.com/admin/internal/web/graphql/core?operation=LoginNotificationsRead' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: _shopify_s=session; _shopify_y=session' \
  -d '{"query":"query { currentBulkOperation { id } }","variables":null,"operationName":null}'
```

## Description

GraphQL query to retrieve the ID of the current bulk operation in Shopify without permission checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Cookie` | Session for auth | Yes |

## Examples

### Basic Usage

```bash
curl -X POST ... -d '{query: "query { currentBulkOperation { id } }"}'
```

### Advanced Usage

```bash
# Extend query for status: query { currentBulkOperation { id status } }
```

## Expected Output

JSON: {"data":{"currentBulkOperation":{"id":"gid://..."}}}

## Related

- [[procedures/Query-Current-Bulk-Operation-ID-Without-Permissions]]
