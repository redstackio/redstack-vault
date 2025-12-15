---
id: proc-uuid-4
tags:
  - coinbase
  - vault-approval
  - balance-manipulation
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
  - Coinbase Vault
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data Manipulation]]'
updated_at: '2025-12-14T17:28:20.289Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Stored Data Manipulation]]'
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Data Manipulation]]'
---
# Approve-Vault-Transfer-for-Negative-Balance

## Summary

This procedure approves the pending vault transfer after an external withdrawal, resulting in double deduction and a negative main wallet balance, demonstrating the full balance manipulation vulnerability.

## Description

Upon approval, Coinbase deducts the transfer amount from the main wallet again, despite the prior external send. This business logic flaw in the web platform allows negative balances, potentially enabling unauthorized extractions. The scenario assumes prior steps completed, with outcomes including vault funding and main wallet overdraw, highlighting double-spending risks in cryptocurrency handling.

## Requirements

1. Active pending vault transfer
2. Prior external transfer completed
3. Access to approval interface

## Defense

Defensive measures and detection strategies:

- Validate available balance before approval
- Alert on negative balance attempts
- Reconcile pending transactions against actual funds

## Objectives

1. Complete vault transfer approval
2. Trigger double deduction
3. Achieve and observe negative balance

## Instructions

### Step 1: Locate Pending Transfer

**Context**: Return to the transaction history to find the pending item.

**Instructions**: In Coinbase, go to 'Transactions' and select the pending vault transfer.

> Pending status should still be visible.

### Step 2: Approve Transfer

**Context**: Confirm the approval to finalize.

**Instructions**: Click 'Approve' on the pending transfer and follow any 2FA prompts.

> Upon approval, vault balance increases; main wallet goes negative.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Data Manipulation]] Data Manipulation

### Sub-Techniques

- [[Stored Data Manipulation]] Stored Data Manipulation

## Commands Used

- None

## Tools Used

- None

## Tags

- [[coinbase]]
- [[vault-approval]]
- [[balance-manipulation]]
