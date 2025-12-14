---
tags:
  - xss
  - persistence
  - submission
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 5e0a48c1-4d34-4ae2-b3eb-039bf162a0a5
created_at: '2025-12-14T03:15:35.894Z'
updated_at: '2025-12-14T03:15:35.894Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit-Order-to-Store-Payload

## Summary

This procedure submits the billing form with the injected XSS payload, storing it server-side in the order database for later execution when details are viewed.

## Description

Following payload injection, this step completes the form submission by clicking 'Place Order', persisting the unsanitized data in ExpressionEngine's backend. The ZIP Code field can also receive the payload if not already targeted. Even with payment failure (e.g., invalid CVV), the order record is created, reflecting the payload in confirmation or admin views. This establishes persistence for the stored XSS attack.

## Requirements

1. Completed payload injection in form fields
2. Valid card details except for testing purposes
3. Active session on the billing page

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all inputs before database storage
- Use prepared statements and escape user data in PHP/ExpressionEngine
- Audit order logs for anomalous data patterns indicating injection attempts

## Objectives

1. Persist the payload in the order record
2. Trigger any immediate reflection on submission
3. Ensure storage without backend errors

## Instructions

### Step 1: Complete Remaining Fields

**Context**: Fill any untouched fields to enable submission.

If not already done, inject the payload into ZIP Code: `'><img src=x onerror=prompt(0);>`.

> Ensures comprehensive coverage across all storable fields.

### Step 2: Submit the Form

**Context**: Finalize the order to store data server-side.

Click 'Place Order' button.

> Order processes; payload is saved in database, potentially visible on confirmation page.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Persistence]]
