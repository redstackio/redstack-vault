---
id: proc-start-cosmos-chain
tags:
  - cosmos-chain
  - local-testnet
  - setup
type: procedure
tools:
  - '[[tools/make]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/setup-chain]]'
verified: false
platforms:
  - Blockchain
  - Cosmos SDK
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:30:46.778Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
---

# Start-Local-Cosmos-Chain

## Summary

This procedure initializes and starts a local Cosmos SDK testnet chain, providing an environment to reproduce the lockup module vulnerability.

## Description

Using the built SDK binaries, the setup_chain script configures a genesis block with the lockup module enabled, allowing creation of periodic-locking-accounts for exploitation testing.

## Requirements

1. Compiled Cosmos SDK binaries
2. Executable setup_chain script
3. Local machine with sufficient resources

## Defense

Defensive measures and detection strategies:

- Restrict local chain startups in production-like environments
- Log and monitor unauthorized testnet initiations
- Use containerized setups (e.g., Docker) for isolation

## Objectives

1. Initialize chain with vulnerable modules
2. Start nodes for transaction processing
3. Verify chain readiness for POC

## Instructions

### Step 1: Prepare Script

**Context**: Ensure the setup script is executable.

**Command** ([[commands/setup-chain]] prep):
```bash
chmod +x setup_chain
```

> Makes the script runnable. Expected output: Permission changed.

### Step 2: Run Chain Setup

**Context**: Launch the local chain.

**Command** ([[commands/setup-chain]]):
```bash
./setup_chain
```

> Initializes genesis, starts nodes. Expected output: Chain running, logs showing block production.

### Step 3: Validate Chain Status

**Context**: Confirm chain is operational.

**Command** (chain status check):
```bash
# Use SDK CLI to query status
cosmos-sdk status
```

> Expected output: Latest block height > 0.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Sub-Techniques


## Commands Used

- [[commands/setup-chain]]
- [[commands/cosmos-status]]

## Tools Used

- [[tools/make]]

## Tags

- [[chain-startup]]
- [[testnet]]
