---
id: cmd-shopify-graphql-publish-927567
data: >-
  fetch("https://yourshop.myshopify.com/admin/online-store/admin/api/unversioned/graphql",
  { "headers": { "accept": "application/json", "accept-language":
  "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7", "cache-control": "no-cache",
  "content-type": "application/json", "pragma": "no-cache", "sec-fetch-dest":
  "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin",
  "x-online-store-web": "1" }, "referrerPolicy": "no-referrer", "body":
  "{\"operationName\":\"ThemePublishLegacy\",\"variables\":{\"id\":\"gid://shopify/OnlineStoreTheme/[THEME_ID]\"},\"query\":\"mutation
  ThemePublishLegacy($id: ID!) {\n  onlineStoreThemePublish(id: $id) {\n   
  theme {\n      id\n      __typename\n    }\n    userErrors {\n     
  field\n      message\n      __typename\n    }\n    __typename\n  }\n}\n\"}",
  "method": "POST", "mode": "cors", "credentials": "include" });
tags:
  - graphql
  - mutation
  - publish
type: command
output: JSON response with published theme details or userErrors if failed
executor: javascript
platforms:
  - Web
  - Shopify
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:29.079Z'
verified: false
validated: true
submitted: true
---
# theme-publish-graphql-mutation

## Command

```javascript
fetch("https://yourshop.myshopify.com/admin/online-store/admin/api/unversioned/graphql", {
  "headers": {
    "accept": "application/json",
    "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-online-store-web": "1"
  },
  "referrerPolicy": "no-referrer",
  "body": "{\"operationName\":\"ThemePublishLegacy\",\"variables\":{\"id\":\"gid://shopify/OnlineStoreTheme/[THEME_ID]\"},\"query\":\"mutation ThemePublishLegacy($id: ID!) {\n  onlineStoreThemePublish(id: $id) {\n    theme {\n      id\n      __typename\n    }\n    userErrors {\n      field\n      message\n      __typename\n    }\n    __typename\n  }\n}\n\"}",
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
});
```

## Description

Sends a GraphQL POST mutation to Shopify's unversioned API to publish a theme by its global ID. Used in browser console to replay or modify requests for unauthorized publication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | GraphQL endpoint URL (shop-specific) | Yes |
| body.variables.id | Theme ID in gid://shopify/OnlineStoreTheme/[ID] format | Yes |
| headers.content-type | Set to application/json | Yes |
| credentials | include to maintain session auth | Yes |

## Examples

### Basic Usage

```javascript
// Publish with specific ID
fetch("https://yourshop.myshopify.com/admin/online-store/admin/api/unversioned/graphql", { /* ... */ "body": "{\"variables\":{\"id\":\"gid://shopify/OnlineStoreTheme/123\"} /* ... */ }" });
```

### Advanced Usage

```javascript
// With custom headers for different locale
fetch("https://yourshop.myshopify.com/admin/online-store/admin/api/unversioned/graphql", { "headers": { /* add custom accept-language */ }, /* rest */ });
```

## Expected Output

Successful: {"data":{"onlineStoreThemePublish":{"theme":{"id":"gid://...","__typename":"OnlineStoreTheme"},"userErrors":[]}}}
Failed: {"data":{"onlineStoreThemePublish":{"userErrors":[{"field":null,"message":"Error message"}]}}}}

## Related

- [[procedures/Modify-and-Execute-Paid-Theme-Publish-Mutation]]
