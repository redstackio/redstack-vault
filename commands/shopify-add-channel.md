---
data: >-
  curl -X POST -H "X-Shopify-Access-Token: 77a01fc64f65fd16b0b38bc31694e4ce"
  "https://while42.myshopify.com/admin/channels.json" -d
  "channel[provider_id]=12"
tags:
  - shopify
  - api
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.718Z'
id: 6ec9cf73-5461-460a-9652-1c3510acbec2
verified: false
validated: true
submitted: true
---
# shopify-add-channel

## Command

```bash
curl -X POST -H "X-Shopify-Access-Token: 77a01fc64f65fd16b0b38bc31694e4ce" "https://while42.myshopify.com/admin/channels.json" -d "channel[provider_id]=12"
```

## Description

Adds a new sales channel with specified provider_id using the token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| channel[provider_id] | Provider ID for new channel | Yes |
| X-Shopify-Access-Token | Auth token | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "X-Shopify-Access-Token: TOKEN" "https://shop.myshopify.com/admin/channels.json" -d "channel[provider_id]=12"
```

## Expected Output

JSON: {"channel": { "id": 456, "provider_id": 12, ... }}

## Related

- [[Related Procedure: Add-Shopify-Sales-Channel]]
