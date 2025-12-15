---
id: proc-uuid-3
tags:
  - coinbase
  - external-transfer
  - double-spending
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
  - Bitcoin (BTC)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data Manipulation]]'
updated_at: '2025-12-14T17:28:20.291Z'
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
# Execute-Concurrent-External-Transfer

## Summary

This procedure exploits the unlocked balance during a pending vault transfer by sending the same funds to an external BTC wallet, achieving partial double-spending.

## Description

While the vault transfer is pending, the main wallet interface allows initiating another transfer using the full balance. This step targets external BTC addresses, processing the transaction immediately. In the Coinbase web environment, this leads to funds being withdrawn externally without reservation conflicts. The outcome is a successful external transfer, leaving the pending vault action to cause over-deduction later.

## Requirements

1. Pending vault transfer active
2. External BTC wallet address ready
3. Same BTC amount available in main wallet

## Defense

Defensive measures and detection strategies:

- Reserve funds on pending transfer initiation
- Flag concurrent transfers from the same balance pool

## Objectives

1. Withdraw funds externally during pending state
2. Confirm no locking prevents the transfer
3. Set up for negative balance on approval

## Instructions

### Step 1: Prepare External Address

**Context**: Obtain a receiving BTC address for the transfer.

**Instructions**: Use an external wallet (e.g., another exchange or personal wallet) to generate a BTC receive address.

> Copy the address for use in Coinbase.

### Step 2: Initiate External Transfer

**Context**: Send the same amount as the pending vault transfer to the external address.

**Instructions**: In Coinbase main wallet, select 'Send', paste external BTC address, enter matching amount, and confirm.

> Transfer processes; funds deduct from main balance.

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
- [[external-transfer]]
- [[double-spending]]
