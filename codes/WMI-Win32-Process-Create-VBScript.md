---
type: code
language: VBScript
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - wmi
  - code-execution
  - office-macro
validated: true
---

# WMI-Win32-Process-Create-VBScript

## Code

```vbscript
r = GetObject("winmgmts:\.\root\cimv2:Win32_Process").Create("calc.exe", null, null, intProcessID)
```

## Description

This VBScript snippet uses WMI to create and start a new process on a Windows system, targeting the Win32_Process class. It spawns calc.exe as a proof-of-concept but can be adapted for any executable. Designed for embedding in Office VBA macros (e.g., DOCM files) to achieve in-memory execution without disk writes.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `calc.exe` | Path to the executable to spawn (replace with target binary) | `powershell.exe` |
| `intProcessID` | Variable to store the new process ID (optional, can be omitted if not needed) | N/A |

## Usage

Embed this code within a VBA Sub in a macro-enabled Word document (DOCM). Trigger it via Document_Open event for automatic execution when the file is opened. Use for initial access in phishing campaigns; replace calc.exe with a payload like a reverse shell executable. Test in a lab environment to ensure macro execution is allowed.

## Detection

- Monitor for WMI process creation events (Event ID 4688 with parent process as winword.exe).
- Enable Office macro logging and scan for VBScript in VBA projects.
- Behavioral detection: Unusual process spawns from Office applications via WMI (query Win32_ProcessStartup).

## Related

- [[procedures/Execute-Code-via-WMI-COM-Functions-in-DOCM-Files]]
