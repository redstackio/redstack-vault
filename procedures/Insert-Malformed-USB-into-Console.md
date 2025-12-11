---
tags:
  - usb
  - filesystem
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - PS4
  - PS5
techniques:
  - '[[Exploitation for Client Execution]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: dc9c775d-13d4-4895-9bd3-70702841c795
created_at: '2025-12-11T03:47:39.381Z'
updated_at: '2025-12-11T03:47:39.381Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1203]]'
---
# Insert Malformed USB into Console

## Summary

This procedure covers the physical insertion of a malformed exFAT USB drive into a PS4 or PS5 console to trigger the vulnerable filesystem reading function.

## Description

Upon insertion, the console attempts to mount the USB and read the up-case table, invoking UVFAT_readupcasetable and potentially causing the buffer overflow due to the malformed structure.

## Requirements

1. Malformed exFAT USB drive
2. Access to the console's USB port
3. Powered-on PS4/PS5

## Defense

Defensive measures and detection strategies:

- Restrict USB access or use USB security policies
- Firmware updates to mitigate known exploits

## Objectives

1. Initiate filesystem mounting
2. Trigger vulnerable code path
3. Prepare for overflow exploitation

## Instructions

### Step 1: Power On Console

**Context**: Ensure the target is ready.

Turn on the PS4/PS5 console.

> The console must be operational for USB detection.

### Step 2: Plug in USB

**Context**: Insert the drive to start the process.

Physically plug the malformed USB into the console's USB port.

> The system will attempt to read the up-case table, triggering the function.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #usb
- #filesystem
