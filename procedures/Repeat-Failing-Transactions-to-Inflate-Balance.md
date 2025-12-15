---
id: proc-repeat-inflation-001
tags:
  - iteration
  - inflation
  - accumulation
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Blockchain
  - Ethereum
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.503Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Repeat Failing Transactions to Inflate Balance

## Summary

This procedure iteratively deploys, funds, and executes the reverting distribution multiple times to accumulate inflated ETH credits on Coinbase wallets without corresponding on-chain transfers.

## Description

Repetition amplifies the exploit: Each cycle adds to the balance discrepancy. Automate if possible (e.g., script in Hardhat), but manual via Remix works. Stop when balance reaches withdrawal threshold (e.g., 1 ETH inflated). Track to avoid detection via volume.

## Requirements

1. Successful single execution validated
2. Sufficient ETH for multiple fundings (e.g., 2 ETH total)
3. Script or manual process for repetition
4. Monitoring access to Coinbase and Etherscan

## Defense

Defensive measures and detection strategies:

- Detect patterns of repeated reverts from same contract/source
- Cap balance credits per tx or time window
- Manual review for anomalous balance growth

## Objectives

1. Execute 10+ cycles
2. Achieve target inflation (e.g., >0.5 ETH)
3. Minimize gas costs

## Instructions

### Step 1: Automate or Loop Manually

**Context**: Prepare for multiple runs.

Use a loop in a deployment script or manually repeat Steps 1-3 from prior procedures 10-20 times.

> Expected: Series of tx hashes, all reverting.

### Step 2: Track Progress

**Context**: Monitor accumulation.

After each cycle, refresh Coinbase balance.

> Expected: Incremental increases (e.g., +0.09 ETH per cycle for 3 wallets).

### Step 3: Validate Total

**Context**: Confirm inflation.

Compare Coinbase total vs. attacker's on-chain spend (should be near-zero net).

> Expected: Inflated balance >> funded amounts.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[iteration]]
- [[inflation]]
- [[accumulation]]
