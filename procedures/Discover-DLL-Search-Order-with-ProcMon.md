---
tags:
  - discovery
  - dll-hijacking
  - procmon
type: procedure
tools:
  - '[[tools/ProcMon]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[DLL Search Order Hijacking]]'
updated_at: '2025-12-14T17:28:58.471Z'
sub_techniques: []
id: ec4ca49b-c3b3-492f-bd83-d6ca73b3000d
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
---
# Discover-DLL-Search-Order-with-ProcMon

## Summary

This procedure uses ProcMon to monitor file system accesses during execution of tibxread.exe, revealing the DLL search order that includes writable PATH directories, enabling identification of hijacking opportunities in the Acronis Cyber Protection Agent.

## Description

In a local attack scenario on Windows, a low-privileged attacker monitors process activity to discover how tibxread.exe searches for dependencies like tcmalloc.dll. The tool captures CreateFile operations, showing searches in system PATH (e.g., C:\Python27) before the executable's directory. This informs the placement of malicious DLLs for escalation. Prerequisites include local access and the Acronis installer.

## Requirements

1. Local low-privileged access to Windows
2. Download Acronis installer from https://mc-beta-cloud.acronis.com/download/u/baas/4.0/12.5.23130/Cyber_Protection_Agent_for_Windows_web.exe
3. ProcMon installed from Sysinternals

## Defense

Defensive measures and detection strategies:

- Use application whitelisting to restrict unsigned DLL loading
- Monitor for unexpected file accesses in PATH directories via Sysmon or EDR
- Enforce secure DLL loading with APIs like LoadLibraryEx with LOAD_LIBRARY_SEARCH flags

## Objectives

1. Identify vulnerable DLL search paths for hijacking
2. Confirm writable directories in the search order
3. Gather evidence for exploitation planning

## Instructions

### Step 1: Launch ProcMon and Set Filters

**Context**: Start monitoring to capture relevant file operations for tibxread.exe.

Launch ProcMon and configure filters for tibxread.exe processes and CreateFile operations targeting DLLs like tcmalloc.dll.

### Step 2: Download and Prepare Installer

**Context**: Obtain the target software to test execution.

Download the installer using a browser or wget equivalent on Windows.

### Step 3: Install and Execute with Monitoring

**Context**: Run the installation and initial execution while capturing logs.

Execute the installer, then run tibxread.exe; review ProcMon for search patterns.

**Expected Output**: Logs showing failed loads from writable PATHs like C:\python27\tcmalloc.dll NAME NOT FOUND.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[DLL Search Order Hijacking]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ProcMon]]

## Tags

- discovery
- dll-hijacking
