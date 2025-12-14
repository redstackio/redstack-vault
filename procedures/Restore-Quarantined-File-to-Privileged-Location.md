---
id: restore-to-privileged-location
tags:
  - restore
  - av-bypass
  - lpe
type: procedure
tools:
  - '[[tools/Process-Monitor]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Registry Run Keys - Startup Folder]]'
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-14T17:29:44.736Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Registry Run Keys - Startup Folder]]'
  - '[[Disable or Modify Tools]]'
---
# Restore-Quarantined-File-to-Privileged-Location

## Summary

This procedure restores the quarantined file via the AV interface to its 'original' path, but due to the directory junction, it places the attacker-controlled payload in a privileged location, achieving escalation.

## Description

Using the Acronis AV quarantine management UI, select the file and restore to original path. The restore follows the junction, writing to the target directory (e.g., Startup), executing the payload on login or enabling further attacks like DLL hijacking. Validate with Process Monitor for privilege confirmation.

## Requirements

1. File in quarantine
2. Junction in place
3. Access to AV UI

## Defense

Defensive measures and detection strategies:

- Implement junction-aware restore validation in AV
- Log all restores and verify paths pre-write
- Monitor file creations in privileged dirs post-restore

## Objectives

1. Redirect write to privileged path
2. Achieve code execution or persistence
3. Confirm escalation

## Instructions

### Step 1: Perform Restore

**Context**: Triggers the vulnerable restore mechanism.

**Command** (None - UI Interaction):
In Acronis AV, navigate to quarantine, select 'eicar.bat', and choose 'Restore to original location'.

> The file writes via junction to Startup. Expected output: Restore success, file in target dir.

### Step 2: Validate Execution

**Context**: Confirm impact using monitoring tool.

**Tool** ([[tools/Process-Monitor]]):
Run ProcMon to filter for process creation from the restored file.

> On login/reboot, observe 'calc.exe' or payload running with user/SYSTEM privs.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Registry Run Keys - Startup Folder]] Registry Run Keys / Startup Folder
- [[Disable or Modify Tools]] Disable or Modify Tools

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/Process-Monitor]]

## Tags

- restore
- av-bypass
- lpe
