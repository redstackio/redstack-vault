---
tags:
  - buffer-overflow
  - packet-crafting
type: procedure
tools:
  - '[[tools/Python3]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Exploitation for Client Execution]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: b2e77685-2299-4733-af39-c263fbe02c1b
created_at: '2025-12-14T17:28:28.365Z'
updated_at: '2025-12-14T17:28:28.365Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Send-svc_deltadescription-Packet

## Summary

This procedure sends an svc_deltadescription packet to the Counter-Strike 1.6 client, defining the memory layout of structures like event_t with fields positioned to enable stack overflow, including a string field at offset 0xac for ROP payload injection.

## Description

In the GoldSrc engine, the svc_deltadescription packet sets up field descriptions used by subsequent delta packets. By crafting fields with offsets and sizes that target the stack return address (e.g., 0xac), attackers prepare for overflow without bounds checking in DELTA_ParseDelta. This is sent over the network to a connected client, exploiting the packet parsing logic in a client-server game context. Prerequisites include network access to the client and knowledge of structure layouts from reverse engineering.

## Requirements

1. Python3 environment for packet crafting
2. Knowledge of GoldSrc packet formats (svc_deltadescription opcode 26)
3. Client connected to attacker's server on port 27015

## Defense

Defensive measures and detection strategies:

- Implement input validation in DELTA_ParseDelta to check field_offset + field_size against structure size
- Use stack canaries or ASLR to randomize return addresses
- Monitor for anomalous packet sizes in network traffic to game ports

## Objectives

1. Set up vulnerable field descriptions for delta parsing
2. Position payload at return address offset
3. Avoid null bytes in payload using integer fillers

## Instructions

### Step 1: Craft Packet Structure

**Context**: Build the binary packet with field list: first String at 0xac (size for ROP), followed by Integers to pad.

**Command** (Python scripting):
```python
# Example snippet in poc.py
packet = b'\x1a' + struct.pack('<H', num_fields)  # svc_deltadescription
for field in fields:
    packet += field_type + struct.pack('<HH', offset, size)
send_to_client(packet)
```

> Constructs and transmits the packet; expected output is client acknowledgment without error.

### Step 2: Transmit to Client

**Context**: Send via UDP/TCP socket to client's game connection.

**Command** (Integrated in script):
```python
socket.sendto(packet, client_addr)
```

> Packet delivery confirmed by socket response; success if client remains connected.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Python3]]

## Tags

- buffer-overflow
- packet-crafting
