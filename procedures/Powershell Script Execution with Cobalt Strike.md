---
id: 0ad55538-85d3-4c0e-afa3-71b441efd5db
name: Powershell Script Execution with Cobalt Strike
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:16.497331+00:00'
updated_at: '2023-04-10T20:36:20.364956+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[PowerShell|T1086 - PowerShell]]'
- '[[System Time Discovery|T1124 - System Time Discovery]]'
tags:
- '[[Cobalt Strike]]'
- '[[Powershell and .NET]]'
- '[[Powershell commands]]'
commands:
- '[[Execute Powershell Script]]'
- '[[Import Powershell Script into Beacon Memory]]'
- '[[Inject Unmanaged Powershell into a Process]]'
- '[[Launch Function using Unmanaged Powershell]]'
---

# Powershell Script Execution with Cobalt Strike

## Summary

Powershell Script Execution with Cobalt Strike is a technique used by attackers to execute malicious scripts on a target system. This technique involves using Cobalt Strike to generate a Powershell script that is then executed on the target system. The script can be used to perform a variety of mal

## Description

# Description

Powershell Script Execution with Cobalt Strike is a technique used by attackers to execute malicious scripts on a target system. This technique involves using Cobalt Strike to generate a Powershell script that is then executed on the target system. The script can be used to perform a variety of malicious activities such as downloading and executing additional payloads, exfiltrating data, or establishing persistence.

From a technical perspective, this technique involves using Cobalt Strike's Beacon payload to establish a C2 channel with the target system. Once the C2 channel is established, Cobalt Strike can generate a Powershell script that is encoded and delivered to the target system using the 'Powershell Script Execution' command. The script is then executed on the target system, allowing the attacker to carry out their objectives.

The business value of this technique is that it allows attackers to gain a foothold on a target system and carry out malicious activities without being detected. This can result in the theft of sensitive data, disruption of business operations, and financial losses.

 

## Requirements

1. Access to a Cobalt Strike server

1. Access to a target system with Powershell enabled

 

## Defense

1. Implement strict application whitelisting policies to prevent the execution of unauthorized scripts

1. Regularly monitor and analyze network traffic for any signs of malicious activity

1. Conduct regular security awareness training for employees to help them identify and report suspicious activity

 

## Objectives

1. Execute a malicious Powershell script on a target system

1. Establish persistence on a target system

1. Download and execute additional payloads on a target system

1. Exfiltrate data from a target system

 

# Instructions

1. To import a Powershell script from the control server and save it in memory, use the command 'powershell-import' followed by the path to the script. 

To execute the script, use the command 'powershell' followed by the commandlet and any arguments. This will download the script from the server and execute the specified function, returning the output.

To launch a function using Unmanaged Powershell, use the command 'powerpick' followed by the commandlet and any arguments. This will execute the function without starting powershell.exe. The program used is set by spawnto.

To inject Unmanaged Powershell into a specific process and execute a command, use the command 'psinject' followed by the process ID and architecture, commandlet, and any arguments. This is useful for long-running Powershell jobs.

 



**Code**: [[# Import a Powershell .ps1 script from the control]]



> The 'powershell-import' command is used to import a Powershell script from the control server and save it in memory. The 'powershell' command is used to execute the imported script, downloading it from the server and executing the specified function. The 'powerpick' command is used to launch a function using Unmanaged Powershell, and the 'psinject' command is used to inject Unmanaged Powershell into a specific process and execute a command.



**Command** ([[Import Powershell Script into Beacon Memory]]):

```powershell
powershell-import [/path/to/script.ps1]
```





**Command** ([[Execute Powershell Script]]):

```powershell
powershell [commandlet][arguments]
```





**Command** ([[Launch Function using Unmanaged Powershell]]):

```bash
powerpick [commandlet] [argument]
```





**Command** ([[Inject Unmanaged Powershell into a Process]]):

```bash
psinject [pid][arch] [commandlet] [arguments]
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[PowerShell|T1086 - PowerShell]]
- [[System Time Discovery|T1124 - System Time Discovery]]

## Commands Used

- [[Execute Powershell Script]]
- [[Import Powershell Script into Beacon Memory]]
- [[Inject Unmanaged Powershell into a Process]]
- [[Launch Function using Unmanaged Powershell]]

## Tags

- [[Cobalt Strike]]
- [[Powershell and .NET]]
- [[Powershell commands]]


