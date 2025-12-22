---
id: proc-execute-fund-transfer
tags:
  - fund-theft
  - access-bypass
  - msg-execute-forgery
type: procedure
tools:
  - '[[tools/cargo]]'
  - '[[tools/Rust]]'
tactics:
  - '[[Defense Evasion]]'
  - '[[Collection]]'
commands:
  - '[[commands/cargo-run]]'
verified: false
platforms:
  - Blockchain
  - Cosmos SDK
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:30:46.774Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Credentials In Files]]'
---
---

# Execute-Unauthorized-Fund-Transfer

## Summary

This procedure demonstrates the core exploitation by creating a periodic locking account, locking funds, waiting for unlock, and forging a MsgExecute to transfer funds using an arbitrary victim sender address.

## Description

The attack leverages the lack of sender validation in lockup.go's SendCoins (lines 285-284) and MsgExecute packing, allowing msg.Sender to be set arbitrarily, bypassing owner checks unlike in multisig contexts.

## Requirements

1. Running local Cosmos chain
2. Configured Rust POC project
3. Victim and attacker account keys

## Defense

Defensive measures and detection strategies:

- Validate msg.Sender against context in all modules
- Monitor for anomalous transfers from locking accounts
- Implement rate limiting on MsgExecute for locking periods

## Objectives

1. Create and lock funds in victim's account
2. Forge transfer message post-unlock
3. Achieve unauthorized fund movement

## Instructions

### Step 1: Create Locking Account

**Context**: Set up a periodic-locking-account for the victim (main.rs line 28).

**Command** ([[commands/cargo-run]] partial):
```bash
cargo run -- create-locking-account
```

> Executes Rust code to broadcast MsgPeriodicVestingAccount creation. Expected output: Account address returned.

### Step 2: Lock and Wait

**Context**: Lock funds and simulate unlock period.

**Instructions**: Use Rust client to send lock message, then wait (small period for POC).

**Command** (integrated in run):
```bash
# Handled in main.rs lock function
```

> Expected output: Lock transaction confirmed; wait logs period end.

### Step 3: Forge and Transfer

**Context**: Craft MsgExecute with arbitrary sender (main.rs line 55).

**Command** ([[commands/cargo-run]]):
```bash
cargo run -- execute-transfer
```

> Broadcasts forged SendCoins in MsgExecute. Expected output: Funds transferred to attacker.

### Step 4: Verify Theft

**Context**: Check balances.

**Command** (query balance):
```bash
cosmos-sdk query bank balances <victim-addr>
```

> Expected output: Victim balance reduced, attacker increased.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion
- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Credentials In Files]] Credentials In Files (message forgery as credential abuse)

### Sub-Techniques


## Commands Used

- [[commands/cargo-run]]
- [[commands/query-balance]]

## Tools Used

- [[tools/cargo]]
- [[tools/Rust]]

## Tags

- [[exploit-execution]]
- [[fund-theft]]
