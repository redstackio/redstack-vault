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
impact_level: high
detection_risk: medium
sub_techniques: []
id: 615e4efa-8099-4e36-876a-2ee88c593071
created_at: '2025-12-11T06:10:22.254Z'
updated_at: '2025-12-11T06:10:22.254Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Issue Free DAI via End.Skip

## Summary

This procedure uses the end.skip method to process a fake auction and issue free DAI to the attacker based on the arbitrary bid value set in the previous step.

## Description

After creating a fake auction, calling end.skip trusts the bid and mints DAI without requiring actual payment, exploiting the lack of validation in the end contract during liquidation.

## Requirements

1. Existing fake auction ID from flip.kick
2. System in liquidation phase
3. Ethereum network access

## Defense

Defensive measures and detection strategies:

- Add validation in end.skip to verify bid legitimacy
- Monitor for large DAI issuances without corresponding payments

## Objectives

1. Obtain free DAI equal to fake bid
2. Prepare for collateral conversion
3. Escalate to full theft

## Instructions

### Step 1: Call End.Skip on Fake Auction

**Context**: Process the auction to issue DAI.

**Command** ([[commands/end-skip-issue-dai]]):
```solidity
end.skip(auctionId);
```

> This issues DAI to the caller's address based on the bid, expected to increase balance.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/end-skip-issue-dai]]

## Tools Used



## Tags

- [[blockchain]]
- [[ethereum]]
