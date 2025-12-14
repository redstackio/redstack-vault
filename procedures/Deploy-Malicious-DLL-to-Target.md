---
id: proc-deploy-dll-001
tags:
  - deployment
  - file-placement
  - dll
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
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:29:19.651Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Deploy-Malicious-DLL-to-Target

## Summary

This procedure transfers and places the malicious tcmalloc.dll into the writable C:\Python27 directory on the target Windows machine, positioning it for hijacking during DLL searches.

## Description

As an authenticated user, copy the generated DLL to C:\Python27, which is included in the system PATH and searched by TrueImage.exe. This step requires no admin rights due to the directory's permissions. Prerequisites: DLL generated, network or local access to target. Expected outcome: DLL in place, ready for admin-triggered load.

## Requirements

1. Malicious tcmalloc.dll file from msfvenom
2. Authenticated user access to target
3. File transfer method (e.g., USB, SMB, RDP clipboard)

## Defense

Defensive measures and detection strategies:

- Restrict write access to PATH directories
- Enable file integrity monitoring (e.g., Sysmon Event ID 11 for file creates in Python27)
- Audit unexpected file placements in application directories

## Objectives

1. Position DLL in untrusted PATH location
2. Ensure stealthy placement without alerts
3. Verify writability without escalation

## Instructions

### Step 1: Transfer DLL to Target

**Context**: Move the file from attacker machine to target.

Use SMB share, email, or direct copy if local: e.g., `copy tcmalloc.dll \\target\C$\Python27\` from admin share if available, or as user via explorer.

### Step 2: Place in C:\Python27

**Context**: Ensure correct directory for PATH search.

Navigate to C:\Python27 and paste tcmalloc.dll.

> Expected: File appears in dir listing.

### Step 3: Confirm Permissions

**Context**: Test that the DLL won't be overwritten or blocked.

Run `icacls C:\Python27\tcmalloc.dll` to check ACLs; should allow user read/execute.

> Success: No inheritance issues, file intact.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- deployment
- transfer
- path-hijack
