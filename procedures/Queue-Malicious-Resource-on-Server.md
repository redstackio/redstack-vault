---
tags:
  - resource-queue
  - eventscript-bypass
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/SV_AddResource-Queue-Malicious-File]]'
verified: false
platforms:
  - Windows
  - Game Engine
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:10.360Z'
sub_techniques: []
id: ef10e1d2-c972-4ccb-9941-42499e4c9d1a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Queue-Malicious-Resource-on-Server

## Summary

This procedure adds a malicious DLL to the server's resource download list using the eventscript type to evade validation checks in the GoldSource Engine.

## Description

By calling SV_AddResource in SV_CreateResourceList with type t_eventscript, the engine treats the DLL as a non-generic resource, skipping IsSafeFileToDownload. The filename can include forbidden extensions like .dll. Prerequisites: Modified server source or plugin access, prepared DLL. Outcome: DLL queued for HTTP download by connecting clients.

## Requirements

1. Access to server source code or modding hooks
2. Malicious DLL file (e.g., TrackerUI.dll) with size obtainable via FS_FileSize
3. sv_downloadurl already configured

## Defense

Defensive measures and detection strategies:

- Validate all SV_AddResource calls for safe types and extensions
- Log resource additions and alert on eventscript usage for binaries
- Client patches to check all downloads regardless of type

## Objectives

1. Add DLL to resource list without triggering checks
2. Ensure fatal missing flag forces download
3. Set up for client-side execution

## Instructions

### Step 1: Prepare Filename and Size

**Context**: Identify the malicious file path and compute its size for the resource entry.

**Command**:
No command; use filesystem functions.

> Example: filename = "bin\\TrackerUI.dll"; size = FS_FileSize(filename). Ensure path avoids '..' or 'server.cfg' to pass weak CL_CheckFile.

### Step 2: Invoke SV_AddResource

**Context**: Queue the resource in SV_CreateResourceList to include it in client batch requests.

**Command** ([[commands/SV_AddResource-Queue-Malicious-File]]):
```c++
SV_AddResource (t_eventscript, filename, FS_FileSize (filename), RES_FATALIFMISSING, 0);
```

> Parameters: t_eventscript bypasses full validation, filename with .dll extension, size for transfer, RES_FATALIFMISSING requires download, 0 for no compression. Expected output: Resource appended to list; no refusal.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used

- [[commands/SV_AddResource-Queue-Malicious-File]]

## Tools Used


## Tags

- resource-queue
- eventscript-bypass
