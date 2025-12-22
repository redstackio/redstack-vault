---
tags:
  - rce
  - batch-execution
  - windows
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/Launch-Notepad-via-Batch-Script]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2024-10-04T00:00:00Z'
techniques:
  - '[[Malicious File]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T03:46:31.996Z'
skill_level: low
impact_level: high
detection_risk: high
sub_techniques: []
id: 636a225d-002c-437a-b3d4-dbfe498d4cf5
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Malicious File]]'
  - '[[Windows Command Shell]]'
---
# Execute Downloaded Malicious Batch File

## Summary

This procedure covers the user interaction to open and execute the downloaded file, resulting in remote code execution on the Windows client by running the disguised batch script.

## Description

After downloading the file as PoC.torrent, the user is tricked into opening it, which Windows executes as a batch file due to its content, ignoring the extension. The payload launches an application like Notepad, proving RCE. In a real attack, this could install malware or enable XSS. No server interaction needed post-download; relies on social engineering.

## Requirements

1. Downloaded file on Windows machine
2. User permissions to execute files
3. Default file associations for .torrent (opens in editor or executes based on content)

## Defense

Defensive measures and detection strategies:

- Warn users against opening unexpected downloads
- Enable Windows Defender real-time protection for script execution
- Use file extension blocking policies
- Log anomalous application launches (e.g., via Sysmon)

## Objectives

1. Execute the batch payload
2. Demonstrate RCE via application launch
3. Enable further exploitation like malware deployment

## Instructions

### Step 1: Locate and Open File

**Context**: Initiate execution by user action.

**Instructions**: Find PoC.torrent in downloads folder and double-click to open.

> Windows runs the batch content, suppressing echo and starting Notepad.

### Step 2: Execute Payload Command

**Context**: The embedded command runs automatically.

**Command** ([[commands/Launch-Notepad-via-Batch-Script]]):
```batch
@echo off
START C:\Windows\NOTEPAD.EXE
```

> This launches Notepad.exe silently. Expected: Notepad window opens.

### Step 3: Verify Execution

**Context**: Confirm RCE success.

**Instructions**: Observe the launched application or check task manager for notepad.exe.

> Success if external process starts; extend payload for real attacks.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Malicious File]]
- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used

- [[commands/Launch-Notepad-via-Batch-Script]]

## Tools Used


## Tags

- rce
- batch-execution
- windows
