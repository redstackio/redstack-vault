---
id: proc-test-giftcert-impact
tags:
  - csrf
  - dos
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:27:42.810Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Test-Impact-of-Adding-Gift-Certificate

## Summary

This procedure manually adds a gift certificate to the cart via the vulnerable endpoint and assesses the persistent disruption to user purchasing capabilities.

## Description

After adding a gift card (e.g., $100), the cart cannot be emptied, credit card payments are disabled, and the issue persists across logouts and sessions for weeks, effectively locking the account from normal use. Targets Demandware eCommerce; outcomes include confirmed denial of service.

## Requirements

1. Authenticated account on target site
2. Browser for manual testing
3. Access to cart and checkout pages

## Defense

Defensive measures and detection strategies:

- Allow full cart emptying including gift certs
- Session-based cart resets on logout
- Alert on unusual cart modifications

## Objectives

1. Add gift cert to cart
2. Verify persistence and lockout
3. Document financial impact

## Instructions

### Step 1: Add Gift Certificate

**Context**: Use the endpoint to insert a gift cert into an active cart.

Navigate to the GiftCert-Purchase page and submit a POST with amount=100 and recipient email. No command needed; use browser form.

> Expected output: Confirmation of addition to cart.

### Step 2: Test Cart Behaviors

**Context**: Attempt to remove item and use payments.

Try emptying cart, proceeding to checkout with credit card, and logging out/in.

> Expected output: Item persists; credit card option gone; lockout confirmed after re-login.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[dos]]
- [[web]]
