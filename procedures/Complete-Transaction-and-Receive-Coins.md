---
id: proc-uuid-5
tags:
  - idor
  - completion
  - exploitation
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:33.677Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Complete-Transaction-and-Receive-Coins

## Summary

Finalizes the PayPal payment at the reduced price and verifies the receipt of the larger coin quantity, confirming the IDOR exploitation success.

## Description

With the swapped order_id, the transaction processes as $1.99, but Reddit's fulfillment uses the large package context, crediting extra coins. This step validates the financial impact.

## Requirements

1. Modified response forwarded
2. PayPal login
3. Reddit account balance check access

## Defense

Defensive measures and detection strategies:

- Re-validate order details at fulfillment stage
- Discrepancy alerts for coin credits vs. payments
- Post-transaction audits

## Objectives

1. Process low payment
2. Credit high-value coins
3. Confirm exploit

## Instructions

### Step 1: Pay via PayPal

**Context**: Complete the transaction on the redirected page.

Manual: Enter PayPal credentials and confirm $1.99 payment.

> Transaction should succeed without issues.

### Step 2: Verify Coin Balance

**Context**: Check Reddit account after redirect back.

Manual: View coin balance; expect 1100 coins added.

> Success if coins exceed paid amount.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- idor
- verification
- financial
