---
tags:
  - blockchain
  - ethereum
  - smart-contract
  - exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/flip-kick-fake-auction]]'
  - '[[commands/end-skip-issue-dai]]'
  - '[[commands/end-pack-prepare-collateral]]'
  - '[[commands/end-cash-transfer-collateral]]'
  - '[[commands/end-flow-initiate-liquidation]]'
platforms:
  - Blockchain
  - Ethereum
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: 8ec827c1-93de-4202-8c9d-f874ddbf52c3
created_at: '2025-12-11T06:10:22.262Z'
updated_at: '2025-12-11T06:10:22.262Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Create Fake Auction via Flip.Kick

## Summary

This procedure exploits the lack of validation and access control in the flip.kick method of the flipper contract to create a fake auction with arbitrary bid values during the liquidation phase of the MakerDAO MCD system, enabling further steps to steal collateral.

## Description

The flip.kick method is publicly callable and does not validate parameters adequately during liquidation, allowing attackers to set a large fake bid without spending DAI. This is typically performed after initiating liquidation via end.flow. The target environment is an Ethereum blockchain with deployed MCD contracts in Solidity.

## Requirements

1. Access to Ethereum network with MCD system deployed
2. Ability to call smart contract methods (e.g., via web3 provider)
3. System in liquidation phase or ability to trigger it

## Defense

Defensive measures and detection strategies:

- Implement access controls and parameter validation in flip.kick
- Monitor for unusual auction creations during liquidation with large bid values

## Objectives

1. Create a fake auction with inflated bid
2. Set up for free DAI issuance
3. Enable collateral theft

## Instructions

### Step 1: Initiate Liquidation if Needed

**Context**: Ensure the system is in liquidation phase to allow public calls to flip.kick.

**Command** ([[commands/end-flow-initiate-liquidation]]):
```solidity
end.flow();
```

> This fixes the exchange rate and starts liquidation, expected to transition the system state.

### Step 2: Call Flip.Kick with Arbitrary Parameters

**Context**: Create the fake auction by setting a large bid and small lot.

**Command** ([[commands/flip-kick-fake-auction]]):
```solidity
flip.kick({bid: totalDAISupply, lot: smallNonZeroValue});
```

> This initiates the auction without validation, returning an auction ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/flip-kick-fake-auction]]
- [[commands/end-flow-initiate-liquidation]]

## Tools Used



## Tags

- [[blockchain]]
- [[ethereum]]
