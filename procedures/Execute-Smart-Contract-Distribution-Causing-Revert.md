---
id: proc-execute-reverting-distribution-001
tags:
  - distribution
  - revert
  - exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Blockchain
  - Ethereum
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.505Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute Smart Contract Distribution Causing Revert

## Summary

This procedure triggers the distributor contract's ETH distribution function with a list of valid Coinbase wallets and a faulty one, causing a revert on the blockchain while Coinbase credits the partial transfers.

## Description

The core exploit step: Calling the payable distribute function sends ETH in sequence, crediting early wallets on Coinbase before the revert undoes the blockchain state. This creates the balance inflation discrepancy. Requires interaction via contract ABI; monitor both blockchain and Coinbase for outcomes.

## Requirements

1. Funded distributor contract
2. List of 3+ valid Coinbase ETH addresses + faulty address
3. Wallet connected for transaction signing
4. ABI of distributor (from deployment)

## Defense

Defensive measures and detection strategies:

- Verify full tx success (no reverts) before crediting any partial events
- Alert on credits from reverted txs
- Simulate tx outcomes in sandbox before processing

## Objectives

1. Initiate distribution triggering partial credits
2. Confirm blockchain revert
3. Observe Coinbase balance increase

## Instructions

### Step 1: Prepare Recipient List

**Context**: Assemble addresses for the call.

List: [coinbase_wallet1, coinbase_wallet2, faulty_address]. Ensure faulty is the last.

> Expected: Array ready for function input.

### Step 2: Interact with Contract

**Context**: Call distribute via Remix or Etherscan.

In Remix, load deployed contract ABI/address, call distribute with recipients array and value (e.g., 0.1 ETH), execute.

> Expected: Tx submitted; status 'Reverted' on Etherscan.

### Step 3: Monitor Coinbase

**Context**: Check for credits post-tx.

Log into Coinbase, view ETH balance for targeted wallets.

> Expected: Increase by partial amount (e.g., 0.03 ETH per valid wallet).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[distribution]]
- [[revert]]
- [[exploit]]
