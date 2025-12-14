---
tags:
  - installation
  - windows
  - acronis
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Execution through API]]'
updated_at: '2025-12-14T17:28:58.460Z'
sub_techniques: []
id: 7e384f33-23af-4ef3-bcb3-bf769ae8d212
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Execution through API]]'
---
# Install-Acronis-Cyber-Protection-Agent

## Summary

This procedure installs the Acronis Cyber Protection Agent on a Windows system, deploying the vulnerable tibxread.exe utility necessary for subsequent DLL hijacking exploitation.

## Description

The installation places tibxread.exe at C:\Program Files\BackupClient\BackupAndRecovery\, setting up the environment for monitoring and hijacking. This step requires running the official installer as a low-privileged user, which completes without elevation for basic setup. Expected outcome is the executable ready for testing DLL loads.

## Requirements

1. Downloaded installer: Cyber_Protection_Agent_for_Windows_web.exe
2. Local execution privileges
3. Sufficient disk space in Program Files

## Defense

Defensive measures and detection strategies:

- Verify installer integrity with hashes before running
- Use endpoint protection to scan installers for malware
- Log software installations via Windows Event Logs (ID 11707)

## Objectives

1. Deploy the vulnerable agent software
2. Confirm tibxread.exe placement
3. Prepare for execution monitoring

## Instructions

### Step 1: Run Installer

**Context**: Execute the downloaded file to initiate installation.

Double-click or run via command line:

```cmd
Cyber_Protection_Agent_for_Windows_web.exe
```

> Follow on-screen prompts to complete installation; no custom options needed.

### Step 2: Verify Installation

**Context**: Check for the key executable.

Navigate to C:\Program Files\BackupClient\BackupAndRecovery\ and confirm tibxread.exe exists.

**Expected Output**: File present and executable (size ~1MB).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Execution through API]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- installation
- acronis
