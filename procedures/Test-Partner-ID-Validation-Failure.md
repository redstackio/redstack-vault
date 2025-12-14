---
tags:
  - web
  - validation-test
  - sqli
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 313eede5-09b4-44ae-b60d-6987744e1566
created_at: '2025-12-14T03:46:20.634Z'
updated_at: '2025-12-14T03:46:20.634Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test Partner ID Validation Failure

## Summary

This procedure tests the standard validation of the partner ID field to establish baseline behavior before attempting exploitation.

## Description

In the Teavana sign-up form, entering a normal invalid partner ID triggers a verification failure, confirming the field's reliance on backend SQL queries vulnerable to injection. This step uses the Salesforce Commerce Cloud's AJAX handling and highlights the lack of sanitization. Expected outcomes include an error message, validating the bypass potential without alerting defenses.

## Requirements

1. Loaded sign-up form
2. Web browser
3. Basic knowledge of form submission

## Defense

Defensive measures and detection strategies:

- Enforce strict input length and format checks client-side
- Log failed validations for anomaly detection

## Objectives

1. Confirm validation enforces partner ID checks
2. Observe error messaging for injection clues
3. Set up for payload comparison

## Instructions

### Step 1: Enter Invalid Partner ID and Submit

**Context**: Fill required fields and use a simple test value to trigger the check.

**Action**:

Input '1234' in the partnerno field, complete other fields (e.g., email: test@example.com, password: test123), and submit.

> Expected output: Error message 'We are unable to verify Starbucks partner ID' appears, preventing sign-up. This indicates SQL-based verification; no account is created.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web
- validation-test
- sqli
