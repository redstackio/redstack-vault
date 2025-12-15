---
id: proc-withdraw-inflated-001
tags:
  - withdrawal
  - cashout
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Blockchain
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:36.502Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Withdraw Inflated Balance to External Wallet

## Summary

This procedure transfers the inflated ETH balance from Coinbase to an external attacker-controlled wallet, realizing the financial gain from the balance inflation exploit.

## Description

The final step: Using Coinbase's withdrawal feature to move 'credited' ETH off-platform. Coinbase processes based on internal records, not blockchain state, enabling the theft. Use a non-KYC wallet to launder; expect possible delays or flags on large amounts.

## Requirements

1. Inflated balance in Coinbase account
2. External Ethereum wallet address (e.g., fresh MetaMask)
3. Verified Coinbase account (2FA enabled)
4. Withdrawal limits checked (may need verification)

## Defense

Defensive measures and detection strategies:

- Reconcile balances with blockchain before withdrawals
- Flag rapid balance growth followed by large outflows
- Implement withdrawal holds for anomalous accounts

## Objectives

1. Initiate withdrawal of full inflated amount
2. Confirm receipt in external wallet
3. Avoid detection during transfer

## Instructions

### Step 1: Prepare External Wallet

**Context**: Set up receiving address.

Create or use existing external wallet, copy ETH address.

> Expected: Valid address ready.

### Step 2: Initiate Withdrawal

**Context**: Use Coinbase interface.

Log in, go to Portfolio > ETH > Send, enter external address, amount (full inflated), confirm 2FA.

> Expected: Pending withdrawal notification.

### Step 3: Verify Receipt

**Context**: Monitor blockchain.

Check Etherscan for incoming tx to external wallet.

> Expected: ETH received, matching withdrawn amount.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[withdrawal]]
- [[cashout]]
- [[Exfiltration]]
