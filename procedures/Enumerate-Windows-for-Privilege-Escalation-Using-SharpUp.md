---
type: procedure
tactics:
  - '[[Discovery]]'
  - '[[Persistence]]'
  - '[[Privilege Escalation]]'
techniques:
  - '[[Account Discovery]]'
  - '[[File and Directory Discovery]]'
  - '[[File System Permissions Weakness]]'
  - '[[Permission Groups Discovery]]'
  - '[[System Information Discovery]]'
  - '[[System Service Discovery]]'
sub_techniques: []
tags:
  - Enumeration
commands:
  - '[[commands/sharpup-audit-enumeration]]'
tools:
  - '[[tools/SharpUp]]'
platforms:
  - Windows
verified: true
validated: true
---

# Enumerate-Windows-for-Privilege-Escalation-Using-SharpUp

## Summary

This procedure uses SharpUp, a C# tool that implements the functionality of the PowerUp PowerShell script, to enumerate common privilege escalation vectors on Windows systems. It scans for vulnerable services, weak file and registry permissions, DLL hijacking opportunities, and other misconfigurations that could allow escalation from a low-privileged user to SYSTEM or administrator.

## Description

SharpUp performs automated checks for privilege escalation paths by inspecting services that can be modified, files with weak permissions that enable DLL hijacking or binary replacement, registry keys with improper access controls, and system configurations like AlwaysInstallElevated. This is particularly useful in post-exploitation scenarios where an attacker has initial low-level access to a Windows host and needs to identify quick wins for privilege escalation. The tool outputs categorized results, highlighting exploitable issues with details like paths, permissions, and potential abuse methods. Run it from a compromised shell to avoid detection, and review outputs for immediate exploitation opportunities.

## Requirements

1. Compromised access to a Windows system (local shell or remote execution capability).
2. .NET Framework 3.5 or later installed on the target.
3. Ability to execute unsigned binaries (may require bypassing execution policies via PowerShell).
4. Optional: Network access to download the SharpUp binary if not pre-staged.

## Defense

- Enable Windows Defender Application Control (WDAC) or AppLocker to restrict execution of unsigned .NET binaries.
- Implement PowerShell logging (Module, ScriptBlock, and Transcription) to capture execution of related scripts.
- Regularly audit service binaries, file permissions, and registry keys using tools like WinPEAS or manual checks.
- Monitor for anomalous process creation involving .NET executables in sensitive directories.

## Objectives

1. Identify modifiable services that allow binary replacement for privilege escalation.
2. Detect weak permissions on executable files or directories enabling DLL hijacking or path hijacking.
3. Enumerate registry misconfigurations, such as unquoted paths or weak run keys.
4. Gather system information to prioritize escalation vectors based on current user context.

## Instructions

### Step 1: Obtain and Stage SharpUp Binary

**Context**: SharpUp must be available on the target system to perform the enumeration without relying on external downloads during execution, reducing network-based detection.

Download the precompiled SharpUp.exe from the official GitHub repository or compile it from source using Visual Studio on a development machine, then transfer it to the target (e.g., via SMB, HTTP, or existing shell). Place it in a temporary directory like C:\Temp. If using the PowerShell version (SharpUp.ps1), ensure PowerShell execution policy allows script running (e.g., Set-ExecutionPolicy Bypass).

### Step 2: Execute SharpUp Audit

**Context**: The core enumeration step runs SharpUp in audit mode to scan the system comprehensively for privilege escalation opportunities. This aggregates checks across services, files, registry, and configurations.

**Command** ([[commands/sharpup-audit-enumeration]]):
```cmd
SharpUp.exe audit
```

Run this from an elevated command prompt if possible, but it works from low-priv contexts to identify escalation paths. The tool will output sections detailing findings, such as modifiable services or weak permissions. If using the .ps1 variant, execute `powershell.exe -ExecutionPolicy Bypass -File SharpUp.ps1 -Audit`.

### Step 3: Review and Validate Findings

**Context**: Analyze the audit output to identify and verify exploitable vectors, focusing on those feasible with current privileges (e.g., writable service binaries).

Parse the console output for key sections like "Modifiable Services," "Weak Permissions," and "Registry Checks." For each potential vector, note the path, current permissions (using icacls or AccessChk), and abuse method (e.g., replace binary with a malicious one). Cross-verify with manual tools like AccessChk ([[tools/AccessChk]]) for false positives. Prioritize issues like unquoted service paths or always-elevated installers for immediate exploitation.
