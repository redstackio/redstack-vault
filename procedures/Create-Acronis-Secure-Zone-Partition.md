---
id: uuid-create-secure-zone
tags:
  - prerequisite
  - windows
  - acronis
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:09.436Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create Acronis Secure Zone Partition

## Summary

This procedure sets up the Acronis Secure Zone partition, a prerequisite for triggering the vulnerable aszbrowsehelper.exe process in Acronis True Image 2021.

## Description

The Acronis Secure Zone is a protected partition used for backups. Creating it involves using the Acronis tool to allocate space on a disk partition, requiring a reboot. This step assumes the target has Acronis True Image 2021 installed and local user access. Once created, it enables access to the Secure Zone, which invokes the vulnerable process. Expected outcome: A functional Secure Zone partition ready for exploitation.

## Requirements

1. Acronis True Image 2021 installed on Windows
2. Local user account with ability to reboot
3. Available disk space (e.g., 500MB on a partition)

## Defense

Defensive measures and detection strategies:

- Monitor Acronis tool usage and unexpected reboots
- Restrict non-admin users from creating Secure Zones via group policy
- Audit partition changes with Windows Event Logs (Event ID 5136)

## Objectives

1. Prepare the environment for DLL hijacking trigger
2. Ensure vulnerable process can be invoked
3. Validate setup without alerting defenses

## Instructions

### Step 1: Launch Acronis Secure Zone Tool

**Context**: Initiate the creation process from the Acronis interface.

No command required; use GUI: Open Acronis True Image 2021, go to Tools tab, select Acronis Secure Zone.

> Select target partition, specify size (e.g., 500MB), and proceed.

### Step 2: Complete Partition Creation

**Context**: Finalize setup requiring system reboot.

No command; follow prompts to reboot.

> Post-reboot, verify Secure Zone appears in Acronis Tools.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[prerequisite]]
- [[windows]]
- [[acronis]]
