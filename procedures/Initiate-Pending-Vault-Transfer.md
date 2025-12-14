---
id: proc-uuid-2
tags:
  - coinbase
  - pending-transfer
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
  - Coinbase Vault
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data Manipulation]]'
updated_at: '2025-12-14T17:28:20.294Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[Stored Data Manipulation]]'
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Data Manipulation]]'
---
# Initiate-Pending-Vault-Transfer

## Summary

This procedure initiates a transfer from the main Coinbase wallet to a vault, placing it in a pending approval state that does not lock the funds, setting up for potential double-spending exploits.

## Description

Coinbase's vault transfer feature requires approval for security, but during the pending period (typically a few minutes), the main wallet balance remains available for other transactions. This business logic gap allows the same funds to be used concurrently. The procedure targets the web interface, assuming a vault exists and BTC balance is available. Outcomes include a pending transaction with no balance reservation, enabling further manipulation.

## Requirements

1. Existing Coinbase vault
2. Sufficient BTC in main wallet (e.g., 0.01 BTC for testing)
3. Web access to Coinbase wallet interface

## Defense

Defensive measures and detection strategies:

- Lock balances immediately upon transfer initiation
- Monitor for multiple pending transactions on the same funds

## Objectives

1. Place funds in pending vault transfer
2. Confirm balance remains unlocked
3. Enable concurrent transaction opportunities

## Instructions

### Step 1: Select Transfer Option

**Context**: From the main wallet, choose to transfer to the vault.

**Instructions**: In the Coinbase wallet, select BTC balance, click 'Send' or 'Transfer', choose the vault as destination, enter amount (e.g., full available BTC), and initiate.

> The interface shows the transfer as pending; balance does not deduct yet.

### Step 2: Verify Pending State

**Context**: Check transaction history to confirm status.

**Instructions**: Navigate to transaction history and observe the pending vault transfer.

> Expected: Pending status with timer (few minutes); main balance unchanged.

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
- [[pending-transfer]]
- [[double-spending]]
