---
tags:
  - execution
  - msi
  - repair
type: procedure
tools:
  - '[[tools/cmd-exe]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/msiexec-repair-msi]]'
platforms:
  - Windows
techniques:
  - '[[Execution through API]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: e94513d8-3cc0-471d-9a06-3fba4d57b4e7
created_at: '2025-12-14T17:29:44.285Z'
updated_at: '2025-12-14T17:29:44.285Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Execution through API]]'
---
# Initiate MSI Repair Process

## Summary

This procedure triggers a repair operation on the Acronis MSI file using msiexec, creating a temporary folder and schedule.dll in %TEMP%, which is writable by the user and exploitable for DLL hijacking.

## Description

The repair command (/fa) forces reinstallation of all components, causing MsiExec.exe to run elevated and generate files in %TEMP%. This is vulnerable because %TEMP% lacks validation, allowing tampering. The process takes a few seconds to create the DLL, and MsiExec auto-elevates, loading the DLL without checks.

## Requirements

1. Path to the Acronis MSI file identified
2. cmd.exe access as non-admin
3. No UAC interference during initial trigger

## Defense

Defensive measures and detection strategies:

- Disable auto-elevation for MsiExec.exe
- Monitor msiexec executions via Sysmon or ETW
- Harden %TEMP% permissions or use non-writable temp paths

## Objectives

1. Start the repair to generate schedule.dll
2. Observe temporary folder creation
3. Prepare for DLL replacement before loading

## Instructions

### Step 1: Execute Repair Command

**Context**: Run msiexec to initiate the repair, creating the vulnerable DLL.

**Command** ([[commands/msiexec-repair-msi]]):

```cmd
msiexec /fa C:\Windows\Installer\installer_name.msi
```

> The /fa parameter forces all actions (repair); replace installer_name.msi with the actual filename. Expected output: Process starts, and after ~10 seconds, a new folder like {random} appears in %TEMP% containing schedule.dll.

### Step 2: Monitor TEMP Directory

**Context**: Verify the DLL creation without interrupting the process.

```cmd
cd %TEMP%
dir /b schedule.dll
```

> Confirms schedule.dll exists; do not proceed to replacement until visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Execution through API]] Native API

### Sub-Techniques


## Commands Used

- [[commands/msiexec-repair-msi]]

## Tools Used

- [[tools/cmd-exe]]

## Tags

- [[Execution]]
- [[msi]]
- [[repair]]
