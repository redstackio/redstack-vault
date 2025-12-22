---
tags:
  - xss
  - injection
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 48daf373-841a-4709-bd9d-9cb48c855df1
created_at: '2025-12-14T03:16:25.352Z'
updated_at: '2025-12-14T03:16:25.352Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Draft-Order-with-Malicious-Product-Name

## Summary

This procedure injects a malicious JavaScript payload into a product name during the creation of a Shopify draft order, setting the stage for XSS exploitation in the admin timeline by leveraging unsanitized input storage.

## Description

In the Shopify Admin Site, draft orders allow admins to create pending orders with custom product details. By setting a product name to an XSS payload like "><img src=x onerror=alert('XSS')>, the input is stored without immediate sanitization. This payload remains dormant until rendered in a context like the timeline, where it can execute in the browser of any viewing admin. Prerequisites include authenticated access to the Shopify admin panel. Expected outcomes include successful payload storage, verifiable in draft details, with no execution at this stage.

## Requirements

1. Authenticated Shopify admin account
2. Access to Orders > Drafts section
3. Web browser for manual input

## Defense

Defensive measures and detection strategies:

- Implement client-side and server-side input sanitization for all product fields using libraries like DOMPurify
- Enable Content Security Policy (CSP) to restrict inline script execution in admin panels
- Monitor for anomalous JavaScript alerts or network requests from admin sessions

## Objectives

1. Store unsanitized XSS payload in draft order product name
2. Prepare for later rendering in timeline without product link sanitization
3. Enable cross-admin JavaScript execution for data exfiltration

## Instructions

### Step 1: Access Draft Orders

**Context**: Log in and navigate to the draft orders creation interface to begin inputting malicious data.

No specific command; perform via UI: Go to https://yourstore.myshopify.com/admin/drafts/new.

> Expected: New draft order form loads.

### Step 2: Add Malicious Product

**Context**: Inject the payload into the product name field to exploit lack of sanitization.

No specific command; UI action: Search or create a product, edit name to "><img src=x onerror=alert('XSS')>, add to draft.

> Explanation: The payload closes any open tags and injects an onerror handler. Expected output: Product added with payload visible in draft summary.

### Step 3: Save Draft

**Context**: Persist the draft to store the payload in the backend.

UI action: Click Save to store the draft.

> Expected: Draft appears in the list; inspect details to confirm payload presence without execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[shopify]]
- [[injection]]
