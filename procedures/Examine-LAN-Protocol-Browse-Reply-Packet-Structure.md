---
id: proc-examine-lan-packet
tags:
  - packet-analysis
  - lan-protocol
  - p2p
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
updated_at: '2025-12-14T17:23:42.163Z'
skill_level: advanced
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Examine LAN Protocol Browse-Reply Packet Structure

## Summary

This procedure dissects the LAN protocol's browse-reply packet structure in Mario Kart 8 Deluxe to identify fields controlling application data, enabling crafting of packets that trigger the buffer overflow.

## Description

The browse-reply packet begins with a u8 type field (0x1), followed by a u32 body size (typically 1266 bytes), 42 bytes of miscellaneous data, 0x180 bytes of application data space starting at index 47, and a u32 app data length field at offset 431. By controlling the app data length and content, attackers can influence the memcpy in CopyAppData to overflow the stack.

## Requirements

1. Packet capture tools or protocol analyzer for Nintendo LAN traffic
2. Knowledge of binary packet formats and Nintendo's P2P protocols
3. Sample legitimate packets from a LAN session

## Defense

Defensive measures and detection strategies:

- Validate packet body sizes and app data lengths against expected norms
- Use network monitoring to detect oversized or malformed LAN packets
- Firmware updates to enforce strict packet parsing bounds

## Objectives

1. Map all critical packet fields, especially app data sections
2. Identify offsets for length control and data injection
3. Prepare templates for malicious packet construction

## Instructions

### Step 1: Capture Legitimate Packets

**Context**: Obtain sample browse-reply packets from a real LAN session.

Join a LAN game session and use a packet sniffer to capture traffic, filtering for type 0x1 packets.

**Expected Output**: Raw hex dumps of packets with body size 1266.

### Step 2: Dissect Packet Fields

**Context**: Break down the packet structure byte-by-byte.

Parse the u8 type, u32 body size, 42-byte misc, app data at +47 (0x180 bytes), and u32 length at +431.

**Expected Output**: Annotated packet diagram showing controllable fields.

### Step 3: Test Data Control

**Context**: Verify ability to modify app data without crashing the parser.

Craft and send modified packets with varying app data lengths to observe processing.

**Expected Output**: Confirmation of length field influencing CopyAppData.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- packet-analysis
- lan-protocol
- nintendo-switch
