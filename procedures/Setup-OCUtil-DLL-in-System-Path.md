---
tags:
  - dll
  - environment
  - setup
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:48.894Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 55b846ee-fa94-46c0-a38e-60310cb1b570
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Setup OCUtil DLL in System Path

## Summary

This procedure places the vulnerable OCUtil_x64.dll from the Nextcloud Windows client into the system PATH, allowing dynamic loading by the PoC executable.

## Description

The Nextcloud desktop client uses OCUtil.dll for context menu integration in explorer.exe. To exploit the memory leak, the DLL must be loadable via LoadLibrary. Extract it from the installer (typically in C:\Program Files\Nextcloud) and add to PATH. This setup enables the PoC to call IsChildFile without file path issues. Target environment is Windows with Nextcloud installed.

## Requirements

1. Nextcloud Windows desktop client installed
2. Access to extract DLL from installation directory
3. Ability to modify PATH (may require admin rights)

## Defense

Defensive measures and detection strategies:

- Restrict DLL loading to trusted paths via AppLocker
- Audit PATH modifications and unexpected DLL placements
- Use integrity checks on system libraries

## Objectives

1. Make OCUtil_x64.dll discoverable by the system
2. Ensure compatibility with PoC's dynamic loading
3. Avoid conflicts with legitimate Nextcloud installation

## Instructions

### Step 1: Extract the DLL

**Context**: Locate and copy the vulnerable DLL from the Nextcloud installation.

Navigate to the Nextcloud program files directory (e.g., C:\Program Files\Nextcloud) and copy OCUtil_x64.dll.

> Verify the file version matches the vulnerable build from the report.

### Step 2: Add to PATH

**Context**: Place the DLL in a directory included in Windows PATH for global accessibility.

Copy the DLL to C:\Windows\System32 (or another PATH directory), then verify by opening Command Prompt and running `where OCUtil_x64.dll`.

> If PATH modification is needed, use System Properties > Environment Variables to append the directory.

### Step 3: Test Loading

**Context**: Confirm the DLL can be loaded without errors.

Use a simple tool like Dependency Walker or run a test LoadLibrary call in a script.

> Expected: DLL path resolved correctly; no 'module not found' errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dll
- environment
- setup
