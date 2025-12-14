---
id: proc-shopify-complete-checkout-001
tags:
  - shopify
  - checkout
  - completion
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:37.785Z'
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
# Complete-Checkout-Process

## Summary

This procedure finalizes the order in Shopify's checkout, storing the injected XSS payload and generating the vulnerable thank you page URL with a unique checkout ID.

## Description

Following payload injection, this step handles shipping and payment progression. Since the product is $0, payment can be skipped or use a test method. The order completion persists the first name payload, which will render on the thank you page.

## Requirements

1. Payload-injected checkout session
2. $0 product to avoid real payment
3. Valid shipping details

## Defense

Defensive measures and detection strategies:

- Audit order data for malicious strings before storage
- Delay thank you page rendering until sanitization
- Monitor for zero-value orders with suspicious inputs

## Objectives

1. Persist the payload in order records
2. Generate thank you page
3. Transition to exploitation phase

## Instructions

### Step 1: Select Shipping

**Context**: Choose free option.

Click 'Continue to shipping method' and select the $0 or free shipping option.

### Step 2: Proceed to Payment

**Context**: Handle payment minimally.

Click 'Continue to payment method'; since $0, skip card details if possible or use test info.

### Step 3: Finalize Order

**Context**: Submit and confirm.

Click 'Complete order' to process.

**Expected Output**: Redirect to thank you page with order confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- order-completion
- persistence
