---
id: a303bad0-2fb6-4afc-bf7b-0c79383e5216
name: KiTrap0D Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.418151+00:00'
updated_at: '2023-04-10T20:37:33.719970+00:00'
tactics:
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
tags:
- '[[EoP - Common Vulnerabilities and Exposure]]'
- '[[MS10-015 (KiTrap0D) - Microsoft Windows NT/2000/2003/2008/XP/Vista/7]]'
- '[[Windows - Privilege Escalation]]'
---

# KiTrap0D Privilege Escalation

## Summary

KiTrap0D Privilege Escalation is a technique that abuses the Windows kernel to escalate privileges from a low-privileged user to SYSTEM. The attack involves exploiting a vulnerability in the KiTrap0D system call handler in the Windows kernel. An attacker can use this vulnerability to execute arbitr

## Description

# Description

KiTrap0D Privilege Escalation is a technique that abuses the Windows kernel to escalate privileges from a low-privileged user to SYSTEM. The attack involves exploiting a vulnerability in the KiTrap0D system call handler in the Windows kernel. An attacker can use this vulnerability to execute arbitrary code in kernel mode and gain elevated privileges. This technique can be used to bypass access controls, install persistent malware, or perform other malicious activities.

## Requirements

1. Access to a vulnerable Windows system

1. Ability to execute the MS10-015 KiTrap0D exploit

## Defense

1. Apply security patches and updates to vulnerable systems

1. Implement least privilege access controls to limit the impact of privilege escalation attacks

1. Monitor for suspicious activity and kernel-level events

## Objectives

1. Gain elevated privileges from a low-privileged user account

1. Bypass access controls and perform malicious activities

# Instructions

1. To use this exploit, first download it from the provided link. Then, open Metasploit and load the exploit using the command 'use exploit/windows/local/ms10_015_kitrap0d'. Set the required options using the 'set' command, such as the target system and payload. Finally, execute the exploit using the 'exploit' command.

**Code**: [[https://www.exploit-db.com/exploits/11199

Metaspl]]

> This exploit takes advantage of a vulnerability in the KiTrap0D system call of Windows, allowing an attacker to escalate their privileges from user mode to kernel mode. This can be used to gain full control of the system. The exploit is specific to the MS10-015 security update, which was released in 2010.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]

## Tags

- [[EoP - Common Vulnerabilities and Exposure]]
- [[MS10-015 (KiTrap0D) - Microsoft Windows NT/2000/2003/2008/XP/Vista/7]]
- [[Windows - Privilege Escalation]]
