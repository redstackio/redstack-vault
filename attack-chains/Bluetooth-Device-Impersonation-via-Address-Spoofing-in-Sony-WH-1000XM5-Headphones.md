---
id: ac-uuid-001
name: >-
  Bluetooth Device Impersonation via Address Spoofing in Sony WH-1000XM5
  Headphones
tags:
  - bluetooth
  - spoofing
  - impersonation
  - mitm
  - dos
  - authentication-bypass
  - iot
type: attack_chain
tools:
  - '[[tools/Golang]]'
  - '[[tools/BlueZ]]'
  - '[[tools/Wireshark]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Linux
  - Bluetooth
  - IoT
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Spoof-Bluetooth-Address-and-Name-Using-Golang-and-BlueZ]]'
  - '[[procedures/Set-Bluetooth-Adapter-to-Discoverable-State]]'
  - '[[procedures/Idle-or-Power-Off-Headphones-to-Trigger-Reconnection]]'
  - '[[procedures/Power-Off-Legitimate-Paired-Device]]'
  - >-
    [[procedures/Power-On-Headphones-Without-Pairing-Mode-for-Automatic-Connection]]
step_count: 5
techniques:
  - '[[Valid Accounts]]'
  - '[[Use Alternate Authentication Material]]'
updated_at: '2025-12-14T17:31:52.375Z'
description: >-
  Multi-stage attack exploiting authentication deficiencies in the Sony
  WH-1000XM5 headphones' Bluetooth reconnection process to impersonate a paired
  device, enabling unauthorized access, MitM, DoS, and link key hijacking.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Use Alternate Authentication Material]]'
---
# Bluetooth Device Impersonation via Address Spoofing in Sony WH-1000XM5 Headphones

Multi-stage attack chain demonstrating exploitation of authentication deficiencies in the Sony WH-1000XM5 headphones' Bluetooth reconnection process, allowing impersonation of a previously paired device without user interaction or pairing mode.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Spoof Device Identity] --> B[Set Discoverable]
    B --> C[Trigger Reconnection]
    C --> D[Remove Legitimate Device]
    D --> E[Establish Unauthorized Connection]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Golang]]
- [[tools/BlueZ]]
- [[tools/Wireshark]]

### Target Environment

- Sony WH-1000XM5 headphones with previously paired Bluetooth device (e.g., Surface Laptop 4)
- Attacker device: Raspberry Pi running Raspberry Pi OS (Bullseye) with Bluetooth adapter
- Bluetooth services enabled

### Initial Access Requirements

- Physical proximity to target headphones (Bluetooth range, ~10m)
- Knowledge of legitimate paired device's Bluetooth address and name
- No credentials required; exploits reconnection flaw

## Detailed Attack Procedures

### Step 1: Spoof Bluetooth Identity
procedure: [[procedures/Spoof-Bluetooth-Address-and-Name-Using-Golang-and-BlueZ]]

**Objective**: Impersonate the legitimate paired device by changing the attacker's Bluetooth address and name to match the target.

**Instructions**: Compile and execute the Golang script to spoof the address, edit machine info for name, and restart Bluetooth service.

**Expected Output**: Raspberry Pi's Bluetooth identity matches the legitimate device.

**Success Indicators**:
- Bluetooth address changed to spoofed MAC (e.g., 00:11:22:33:44:55)
- Device name updated (e.g., 'Surface Laptop 4')

### Step 2: Enable Discovery
procedure: [[procedures/Set-Bluetooth-Adapter-to-Discoverable-State]]

**Objective**: Make the spoofed device visible for automatic reconnection.

**Instructions**: Use BlueZ tools to set the adapter to discoverable mode.

**Expected Output**: Adapter in discoverable state, ready for connection.

**Success Indicators**:
- `bluetoothctl` shows discoverable: yes
- Headphones can detect the spoofed device

### Step 3: Trigger Reconnection on Headphones
procedure: [[procedures/Idle-or-Power-Off-Headphones-to-Trigger-Reconnection]]

**Objective**: Simulate disconnection to initiate the vulnerable reconnection process.

**Instructions**: Leave headphones idle or power off briefly.

**Expected Output**: Headphones enter reconnection seeking mode.

**Success Indicators**:
- No active connection to legitimate device
- Headphones ready to reconnect

### Step 4: Remove Legitimate Device
procedure: [[procedures/Power-Off-Legitimate-Paired-Device]]

**Objective**: Force headphones to connect to the spoofed device by removing the real one from range.

**Instructions**: Power off the legitimate paired device (e.g., Surface Laptop 4).

**Expected Output**: Legitimate device unavailable for Bluetooth.

**Success Indicators**:
- No Bluetooth signal from legitimate device
- Headphones scan for alternatives

### Step 5: Establish Connection
procedure: [[procedures/Power-On-Headphones-Without-Pairing-Mode-for-Automatic-Connection]]

**Objective**: Power on headphones to auto-connect to spoofed device without authentication.

**Instructions**: Power on headphones (short press <5s) and capture packets with Wireshark to verify unauthorized connection.

**Expected Output**: Automatic pairing to attacker's device, as seen in pcapng capture.

**Success Indicators**:
- Connection established without pairing mode
- Bluetooth packets show impersonated link
- Potential for MitM/DoS

## Attack Chain Summary

### Key Achievements

1. Successful spoofing of Bluetooth identity using Golang and BlueZ
2. Unauthorized reconnection bypassing SSP standards
3. Enabled MitM, DoS, and link key hijacking on Bluetooth sessions

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Use Alternate Authentication Material]] Use Alternate Authentication Material

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
