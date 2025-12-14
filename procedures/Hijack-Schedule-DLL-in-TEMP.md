---
tags:
  - dll-hijacking
  - privilege-escalation
type: procedure
tools:
  - '[[tools/cmd-exe]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Windows
techniques:
  - '[[DLL Search Order Hijacking]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 1db6f0e8-c313-4c51-b648-4040b4948434
created_at: '2025-12-14T17:29:44.281Z'
updated_at: '2025-12-14T17:29:44.281Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
---
# Hijack Schedule DLL in TEMP

## Summary

This procedure replaces the legitimate schedule.dll created during MSI repair with a malicious DLL, enabling hijacking when loaded by the elevated MsiExec.exe process.

## Description

The MSI repair drops schedule.dll in a predictable %TEMP% subfolder without integrity checks. Attackers can overwrite it with a DLL that executes payload code (e.g., spawning SYSTEM cmd.exe) upon loading. This exploits the trust in the temp location, leading to privilege escalation.

## Requirements

1. MSI repair initiated and schedule.dll created
2. Malicious DLL prepared (e.g., compiled to spawn elevated shell)
3. Write access to %TEMP%

## Defense

Defensive measures and detection strategies:

- Implement DLL search order hardening
- Use integrity monitoring on %TEMP% files
- Block unsigned DLL loads in elevated processes

## Objectives

1. Substitute the DLL for hijacking
2. Ensure malicious DLL matches architecture (x64/x86)
3. Maintain process continuity

## Instructions

### Step 1: Locate and Backup Original DLL

**Context**: Find the exact path to schedule.dll in the temp folder.

```cmd
cd %TEMP%
for /d %i in (*) do if exist "%i\schedule.dll" echo %i
copy "%i\schedule.dll" schedule.dll.bak
```

> Identifies and backs up the original; note the folder path.

### Step 2: Replace with Malicious DLL

**Context**: Overwrite with attacker-controlled DLL.

No command; manually copy the malicious schedule.dll (provided or compiled) to the temp folder path.

> Ensure the DLL exports required functions; test in a lab. Expected: Replacement succeeds without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[DLL Search Order Hijacking]] Hijack DLL

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/cmd-exe]]

## Tags

- [[dll-hijacking]]
- [[privilege-escalation]]
