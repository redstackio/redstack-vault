---
id: bc1fdf28-7546-4e52-9e41-fca4862c7bde
name: Windows - Impersonation Privileges Elevation with Meterpreter
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.115570+00:00'
updated_at: '2023-04-10T20:37:40.595834+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[Process Injection|T1055 - Process Injection]]'
- '[[Valid Accounts|T1078 - Valid Accounts]]'
tags:
- '[[EoP - Impersonation Privileges]]'
- '[[Meterpreter getsystem and alternatives]]'
- '[[Windows - Privilege Escalation]]'
---

# Windows - Impersonation Privileges Elevation with Meterpreter

## Summary

This procedure is used to elevate privileges on a Windows system by abusing impersonation privileges. By using Meterpreter's getsystem command, an attacker can escalate their privileges to SYSTEM level. This technique is commonly used by attackers who have already gained access to a low-privileged 

## Description

# Description

This procedure is used to elevate privileges on a Windows system by abusing impersonation privileges. By using Meterpreter's getsystem command, an attacker can escalate their privileges to SYSTEM level. This technique is commonly used by attackers who have already gained access to a low-privileged account on a system and are looking to escalate their privileges to gain access to sensitive information or perform malicious actions. To use this technique, the attacker must have already gained access to a system using a valid account or other means of execution.

Technical Explanation: Meterpreter is a post-exploitation tool that is commonly used by attackers to maintain access to a compromised system. The getsystem command is a built-in Meterpreter command that allows an attacker to escalate their privileges to the highest level, SYSTEM. This is achieved by injecting a DLL into a system process that has the SeDebugPrivilege privilege, which allows the attacker to manipulate access tokens and impersonate other users or groups. Once the attacker has escalated their privileges, they can perform a variety of actions, including installing malware, modifying system settings, or accessing sensitive information.

Business Value: By using this technique, attackers can gain access to sensitive information or perform malicious actions on a compromised system. This can result in data theft, financial loss, or damage to a company's reputation.

## Requirements

1. Valid account or other means of execution on target system

1. Meterpreter

## Defense

1. Ensure that all user accounts have the least amount of privileges necessary to perform their job functions

1. Use endpoint detection and response (EDR) tools to monitor for suspicious behavior and unauthorized access

1. Implement multi-factor authentication to prevent unauthorized access to user accounts

## Objectives

1. Escalate privileges to SYSTEM level

# Instructions

1. To elevate privileges, you can use one of the following commands:
1. getsystem
2. Tokenvator.exe getsystem cmd.exe
3. incognito.exe execute -c "NT AUTHORITY\SYSTEM" cmd.exe
4. psexec -s -i cmd.exe
5. python getsystem.py # from https://github.com/sailay1996/tokenx_privEsc

**Code**: [[meterpreter> getsystem 
Tokenvator.exe getsystem c]]

> The above commands are used to escalate privileges on a Windows system. The 'getsystem' command is a built-in Meterpreter command that attempts to elevate the current session to the highest privilege level available on the target system. Tokenvator.exe is a tool that can be used to elevate privileges by injecting a DLL into a process with SYSTEM-level privileges. Incognito.exe is a tool that can be used to impersonate a user or elevate privileges by executing commands as SYSTEM. Psexec.exe is a tool that can be used to execute commands on a remote system with SYSTEM-level privileges. Finally, 'python getsystem.py' is a Python script that can be used to elevate privileges on a target system.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[Process Injection|T1055 - Process Injection]]
- [[Valid Accounts|T1078 - Valid Accounts]]

## Tags

- [[EoP - Impersonation Privileges]]
- [[Meterpreter getsystem and alternatives]]
- [[Windows - Privilege Escalation]]
