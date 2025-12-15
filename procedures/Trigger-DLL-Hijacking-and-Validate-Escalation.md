---
tags:
  - privilege-escalation
  - dll-hijacking
  - validation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/whoami-privilege-check]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[DLL Search Order Hijacking]]'
updated_at: '2025-12-14T17:28:58.444Z'
sub_techniques: []
id: 3e133028-477d-4cf5-abec-fff167f612aa
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
---
# Trigger-DLL-Hijacking-and-Validate-Escalation

## Summary

This procedure executes tibxread.exe to load the malicious tcmalloc.dll from the PATH, triggering arbitrary code execution in the process context, followed by validation of privilege escalation via logging the security context.

## Description

Running the executable causes Windows to load tcmalloc.dll from the hijacked PATH location, executing the payload (e.g., mmg.bat) with tibxread.exe's privileges. Validation uses whoami to confirm escalation, such as from user to SYSTEM. This achieves horizontal/vertical escalation for low-privileged attackers.

## Requirements

1. Installed Acronis agent with tibxread.exe
2. Malicious DLL in writable PATH
3. mmg.bat with validation commands in C:\attacker

## Defense

Defensive measures and detection strategies:

- Hook DLL loading with ETW or API monitoring
- Detect anomalous process DLL loads via behavioral analytics
- Run processes with restricted PATH or in isolated environments

## Objectives

1. Load and execute malicious DLL
2. Run arbitrary code in elevated context
3. Confirm escalation level

## Instructions

### Step 1: Execute tibxread.exe

**Context**: Trigger the DLL search and load.

Run the executable:

```cmd
C:\Program Files\BackupClient\BackupAndRecovery\tibxread.exe
```

> The process loads tcmalloc.dll from PATH, executing mmg.bat silently.

### Step 2: Validate with Command

**Context**: Check execution context post-load.

Use [[commands/whoami-privilege-check]] as part of mmg.bat:

```cmd
whoami /all >> c:\attacker\who.txt
```

**Expected Output**: File c:\attacker\who.txt contains elevated user info, e.g., groups including Administrators or SYSTEM.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[DLL Search Order Hijacking]]

### Sub-Techniques


## Commands Used

- [[commands/whoami-privilege-check]]

## Tools Used


## Tags

- escalation
- validation
