---
data: >-
  curl -X POST 'https://your-shop.myshopify.com/admin/api/2023-10/graphql.json'
  -H 'Content-Type: application/json' -H 'X-Shopify-Access-Token:
  your_staff_token' -d
  '{"operationName":"EmbeddedAppAnalyticsToken","variables":{"apiKey":"a53cf2ce9b5dabf5dd222b3615c29569"},"query":"query
  EmbeddedAppAnalyticsToken($apiKey:String!){appByKey:appByKey(apiKey:$apiKey){id
  installation{id legacyEasdkAnalyticsToken typename}}"}'
tags:
  - graphql
  - shopify
  - token-extraction
type: command
output: null
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.302Z'
id: 90719d99-a8f7-43c4-97c6-0926e92f0d6c
verified: false
validated: true
submitted: true
---
# graphql-query-extract-analytics-token

## Command

```bash
curl -X POST 'https://your-shop.myshopify.com/admin/api/2023-10/graphql.json' \
  -H 'Content-Type: application/json' \
  -H 'X-Shopify-Access-Token: your_staff_token' \
  -d '{"operationName":"EmbeddedAppAnalyticsToken","variables":{"apiKey":"a53cf2ce9b5dabf5dd222b3615c29569"},"query":"query EmbeddedAppAnalyticsToken($apiKey:String!){appByKey:appByKey(apiKey:$apiKey){id installation{id legacyEasdkAnalyticsToken typename}}"}'
```

## Description

This curl command sends a GraphQL query to Shopify's Admin API to extract the legacyEasdkAnalyticsToken from an app installation using the app's API key, bypassing permission requirements.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `https://your-shop.myshopify.com/admin/api/2023-10/graphql.json` | GraphQL endpoint URL (replace with target shop) | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON content type | Yes |
| `-H 'X-Shopify-Access-Token: your_staff_token'` | Authenticates with staff token (replace with actual token) | Yes |
| `-d '{...}'` | JSON payload with operationName, variables (apiKey), and query | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://example.myshopify.com/admin/api/2023-10/graphql.json' -H 'Content-Type: application/json' -H 'X-Shopify-Access-Token: shpat_abc123' -d '{"operationName":"EmbeddedAppAnalyticsToken","variables":{"apiKey":"a53cf2ce9b5dabf5dd222b3615c29569"},"query":"query EmbeddedAppAnalyticsToken($apiKey:String!){appByKey:appByKey(apiKey:$apiKey){id installation{id legacyEasdkAnalyticsToken typename}}"}'
```

### Advanced Usage

For different API versions or additional fields, modify the query string in the -d payload.

## Expected Output

JSON response: {"data":{"appByKey":{"installation":{"id":"gid://...","legacyEasdkAnalyticsToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."}}}}. Look for the token in legacyEasdkAnalyticsToken.

## Related

- [[Related Procedure: Extract-Shopify-Analytics-Token-via-GraphQL]]
