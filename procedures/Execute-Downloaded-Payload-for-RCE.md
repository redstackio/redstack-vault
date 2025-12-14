---
id: proc-uuid-3
tags:
  - rce
  - batch
  - malware-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/rce-batch-payload]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Malicious File]]'
updated_at: '2025-12-14T17:23:28.234Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Malicious File]]'
---
# Execute-Downloaded-Payload-for-RCE

## Summary

This procedure involves opening the spoofed .torrent file downloaded via WebTorrent, executing the embedded .bat payload to achieve remote code execution on the victim's Windows machine.

## Description

After download, the file appears as a harmless .torrent but contains batch script code. Opening it in Windows runs the payload, launching an application like Notepad.exe as a proof-of-concept for arbitrary RCE. This can be extended to full malware installation or XSS exploitation.

## Requirements

1. Downloaded file (PoC.torrent with .bat content)
2. Windows OS
3. User permission to execute files

## Defense

Defensive measures and detection strategies:

- Enable Windows Defender real-time protection for script execution
- Use file extension blocking or verification tools
- Log and alert on unexpected application launches (e.g., via Sysmon)
- Train users to scan files with antivirus before opening

## Objectives

1. Execute disguised malware file
2. Demonstrate RCE via system command invocation
3. Enable further compromise like malware persistence

## Instructions

### Step 1: Open Downloaded File

**Context**: Double-click the saved PoC.torrent to trigger execution.

**Command** ([[commands/rce-batch-payload]]):
```batch
@echo off
START C:\Windows\NOTEPAD.EXE
```

> The batch script suppresses output and starts Notepad.exe, proving RCE.

### Step 2: Verify Execution

**Context**: Confirm payload ran successfully.

**Instructions**: Observe Notepad opening without user intent.

> Expected: Application launches, indicating successful code execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Malicious File]] Malicious File

### Sub-Techniques


## Commands Used

- [[commands/rce-batch-payload]]

## Tools Used


## Tags

- rce
- windows
- execution
