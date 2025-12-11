---
tags:
  - blockchain
  - ethereum
  - smart-contract
  - exploit
type: procedure
tools: []
tactics:
  - '[[Execution]]'
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
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: 9d211fc8-3755-46ad-a785-d43901e261b6
created_at: '2025-12-11T06:10:22.250Z'
updated_at: '2025-12-11T06:10:22.250Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Convert DAI to Collateral via End.Pack and End.Cash

## Summary

This procedure converts the free DAI obtained into all available collateral by calling end.pack and end.cash, completing the theft if the DAI matches the total supply.

## Description

Using the issued DAI, end.pack prepares the conversion, and end.cash transfers the collateral, exploiting trust in the end contract.

## Requirements

1. Free DAI from end.skip
2. DAI amount at least total supply
3. System in liquidation

## Defense

Defensive measures and detection strategies:

- Validate DAI amounts in end.pack and end.cash
- Audit for large collateral transfers

## Objectives

1. Convert DAI to collateral
2. Transfer all collateral to attacker
3. Achieve complete fund loss for users

## Instructions

### Step 1: Call End.Pack to Prepare

**Context**: Pack the DAI for conversion.

**Command** ([[commands/end-pack-prepare-collateral]]):
```solidity
end.pack(daiAmount);
```

> Prepares the DAI for cashing out.

### Step 2: Call End.Cash to Transfer

**Context**: Complete the conversion and transfer collateral.

**Command** ([[commands/end-cash-transfer-collateral]]):
```solidity
end.cash();
```

> Transfers all collateral to the attacker.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/end-pack-prepare-collateral]]
- [[commands/end-cash-transfer-collateral]]

## Tools Used



## Tags

- [[blockchain]]
- [[ethereum]]
