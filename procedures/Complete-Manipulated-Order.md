---
id: proc-uuid-complete-order
tags:
  - payment
  - order-completion
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:29.039Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Complete-Manipulated-Order

## Summary

This procedure finalizes the exploited checkout by processing payment with the reduced total, realizing the price manipulation.

## Description

With the cart total lowered via the negative donation, standard payment flow proceeds unchanged. This targets Zomato's payment integration, assuming no further validations. Prerequisites include the tampered cart; outcomes are a successful order with minor savings.

## Requirements

1. Valid payment method (card, UPI)
2. Manipulated cart active
3. Zomato account logged in

## Defense

Defensive measures and detection strategies:

- Re-validate totals at payment gateway
- Flag orders with negative components in backend
- Post-order audits for discrepancies

## Objectives

1. Process payment at reduced rate
2. Confirm order placement
3. Avoid payment failures

## Instructions

### Step 1: Proceed to Payment

**Context**: Initiate finalization.

Click 'Place Order'; select payment option.

> Expected: Payment page loads with reduced total.

### Step 2: Submit Payment

**Context**: Complete transaction.

Enter details and confirm; monitor for success.

> Expected: Order confirmed; receipt shows manipulated amount.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- payment
- order-completion
