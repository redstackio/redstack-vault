---
tags:
  - xss
  - guest-checkout
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:33.597Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 86924f28-3594-4e99-8d8f-4fc19936c31f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Perform-Guest-Checkout-to-Store-XSS-Payload

## Summary

This procedure completes a guest checkout on Shopify with the malicious _landing_page cookie set, storing the JavaScript payload in the order's conversion data for later admin exploitation.

## Description

During guest checkout, Shopify captures the _landing_page cookie and associates it with the order for analytics. Unsanitized, this allows the javascript: URI to be persisted server-side. The attack requires a valid product in the store and minimal user details; outcomes include the payload being reflected as a link in admin order views.

## Requirements

1. Malicious cookie already set from prior procedure
2. Public access to storefront with products available
3. Valid payment method for minimal purchase (or test mode if available)

## Defense

Defensive measures and detection strategies:

- Validate and escape landing page URLs during order creation, stripping protocol handlers like javascript:
- Rate-limit guest checkouts to detect abuse patterns
- Audit order data for suspicious URI schemes in logs

## Objectives

1. Persist the payload in order metadata without detection
2. Generate a valid order ID for admin access
3. Ensure no sanitization occurs during storage

## Instructions

### Step 1: Add Product to Cart

**Context**: Initiate the purchase process to trigger order creation.

Browse to a product page, select a low-cost item, and click 'Add to cart'.

> Expected: Cart updates; proceed to checkout button appears.

### Step 2: Complete Guest Checkout

**Context**: Use guest mode to submit the order, capturing the cookie value.

Click 'Checkout', select 'Continue as guest', enter fake details (name, email, address, payment info), and submit. Avoid login to ensure guest flow.

> Expected: Order confirmation with ID; payload stored invisibly in backend.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[xss]]
- [[guest-checkout]]
