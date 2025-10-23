---
id: 4227632a-32b7-48cd-bb26-7e8243e4097e
name: Windows Startup Elevated Persistence via User Startup Folder
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.073534+00:00'
updated_at: '2023-04-10T20:37:28.221258+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Bypass User Account Control|T1088 - Bypass User Account Control]]'
- '[[Registry Run Keys / Startup Folder|T1060 - Registry Run Keys / Startup Folder]]'
tags:
- '[[Elevated]]'
- '[[Startup Elevated]]'
- '[[Windows - Persistence]]'
---

# Windows Startup Elevated Persistence via User Startup Folder

## Summary

This technique involves placing a batch script in the User Startup folder to achieve persistence with elevated privileges. When a user logs in, the script will execute with the same privileges as the user, which can be escalated if the user has administrative privileges. The script can be used to e

## Description

# Description

This technique involves placing a batch script in the User Startup folder to achieve persistence with elevated privileges. When a user logs in, the script will execute with the same privileges as the user, which can be escalated if the user has administrative privileges. The script can be used to execute additional commands or malware, bypassing UAC and other security measures. This technique can be used by an attacker to maintain access to a compromised system.

Technical Explanation: An attacker can create a batch script that executes their desired commands or malware. The script can then be placed in the User Startup folder, which will cause it to execute every time the user logs in. If the user has administrative privileges, the script will execute with those privileges. If not, the attacker can use other techniques to escalate privileges.

Business Value: This technique can be used by attackers to maintain access to a compromised system, allowing them to steal sensitive data, install additional malware, or use the compromised system as a foothold for further attacks.

 

## Requirements

1. Access to the User Startup folder

 

## Defense

1. Monitor the User Startup folder for any unauthorized scripts or executables

1. Implement application whitelisting to prevent unauthorized scripts or executables from executing

1. Enforce the principle of least privilege to limit the privileges of users and reduce the impact of any successful attack

 

## Objectives

1. Achieve persistence on a compromised system

1. Execute additional commands or malware with elevated privileges

1. Bypass UAC and other security measures

 

# Instructions

1. To create a batch script in the user startup folder, follow these steps:
1. Open Notepad or any other text editor.
2. Write your batch script.
3. Save the file with a .bat extension.
4. Copy the file to the following directory: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp

 



**Code**: [[C:\ProgramData\Microsoft\Windows\Start Menu\Progra]]



> This command allows you to create a batch script that will run automatically when a user logs into their account. By copying the batch script to the user startup folder, it will be executed every time the user logs in. This can be useful for automating certain tasks or launching specific programs on startup.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Bypass User Account Control|T1088 - Bypass User Account Control]]
- [[Registry Run Keys / Startup Folder|T1060 - Registry Run Keys / Startup Folder]]

## Tags

- [[Elevated]]
- [[Startup Elevated]]
- [[Windows - Persistence]]


