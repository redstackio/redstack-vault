---
tags:
  - shopify
  - oauth
  - scope-abuse
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/shopify-oauth-authorize-with-channels-scopes]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:01.771Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: ee475453-6476-4464-838e-6bef4b587584
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Request-Undocumented-Shopify-OAuth-Scopes

## Summary

This procedure requests authorization for a Shopify app installation by including undocumented scopes like read_channels and write_channels, exploiting a naming issue in the API to gain unauthorized access to beta endpoints without special permissions.

## Description

In the Shopify OAuth flow, apps can request scopes that are not publicly documented. By including read_channels and write_channels in the scope parameter, an attacker can obtain an access token capable of interacting with the /admin/channels endpoint, which is intended for engineering teams only. This bypasses access controls due to a code-level naming flaw, allowing manipulation of sales channels that control merchant sales operations across platforms.

## Requirements

1. Valid Shopify app client_id
2. Target shop domain (e.g., while42.myshopify.com)
3. Redirect URI registered with the app
4. Network access to Shopify admin endpoints

## Defense

Defensive measures and detection strategies:

- Enforce strict scope validation in OAuth, rejecting undocumented scopes
- Implement engineering flag checks for beta APIs
- Monitor OAuth requests for excessive or unknown scopes
- Log and alert on access to internal endpoints

## Objectives

1. Obtain authorization code with channels scopes
2. Enable subsequent API access for channel manipulation
3. Disrupt sales configurations without detection

## Instructions

### Step 1: Construct OAuth Authorization Request

**Context**: Build the GET request to the authorize endpoint, appending the target shop, client_id, scopes including undocumented ones, redirect_uri, and state.

**Command** ([[commands/shopify-oauth-authorize-with-channels-scopes]]):
```bash
curl "https://while42.myshopify.com/admin/oauth/authorize?client_id=fc49e813f5aad9c8d8f65117031a9684&scope=read_apps,write_apps,write_content,read_content,write_customers,read_customers,read_disputes,write_fulfillments,read_fulfillments,write_gift_cards,read_gift_cards,write_orders,read_orders,read_products,write_products,read_script_tags,write_script_tags,write_scripts,read_scripts,read_shipping,write_shipping,write_social_network_accounts,read_social_network_accounts,read_themes,write_themes,read_channels,write_channels&redirect_uri=http://while42.myshopify.com/&state=123&shop=while42"
```

> This initiates the OAuth flow. The response redirects to the redirect_uri with an authorization code if scopes are accepted.

### Step 2: Handle Redirect and Extract Code

**Context**: Capture the redirect response to obtain the code parameter for token exchange.

**Command** (Manual handling or browser simulation):
```bash
# Follow redirect and parse ?code=AUTH_CODE from URL
```

> Expected: Authorization code in query string.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/shopify-oauth-authorize-with-channels-scopes]]

## Tools Used


## Tags

- [[shopify]]
- [[oauth]]
- [[scope-abuse]]
