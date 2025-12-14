---
id: uuid-trigger-dll
tags:
  - dll-hijacking
  - execution
  - windows
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
  - '[[DLL Search Order Hijacking]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:29:09.430Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
  - '[[Windows Command Shell]]'
---
# Trigger Aszbrowsehelper EXE to Load Malicious DLL

## Summary

This procedure triggers the aszbrowsehelper.exe process in Acronis True Image 2021 to load the hijacked tcmalloc.dll, resulting in arbitrary code execution with administrative privileges.

## Description

Accessing the Acronis Secure Zone via the Manage Wizard or Windows Explorer launches aszbrowsehelper.exe, which loads tcmalloc.dll from the user PATH without validation. The malicious DLL executes its payload, spawning an elevated command shell. Requires prior DLL placement and Secure Zone existence. Outcome: Admin-level cmd.exe spawned.

## Requirements

1. Malicious tcmalloc.dll in %USERPROFILE%\AppData\Local\Microsoft\WindowsApps
2. Acronis True Image 2021 with Secure Zone created
3. Local user session

## Defense

Defensive measures and detection strategies:

- Patch Acronis True Image to version addressing DLL hijacking
- Monitor process creation for aszbrowsehelper.exe with Sysmon (Event ID 1, Image: aszbrowsehelper.exe)
- Block execution of DLLs from user directories via AppLocker

## Objectives

1. Execute malicious code via DLL hijacking
2. Gain initial administrative access
3. Confirm exploitation success

## Instructions

### Step 1: Access Secure Zone

**Context**: Invoke the vulnerable process through Acronis interface.

No command; GUI: Open Acronis True Image, Tools > Manage Acronis Secure Zone Wizard.

> Alternatively, browse Secure Zone in Explorer.

### Step 2: Observe Payload Execution

**Context**: The process loads the DLL and runs the payload.

No command; monitor for spawned cmd.exe.

> Elevated shell appears if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[DLL Search Order Hijacking]]
- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dll-hijacking]]
- [[Execution]]
- [[windows]]
