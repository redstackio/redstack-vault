---
id: proc-uuid-modify-amount
tags:
  - parameter-tampering
  - business-logic
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:29:29.045Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Donation-Amount-to-Negative

## Summary

This procedure alters the support rider donation price fields in the intercepted HTTP request to a negative fractional value like -0.99, exploiting the lack of server-side validation to reduce the order total.

## Description

During Zomato's checkout, the donation request payload includes fields for the amount that accept negative values due to insufficient bounds checking. This procedure targets those fields in the proxy tool, changing them to induce a discount. It assumes the request is already intercepted; the result is a tampered payload ready for forwarding, leading to minor financial impact per order.

## Requirements

1. Intercepted request in Burp Suite Repeater or Proxy
2. Knowledge of payload format (JSON with 'donation_money' fields)
3. No additional tools beyond proxy

## Defense

Defensive measures and detection strategies:

- Server-side validation to enforce positive-only amounts (e.g., >=0)
- Input sanitization rejecting fractional negatives
- Audit logs for negative values in requests

## Objectives

1. Identify and edit the two donation price fields
2. Set values to -0.99 for maximum ~1 rupee reduction
3. Ensure payload remains structurally valid

## Instructions

### Step 1: Inspect Payload

**Context**: Locate editable fields.

In Burp, view raw request; find JSON keys like "donation_money_1" and "donation_money_2".

> Expected: Original positive values (e.g., 25.00) displayed.

### Step 2: Edit to Negative

**Context**: Apply the manipulation.

Change both fields to "-0.99"; drop any client-side JS validations.

> Expected: Payload updated; preview total reduction in UI if resent.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- parameter-tampering
- business-logic
