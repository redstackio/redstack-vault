---
id: proc-uuid-004
name: Power-Off-Legitimate-Paired-Device
tags:
  - dos
  - bluetooth
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - IoT
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:31:52.343Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Power-Off-Legitimate-Paired-Device

## Summary

This procedure removes the legitimate paired device from Bluetooth availability by powering it off, forcing the headphones to connect to the spoofed attacker device.

## Description

By powering off the real device (e.g., Surface Laptop 4), the headphones scan for alternatives, landing on the impersonated one due to the authentication flaw. Physical access to the legitimate device required. Outcome: Legitimate device offline, enabling spoofed connection.

## Requirements

1. Access to the legitimate paired device
2. Proximity within Bluetooth range

## Defense

Defensive measures and detection strategies:

- Use always-on Bluetooth guardians or monitors
- Alert on sudden device disappearances in pairing lists
- Require manual confirmation for reconnections

## Objectives

1. Eliminate legitimate connection option
2. Direct traffic to spoofed device

## Instructions

### Step 1: Power Off Device

**Context**: Shut down or disable Bluetooth on the legitimate device to remove it from range.

**Instructions**: Press power button or run `sudo systemctl stop bluetooth` if applicable. Expected output: Device no longer broadcasting.

### Step 2: Verify Removal

**Context**: Confirm via Bluetooth scanner that the device is unavailable.

**Instructions**: Use `bluetoothctl scan on` on another device. Expected output: No signal from legitimate MAC.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dos]]
- [[bluetooth]]
