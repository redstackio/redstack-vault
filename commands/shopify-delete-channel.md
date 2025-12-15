---
data: >-
  curl -X DELETE -H "X-Shopify-Access-Token: 77a01fc64f65fd16b0b38bc31694e4ce"
  "https://while42.myshopify.com/admin/channels/{channel_id}.json"
tags:
  - shopify
  - api
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.720Z'
id: 74762644-f55b-45a0-b5ed-b832d05ab66f
verified: false
validated: true
submitted: true
---
# shopify-delete-channel

## Command

```bash
curl -X DELETE -H "X-Shopify-Access-Token: 77a01fc64f65fd16b0b38bc31694e4ce" "https://while42.myshopify.com/admin/channels/{channel_id}.json"
```

## Description

Deletes a specific sales channel by ID using the unauthorized token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| channel_id | ID of channel to delete | Yes |
| X-Shopify-Access-Token | Auth token | Yes |

## Examples

### Basic Usage

```bash
curl -X DELETE -H "X-Shopify-Access-Token: TOKEN" "https://shop.myshopify.com/admin/channels/123.json"
```

## Expected Output

HTTP 200 OK with empty body or success message.

## Related

- [[Related Procedure: Delete-Shopify-Sales-Channel]]
