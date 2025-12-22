---
id: proc-uuid-4
tags:
  - modification
  - data-access
  - idor
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:47.477Z'
skill_level: intermediate
impact_level: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Checkout-Ari-and-Resend-Request

## Summary

This procedure modifies the 'checkout_ari' parameter in the intercepted request to access another user's order data, exploiting the IDOR vulnerability.

## Description

By replacing the original 'checkout_ari' with a valid identifier from another transaction, the backend processes the request without authorization checks, returning sensitive data such as addresses, payments, and products.

## Requirements

1. Intercepted request in Burp Repeater
2. Knowledge of other valid 'checkout_ari' values (from prior tests)
3. Understanding of JSON request format

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization for object references
- Validate 'checkout_ari' against user session
- Monitor for parameter tampering in logs

## Objectives

1. Alter the parameter
2. Retrieve unauthorized data
3. Expected outcome: Sensitive information exposed

## Instructions

### Step 1: Edit Parameter

**Context**: Target the vulnerable field.

In Burp Repeater, change 'checkout_ari': 'XXXXXXXXXXXXXXXX' to 'checkout_ari': 'YYYYYYYYYYYYYYYYY'.

> Ensure the request body remains valid JSON.

### Step 2: Send Modified Request

**Context**: Trigger the unauthorized access.

Click 'Send' to resend the request to the API.

> Expected output: Response with other user's order details, including personal info.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[modification]]
- [[data-access]]
- [[idor]]
