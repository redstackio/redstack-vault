---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567895
tags:
  - driver-installation
  - kernel-execution
type: procedure
tools:
  - '[[tools/Steam]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:36.100Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Authorize-Connection-and-Install-Malicious-Drivers

## Summary

This procedure authorizes the Remote Play connection on the host, causing SteamServices to install the previously replaced malicious kernel drivers, achieving arbitrary code execution at kernel level.

## Description

Upon authorization, SteamServices.exe installs drivers from the tampered directory without rechecking integrity, loading malicious sys files into kernel space for full system privileges.

## Requirements

1. Remote Play connection initiated from SteamLink
2. Modified drivers in place
3. Steam running on host

## Defense

Defensive measures and detection strategies:

- Enable driver signature enforcement (e.g., via boot options)
- Monitor kernel driver loads with Event Viewer (Event ID 2003 for unsigned drivers)
- Use EDR tools to block unsigned or anomalous driver installations

## Objectives

1. Approve connection to trigger installation
2. Load malicious drivers into kernel
3. Verify escalation success

## Instructions

### Step 1: Receive Authorization Prompt

**Context**: Wait for the connection request in Steam.

A popup or notification appears in Steam on the host PC.

> Expected output: Prompt to allow Remote Play.

### Step 2: Authorize the Connection

**Context**: Approve to initiate driver setup.

Click "Accept" or enter the pairing code if prompted.

> Expected output: Connection established, drivers installing.

### Step 3: Verify Driver Installation

**Context**: Confirm malicious drivers are loaded.

Open Device Manager, check Sound, video and game controllers for Steam Streaming Microphone (40KB) and Speakers (8KB). Use tools like DriverView to inspect loaded drivers.

> Expected output: Tampered devices present, kernel payload active if implemented.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Steam]]

## Tags

- [[driver-installation]]
- [[kernel-execution]]
