---
id: proc-compile-dll
tags:
  - deserialization
  - dll-compilation
type: procedure
tools:
  - '[[tools/build_dll.bat]]'
  - '[[tools/Visual-Studio]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/build-dll]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[PowerShell]]'
updated_at: '2025-12-14T17:23:36.029Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[PowerShell]]'
---
# Compile-Deserialization-DLL-Gadget

## Summary

This procedure compiles a C# DLL gadget on a Windows system using Visual Studio and build_dll.bat from the BishopFox guide, creating a payload that triggers insecure deserialization in Telerik UI for RCE proof-of-concept (e.g., sleep delay).

## Description

The DLL acts as a deserialization gadget chain exploiting CVE-2019-18935, where uploaded .NET assemblies are processed unsafely during file handling. The build script compiles source code into a DLL executable on the attacker's local machine, ready for upload to the target.

## Requirements

1. Windows machine with Visual Studio installed
2. build_dll.bat script from BishopFox repo
3. .NET Framework matching target (e.g., 4.0+ for Telerik)

## Defense

Defensive measures and detection strategies:

- Avoid deserializing untrusted data in .NET applications
- Use safe serializers like Json.NET with type whitelisting
- Scan for known gadget chains in uploaded files

## Objectives

1. Generate a functional deserialization payload
2. Prepare for RCE triggering via upload
3. Enable proof-of-concept or full exploitation

## Instructions

### Step 1: Run Build Script

**Context**: Execute the batch file in a Visual Studio command prompt to compile the gadget DLL.

**Command** ([[commands/build-dll]]):

```bash
build_dll.bat
```

> Run in a Developer Command Prompt for VS. Expected output: Compiled DLL (e.g., sleep.dll) in the output directory, confirming gadget readiness for deserialization exploit.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[PowerShell]] PowerShell (adapted for .NET execution)

### Sub-Techniques


## Commands Used

- [[commands/build-dll]]

## Tools Used

- [[tools/build_dll.bat]]
- [[tools/Visual-Studio]]

## Tags

- deserialization
- dll-compilation
