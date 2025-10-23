---
id: 9fd32b3d-3960-496b-bed5-fec0b9537c52
name: Windows Defender Application Control Device Guard Configuration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.666788+00:00'
updated_at: '2023-04-10T20:37:05.615899+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Code Signing|T1116 - Code Signing]]'
- '[[Group Policy Modification|T1484 - Group Policy Modification]]'
tags:
- '[[Windows Defender Application Control]]'
- '[[Windows - Defenses]]'
---

# Windows Defender Application Control Device Guard Configuration

## Summary

Windows Defender Application Control Device Guard Configuration is a security feature in Windows that allows administrators to control which applications are allowed to run on a system. It uses code signing and application control to ensure that only trusted applications are allowed to run. This fe

## Description

# Description

Windows Defender Application Control Device Guard Configuration is a security feature in Windows that allows administrators to control which applications are allowed to run on a system. It uses code signing and application control to ensure that only trusted applications are allowed to run. This feature is particularly useful for protecting against malware and other types of attacks that rely on the execution of untrusted code on a system. By limiting the applications that are allowed to run, administrators can reduce the attack surface of a system and make it more difficult for attackers to carry out their objectives.

From a technical standpoint, Device Guard Configuration works by creating a policy that specifies which applications are allowed to run on a system. This policy is enforced by the Windows operating system, which checks the digital signature of each application that attempts to run. If the application is not on the allowed list, it will be blocked from running. This feature is available on Windows 10 Enterprise and Windows Server 2016 and later.

From a business perspective, Device Guard Configuration can help organizations protect their systems and data from cyber attacks. By limiting the applications that are allowed to run, organizations can reduce the risk of malware infections, data breaches, and other types of attacks that rely on the execution of untrusted code. This can help organizations avoid costly downtime, reputational damage, and legal liabilities.

 

## Requirements

1. Windows 10 Enterprise or Windows Server 2016 or later

1. Administrator privileges

 

## Defense

1. Ensure that only trusted applications are allowed to run by configuring Device Guard Configuration policies.

1. Regularly update the allowed list of applications to ensure that only the latest versions of trusted applications are allowed to run.

1. Monitor and analyze system logs to detect any attempts to run untrusted applications.

 

## Objectives

1. To limit the applications that are allowed to run on a system.

1. To reduce the attack surface of a system.

1. To protect against malware and other types of attacks that rely on the execution of untrusted code.

 

# Instructions

1. Use this command to configure Device Guard on Windows 10 devices.

 



**Code**: [[WDAC/UMCI/Device Guard]]



> Device Guard is a set of hardware and software security features that are available on Windows 10 Enterprise and Windows Server 2016. It is designed to prevent malware and untrusted code from running on a device by ensuring that only trusted applications are allowed to run. To configure Device Guard, you can use the WDAC (Windows Defender Application Control) or UMCI (User Mode Code Integrity) features. The WDAC feature allows you to create code integrity policies that define which applications are allowed to run on a device, while the UMCI feature enforces the code integrity policies by blocking any applications that are not on the allowed list. This command provides a convenient way to configure Device Guard on a Windows 10 device by providing multiple commands that can be used to create and manage code integrity policies, enable or disable UMCI, and view the status of Device Guard.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Code Signing|T1116 - Code Signing]]
- [[Group Policy Modification|T1484 - Group Policy Modification]]

## Tags

- [[Windows Defender Application Control]]
- [[Windows - Defenses]]


