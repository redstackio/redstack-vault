---
tags:
  - dll-hijacking
  - payload-placement
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
updated_at: '2025-12-14T17:28:58.455Z'
sub_techniques: []
id: 0b857bd8-cbfc-48d5-93c0-81890639b8f7
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
---
# Place-Malicious-DLL-in-Writable-PATH

## Summary

This procedure involves creating or using a writable directory in the system PATH and placing a malicious tcmalloc.dll there, configured to execute arbitrary code like a batch file for privilege escalation upon loading by tibxread.exe.

## Description

Targeting writable PATH entries like C:\Python27, the attacker drops a DLL that hijacks the load process. The DLL is crafted (e.g., using MSVC) to run a payload such as C:\attacker\mmg.bat on DllMain entry. This exploits the search order without needing admin rights for placement.

## Requirements

1. Write access to a PATH directory (e.g., C:\Python27)
2. Compiled malicious tcmalloc.dll (sample attached in report)
3. Optional: Create C:\attacker folder and mmg.bat payload

## Defense

Defensive measures and detection strategies:

- Remove or protect writable directories from PATH
- Enable DLL secure loading policies via registry (e.g., SafeDLLSearchMode)
- Scan PATH directories for unauthorized DLLs with integrity checks

## Objectives

1. Position hijacking payload in search path
2. Configure DLL for code execution
3. Ensure compatibility with tibxread.exe architecture (x64/x86)

## Instructions

### Step 1: Prepare Payload Directory

**Context**: Set up folder for batch file if needed.

Create C:\attacker and place mmg.bat containing escalation commands.

### Step 2: Copy Malicious DLL

**Context**: Place the DLL in writable PATH.

Copy tcmalloc.dll to C:\Python27 (or similar).

```cmd
copy tcmalloc.dll C:\Python27\
```

> Ensure the DLL exports required functions to avoid crashes.

**Expected Output**: DLL file in PATH directory, verifiable with dir C:\Python27\tcmalloc.dll.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[DLL Search Order Hijacking]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dll-hijacking
- payload
