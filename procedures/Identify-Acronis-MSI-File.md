---
tags:
  - recon
  - windows
  - msi
type: procedure
tools:
  - '[[tools/cmd-exe]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Windows
techniques:
  - '[[File and Directory Discovery]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 516391f6-f165-4525-8f21-c938b340def3
created_at: '2025-12-14T17:29:44.289Z'
updated_at: '2025-12-14T17:29:44.289Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Identify Acronis MSI File

## Summary

This procedure locates the Acronis True Image MSI installer file in the C:\Windows\Installer directory, which is readable by non-admin users, setting up the initial target for the privilege escalation exploit.

## Description

In the attack scenario, non-administrative users can read MSI files in C:\Windows\Installer due to default permissions. The Acronis MSI is large (1.3 GB) and identifiable by its author metadata. This step is crucial as MSI names are random GUIDs per installation, requiring manual or scripted inspection to find the correct file. Prerequisites include local access to a Windows system with Acronis True Image installed.

## Requirements

1. Non-admin user account on Windows
2. Access to File Explorer or cmd.exe for directory browsing
3. Acronis True Image installed on the target system

## Defense

Defensive measures and detection strategies:

- Restrict read permissions on C:\Windows\Installer to admins only
- Monitor access to Installer directory via file auditing
- Use application whitelisting to prevent unauthorized MSI executions

## Objectives

1. Locate the exploitable Acronis MSI file
2. Note its exact path for repair initiation
3. Confirm readability without elevation

## Instructions

### Step 1: Access Installer Directory

**Context**: Open the readable C:\Windows\Installer to inspect MSI files.

No specific command; use File Explorer or cmd.exe to navigate:

```cmd
cd /d C:\Windows\Installer
dir *.msi /s
```

> This lists all MSI files; look for one around 1.3 GB with 'Acronis' in properties or metadata.

### Step 2: Verify MSI Details

**Context**: Confirm the file is the Acronis installer by checking author.

Use PowerShell or properties dialog to inspect:

```powershell
Get-ItemProperty 'C:\Windows\Installer\{GUID}.msi' | Select-Object Author
```

> Expected output: Author field shows 'Acronis'; note the full path.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/cmd-exe]]

## Tags

- [[recon]]
- [[windows]]
- [[msi]]
