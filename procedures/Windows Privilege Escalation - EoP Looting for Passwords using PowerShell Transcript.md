---
id: d99cba06-5e7c-42ac-8d5e-584d87388c0d
name: Windows Privilege Escalation - EoP Looting for Passwords using PowerShell Transcript
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:29.327427+00:00'
updated_at: '2023-04-10T20:37:50.000755+00:00'
tactics:
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
tags:
- '[[EoP - Looting for passwords]]'
- '[[Powershell Transcript]]'
- '[[Windows - Privilege Escalation]]'
---

# Windows Privilege Escalation - EoP Looting for Passwords using PowerShell Transcript

## Summary

This procedure involves exploiting a vulnerability in Windows to escalate privileges and loot passwords using PowerShell Transcript. The attacker can use this technique to gain administrative access to the target system and steal sensitive information.

PowerShell Transcript is a built-in feature i

## Description

# Description

This procedure involves exploiting a vulnerability in Windows to escalate privileges and loot passwords using PowerShell Transcript. The attacker can use this technique to gain administrative access to the target system and steal sensitive information.

PowerShell Transcript is a built-in feature in Windows that records all PowerShell commands and their output to a log file. An attacker can use this log file to extract passwords and other sensitive information that were entered by the user during the session.

This procedure is valuable to attackers as it allows them to easily escalate their privileges and gain access to sensitive information without being detected by security measures.

 

## Requirements

1. Access to a Windows system with PowerShell Transcript enabled

1. Knowledge of PowerShell scripting

 

## Defense

1. Disable PowerShell Transcript to prevent attackers from using it

1. Monitor PowerShell commands for suspicious activity

1. Implement strong password policies to minimize the impact of password theft

 

## Objectives

1. Escalate privileges on a Windows system

1. Loot passwords and sensitive information

 

# Instructions

1. Use the PowerShell Transcript command to record all commands and their output to a text file.

 



**Code**: [[C:\Users\<USERNAME>\Documents\PowerShell_transcrip]]



> The PowerShell Transcript command is used to create a record of all PowerShell commands and their output to a text file. This can be useful for troubleshooting, auditing, or training purposes. The <USERNAME> field should be replaced with the username of the user running the command. The <HOSTNAME> field should be replaced with the hostname of the computer running the command. The <RANDOM> field should be replaced with a random string of characters. The <TIMESTAMP> field should be replaced with a timestamp in the format YYYY-MM-DD_HH-MM-SS. The <DATE> field should be replaced with the current date in the format YYYY-MM-DD. The resulting file will be saved in two locations, the user's Documents folder and a folder named Transcripts with the current date as the folder name.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]

## Tags

- [[EoP - Looting for passwords]]
- [[Powershell Transcript]]
- [[Windows - Privilege Escalation]]


