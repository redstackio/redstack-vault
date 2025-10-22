---
id: 0fb5d900-a59a-4986-a6a9-e290ba822bd0
name: Windows Privilege Escalation - Powershell History Looting
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:29.295094+00:00'
updated_at: '2023-04-10T20:37:49.652376+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Bypass User Account Control|T1088 - Bypass User Account Control]]'
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
- '[[Credentials In Files|T1552.001 - Credentials In Files]]'
- '[[Credentials in Registry|T1552.002 - Credentials in Registry]]'
tags:
- '[[EoP - Looting for passwords]]'
- '[[Powershell History]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Set PSReadlineOption]]'
---

# Windows Privilege Escalation - Powershell History Looting

## Summary

This procedure focuses on looting for passwords by examining the PowerShell command history. PowerShell history is a log of all PowerShell commands executed on a system. This procedure aims to identify passwords that may have been passed as parameters to PowerShell commands. The attacker can then u

## Description

# Description

This procedure focuses on looting for passwords by examining the PowerShell command history. PowerShell history is a log of all PowerShell commands executed on a system. This procedure aims to identify passwords that may have been passed as parameters to PowerShell commands. The attacker can then use these passwords to escalate privileges and gain access to sensitive information. To execute this procedure, the attacker needs to have already gained access to a system with low-level privileges and be able to execute PowerShell commands.

## Requirements

1. Access to a system with low-level privileges

1. Ability to execute PowerShell commands

## Defense

1. Monitor PowerShell command history for suspicious activity

1. Enforce strong password policies to minimize the risk of password theft

1. Implement least privilege access to minimize the potential impact of privilege escalation

## Objectives

1. Identify passwords that may have been passed as parameters to PowerShell commands

1. Escalate privileges and gain access to sensitive information

# Instructions

1. To disable the saving of Powershell history, run the following command:

**Code**: [[Set-PSReadlineOption -HistorySaveStyle SaveNothing]]

> This command sets the PSReadline option to SaveNothing, which prevents Powershell from saving command history to a file. This can be useful for security reasons, as it prevents others from seeing your command history and potentially finding sensitive information.

**Command** ([[Set PSReadlineOption]]):

```bash
Set-PSReadlineOption -HistorySaveStyle SaveNothing
```

2. This command will allow you to view your PowerShell command history and search for any passwords that may have been entered. Simply copy and paste the command into your PowerShell terminal.

**Code**: [[type %userprofile%\AppData\Roaming\Microsoft\Windo]]

> The 'type' command is used to display the contents of a file. In this case, we are displaying the contents of three different files where PowerShell command history is stored. The 'cat' command is used to concatenate the contents of a file and display it in the terminal. We are using it to display the history save path and then search for any instances of the word 'passw' (which could indicate a password was entered). The 'Get-PSReadlineOption' command is used to retrieve the current PSReadline options, and we are using it to get the history save path.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Bypass User Account Control|T1088 - Bypass User Account Control]]
- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

### Sub-Techniques

- [[Credentials In Files|T1552.001 - Credentials In Files]]
- [[Credentials in Registry|T1552.002 - Credentials in Registry]]

## Commands Used

- [[Set PSReadlineOption]]

## Tags

- [[EoP - Looting for passwords]]
- [[Powershell History]]
- [[Windows - Privilege Escalation]]
