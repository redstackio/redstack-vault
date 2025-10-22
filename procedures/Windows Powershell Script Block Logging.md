---
id: e10b9099-061d-44d1-b9ec-dbbc8870f956
name: Windows Powershell Script Block Logging
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.574872+00:00'
updated_at: '2023-04-10T20:37:05.221062+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Powershell]]'
- '[[Script Block Logging]]'
- '[[Windows - Defenses]]'
---

# Windows Powershell Script Block Logging

## Summary

Windows PowerShell Script Block Logging is a security feature that logs detailed information about the execution of PowerShell commands and scripts. This feature can help defenders detect malicious PowerShell activity and gain insight into the actions of an attacker. Script Block Logging records th

## Description

# Description

Windows PowerShell Script Block Logging is a security feature that logs detailed information about the execution of PowerShell commands and scripts. This feature can help defenders detect malicious PowerShell activity and gain insight into the actions of an attacker. Script Block Logging records the full command or script that was executed, the user account that executed it, and the time of execution. This information can be used to identify potentially malicious activity, such as the use of obfuscated or encoded commands, and can help defenders quickly respond to security incidents.

From a technical perspective, Script Block Logging works by intercepting PowerShell commands and scripts and logging them to the Windows event log. This feature is enabled by default in newer versions of Windows, but it may need to be manually enabled in older versions. To enable Script Block Logging, administrators can use the 'Enable Script Block Logging' command.

From a business perspective, Script Block Logging is an important tool for defending against cyber attacks. By enabling this feature, organizations can better protect their systems and data from malicious PowerShell activity. This can help prevent data breaches, intellectual property theft, and other cyber security incidents.

## Requirements

1. Administrator access to enable Script Block Logging

1. PowerShell version 5 or later

## Defense

1. Regularly review the Windows event log for suspicious PowerShell activity

1. Implement strong access controls to prevent unauthorized access to PowerShell

1. Use endpoint protection solutions to detect and block malicious PowerShell activity

## Objectives

1. Detect malicious PowerShell activity

1. Gain insight into attacker actions

1. Quickly respond to security incidents

# Instructions

1. To enable script block logging, run the following command:

**Code**: [[function Enable-PSScriptBlockLogging
{
    $basePa]]

> This command creates a registry key to enable script block logging in PowerShell. Script block logging records the input and output of each command that is executed in PowerShell, including any scripts that are run. This can be useful for troubleshooting and auditing purposes.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Scripting|T1064 - Scripting]]

## Tags

- [[Powershell]]
- [[Script Block Logging]]
- [[Windows - Defenses]]
