---
tags:
  - xss
  - oauth
  - shopify-admin
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/shopify-oauth-authorize-malicious-app]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 79b108ca-cc64-4c93-b327-5b524ad99552
created_at: '2025-12-13T23:55:20.840Z'
updated_at: '2025-12-13T23:55:20.840Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Authorize-App-to-Trigger-XSS-on-Admin-Panel

## Summary

This procedure authorizes the malicious sales channel app on a target shop using OAuth, integrating the SVG icon into the admin panel and triggering XSS upon rendering.

## Description

Authorization installs the app, causing the icon to load in the shop's admin interface where the onload payload executes. This extends the XSS to merchant contexts on $shop.myshopify.com/admin/. Requires the app to be saved with the payload; enables exfiltration from shop admins.

## Requirements

1. Malicious app saved and ready for installation
2. Target shop URL (e.g., example.myshopify.com)
3. Access to construct and visit the OAuth URL

## Defense

Defensive measures and detection strategies:

- Review app icons post-installation for sanitization
- Block or scan SVGs in admin-rendered assets
- Detect anomalous JavaScript in OAuth flows

## Objectives

1. Install the app to embed the payload in shop admin
2. Execute XSS in merchant/employee sessions
3. Facilitate data exfiltration or hijacking

## Instructions

### Step 1: Construct OAuth Authorization URL

**Context**: Build the URL with app client_id and redirect to initiate installation.

Use [[commands/shopify-oauth-authorize-malicious-app]]:

The command is a URL to visit in the browser: /admin/oauth/authorize?client_id=672a937d5eb24e10c756ea256c73bb8c&scope=read_products&redirect_uri=https://attackerdoma.in/93ba4bef-cff1-43b1-922d-0631bd387e2e.html&state=nonce on $shop.myshopify.com.

> Navigate to the full URL. Expected output: OAuth consent page loads.

### Step 2: Complete Authorization and Load Admin

**Context**: Approve the app installation to trigger icon rendering in admin.

No specific command; Click "Install app" on the consent page, then access /admin/.

> App installs; admin loads with icon. Expected output: XSS alert fires in admin context.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/shopify-oauth-authorize-malicious-app]]

## Tools Used


## Tags

- [[xss]]
- [[oauth]]
- [[shopify-admin]]
