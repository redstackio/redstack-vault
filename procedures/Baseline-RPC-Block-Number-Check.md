---
id: proc-001
tags:
  - recon
  - rpc
  - json-rpc
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/rpc-eth-blocknumber-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:26:48.681Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Baseline RPC Block Number Check

## Summary

This procedure queries the current block number on a JSON-RPC endpoint to establish a baseline for the blockchain's synced state, useful for verifying node health before attempting exploits like DoS.

## Description

In the context of testing Rootstock RPC nodes, this step involves sending a POST request to the eth_blockNumber method. It confirms the endpoint is responsive and provides the current block height, which should be non-zero if synced. This is a reconnaissance step to ensure the target is in a normal operational state prior to exploitation.

## Requirements

1. Network access to the RPC endpoint (e.g., https://bounty-node.rsk.co on port 443)
2. curl tool installed
3. No authentication needed for public endpoints

## Defense

Defensive measures and detection strategies:

- Rate-limit JSON-RPC requests to prevent reconnaissance flooding
- Monitor for unusual eth_blockNumber queries from new IPs
- Log all RPC method calls and alert on baseline checks during off-hours

## Objectives

1. Confirm endpoint accessibility and sync status
2. Record pre-exploit block height for impact comparison
3. Identify if debugging methods might be exposed indirectly

## Instructions

### Step 1: Query Block Number

**Context**: Send a JSON-RPC request to retrieve the current block number, establishing the baseline.

**Command** ([[commands/rpc-eth-blocknumber-query]]):
```bash
curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"eth_blockNumber", "params": [], "id":1337}' https://bounty-node.rsk.co
```

> This command uses silent mode (-s), POST method, JSON headers, and a payload with method eth_blockNumber. Expected output is a JSON object with the block number in hex (e.g., "0x437ca"), indicating a synced node.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/rpc-eth-blocknumber-query]]

## Tools Used

- [[tools/curl]]

## Tags

- recon
- rpc
- baseline
