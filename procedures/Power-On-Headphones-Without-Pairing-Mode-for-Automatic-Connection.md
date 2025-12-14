---
id: proc-uuid-005
name: Power-On-Headphones-Without-Pairing-Mode-for-Automatic-Connection
tags:
  - bluetooth
  - authentication-bypass
type: procedure
tools:
  - '[[tools/Wireshark]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - IoT
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:52.330Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Power-On-Headphones-Without-Pairing-Mode-for-Automatic-Connection

## Summary

This procedure powers on the Sony WH-1000XM5 headphones without entering pairing mode, resulting in automatic unauthorized connection to the spoofed device, bypassing SSP authentication.

## Description

A short power button press (<5 seconds) triggers reconnection to the impersonated device. Capture packets with Wireshark to verify. Exploits firmware flaw in reconnection logic. Outcome: Established link enabling MitM/DoS.

## Requirements

1. Spoofed device in discoverable mode
2. Legitimate device powered off
3. Wireshark for packet capture (optional but recommended)

## Defense

Defensive measures and detection strategies:

- Firmware updates enforcing SSP on reconnections
- User notifications for unexpected connections
- Packet inspection for anomalous Bluetooth handshakes

## Objectives

1. Initiate auto-reconnect
2. Confirm unauthorized link
3. Capture evidence of bypass

## Instructions

### Step 1: Power On Headphones

**Context**: Press power button briefly to avoid pairing mode and trigger reconnection.

**Instructions**: Hold <5s. Expected output: Headphones power on and connect automatically.

### Step 2: Capture and Verify Connection

**Context**: Use Wireshark to monitor Bluetooth traffic for confirmation.

**Instructions**: Start capture on Bluetooth interface; look for connection packets to spoofed MAC. Expected output: pcapng file showing direct link without pairing (e.g., WH-1000XM5_vuln_poc.pcapng).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Wireshark]]

## Tags

- [[bluetooth]]
- [[authentication-bypass]]
