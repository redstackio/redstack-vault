---
id: be08493b-0e97-4fc6-a572-eeb0cc10c467
name: MS16-032 Local Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.497881+00:00'
updated_at: '2023-04-10T20:37:46.934318+00:00'
tactics:
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
tags:
- '[[EoP - Common Vulnerabilities and Exposure]]'
- '[[MS16-032 - Microsoft Windows 7 < 10 / 2008 < 2012 R2 (x86/x64)]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Download binary exe]]'
- '[[Download PowerShell script]]'
- '[[Use Metasploit exploit]]'
---

# MS16-032 Local Privilege Escalation

## Summary

MS16-032 is a local privilege escalation vulnerability that exists in the Windows kernel-mode driver (Win32k.sys) due to improper handling of objects in memory. An attacker can exploit this vulnerability by running a specially crafted application to take control of an affected system. Successful ex

## Description

# Description

MS16-032 is a local privilege escalation vulnerability that exists in the Windows kernel-mode driver (Win32k.sys) due to improper handling of objects in memory. An attacker can exploit this vulnerability by running a specially crafted application to take control of an affected system. Successful exploitation of this vulnerability can lead to complete compromise of the affected system.

Technical Explanation: The vulnerability exists due to a flaw in the way the Windows kernel-mode driver handles objects in memory. An attacker can exploit this vulnerability by running a specially crafted application to take control of an affected system. Successful exploitation of this vulnerability can lead to complete compromise of the affected system.

Business Value: This procedure allows an attacker to escalate privileges on a Windows system, potentially leading to complete compromise of the affected system. This can be used to gain access to sensitive information, steal data, or carry out further attacks.

## Requirements

1. Access to an affected Windows system

## Defense

1. Ensure that all Windows systems are up-to-date with the latest security patches

1. Implement the principle of least privilege to limit the damage that can be caused by a compromised account

1. Monitor for suspicious activity on Windows systems, such as attempts to exploit this vulnerability

## Objectives

1. Escalate privileges on a Windows system

# Instructions

1. This command checks if the Windows Update KB3139914 is installed on the system.

**Code**: [[wmic qfe list | findstr &quot;3139914&quot;]]

> The 'wmic qfe list' command lists all installed Windows updates and the 'findstr &quot;3139914&quot;' command searches for the specific update KB3139914. If the update is installed, the command will return information about it, otherwise it will return nothing.

2. This command will exploit the MS16-032 vulnerability in Windows to escalate local privileges. The command can be executed in Powershell using the provided script or binary executable. The Metasploit module is also available for this exploit.

**Code**: [[Powershell:
https://www.exploit-db.com/exploits/39]]

> The MS16-032 vulnerability allows an attacker to elevate their privileges on a Windows system by exploiting the Secondary Logon Service. The vulnerability can be exploited locally by an attacker with low privileges. The exploit works by creating a malicious process that inherits the Secondary Logon Service's access token, which has elevated privileges. The attacker can then use this process to execute arbitrary code with elevated privileges.

**Command** ([[Download PowerShell script]]):

```powershell
https://github.com/FuzzySecurity/PowerShell-Suite/blob/master/Invoke-MS16-032.ps1
```

**Command** ([[Download binary exe]]):

```bash
https://github.com/Meatballs1/ms16-032
```

**Command** ([[Use Metasploit exploit]]):

```bash
exploit/windows/local/ms16_032_secondary_logon_handle_privesc
```

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]

## Commands Used

- [[Download binary exe]]
- [[Download PowerShell script]]
- [[Use Metasploit exploit]]

## Tags

- [[EoP - Common Vulnerabilities and Exposure]]
- [[MS16-032 - Microsoft Windows 7 < 10 / 2008 < 2012 R2 (x86/x64)]]
- [[Windows - Privilege Escalation]]
