---
id: 947dcf82-a5a5-450b-91c5-f4d05c847814
name: Windows - Elevated RDP Backdoor with Sticky Keys
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.206626+00:00'
updated_at: '2023-04-10T20:37:26.450490+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Accessibility Features|T1015 - Accessibility Features]]'
- '[[Hide Artifacts|T1564 - Hide Artifacts]]'
- '[[Registry Run Keys / Startup Folder|T1060 - Registry Run Keys / Startup Folder]]'
- '[[Remote Desktop Protocol|T1076 - Remote Desktop Protocol]]'
- '[[Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques:
- '[[Hidden File System|T1564.005 - Hidden File System]]'
tags:
- '[[Elevated]]'
- '[[RDP Backdoor]]'
- '[[sethc.exe]]'
- '[[Windows - Persistence]]'
---

# Windows - Elevated RDP Backdoor with Sticky Keys

## Summary

This procedure leverages the Sticky Keys backdoor to create an elevated RDP backdoor. Sticky Keys is a Windows accessibility feature that allows users to press a modifier key (Shift, Ctrl, Alt) and have it remain active until another key is pressed. By replacing the sethc.exe file (the process that

## Description

# Description

This procedure leverages the Sticky Keys backdoor to create an elevated RDP backdoor. Sticky Keys is a Windows accessibility feature that allows users to press a modifier key (Shift, Ctrl, Alt) and have it remain active until another key is pressed. By replacing the sethc.exe file (the process that launches Sticky Keys) with a command prompt, an attacker can execute commands with SYSTEM privileges by pressing Shift five times at the Windows login screen. Once the attacker has access to the system, they can enable RDP and create a backdoor account to maintain access to the system. This technique is effective because it is often overlooked by defenders and does not require any additional tools.

 

## Requirements

1. Access to the target system

1. Ability to modify system files

1. Knowledge of Sticky Keys backdoor

 

## Defense

1. Disable the Sticky Keys feature on all systems

1. Monitor for changes to the sethc.exe file

1. Implement two-factor authentication for RDP access

 

## Objectives

1. Gain persistent access to the compromised system

1. Escalate privileges to SYSTEM level

1. Create an elevated RDP backdoor account

1. Maintain access to the compromised system

 

# Instructions

1. This command adds a registry key to enable sticky keys backdoor. Sticky keys is a feature that allows key combinations to be pressed one key at a time instead of simultaneously. By default, if you press the shift key five times in a row, Windows will activate the Sticky Keys feature. By replacing the sethc.exe file with cmd.exe, you can open a command prompt with SYSTEM privileges by pressing the shift key five times in a row at the login screen.

 



**Code**: [[REG ADD "HKLM\SOFTWARE\Microsoft\Windows NT\Curren]]



> This command adds a registry key to the specified location in the Windows Registry. The /t flag specifies the data type of the registry value, in this case, REG_SZ (string value). The /v flag specifies the name of the registry value, in this case, Debugger. The /d flag specifies the data for the registry value, in this case, the path to cmd.exe. The /f flag specifies that the command should overwrite any existing registry values without prompting for confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Accessibility Features|T1015 - Accessibility Features]]
- [[Hide Artifacts|T1564 - Hide Artifacts]]
- [[Registry Run Keys / Startup Folder|T1060 - Registry Run Keys / Startup Folder]]
- [[Remote Desktop Protocol|T1076 - Remote Desktop Protocol]]
- [[Valid Accounts|T1078 - Valid Accounts]]

### Sub-Techniques

- [[Hidden File System|T1564.005 - Hidden File System]]

## Tags

- [[Elevated]]
- [[RDP Backdoor]]
- [[sethc.exe]]
- [[Windows - Persistence]]


