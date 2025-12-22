---
id: proc-fund-distributor-001
tags:
  - ethereum
  - funding
  - transfer
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Blockchain
  - Ethereum
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.510Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Fund the Smart Contract with ETH

## Summary

This procedure transfers ETH from an attacker's wallet to the deployed distributor smart contract, providing funds for the subsequent distribution attempts that will partially credit Coinbase wallets.

## Description

Funding is a standard Ethereum transaction but critical for the exploit, as it supplies the ETH that appears to be distributed (though reverted on-chain). The amount should cover partial sends to valid wallets (e.g., 0.1 ETH for 3-4 recipients). Use any Ethereum wallet interface; no special privileges needed beyond gas fees.

## Requirements

1. Deployed distributor contract address
2. Attacker's Ethereum wallet with sufficient ETH (e.g., 0.2 ETH total)
3. Network access (e.g., via MetaMask)
4. Gas estimation tool (built into wallets)

## Defense

Defensive measures and detection strategies:

- Flag large or frequent fundings to new contracts interacting with exchange wallets
- Rate-limit contract funding from suspicious sources
- Correlate funding with subsequent reverting txs

## Objectives

1. Transfer ETH to contract without loss
2. Verify contract balance increase
3. Prepare for distribution execution

## Instructions

### Step 1: Prepare Wallet

**Context**: Ensure wallet has ETH and connect to network.

Open MetaMask, switch to Ethereum mainnet, confirm balance > intended fund amount + gas (e.g., 0.15 ETH total for 0.1 ETH fund).

> Expected: Wallet ready, no errors.

### Step 2: Execute Transfer

**Context**: Send ETH directly to contract address.

In MetaMask, select 'Send', enter distributor contract address, amount (e.g., 0.1 ETH), confirm gas, and submit.

> Expected: Tx hash; check Etherscan for confirmation and contract balance update.

### Step 3: Verify Funding

**Context**: Confirm success on blockchain explorer.

Visit Etherscan.io, search contract address, view 'ETH Balance' tab.

> Expected: Balance matches sent amount.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ethereum]]
- [[funding]]
- [[transfer]]
