---
tags:
  - memory-leak
  - poc
  - compilation
type: procedure
tools:
  - '[[tools/Visual-Studio-2017]]'
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
updated_at: '2025-12-14T17:26:48.896Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 3ee7cfc7-6be1-4497-945a-7c9d24cefdfa
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Compile PoC Executable for Nextcloud Memory Leak

## Summary

This procedure compiles a C++ proof-of-concept executable that exploits the memory leak in Nextcloud's OCUtil.dll IsChildFile function, enabling repeated calls to allocate memory without freeing it.

## Description

The PoC targets the vulnerability in FileUtil.cpp line 42, where memory allocation occurs but deallocation fails under certain conditions. The executable uses LoadLibrary to load OCUtil_x64.dll, GetProcAddress to retrieve IsChildFile, and calls it in an infinite loop with sample paths like parent folder and child file. This demonstrates uncontrolled resource consumption leading to DoS when integrated with explorer.exe context menus. Prerequisites include Visual Studio 2017 and the PoC source code from the report.

## Requirements

1. Windows machine with Visual Studio 2017 installed
2. PoC C++ source code (solution file) available
3. Basic C++ compilation knowledge

## Defense

Defensive measures and detection strategies:

- Patch Nextcloud client to fixed version
- Monitor process memory usage anomalies in explorer.exe
- Use memory debugging tools like Application Verifier

## Objectives

1. Generate a working executable to trigger the leak
2. Verify compilation targets x64 for DLL compatibility
3. Prepare for execution in a controlled environment

## Instructions

### Step 1: Open Project in Visual Studio

**Context**: Load the PoC solution to access the C++ code that implements the leak demonstration.

Open Visual Studio 2017 and load the .sln file from the PoC attachment.

> Ensure the project is configured for Release x64 build to match the DLL architecture.

### Step 2: Build the Solution

**Context**: Compile the code into an executable that can load and call the vulnerable function.

In Visual Studio, select Build > Build Solution (or press Ctrl+Shift+B).

> The build process links against Windows APIs for DLL loading. Successful build outputs tests.exe in the bin/Release directory.

### Step 3: Verify Output

**Context**: Confirm the executable is ready and free of errors.

Check the Output window in Visual Studio for successful compilation messages, then locate tests.exe.

> Run `tests.exe /?` if applicable, but primarily test by executing to ensure no immediate crashes.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Visual-Studio-2017]]

## Tags

- memory-leak
- poc
- compilation
