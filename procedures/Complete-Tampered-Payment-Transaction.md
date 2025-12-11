---
tags:
  - transaction-completion
  - fraud
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: c04cd657-c260-4965-8475-ce5e1d2d68b2
created_at: '2025-12-11T06:10:15.781Z'
updated_at: '2025-12-11T06:10:15.781Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
---
# Complete Tampered Payment Transaction

## Summary

This procedure completes the payment after tampering, resulting in the injected amount being credited to the Steam wallet.

## Description

After forwarding the modified request, pay the small amount and wait for processing. The vulnerability causes Smart2Pay to credit the injected larger amount, leading to free wallet funds.

## Requirements

1. Tampered request forwarded
2. Ability to complete the payment (e.g., with $1)
3. Access to check Steam wallet balance

## Defense

Defensive measures and detection strategies:

- Monitor discrepancies between paid and credited amounts
- Implement transaction auditing

## Objectives

1. Finalize the fraudulent transaction
2. Verify credited amount
3. Achieve financial impact

## Instructions

### Step 1: Proceed with Payment

**Context**: Complete the transaction on the payment page.

Pay the displayed small amount (e.g., $1).

### Step 2: Check Wallet Balance

**Context**: Verify the credit.

Refresh Steam wallet to confirm the larger injected amount is added.

> Transaction should process successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- transaction-completion
- fraud
