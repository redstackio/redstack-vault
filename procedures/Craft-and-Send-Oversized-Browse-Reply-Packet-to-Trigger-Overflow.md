---
id: proc-craft-oversized-packet
tags:
  - packet-crafting
  - buffer-overflow
  - rce
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Nintendo Switch
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:42.158Z'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Craft and Send Oversized Browse-Reply Packet to Trigger Overflow

## Summary

This procedure crafts a malicious browse-reply packet with an appDataLength set to 150 bytes (exceeding the 128-byte buffer) and sends it to a target Nintendo Switch peer, triggering the stack buffer overflow in Mario Kart 8 Deluxe's Pia library for potential RCE.

## Description

By setting appDataLength <= outBufSize (150) in the packet at offset 431, but leveraging the memcpy that copies 150 bytes from packet +48 into a 128-byte stack buffer, the procedure overwrites adjacent stack memory with controlled data. This can be chained with an information leak to achieve remote code execution in user-mode on the target console during LAN/LDN sessions.

## Requirements

1. Custom packet crafting script or tool compatible with Nintendo LAN protocol
2. Network access to join or spoof a LAN/LDN session
3. Target peer running vulnerable Mario Kart 8 Deluxe in P2P mode

## Defense

Defensive measures and detection strategies:

- Disable LAN/LDN modes or use isolated networks for gaming
- Implement peer authentication to prevent spoofed packets
- Monitor for stack overflows via crash reports or anomaly detection in game logs

## Objectives

1. Construct a packet that bypasses length checks but overflows the buffer
2. Deliver the packet to trigger memcpy beyond bounds
3. Achieve stack overwrite leading to RCE with additional primitives

## Instructions

### Step 1: Build Packet Template

**Context**: Assemble the base browse-reply packet structure.

Set u8 type=0x1, u32 body size=1266, fill 42-byte misc, prepare 0x180-byte app data at +47, and set u32 appDataLength=150 at +431.

**Expected Output**: Valid packet hex ready for data injection.

### Step 2: Inject Controlled Data

**Context**: Place attacker-controlled payload starting at packet +48 to overwrite stack.

Fill the app data section with payload designed for stack smash, targeting return addresses or chaining gadgets.

**Expected Output**: Packet with overflow-inducing data.

### Step 3: Send to Target and Observe

**Context**: Transmit the packet in a P2P session and monitor target response.

Spoof or send as a peer in LAN/LDN, watching for crash or execution indicators.

**Expected Output**: Target console overflow, potential RCE if leaked addresses used.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- packet-crafting
- buffer-overflow
- rce
