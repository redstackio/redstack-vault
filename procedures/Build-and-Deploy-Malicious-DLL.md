---
id: proc-malicious-dll-build-001
tags:
  - dll-compilation
  - code-injection
  - cross-compilation
type: procedure
tools:
  - '[[tools/x86_64-w64-mingw32-gpp]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/compile-calc-dll]]'
  - '[[commands/copy-calc-dll-to-stage]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Dynamic-link Library Injection]]'
  - '[[DLL Side-Loading]]'
updated_at: '2025-12-14T17:29:44.235Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Dynamic-link Library Injection]]'
  - '[[DLL Side-Loading]]'
---
# Build and Deploy Malicious DLL

## Summary

This procedure compiles a malicious OpenSSL Engine DLL from C source code that executes arbitrary commands (PoC: system("calc")) upon loading and deploys it to the staging path referenced in openssl.cnf, enabling code injection when curl loads OpenSSL.

## Description

The DLL acts as a custom OpenSSL Engine, with its DllMain triggered on DLL_PROCESS_ATTACH to run system commands. Source calc.c includes #include <windows.h> and DllMain exporting the payload. Cross-compilation targets Windows x64. Deployment places it in c:\stage for config loading. This exploits the lack of path validation in curl's OpenSSL integration, leading to execution with curl's privileges.

## Requirements

1. Cross-compilation environment (MinGW-w64 installed)
2. C source file calc.c with malicious DllMain
3. Access to copy files to c:\stage

## Defense

Defensive measures and detection strategies:

- Enable DLL signing enforcement in OpenSSL/curl
- Audit DLL loads in curl processes via ETW or ProcMon
- Restrict execution of unsigned DLLs in system paths

## Objectives

1. Generate functional malicious DLL for OpenSSL Engine
2. Position DLL for automatic loading via config
3. Ensure payload executes on DLL attach

## Instructions

### Step 1: Compile the Malicious DLL

**Context**: Build calc.c into a shared DLL using cross-compiler.

**Command** ([[commands/compile-calc-dll]]):
```bash
x86_64-w64-mingw32-g++ calc.c -o calc.dll -shared
```

> Compiles to calc.dll; expected: Binary generated without errors.

### Step 2: Deploy DLL to Staging Path

**Context**: Place DLL where openssl.cnf expects it for loading.

**Command** ([[commands/copy-calc-dll-to-stage]]):
```cmd
copy calc.dll c:\stage
```

> Copies file; expected: "File copied successfully".

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Dynamic-link Library Injection]] Dynamic-link Library Injection
- [[DLL Side-Loading]] DLL Side-Loading

### Sub-Techniques


## Commands Used

- [[commands/compile-calc-dll]]
- [[commands/copy-calc-dll-to-stage]]

## Tools Used

- [[tools/x86_64-w64-mingw32-gpp]]

## Tags

- dll-injection
- compilation
