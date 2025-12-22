---
id: cmd-curl-view-item
data: >-
  curl -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json"
  https://api.instacart.com/v2/items/{ITEM_ID}
tags:
  - api
  - recon
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.357Z'
verified: false
validated: true
submitted: true
---
# curl-view-item

## Command

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" https://api.instacart.com/v2/items/{ITEM_ID}
```

## Description

This command retrieves details of an item from Instacart's API using a direct item ID, useful for testing IDOR by viewing unlisted items.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: Bearer YOUR_TOKEN"` | Authentication header with session token | Yes |
| `-H "Content-Type: application/json"` | Sets request content type | Yes |
| `https://api.instacart.com/v2/items/{ITEM_ID}` | Endpoint with item ID placeholder | Yes |

## Examples

### Basic Usage

```bash
curl -H "Authorization: Bearer abc123" -H "Content-Type: application/json" https://api.instacart.com/v2/items/12345
```

### Advanced Usage

```bash
curl -v -H "Authorization: Bearer abc123" -H "Content-Type: application/json" https://api.instacart.com/v2/items/99999
```

## Expected Output

JSON object with item details like {"id": 99999, "name": "Hidden Item", "price": 10.99} on success; 404 or error on failure.

## Related

- [[commands/curl-add-to-cart]]
- [[procedures/Manipulate-Item-IDs-to-Access-Unlisted-Items-via-IDOR]]
