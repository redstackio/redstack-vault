---
id: 17b5e40e-92e1-4209-a408-1d61d74c11a7
name: Send-Malicious-NOTIFY-REQUEST-GET-OBJECTS
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.809Z'
tactics:
  - '[[Impact]]'
techniques:
  - '[[OS Exhaustion Flood]]'
sub_techniques: []
tags:
  - dos
  - memory-exhaustion
  - cryptonote
  - monero
commands: []
platforms:
  - Linux
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
---

# Send-Malicious-NOTIFY-REQUEST-GET-OBJECTS

## Summary

This procedure crafts and sends a NOTIFY_REQUEST_GET_OBJECTS message with an excessively large array of block or transaction IDs, exploiting the absence of bounds checking to cause uncontrolled memory allocation in the Monero node's core.

## Description

The vulnerability lies in the handle_get_objects function in cryptonote_protocol_handler.inl, where arg.blocks.size() or arg.txs.size() is not validated, leading to allocation of large buffers via m_core.handle_get_objects. A secondary amplification occurs in fluffy block handling without duplicate checks. This is a remote, unauthenticated attack requiring P2P access. The scale needed is large (e.g., millions of IDs), making it theoretical without optimized implementation, but feasible against resource-constrained nodes.

## Requirements

1. Established P2P connection from prior procedure
2. Ability to serialize CryptoNote binary messages (C++ implementation recommended)
3. Sufficient attacker bandwidth to transmit large payloads

## Defense

Defensive measures and detection strategies:

- Implement bounds checking on request array sizes in protocol handler
- Monitor for unusually large incoming P2P messages
- Use resource limits (e.g., ulimit) on the daemon process

## Objectives

1. Trigger excessive memory allocation on the target node
2. Amplify impact via duplicate or fluffy transaction requests
3. Render the node unresponsive to legitimate peers

## Instructions

### Step 1: Craft the Malicious Request

**Context**: Build the NOTIFY_REQUEST_GET_OBJECTS message (command ID 0x0004) with oversized arrays. Each ID is a 32-byte hash; set size to 1,000,000+ for exhaustion.

In C++, use the protocol structures:

```cpp
cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request arg;
arg.blocks.resize(1000000); // Fill with dummy hashes
arg.txs.resize(1000000);
// Serialize to binary blob
blobdata blob = t_serializable_object_to_blob(arg);
// Send via P2P channel
```

> The serialized blob will be large; transmit it over the socket. Expected output: No immediate response, but node begins processing.

### Step 2: Optional Amplification with Fluffy Blocks

**Context**: Send NOTIFY_REQUEST_FLUFFY_MISSING_TX with duplicate large transaction indices to exacerbate memory use.

Craft similar oversized request without duplicate validation:

```cpp
// Similar serialization for fluffy request
// Repeat indices for same large txs
```

> This causes repeated allocations. Expected output: Further memory spike.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[OS Exhaustion Flood]] OS Exhaustion Floods

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dos]]
- [[memory-exhaustion]]
- [[monero]]
