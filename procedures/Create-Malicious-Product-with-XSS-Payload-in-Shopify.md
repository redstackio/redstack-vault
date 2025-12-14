---
id: proc-create-xss-product
tags:
  - xss
  - injection
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:38.096Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Product-with-XSS-Payload-in-Shopify

## Summary

This procedure involves creating a product in the Shopify admin interface with a malicious JavaScript payload embedded in the product name field, exploiting insufficient input sanitization to store the payload for later execution.

## Description

In the context of the Judge.me Shopify app vulnerability, product names are stored without proper HTML escaping. An attacker with admin access crafts a product title containing an XSS payload, such as an img tag with an onerror handler. This payload remains dormant until rendered in an unsafe context, like the app's deletion interface. Prerequisites include admin privileges on a Shopify store with the Judge.me app installed. Expected outcomes include successful storage of the payload, verifiable by inspecting the product list where raw HTML tags are visible.

## Requirements

1. Valid Shopify admin credentials
2. Judge.me app installed and configured in the store
3. Access to the Shopify admin dashboard via web browser

## Defense

Defensive measures and detection strategies:

- Implement server-side input sanitization for all user-controlled fields using libraries like DOMPurify
- Enable Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous product creations with suspicious characters (e.g., <, >, ") via audit logs

## Objectives

1. Store unsanitized XSS payload in product metadata
2. Prepare for payload execution in admin-facing interfaces
3. Demonstrate lack of input validation in Shopify product creation

## Instructions

### Step 1: Access Product Creation

**Context**: Log in to the Shopify admin and navigate to the product creation page to input the malicious payload.

No specific command; perform via UI:

1. Go to Shopify Admin > Products > Add product.
2. In the Title field, enter: `444"><img src=x onerror=prompt(document.domain)>`
3. Fill minimal details (e.g., blank description) and click Save.

> This stores the payload without escaping, as verified by viewing the product list where the HTML breaks out of any containing elements.

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
- [[injection]]
- [[shopify]]
