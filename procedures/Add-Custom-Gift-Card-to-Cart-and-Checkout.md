---
id: proc-uuid-4
tags:
  - xss
  - persistence
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:36.290Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Add-Custom-Gift-Card-to-Cart-and-Checkout

## Summary

This procedure finalizes the malicious design, adds it to the cart, and advances to checkout where the stored payload will be rendered as a clickable link.

## Description

Following payload injection in the Shopify design tool, this step completes the customization and adds the tainted gift card to the shopping cart. Navigation to https://checkout.shopify.com/ stores the artwork URL server-side, making it persistent for any user viewing the checkout. This sets up the stored XSS for execution upon link interaction.

## Requirements

1. Payload successfully injected
2. Active browser session
3. Cart functionality enabled

## Defense

Defensive measures and detection strategies:

- Scan cart items for malicious URLs before rendering
- Restrict custom uploads in checkout contexts

## Objectives

1. Persist the payload via cart addition
2. Transition to vulnerable checkout rendering
3. Simulate victim interaction setup

## Instructions

### Step 1: Complete Design

**Context**: Finalize the gift card with the injected URL.

No command required.

> Review and save the design, ensuring the artwork URL is associated.

### Step 2: Add to Cart and Checkout

**Context**: Move the item to cart and load checkout.

No command required.

> Click 'Add to Cart', then proceed to https://checkout.shopify.com/. The custom item should appear with its artwork link.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Persistence]]
- [[shopify]]
