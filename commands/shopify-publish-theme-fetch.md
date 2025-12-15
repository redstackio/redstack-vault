---
id: cmd-shopify-publish-fetch
data: >-
  fetch("https://yourshop.myshopify.com/admin/online-store/admin/api/unversioned/graphql",
  { "headers": { "accept": "application/json", "accept-language":
  "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7", "cache-control": "no-cache",
  "content-type": "application/json", "pragma": "no-cache", "sec-fetch-dest":
  "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin",
  "x-online-store-web": "1" }, "referrerPolicy": "no-referrer", "body":
  "{\"operationName\":\"ThemePublishLegacy\",\"variables\":{\"id\":\"gid://shopify/OnlineStoreTheme/[THEME_ID]\"},\"query\":\"mutation
  ThemePublishLegacy($id: ID!) {\n onlineStoreThemePublish(id: $id) {\n theme
  {\n id\n __typename\n }\n userErrors {\n field\n message\n __typename\n }\n
  __typename\n }\n}\

  \"}", "method": "POST", "mode": "cors", "credentials": "include" });
tags:
  - graphql
  - shopify
  - race-condition
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.793Z'
verified: false
validated: true
submitted: true
---
# shopify-publish-theme-fetch

## Command

```javascript
fetch("https://yourshop.myshopify.com/admin/online-store/admin/api/unversioned/graphql", { "headers": { "accept": "application/json", "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7", "cache-control": "no-cache", "content-type": "application/json", "pragma": "no-cache", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "x-online-store-web": "1" }, "referrerPolicy": "no-referrer", "body": "{\"operationName\":\"ThemePublishLegacy\",\"variables\":{\"id\":\"gid://shopify/OnlineStoreTheme/[THEME_ID]\"},\"query\":\"mutation ThemePublishLegacy($id: ID!) {\n onlineStoreThemePublish(id: $id) {\n theme {\n id\n __typename\n }\n userErrors {\n field\n message\n __typename\n }\n __typename\n }\n}\
\"}", "method": "POST", "mode": "cors", "credentials": "include" });
```

## Description

This JavaScript fetch command sends a GraphQL mutation to publish a Shopify theme by its ID, exploited in a race condition to publish paid themes without purchase. Execute in browser console during installation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | GraphQL endpoint: https://yourshop.myshopify.com/admin/online-store/admin/api/unversioned/graphql | Yes |
| body.variables.id | Theme ID in format gid://shopify/OnlineStoreTheme/[ID], replace [THEME_ID] | Yes |
| headers | Standard JSON headers plus x-online-store-web:1 for Shopify context | Yes |
| credentials | 'include' to send auth cookies | Yes |

## Examples

### Basic Usage

Replace [THEME_ID] with actual ID and run in console:

```javascript
fetch("https://yourshop.myshopify.com/admin/online-store/admin/api/unversioned/graphql", { "headers": { "accept": "application/json", "content-type": "application/json", "x-online-store-web": "1" }, "body": "{\"operationName\":\"ThemePublishLegacy\",\"variables\":{\"id\":\"gid://shopify/OnlineStoreTheme/123456\"},\"query\":\"mutation ThemePublishLegacy($id: ID!) { onlineStoreThemePublish(id: $id) { theme { id } userErrors { message } } }\"}", "method": "POST", "credentials": "include" });
```

### Advanced Usage

Use full headers for precise replication:

```javascript
// As shown in command above with all headers
```

## Expected Output

JSON response like {"data":{"onlineStoreThemePublish":{"theme":{"id":"gid://..."},"userErrors":[]}}} on success, or errors like "missing required file" if timed poorly.

## Related

- [[procedures/Extract-and-Publish-Temporary-Theme-ID]]
