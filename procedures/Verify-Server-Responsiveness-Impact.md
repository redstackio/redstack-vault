---
id: proc-004
tags:
  - dos
  - verification
  - impact
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/rpc-web3-clientversion-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:48.654Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Verify Server Responsiveness Impact

## Summary

This procedure checks the RPC server's responsiveness post-exploit by querying the client version, confirming DoS through timeouts and errors.

## Description

After triggering evm_reset, this tests a simple method like web3_clientVersion. Pre-exploit success versus post-exploit 504 errors demonstrates the hang's impact, affecting all RPC interactions.

## Requirements

1. Prior execution of evm_reset
2. curl for repeated queries
3. Endpoint URL known

## Defense

Defensive measures and detection strategies:

- Implement health checks for RPC methods
- Log timeout rates and correlate with reset attempts
- Use load balancers to isolate affected nodes

## Objectives

1. Measure responsiveness degradation
2. Confirm DoS propagation
3. Quantify service loss

## Instructions

### Step 1: Pre- and Post-Reset Query

**Context**: Run before reset for baseline, then after to verify failure.

**Command** ([[commands/rpc-web3-clientversion-query]]):
```bash
curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"web3_clientVersion", "params": {}, "id":1337}' https://bounty-node.rsk.co
```

> Pre: JSON with version (e.g., "RskJ/0.4.0..."). Post: 504 HTML timeout.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/rpc-web3-clientversion-query]]

## Tools Used

- [[tools/curl]]

## Tags

- verification
- timeout
- dos
