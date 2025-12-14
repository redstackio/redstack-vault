---
id: cmd-test-woocommerce-key
data: 'curl -u "ck_abc123:cs_def456" "https://target.com/wp-json/wc/v3/products"'
tags:
  - api
  - test
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:14.189Z'
verified: false
validated: true
submitted: true
---
# test-api-key

## Command

```bash
curl -u "ck_abc123:cs_def456" "https://target.com/wp-json/wc/v3/products"
```

## Description

Tests WooCommerce API key validity by fetching products list, confirming read access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Basic auth with consumer_key:consumer_secret | Yes |
| URL | API endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -u "ck_key:cs_secret" "https://site.com/wp-json/wc/v3/products"
```

### Advanced Usage

```bash
curl -u "ck_key:cs_secret" -H "Content-Type: application/json" "https://site.com/wp-json/wc/v3/products?per_page=1"
```

## Expected Output

JSON array of products if valid, or 401 Unauthorized if invalid.

## Related

- [[commands/create-woocommerce-api-key]]
