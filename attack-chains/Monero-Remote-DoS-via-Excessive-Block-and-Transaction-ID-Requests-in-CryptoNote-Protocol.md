---
tags:
  - dos
  - monero
  - cryptonote
  - memory-exhaustion
  - p2p
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Establish-P2P-Connection-to-Monero-Node]]'
  - '[[procedures/Send-Malicious-NOTIFY-REQUEST-GET-OBJECTS]]'
  - '[[procedures/Observe-Monero-Node-Memory-Exhaustion]]'
step_count: 3
techniques:
  - '[[OS Exhaustion Flood]]'
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:55.669Z'
description: >-
  A multi-stage remote denial-of-service attack exploiting the lack of bounds
  checking in Monero's CryptoNote protocol, leading to memory exhaustion on the
  target node.
skill_level: intermediate
impact_level: high
id: cb2a4370-9a81-42e9-b76d-d2000a0f4d54
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
  - '[[Endpoint Denial of Service]]'
---
---
id: 123e4567-e89b-12d3-a456-426614174000
name: Monero Remote DoS via Excessive Block and Transaction ID Requests in CryptoNote Protocol
type: attack_chain
description: "A multi-stage remote denial-of-service attack exploiting the lack of bounds checking in Monero's CryptoNote protocol, leading to memory exhaustion on the target node."
verified: false
submitted: false
step_count: 3
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
procedures: [[procedures/Establish-P2P-Connection-to-Monero-Node]], [[procedures/Send-Malicious-NOTIFY-REQUEST-GET-OBJECTS]], [[procedures/Observe-Monero-Node-Memory-Exhaustion]]
techniques: [[OS Exhaustion Flood]], [[Endpoint Denial of Service]]
tactics: [[Impact]]
tags: dos, monero, cryptonote, memory-exhaustion, p2p
platforms: Linux
tools: []
---

# Monero Remote DoS via Excessive Block and Transaction ID Requests in CryptoNote Protocol

Multi-stage attack chain demonstrating a complete remote DoS workflow against a Monero node using the CryptoNote protocol.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Establish P2P Connection] --> B[Send Malicious Request]
    B --> C[Observe Memory Exhaustion]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Custom CryptoNote P2P client (e.g., implemented in C++ based on Monero source)

### Target Environment

- Monero Daemon running on Linux
- P2P port exposed (default 18080)
- Network access to the target's P2P interface

### Initial Access Requirements

- No credentials required
- Attacker must be able to reach the target's P2P port over the network
- Prior access not needed; remote exploitation

## Detailed Attack Procedures

### Step 1: Establish P2P Connection
procedure: [[procedures/Establish-P2P-Connection-to-Monero-Node]]

**Objective**: Initiate a peer-to-peer connection to the target Monero node to enable protocol communication.

**Instructions**: Implement or use a CryptoNote-compatible client to connect to the node's P2P port. This involves handshaking and protocol negotiation as per the CryptoNote P2P specification.

**Expected Output**: Successful connection establishment, confirmed by protocol handshake response.

**Success Indicators**:
- Connection logs show handshake completion
- Node responds to basic P2P messages

### Step 2: Send Malicious Request
procedure: [[procedures/Send-Malicious-NOTIFY-REQUEST-GET-OBJECTS]]

**Objective**: Transmit a crafted NOTIFY_REQUEST_GET_OBJECTS message with an excessively large number of block or transaction IDs to trigger unbounded memory allocation.

**Instructions**: Craft the request message where the blocks or txs array size exceeds safe limits (e.g., millions of IDs). Serialize the binary message according to the CryptoNote protocol and send it over the established P2P connection. Optionally, include duplicate transaction requests in fluffy blocks for amplification.

**Expected Output**: The request is sent; target node begins processing, leading to increased memory usage observable remotely.

**Success Indicators**:
- Request transmission confirmed
- Target node latency increases or becomes unresponsive

### Step 3: Observe Memory Exhaustion
procedure: [[procedures/Observe-Monero-Node-Memory-Exhaustion]]

**Objective**: Monitor the target node for signs of denial of service due to memory exhaustion.

**Instructions**: Use monitoring tools to track the node's resource usage post-request. Watch for process crashes, high memory consumption, or unresponsiveness to further P2P probes.

**Expected Output**: Node crashes or becomes unresponsive, with logs indicating out-of-memory errors in the core handler.

**Success Indicators**:
- Memory usage spikes to exhaustion levels
- Node fails to respond to subsequent requests or crashes

## Attack Chain Summary

### Key Achievements

1. Remote connection to Monero P2P network without authentication
2. Exploitation of unbounded array processing in protocol handler
3. Achievement of full node DoS via memory exhaustion, impacting blockchain synchronization

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[OS Exhaustion Flood]] OS Exhaustion Floods
- [[Endpoint Denial of Service]] Endpoint Denial of Service

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*
