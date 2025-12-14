---
id: ac-hlf-dos-001
tags:
  - dos
  - hyperledger
  - fabric
  - blockchain
  - nil-pointer
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Linux
  - Blockchain
submitted: true
complexity: low
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Exploit-Nil-Pointer-in-Orderer-Consensus-Message]]'
step_count: 1
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:26:48.854Z'
description: >-
  A single-stage attack exploiting a nil pointer dereference in HyperLedger
  Fabric's orderer consensus message handling to cause remote node crashes and
  disrupt blockchain ordering services.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Remote DoS in HyperLedger Fabric via Malformed Orderer Consensus Message

Multi-stage attack chain demonstrating a complete attack workflow targeting HyperLedger Fabric's ordering service.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Send Malformed Message] --> B[Node Crash and DoS]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Network client for sending custom protobuf messages (e.g., custom Go script or grpcurl)

### Target Environment

- HyperLedger Fabric Orderer service running on Linux
- Exposed gRPC endpoints for orderer-to-orderer communication (typically port 7050)
- Blockchain network with Raft or Kafka consensus

### Initial Access Requirements

- Network access to the orderer nodes
- No authentication required for consensus messages in vulnerable versions
- Knowledge of the orderer's gRPC endpoint

## Detailed Attack Procedures

### Step 1: Send Malformed Consensus Message
procedure: [[procedures/Exploit-Nil-Pointer-in-Orderer-Consensus-Message]]

**Objective**: Craft and transmit a specially malformed orderer-to-orderer consensus message with an empty inner message to trigger a nil pointer panic and crash the target orderer node.

**Instructions**: Prepare a protobuf-encoded consensus message where the inner message field is set to nil or empty, lacking proper validation. Use a tool like grpcurl or a custom Go client to send it to the orderer's consensus endpoint. For example, construct the message using the HyperLedger Fabric protobuf definitions (from common/consensus.proto) and ensure the Envelope's payload has an empty ConsensusRequest inner message.

```bash
grpcurl -plaintext -d '{"envelope": {"payload": {"header": {"channel_header": {"type": 2}}, "data": {"type": "CONSENSUS", "payload": null}}}' orderer.example.com:7050 fabric.orderer.Consenter.SubmitConsensusRequest
```

Adjust the protobuf structure based on the exact version (e.g., v1.4.x to v2.2.x affected). Monitor the orderer logs for panic traces indicating nil pointer dereference in abft.go or similar files.

**Expected Output**: The orderer node panics with an error like "runtime error: invalid memory address or nil pointer dereference" and restarts, disrupting the ordering service.

**Success Indicators**:
- Orderer node crashes and logs show panic in consensus message handling
- Blockchain network experiences ordering delays or failures until node recovery
- No response from the orderer gRPC endpoint post-exploit

## Attack Chain Summary

### Key Achievements

1. Remote crash of HyperLedger Fabric orderer nodes without authentication
2. Disruption of blockchain consensus and transaction ordering
3. Demonstration of unvalidated message handling leading to DoS

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Network Denial of Service]] Network Denial of Service

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---
*Last updated: 2023-10-01T12:00:00Z*
