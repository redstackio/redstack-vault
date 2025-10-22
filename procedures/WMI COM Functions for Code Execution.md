---
id: c6a26abb-3e21-4489-88e3-0fb3baa997b4
name: WMI COM Functions for Code Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.555177+00:00'
updated_at: '2023-04-10T20:36:53.013347+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Windows Management Instrumentation|T1047 - Windows Management Instrumentation]]'
tags:
- '[[DOCM - WMI COM functions]]'
- '[[Office - Attacks]]'
---

# WMI COM Functions for Code Execution

## Summary

The WMI COM functions in DOCM files can be used to execute code on a victim's machine. This technique can be used by attackers to gain a foothold on a victim's machine and execute commands. This technique can be used to bypass security controls that may be in place, such as firewalls or antivirus s

## Description

# Description

The WMI COM functions in DOCM files can be used to execute code on a victim's machine. This technique can be used by attackers to gain a foothold on a victim's machine and execute commands. This technique can be used to bypass security controls that may be in place, such as firewalls or antivirus software.

Technical Explanation: The WMI COM functions provide a way for attackers to execute arbitrary code on a victim's machine. The WMI COM functions can be accessed through the Windows Script Host, which is a built-in Windows tool for running scripts. By using the WMI COM functions, attackers can execute code on a victim's machine without having to write a file to disk. This can make it more difficult for defenders to detect and prevent the attack.

Business Value: This technique can be used by attackers to gain access to sensitive information on a victim's machine. By gaining a foothold on a victim's machine, attackers can move laterally through the victim's network and access additional systems and data.

## Requirements

1. Access to a victim's machine

1. Knowledge of the WMI COM functions

1. Knowledge of the Windows Script Host

## Defense

1. Implement application whitelisting to prevent the execution of unauthorized scripts

1. Monitor for suspicious WMI activity

1. Restrict access to the Windows Script Host

## Objectives

1. Execute code on a victim's machine

1. Bypass security controls

# Instructions

1. This command executes the Windows Calculator using Windows Management Instrumentation (WMI).

**Code**: [[r = GetObject(&quot;winmgmts:\\.\root\cimv2:Win32_]]

> The command uses the `GetObject` method to retrieve the `Win32_Process` class from the `root\cimv2` namespace. The `Create` method is then called on the retrieved object to create a new process for the `calc.exe` executable. The `null` parameters indicate that no command line arguments or working directory are specified for the process. The `intProcessID` parameter is also set to `null`, which means that the process ID of the new process is not returned.

2. Execute a PowerShell command with a visible window

**Code**: [[Sub wmi_exec()
    strComputer = "."
    Set objWM]]

> This script can be used to execute a PowerShell command with a visible window. The script uses the Windows Management Instrumentation (WMI) to create a new process for the PowerShell command. The 'ShowWindow' property of the 'Win32_ProcessStartup' class is set to 1 to make the window visible. The 'Create' method of the 'Win32_Process' class is then used to start the PowerShell process with the specified command. The command can be modified by replacing 'powershell.exe' with the path to the desired executable and adding any necessary arguments.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Windows Management Instrumentation|T1047 - Windows Management Instrumentation]]

## Tags

- [[DOCM - WMI COM functions]]
- [[Office - Attacks]]
