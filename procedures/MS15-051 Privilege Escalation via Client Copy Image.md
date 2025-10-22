---
id: 92b72071-dd70-4209-8103-f7671a5a7656
name: MS15-051 Privilege Escalation via Client Copy Image
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.470851+00:00'
updated_at: '2023-04-10T20:37:38.565433+00:00'
tactics:
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
tags:
- '[[EoP - Common Vulnerabilities and Exposure]]'
- '[[MS15-051 (Client Copy Image) - Microsoft Windows 2003/2008/7/8/2012]]'
- '[[Windows - Privilege Escalation]]'
---

# MS15-051 Privilege Escalation via Client Copy Image

## Summary

MS15-051 is a vulnerability in Microsoft Windows that allows an attacker to escalate privileges on a compromised system. The vulnerability is caused by a flaw in the handling of the Client Copy Image functionality in the Windows kernel. An attacker who successfully exploits this vulnerability could

## Description

# Description

MS15-051 is a vulnerability in Microsoft Windows that allows an attacker to escalate privileges on a compromised system. The vulnerability is caused by a flaw in the handling of the Client Copy Image functionality in the Windows kernel. An attacker who successfully exploits this vulnerability could elevate their privileges from a low-integrity process to that of SYSTEM.

To exploit this vulnerability, an attacker would need to have already compromised the target system and have the ability to execute code on it. Successful exploitation of this vulnerability would allow an attacker to take complete control of the affected system, including installing programs, viewing, changing, or deleting data, and creating new accounts with full user rights.

The business value of this attack is that it allows an attacker to gain full control of a system, potentially allowing them to steal sensitive data or use the system as a foothold to launch further attacks.

## Requirements

1. Access to a vulnerable Windows system

1. Ability to execute code on the target system

## Defense

1. Apply the latest security updates and patches to all Windows systems to prevent exploitation of known vulnerabilities.

1. Implement least privilege access controls to limit the ability of attackers to escalate their privileges.

1. Use endpoint detection and response (EDR) solutions to detect and respond to suspicious activity on endpoints.

## Objectives

1. Escalate privileges on a compromised system from a low-integrity process to that of SYSTEM.

# Instructions

1. Fill in the command details and explain the arguments of the command in detail.

**Code**: [[printf("[#] usage: ms15-051 command \n");
printf("]]

> This command is used to exploit the MS15-051 vulnerability in Windows operating systems. The command takes an argument specifying the action to be performed. For example, 'whoami /all' can be used to display all user and group information for the current user. The command is available in both 32-bit and 64-bit versions, which can be downloaded from the provided links. More information about the exploit can be found at the provided link.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]

## Tags

- [[EoP - Common Vulnerabilities and Exposure]]
- [[MS15-051 (Client Copy Image) - Microsoft Windows 2003/2008/7/8/2012]]
- [[Windows - Privilege Escalation]]
