---
type: procedure
description: >-
  Uses WMI COM objects embedded in DOCM macro-enabled Word documents to execute
  arbitrary code on a Windows target without writing files to disk.
verified: true
submitted: false
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Windows Management Instrumentation|T1047 - Windows Management
    Instrumentation]]
sub_techniques: []
tags:
  - '[[tags/DOCM - WMI COM functions]]'
  - '[[tags/Office - Attacks]]'
  - wmi
  - code-execution
  - office-macro
commands: []
platforms:
  - Windows
tools: []
validated: true
---

# Execute-Code-via-WMI-COM-Functions-in-DOCM-Files

## Summary

This procedure demonstrates how to embed WMI COM functions within a macro-enabled DOCM (Word document) to execute arbitrary code on a victim's Windows machine. By leveraging the Windows Management Instrumentation (WMI) via VBScript in Office macros, attackers can achieve remote code execution without dropping files to disk, evading some antivirus and endpoint detection solutions. This is particularly useful for initial access through phishing-delivered malicious documents.

## Description

WMI provides a standardized infrastructure for management data and operations on Windows systems, accessible through COM interfaces. In the context of Office attacks, VBScript code within a DOCM file's VBA macros can instantiate WMI objects to create processes directly in memory. This technique targets the Win32_Process class in the root\cimv2 namespace to spawn executables like calc.exe or powershell.exe. The attack relies on the victim opening the DOCM file and enabling macros, granting the script execution privileges under the user's context. It bypasses file-based detection by avoiding disk writes and can be combined with social engineering for delivery. Expected outcomes include successful process creation, visible or hidden execution depending on configuration, and potential lateral movement if elevated privileges are obtained.

## Requirements

1. Target must be running Windows (tested on Windows 10/11/Server 2019+ with Office 2016+ installed).
2. Victim must open the DOCM file and enable VBA macros (requires user interaction).
3. Attacker knowledge of VBScript and VBA macro embedding in Office documents.
4. No administrative privileges required on target, but execution occurs in user context.

## Defense

- Implement application whitelisting (e.g., AppLocker or WDAC) to block unauthorized Office macro execution.
- Monitor WMI activity via Event ID 5857 (WMI Activity) and 19 (WMI Client) in Windows Event Logs.
- Disable VBA macros by default in Office policies and use Protected View for all documents.
- Enable Office macro antivirus scanning and behavioral detection for WMI process creation from Office apps.

## Objectives

1. Achieve code execution on the target system without file drops.
2. Bypass basic endpoint security controls like antivirus.
3. Establish initial foothold for further post-exploitation.
4. Demonstrate persistence or lateral movement via spawned processes.

## Instructions

### Step 1: Embed WMI Process Creation Script in DOCM Macro

**Context**: Create a simple VBScript snippet using WMI to spawn a benign process like calc.exe. This tests basic execution and verifies macro privileges. Embed this in the DOCM's VBA module to run on document open.

**Code** ([[codes/WMI-Win32-Process-Create-VBScript]]):

```vbscript
r = GetObject("winmgmts:\.\root\cimv2:Win32_Process").Create("calc.exe", null, null, intProcessID)
```

> This VBScript uses the GetObject method to access the Win32_Process class via WMI. The Create method spawns the specified executable (calc.exe here) with no arguments or working directory. The intProcessID variable captures the new process ID if needed. In a DOCM macro, wrap this in a Sub like Private Sub Document_Open() and call it on load. Expected output is the Calculator app launching if successful; no console output, but process creation can be verified via Task Manager.

### Step 2: Embed WMI Script for Visible PowerShell Execution

**Context**: Extend the macro to execute PowerShell with a visible window for interactive commands. This allows running complex payloads while maintaining visibility for troubleshooting or user deception.

**Code** ([[codes/WMI-Execute-PowerShell-Visible-Window-VBScript]]):

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

> This VBScript subroutine connects to the local WMI service, configures Win32_ProcessStartup for a visible window (ShowWindow=1), and creates a PowerShell process. Call this Sub from the DOCM's Document_Open event. Expected output is a visible PowerShell window opening; success is indicated by the window appearing without errors. Modify the executable path or add arguments (e.g., "powershell.exe -Command 'Get-Process'") for custom payloads.
