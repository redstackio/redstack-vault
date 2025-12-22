---
id: proc-005
tags:
  - dos
  - reset
  - confirmation
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/rpc-eth-blocknumber-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:48.647Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Confirm Blockchain Sync Reset

## Summary

This procedure re-queries the block number after evm_reset to confirm the node's sync has been forced back to genesis block 0, validating the full DoS impact.

## Description

Post-reset, the intensive operation desyncs the node. A blockNumber query returning 0x0 proves the reset's success, disrupting all dependent services and users.

## Requirements

1. Completed evm_reset execution
2. Access to the now-unresponsive endpoint
3. curl for verification

## Defense

Defensive measures and detection strategies:

- Periodic sync status monitoring
- Auto-restart nodes on reset detection
- Block evm_reset at the proxy level (e.g., nginx)

## Objectives

1. Verify desync to block 0
2. Assess long-term service disruption
3. Document exploit efficacy

## Instructions

### Step 1: Re-Query Block Number

**Context**: Check if the sync reset occurred by querying post-DoS.

**Command** ([[commands/rpc-eth-blocknumber-query]]):
```bash
curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"eth_blockNumber", "params": [], "id":1337}' https://bounty-node.rsk.co
```

> Expected: {"jsonrpc":"2.0","id":1337,"result":"0x0"}, confirming reset.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/rpc-eth-blocknumber-query]]

## Tools Used

- [[tools/curl]]

## Tags

- confirmation
- sync
- reset
