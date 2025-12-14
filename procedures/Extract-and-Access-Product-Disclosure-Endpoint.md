---
id: proc-extract-access-endpoint
tags:
  - idor
  - information-disclosure
  - endpoint-access
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:44.420Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Extract and Access Product Disclosure Endpoint

## Summary

This procedure extracts the product-specific URL from the victim store's Digital Downloads app and accesses it under the attacker's low-privilege session, disclosing the app installation and product title via page metadata.

## Description

Switch to the victim store admin to navigate the app dashboard, right-click the attached product (e.g., 'Tt') to copy its URL like https://delivery.shopifyapps.com/products/3785077260000. Alternatively, extract the product ID from the store's page source (e.g., view source of https://test.myshopify.com/products/tt and find "rid":3785077260000 in script tags). Then, in the attacker's browser session (logged into their store with the app), visit the URL. The page title reveals 'Digital Downloads/Tt' if attached, or just 'Digital Downloads' otherwise, confirming IDOR without permission checks.

## Requirements

1. Access to victim app dashboard (as admin)
2. Attacker session with app installed
3. Browser developer tools for URL extraction and source inspection

## Defense

Defensive measures and detection strategies:

- Add store and user ownership validation to app endpoints
- Obfuscate or remove sensitive metadata from page titles and sources
- Implement rate limiting on app endpoints and log unauthorized accesses

## Objectives

1. Obtain direct reference to victim product via ID
2. Exploit lack of checks to disclose configuration
3. Validate impact by comparing attached vs. non-attached responses

## Instructions

### Step 1: Extract Product URL or ID

**Context**: Get the endpoint reference from the victim side.

In victim app dashboard, right-click 'Tt' and copy link; or view source of product page to find ID in <script id="__st">.

> Manual inspection; construct URL as https://delivery.shopifyapps.com/products/{ID}.

### Step 2: Access Endpoint as Attacker

**Context**: Use low-privilege session to trigger disclosure.

Paste the URL into attacker's browser (logged into independent store with app).

> Page loads; check document title for product name leakage.

### Step 3: Verify with Non-Attached Product

**Context**: Confirm selective disclosure.

Repeat with 'PP' ID or invalid ID; title lacks product name.

> Difference indicates attachment status revealed.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[idor]]
- [[information-disclosure]]
