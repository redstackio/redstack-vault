---
id: uuid-placeholder
tags:
  - dll-hijacking
  - environment-modification
  - windows
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/set-path-variable]]'
  - '[[commands/echo-path]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[DLL Search Order Hijacking]]'
updated_at: '2025-12-14T17:26:22.853Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
---
# Modify-PATH-Environment-for-DLL-Hijacking

## Summary

This procedure modifies the Windows PATH environment variable by prepending a writable directory, enabling DLL hijacking attacks by altering the search order for DLL loading in applications like GlassWire.

## Description

In scenarios where applications load DLLs from the PATH without enforcing safe search orders, prepending a user-controlled writable directory allows placement of malicious DLLs that get loaded preferentially. This is exploited in GlassWire's service and GUI, which load modules like swift.dll or Wtsapi32.dll from PATH. Prerequisites include local access to set environment variables; changes apply system-wide with /M flag but require reboot for services.

## Requirements

1. Local administrator access to modify system PATH (or user-level for session-specific)
2. A writable directory (e.g., C:\Dima\) not in original PATH
3. Windows OS with GlassWire installed

## Defense

Defensive measures and detection strategies:

- Enforce DLL safe search order via registry (SafeDllSearchMode=1)
- Monitor PATH modifications with event logs (Event ID 4697 for process creation with env changes)
- Use application whitelisting (AppLocker) to block unsigned DLLs
- Audit DLL loads with Sysmon (Rule 7 for image loads from unusual paths)

## Objectives

1. Redirect DLL loading to attacker-controlled directory
2. Prepare for hijacking without alerting the system
3. Ensure changes persist across reboots

## Instructions

### Step 1: Set System PATH

**Context**: Prepend the writable directory to the system PATH to prioritize it in DLL searches.

**Command** ([[commands/set-path-variable]]):
```cmd
setx PATH "C:\\Dima\\;%PATH%" /M
```

> This command sets the PATH environment variable system-wide (/M). It appends the current PATH after the new directory. Reboot or log off/on to apply to new processes. Expected output: Success message if admin privileges are used.

### Step 2: Verify PATH Modification

**Context**: Confirm the PATH has been updated correctly to include the writable directory first.

**Command** ([[commands/echo-path]]):
```cmd
echo %PATH%
```

> Displays the current PATH. Look for C:\Dima\ at the beginning. If not, restart the command prompt or system.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[DLL Search Order Hijacking]] DLL Search Order Hijacking

### Sub-Techniques


## Commands Used

- [[commands/set-path-variable]]
- [[commands/echo-path]]

## Tools Used


## Tags

- [[dll-hijacking]]
- [[environment-modification]]
