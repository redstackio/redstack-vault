---
id: proc-upserve-verify-order
tags:
  - order-verification
  - charge-check
  - financial-impact
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
updated_at: '2025-12-14T17:28:36.496Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Order-Acceptance-and-Reduced-Charge

## Summary

This procedure confirms that the Upserve OLO system has accepted the manipulated order and applied the reduced total to the charge, validating the exploitation's success.

## Description

Post-submission, the system processes the order using the provided confirmation_code and charges the manipulated amount (e.g., $18.70). Order history reflects the tampered total, with negative quantities causing out-of-balance checks that require manual restaurant intervention.

## Requirements

1. Access to order history or confirmation emails.
2. Payment method details to check charged amount.
3. Screenshots or logs for evidence.

## Defense

Defensive measures and detection strategies:

- Implement post-processing audits for order balances.
- Integrate payment gateway validations that reject mismatched totals.
- Use anomaly detection on charge amounts vs. expected values.

## Objectives

1. Confirm order processing without errors.
2. Validate the financial impact (undercharge).
3. Document for proof-of-concept.

## Instructions

### Step 1: Retrieve Order Confirmation

**Context**: Use the returned confirmation_code to query order status.

Access via API GET /orders/{confirmation_code} or user dashboard.

> Expected: Details showing total 1870 cents ($18.70).

### Step 2: Check Payment Charge

**Context**: Review payment processor logs or statements for the applied amount.

Verify charge matches manipulated total, not original prices.

> Success if charged $18.70 instead of higher legitimate amount.

### Step 3: Inspect Order History

**Context**: View stored order in system for tampered values.

Screenshots should show negative quantity and reduced total.

> Indicators: Out-of-balance flag or manual reconciliation needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[order-verification]]
- [[charge-check]]
