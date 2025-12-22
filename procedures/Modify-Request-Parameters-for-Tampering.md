---
tags:
  - parameter-modification
  - injection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[T1659]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: d5df548e-437e-431f-bb5e-779761b94451
created_at: '2025-12-11T06:10:15.785Z'
updated_at: '2025-12-11T06:10:15.785Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1659]]'
---
# Modify Request Parameters for Tampering

## Summary

This procedure modifies the intercepted Smart2Pay request to inject a new 'amount' field via the email parameter, exploiting the weak hash concatenation.

## Description

Alter parameters to change 'Amount=2000' to 'Amount2=000' and split the email to inject 'amount=100' while keeping the concatenated string identical for hash validation. This tampers with the payment amount processed by Smart2Pay.

## Requirements

1. Intercepted request in Burp Suite
2. Understanding of the hash generation method
3. Crafted email from prior step

## Defense

Defensive measures and detection strategies:

- Use secure hashing with delimiters and canonicalization
- Validate parameter integrity server-side

## Objectives

1. Inject desired payment amount
2. Preserve hash validity
3. Enable fraudulent crediting

## Instructions

### Step 1: Analyze Parameters

**Context**: Examine the request in Burp.

Identify Amount, CustomerEmail, and Hash fields.

### Step 2: Inject via Email

**Context**: Modify to inject new field.

Change CustomerEmail to 'brix&amount=100&ab=c%40domain' and adjust Amount accordingly.

> Forward the modified request.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[T1659]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- parameter-modification
- injection
