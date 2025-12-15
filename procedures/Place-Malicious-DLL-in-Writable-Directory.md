---
id: uuid-placeholder
tags:
  - dll-hijacking
  - malware-placement
  - windows
type: procedure
tools:
  - '[[tools/Process-Monitor]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/copy-malicious-dll]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[DLL Search Order Hijacking]]'
updated_at: '2025-12-14T17:26:22.848Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
---
# Place-Malicious-DLL-in-Writable-Directory

## Summary

This procedure involves creating or copying a malicious 32-bit DLL into the prepended writable PATH directory, named to match a DLL loaded by GlassWire (e.g., swift.dll for service or Wtsapi32.dll for GUI), enabling hijacking upon execution.

## Description

Using tools like Process Monitor, identify DLLs loaded by GWCtlSrv.exe (swift.dll, CSUNSAPI.dll, etc.) or GlassWire.exe (Wtsapi32.dll). The malicious DLL should contain arbitrary code, such as a reverse shell, compiled for x86. This exploits the PATH precedence, loading the attacker's DLL instead of legitimate ones from safe directories.

## Requirements

1. Malicious DLL compiled (e.g., with payload for code execution)
2. Identified target DLL name from monitoring
3. Write access to the prepended PATH directory

## Defense

Defensive measures and detection strategies:

- Implement DLL redirection or block loading from user directories
- Scan for unsigned or anomalous DLLs in PATH with antivirus
- Use integrity checks (e.g., Windows Defender Application Control)
- Log file creations in PATH directories (Sysmon Rule 11)

## Objectives

1. Position malicious DLL for automatic loading
2. Match exact name and architecture of target
3. Avoid detection during placement

## Instructions

### Step 1: Identify Target DLL

**Context**: Use Process Monitor to find DLLs loaded from PATH by GlassWire processes.

No command; run [[tools/Process-Monitor]] on GWCtlSrv.exe and filter for DLL loads.

> Expected: List of DLLs like swift.dll or Wtsapi32.dll.

### Step 2: Copy Malicious DLL

**Context**: Place the pre-built malicious DLL in the writable directory with the target name.

**Command** ([[commands/copy-malicious-dll]]):
```cmd
copy malicious.dll C:\\Dima\\Wtsapi32.dll
```

> Replace Wtsapi32.dll with service DLL like swift.dll as needed. Expected output: 1 file(s) copied.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[DLL Search Order Hijacking]] DLL Search Order Hijacking

### Sub-Techniques


## Commands Used

- [[commands/copy-malicious-dll]]

## Tools Used

- [[tools/Process-Monitor]]

## Tags

- [[dll-hijacking]]
- [[malware-placement]]
