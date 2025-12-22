---
id: proc-uuid-002
name: Set-Bluetooth-Adapter-to-Discoverable-State
tags:
  - bluetooth
  - discoverable
type: procedure
tools:
  - '[[tools/BlueZ]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:52.360Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Set-Bluetooth-Adapter-to-Discoverable-State

## Summary

This procedure configures the Bluetooth adapter on a Linux device (e.g., Raspberry Pi) to enter discoverable mode using BlueZ, allowing the spoofed device to be detected by the target headphones during reconnection.

## Description

After spoofing the identity, setting the adapter to discoverable ensures the headphones can scan and connect to it as the legitimate device. This exploits the auto-reconnect feature without SSP checks. Target environment is Raspberry Pi OS with BlueZ. Outcomes include the adapter broadcasting the spoofed identity for pairing.

## Requirements

1. BlueZ Bluetooth stack installed and running
2. Spoofed identity already applied
3. bluetoothctl tool available

## Defense

Defensive measures and detection strategies:

- Disable discoverable mode on untrusted networks
- Log Bluetooth state changes and alert on frequent toggles
- Use device whitelisting in Bluetooth firmware

## Objectives

1. Enable discoverability for spoofed device
2. Prepare for automatic connection
3. Verify state with bluetoothctl

## Instructions

### Step 1: Enter Discoverable Mode

**Context**: Use bluetoothctl to set the adapter discoverable, allowing detection by headphones.

**Command**:
```bash
bluetoothctl discoverable on
```

> Activates discoverable state. Expected output: 'Changing discoverable on succeeded'.

### Step 2: Verify Configuration

**Context**: Check the adapter status to confirm discoverability.

**Command**:
```bash
bluetoothctl show
```

> Displays adapter info. Expected output: Discoverable: yes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/BlueZ]]

## Tags

- [[bluetooth]]
- [[discoverable]]
