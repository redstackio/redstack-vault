---
id: e2e1e2ec-f83f-45c8-b80c-457da64c951c
name: Windows - Unquoted Service Path Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:29.715839+00:00'
updated_at: '2023-04-10T20:37:38.933740+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[DLL Search Order Hijacking|T1038 - DLL Search Order Hijacking]]'
tags:
- '[[EoP - Unquoted Service Paths]]'
- '[[Example]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Execute legit.exe]]'
---

# Windows - Unquoted Service Path Privilege Escalation

## Summary

Windows services can be installed with unquoted paths that contain spaces. This can allow an attacker to escalate privileges by replacing the executable that the service runs with a malicious executable that will run with elevated privileges. This technique is often used by attackers to gain persis

## Description

# Description

Windows services can be installed with unquoted paths that contain spaces. This can allow an attacker to escalate privileges by replacing the executable that the service runs with a malicious executable that will run with elevated privileges. This technique is often used by attackers to gain persistence on a compromised system. To perform this attack, the attacker needs to find a service with an unquoted path and have write access to the location where the service executable is stored. Once the attacker replaces the executable, the service will run the attacker's code with elevated privileges, giving the attacker full control of the system.

 

## Requirements

1. Access to a system with a service installed with an unquoted path

1. Write access to the location where the service executable is stored

 

## Defense

1. Ensure that all services are installed with quoted paths that contain spaces

1. Limit write access to the location where service executables are stored

1. Monitor for changes to service executables and paths

 

## Objectives

1. Gain elevated privileges on a compromised system

 

# Instructions

1. running an executable file

 



**Code**: [[C:\Program Files\something\legit.exe]]



> The path to the executable file that needs to be run. This command is used to execute a program or application on a Windows machine. The path should be the absolute path to the executable file, including the file name and extension. For example, C:\Program Files\something\legit.exe



**Command** ([[Execute legit.exe]]):

```bash
C:\Program Files\something\legit.exe
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[DLL Search Order Hijacking|T1038 - DLL Search Order Hijacking]]

## Commands Used

- [[Execute legit.exe]]

## Tags

- [[EoP - Unquoted Service Paths]]
- [[Example]]
- [[Windows - Privilege Escalation]]


