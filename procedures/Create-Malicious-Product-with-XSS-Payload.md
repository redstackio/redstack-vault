---
tags:
  - xss
  - payload-injection
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - Shopify
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 98d4e415-0cf4-42ca-b829-7cb53458d81a
created_at: '2025-12-14T03:46:32.060Z'
updated_at: '2025-12-14T03:46:32.060Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Product-with-XSS-Payload

## Summary

This procedure injects a stored XSS payload into a Shopify product's name field via the Judge.me app, setting the stage for persistence and later execution in the admin interface.

## Description

In the context of the Judge.me Shopify app, product names are not fully sanitized when associated with questions, especially for out-of-stock items. This procedure creates a product with an HTML-encoded XSS payload in the name, such as `&#34;&#62;&#60;img src=x onerror=prompt(document.domain)&#62; &#60;img src=x onerror=prompt(document.domain)&#62;`, which decodes to `"><img src=x onerror=prompt(document.domain)> <img src=x onerror=prompt(document.domain)>`. The payload is stored server-side and remains dormant until triggered. Prerequisites include access to create products, either as a customer (if permitted) or admin. Expected outcome: Payload stored without immediate execution.

## Requirements

1. Valid Shopify account with product creation permissions
2. Judge.me Product Reviews app installed on the target store
3. Web browser for interface navigation

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding for all user-controlled fields like product names (e.g., use HTML entity encoding consistently)
- Apply Content Security Policy (CSP) to block inline scripts and unsafe image sources in admin panels
- Monitor for anomalous product creations with script-like content via logging

## Objectives

1. Persist XSS payload in product metadata
2. Associate payload with Judge.me for admin exposure
3. Bypass basic sanitization checks

## Instructions

### Step 1: Access Product Creation

**Context**: Log in to the Shopify interface to create a new product.

Navigate to the storefront or admin dashboard and select 'Add Product'. Fill in basic details like description and price, but focus on the name field.

### Step 2: Inject Payload

**Context**: Set the product name to the encoded payload to evade initial filters.

Enter the name as `&#34;&#62;&#60;img src=x onerror=prompt(document.domain)&#62; &#60;img src=x onerror=prompt(document.domain)&#62;`. Save the product.

> Verify by viewing the product page source; the payload should appear encoded but intact.

### Step 3: Confirm Storage

**Context**: Ensure the payload is stored without triggering.

Refresh the product page and inspect the HTML; no alert should fire yet.

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
- [[payload-injection]]
