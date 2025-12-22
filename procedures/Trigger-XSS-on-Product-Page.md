---
tags:
  - xss-trigger
  - execution
  - product-page
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Browser
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:33.421Z'
skill_level: low
impact_level: high
detection_risk: high
sub_techniques: []
id: 82589c97-31f4-403a-a592-735c0645e691
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-on-Product-Page

## Summary

This procedure triggers the stored XSS by viewing the affected WooCommerce product page, executing the JavaScript payload in the browser context of any visitor.

## Description

Once the malicious image is uploaded, WooCommerce displays the unsanitized title metadata on the product page (e.g., in alt text or tooltip). Accessing the page causes the browser to parse and execute the embedded script, allowing actions like cookie theft or page manipulation. This affects all users viewing the page, making it a persistent stored XSS.

## Requirements

1. Published product with malicious image
2. Frontend access to the site (no auth needed for trigger)
3. Vulnerable WooCommerce version (pre-patch)

## Defense

Defensive measures and detection strategies:

- Output-encode metadata with esc_attr or esc_html in templates
- Enable strict XSS protection via plugins like Sucuri
- Monitor browser console for script errors on product pages
- Use HTTP-only cookies to mitigate session theft

## Objectives

1. Load the product page to reflect the malicious metadata
2. Execute JavaScript in the victim's session
3. Achieve impacts like data exfiltration or defacement

## Instructions

### Step 1: Publish Product

**Context**: Make the product visible on the frontend.

In the product editor, set status to Published and save.

> Note the permalink (e.g., /product/malicious-product) for access.

### Step 2: Access Product Page

**Context**: Visit the page to trigger the XSS.

Open a browser and navigate to the product URL (e.g., https://target.com/product/malicious-product).

> The image loads, and metadata title is output, executing the script (e.g., alert or redirect).

### Step 3: Observe Execution

**Context**: Verify the payload runs as intended.

Check for alert popup, network requests to attacker domain, or page changes.

> Success if script executes; inspect page source to see unsanitized title in HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- trigger
- javascript
