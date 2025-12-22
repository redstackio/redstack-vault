---
data: >-
  curl -H "Cookie: shop_session=your_session"
  https://your-shop.myshopify.com/admin/orders/_order_id_/transaction.json
tags:
  - http
  - fetch
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.317Z'
id: e29ff5d5-b12e-4b15-b58a-c5e6ad397724
verified: false
validated: true
submitted: true
---
# curl-fetch-transaction

## Command

```bash
curl -H "Cookie: shop_session=your_session" https://your-shop.myshopify.com/admin/orders/_order_id_/transaction.json
```

## Description

Fetches transaction details from Shopify's admin API to verify uploaded signatures, using curl for API querying.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: shop_session=your_session"` | Auth cookie | Yes |
| `https://.../transaction.json` | API endpoint with order_id | Yes |

## Examples

### Basic Usage

```bash
curl -H "Cookie: shop_session=abc123" https://shop.myshopify.com/admin/orders/123456/transaction.json
```

### Advanced Usage

```bash
curl -H "Cookie: shop_session=abc123" https://shop.myshopify.com/admin/orders/123456/transaction.json | jq '.transaction.signatures'
```

## Expected Output

JSON with transaction object, including 'signatures' array listing uploaded files: {"transaction": {"signatures": [{"url": "https://s3..."}]}}

## Related

- [[commands/curl-upload-signature]]
