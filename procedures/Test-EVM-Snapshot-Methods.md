---
id: proc-002
tags:
  - recon
  - evm
  - debugging
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/rpc-evm-snapshot-create]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:26:48.666Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Test EVM Snapshot Methods

## Summary

This procedure tests the availability of EVM debugging methods by creating multiple snapshots on a JSON-RPC endpoint, revealing if developer tools are exposed on production nodes.

## Description

Targeted at Rootstock RPC nodes, this involves repeated calls to evm_snapshot to capture EVM states. Successful responses indicate misconfigured debugging access, setting up for more impactful exploits like resets. Each call returns an incremental ID, confirming the feature's enablement without immediate harm.

## Requirements

1. Accessible RPC endpoint supporting JSON-RPC 2.0
2. curl for HTTP requests
3. Knowledge of EVM debugging methods from source code

## Defense

Defensive measures and detection strategies:

- Disable evm_* methods in production RPC configs
- Implement method whitelisting to block debugging calls
- Alert on repeated snapshot requests as potential precursor to DoS

## Objectives

1. Probe for exposed debugging functionality
2. Gather evidence of configuration errors
3. Prepare for state-altering exploits

## Instructions

### Step 1: Create Initial Snapshot

**Context**: Send the first evm_snapshot request to test if the method is enabled.

**Command** ([[commands/rpc-evm-snapshot-create]]):
```bash
curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"evm_snapshot", "params": {}, "id":666}' https://bounty-node.rsk.co
```

> The command sends a POST with empty params. Expected output: {"jsonrpc":"2.0","id":666,"result":"0x1"}.

### Step 2: Create Subsequent Snapshots

**Context**: Repeat to observe incremental behavior and confirm persistence.

**Command** ([[commands/rpc-evm-snapshot-create]]):
```bash
curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"evm_snapshot", "params": {}, "id":666}' https://bounty-node.rsk.co
```

> Run 2-3 times. Expected outputs: "0x2", "0x3", etc., indicating active debugging.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/rpc-evm-snapshot-create]]

## Tools Used

- [[tools/curl]]

## Tags

- recon
- evm
- snapshot
