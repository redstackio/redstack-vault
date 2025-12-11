---
tags:
  - exfat
  - usb
  - buffer-overflow
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
skill_level: advanced
impact_level: high
detection_risk: low
sub_techniques: []
id: 2dfbe734-0929-4e84-a36f-e59c6c8d2b56
created_at: '2025-12-11T03:47:39.383Z'
updated_at: '2025-12-11T03:47:39.383Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1203]]'
---
# Craft Malformed exFAT USB

## Summary

This procedure involves creating a USB flash drive with a malformed exFAT filesystem structure, specifically by setting an oversized dataLength in the up-case table to trigger a heap-based buffer overflow during filesystem mounting on PS4/PS5 consoles.

## Description

The procedure targets the UVFAT_readupcasetable function in Sony's exFAT implementation. By crafting a USB with a large dataLength value, the allocation truncates from 64-bit to 32-bit, leading to under-allocation and subsequent overflow. This is useful for local exploitation scenarios aiming at memory corruption and jailbreak.

## Requirements

1. USB flash drive
2. Disk imaging or filesystem manipulation tools (e.g., hex editor or exFAT formatting software)
3. Physical access to the target console

## Defense

Defensive measures and detection strategies:

- Update console firmware to patch known vulnerabilities
- Monitor USB insertion events for anomalous behavior or crashes

## Objectives

1. Prepare a trigger for the exFAT buffer overflow
2. Enable heap corruption upon insertion
3. Facilitate potential kernel code execution

## Instructions

### Step 1: Format USB with exFAT

**Context**: Initialize the USB drive with an exFAT filesystem.

Format the USB drive using standard tools to create an exFAT partition.

> This sets up the base structure for modification.

### Step 2: Modify Up-Case Table Entry

**Context**: Alter the dataLength and sectorSize to cause truncation.

Use a hex editor to set dataLength to 0x100000200 and sectorSize to 0x200 in the up-case table entry.

> This leads to under-allocation when the console allocates heap memory.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #exfat
- #usb
