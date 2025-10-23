---
id: 9df4bfb6-b9cc-4781-892c-a3c835aa6e75
name: Windows - Privileged File Write via UsoDLLLoader
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.353930+00:00'
updated_at: '2023-04-10T20:37:40.964274+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[DLL Search Order Hijacking|T1038 - DLL Search Order Hijacking]]'
- '[[File Permissions Modification|T1222 - File Permissions Modification]]'
tags:
- '[[EoP - Privileged File Write]]'
- '[[UsoDLLLoader]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[File Information]]'
- '[[View System32 directory]]'
---

# Windows - Privileged File Write via UsoDLLLoader

## Summary

This technique abuses the UsoDllLoader COM interface to load a malicious DLL into a Windows process with SYSTEM privileges, allowing for privileged file write operations. The UsoDllLoader interface is used by Windows to manage updates and is present on all Windows versions. By hijacking the DLL sea

## Description

# Description

This technique abuses the UsoDllLoader COM interface to load a malicious DLL into a Windows process with SYSTEM privileges, allowing for privileged file write operations. The UsoDllLoader interface is used by Windows to manage updates and is present on all Windows versions. By hijacking the DLL search order, an attacker can force the UsoDllLoader to load a malicious DLL when it is executed with SYSTEM privileges. This can be used to write malicious DLLs to protected directories, such as the SYSTEM32 directory, which can then be used to escalate privileges further or persist on the system.

 

## Requirements

1. Access to a Windows system

1. Ability to execute code with low privileges

 

## Defense

1. Implement least privilege access for user accounts to limit the ability to execute code with SYSTEM privileges

1. Monitor and restrict access to sensitive system directories, such as SYSTEM32

1. Regularly update and patch Windows systems to prevent known vulnerabilities from being exploited

 

## Objectives

1. Escalate privileges on a Windows system

1. Write malicious DLLs to protected directories

 

# Instructions

1. This command allows an attacker to escalate privileges on a Windows system by exploiting a privileged file write vulnerability in the Windows Core Device Info DLL. The attacker can then copy their own version of the DLL to the system, which will be loaded by the operating system and execute the attacker's code with elevated privileges.

 



**Code**: [[windowscoredeviceinfo.dll]]



> The 'data' field specifies the name of the DLL that contains the vulnerable code. The 'text' field provides context for how this vulnerability could be exploited. The 'instruction' field provides step-by-step instructions for how to perform the privilege escalation attack. The 'explain' field provides additional information about the attack and its potential impact.



**Command** ([[File Information]]):

```bash
windowscoredeviceinfo.dll
```



2. To access the System32 directory path, open the Windows File Explorer and navigate to the C drive. From there, navigate to the Windows folder and then the System32 folder.

 



**Code**: [[C:\Windows\System32\]]



> The System32 directory contains important system files that are necessary for the proper functioning of the Windows operating system. It is important to not delete or modify any files within this directory unless you are an advanced user and know what you are doing.



**Command** ([[View System32 directory]]):

```bash
dir
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[DLL Search Order Hijacking|T1038 - DLL Search Order Hijacking]]
- [[File Permissions Modification|T1222 - File Permissions Modification]]

## Commands Used

- [[File Information]]
- [[View System32 directory]]

## Tags

- [[EoP - Privileged File Write]]
- [[UsoDLLLoader]]
- [[Windows - Privilege Escalation]]


