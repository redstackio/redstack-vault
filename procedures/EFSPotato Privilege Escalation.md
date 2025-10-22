---
id: 05d7c53e-9d16-4829-b860-7913a701a8b5
name: EFSPotato Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.245336+00:00'
updated_at: '2023-04-10T20:37:54.190558+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
sub_techniques:
- '[[Bypass User Account Control|T1548.002 - Bypass User Account Control]]'
tags:
- '[[EFSPotato (MS-EFSR EfsRpcOpenFileRaw)]]'
- '[[EoP - Impersonation Privileges]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Compile EfsPotato.cs with .NET 2.0/3.5]]'
- '[[Compile EfsPotato.cs with .NET 4.x]]'
---

# EFSPotato Privilege Escalation

## Summary

EFSPotato is a technique that allows an attacker to escalate privileges by impersonating other users through the Microsoft Encrypting File System Remote (EFSRPC) protocol. This technique exploits a vulnerability in EFSRPC, which allows the attacker to open a file with SYSTEM privileges. EFSPotato c

## Description

# Description

EFSPotato is a technique that allows an attacker to escalate privileges by impersonating other users through the Microsoft Encrypting File System Remote (EFSRPC) protocol. This technique exploits a vulnerability in EFSRPC, which allows the attacker to open a file with SYSTEM privileges. EFSPotato can be used to bypass User Account Control (UAC) and gain elevated privileges on the target system. This technique can be used in combination with other techniques to achieve persistence on the target system.

From a technical perspective, EFSPotato works by exploiting a race condition in EFSRPC. The attacker first creates a hard link to the target file and then uses the EfsRpcOpenFileRaw function to open the file. The attacker then races to replace the hard link with a symbolic link that points to the target file. This allows the attacker to impersonate the owner of the file and gain elevated privileges.

The business value of this technique is that it allows an attacker to gain elevated privileges on a target system, which can then be used to perform further malicious activities such as data exfiltration or installing backdoors.

## Requirements

1. Access to the target system

1. Ability to compile and execute the EFSPotato code

1. Administrator or SYSTEM privileges on the target system

## Defense

1. Apply the latest security patches to the target system to mitigate the EFSRPC vulnerability

1. Implement the principle of least privilege to restrict the ability of users to escalate privileges

1. Monitor the system for any suspicious activity, such as the creation of hard links or the execution of unknown binaries

## Objectives

1. Gain elevated privileges on the target system

1. Bypass User Account Control (UAC)

1. Achieve persistence on the target system

# Instructions

1. Compile EfsPotato.cs using .NET 4.x or .NET 2.0/3.5

**Code**: [[# .NET 4.x
csc EfsPotato.cs
csc /platform:x86 EfsP]]

> The EfsPotato Compilation Command provides instructions to compile EfsPotato.cs using .NET 4.x or .NET 2.0/3.5. The command can be executed in PowerShell. The command includes multiple commands for compiling EfsPotato.cs with different platforms. Users can choose the appropriate command based on their requirements. The instructions are provided in the 'instruction' field and the arguments of the command are explained in detail in the 'explain' field.

**Command** ([[Compile EfsPotato.cs with .NET 4.x]]):

```bash
csc EfsPotato.cs
csc /platform:x86 EfsPotato.cs
```

**Command** ([[Compile EfsPotato.cs with .NET 2.0/3.5]]):

```bash
C:\Windows\Microsoft.Net\Framework\V3.5\csc.exe EfsPotato.cs
C:\Windows\Microsoft.Net\Framework\V3.5\csc.exe /platform:x86 EfsPotato.cs
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]

### Sub-Techniques

- [[Bypass User Account Control|T1548.002 - Bypass User Account Control]]

## Commands Used

- [[Compile EfsPotato.cs with .NET 2.0/3.5]]
- [[Compile EfsPotato.cs with .NET 4.x]]

## Tags

- [[EFSPotato (MS-EFSR EfsRpcOpenFileRaw)]]
- [[EoP - Impersonation Privileges]]
- [[Windows - Privilege Escalation]]
