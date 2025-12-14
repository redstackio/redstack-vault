---
id: acronis-trigger-update
tags:
  - lpe
  - symlink
  - trigger
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:36.745Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Trigger-Acronis-Update-for-File-Overwrite

## Summary

This procedure initiates the Acronis True Image update process through the UI, causing the SYSTEM-privileged installer to write to the symlinked log file and overwrite the targeted protected system file.

## Description

After setting up the symlink, triggering the update download and installation exploits the vulnerability. The application checks for updates in the Account tab, downloads the latest version, and runs setupapp_amd64.exe with elevated privileges. This process appends to inst.log, which via the symlink modifies the target file (e.g., pci.sys). Successful execution can corrupt the driver, leading to system instability or escalation opportunities upon reboot or further exploitation.

## Requirements

1. Symlink already created pointing to target file
2. Acronis True Image installed and accessible via UI
3. Internet access for update download
4. Local user account with application launch permissions

## Defense

Defensive measures and detection strategies:

- Run Acronis updates in isolated environments or with sandboxing
- Monitor process execution of setupapp_amd64.exe for unexpected file writes
- Implement application whitelisting to restrict update behaviors
- Patch Acronis True Image to versions addressing symlink issues

## Objectives

1. Initiate privileged write operation via update
2. Overwrite target file to achieve escalation
3. Validate exploitation by observing system changes

## Instructions

### Step 1: Start Update Download

**Context**: Use the Acronis UI to begin the update process, downloading the installer.

**Command** (No CLI; UI action):

> Navigate to Account tab, click 'A new version is available'. Expected output: Download progress in UI.

### Step 2: Run Installation

**Context**: Proceed with installation to trigger the log write and overwrite.

**Command** (No CLI; UI action):

> Open downloaded installer, click 'Update'. Expected output: Installation completes; check target file for changes.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- lpe
- symlink
- trigger
