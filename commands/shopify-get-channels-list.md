---
data: >-
  curl -H "X-Shopify-Access-Token: 77a01fc64f65fd16b0b38bc31694e4ce"
  "https://while42.myshopify.com/admin/channels.json"
tags:
  - shopify
  - api
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.721Z'
id: 18ca1512-2bf6-4926-a1cd-4822c87123ca
verified: false
validated: true
submitted: true
---
# shopify-get-channels-list

## Command

```bash
curl -H "X-Shopify-Access-Token: 77a01fc64f65fd16b0b38bc31694e4ce" "https://while42.myshopify.com/admin/channels.json"
```

## Description

Retrieves the list of sales channels using the access token header on the undocumented beta endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| X-Shopify-Access-Token | Access token for auth | Yes |

## Examples

### Basic Usage

```bash
curl -H "X-Shopify-Access-Token: TOKEN" "https://shop.myshopify.com/admin/channels.json"
```

### Advanced Usage

Pipe to jq for parsing: curl ... | jq '.channels'

## Expected Output

JSON: {"channels": [{ "id": 123, "type": "online_store", ... }]}

## Related

- [[Related Procedure: List-Shopify-Sales-Channels]]
