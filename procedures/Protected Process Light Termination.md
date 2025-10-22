---
id: 08207f16-8216-4efa-9c25-589e8798f0b5
name: Protected Process Light Termination
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.597041+00:00'
updated_at: '2023-04-10T20:37:03.700126+00:00'
tags:
- '[[Protected Process Light]]'
- '[[Windows - Defenses]]'
commands:
- '[[Kill MsMpEng.exe process]]'
---

# Protected Process Light Termination

## Summary

This procedure is used to bypass Windows Defender's Protected Process Light (PPL) feature, which is designed to prevent unauthorized access to critical system processes. By terminating the Microsoft Defender process, an attacker can disable PPL and gain access to the LSASS process, which contains s

## Description

# Description

This procedure is used to bypass Windows Defender's Protected Process Light (PPL) feature, which is designed to prevent unauthorized access to critical system processes. By terminating the Microsoft Defender process, an attacker can disable PPL and gain access to the LSASS process, which contains sensitive information such as passwords. This technique can be used as part of a larger attack chain to gain access to a target's network and exfiltrate sensitive data.

Technical Explanation: Protected Process Light is a security feature in Windows Defender that prevents unauthorized access to critical system processes. By default, PPL is enabled for the LSASS process, which contains sensitive information such as passwords. However, PPL can be bypassed by terminating the Microsoft Defender process, which disables the PPL feature for LSASS.

Business Value: This technique can be used by attackers to gain access to sensitive information such as passwords, which can be used to further compromise a target's network and exfiltrate valuable data.

## Requirements

1. Administrator-level access

1. Ability to terminate Microsoft Defender process

## Defense

1. Ensure that all systems have up-to-date security patches installed

1. Implement strong password policies and multi-factor authentication

1. Use endpoint detection and response (EDR) tools to monitor for suspicious activity

## Objectives

1. Gain access to sensitive information such as passwords

1. Bypass Windows Defender's Protected Process Light feature

# Instructions

1. This command is used to check if LSASS (Local Security Authority Subsystem Service) is running in PPL (Protected Process Light) mode. PPL is a security feature that isolates certain critical system processes to prevent tampering and exploitation by malicious software. To run this command, open PowerShell and type the command as it appears in the 'data' field.

**Code**: [[reg query HKEY_LOCAL_MACHINE\SYSTEM\CurrentControl]]

> The command queries the Windows registry for the 'RunAsPPL' value under the 'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa' key. If the value is set to '1', LSASS is running in PPL mode. If the value is set to '0' or the value does not exist, LSASS is not running in PPL mode.

2. Use this command to terminate the Microsoft Defender process.

**Code**: [[taskkill /f /im MsMpEng.exe
ERROR: The process "Ms]]

> The 'taskkill' command is used to terminate a process by its name or process ID (PID). The '/f' parameter is used to forcefully terminate the process. The '/im' parameter followed by the process name 'MsMpEng.exe' specifies the process to be terminated. However, in this case, the process is a protected process and cannot be terminated even with Administrator privilege. This command can be used as an example to demonstrate that some processes are protected and cannot be terminated through normal means.

**Command** ([[Kill MsMpEng.exe process]]):

```bash
taskkill /f /im MsMpEng.exe
```

## Commands Used

- [[Kill MsMpEng.exe process]]

## Tags

- [[Protected Process Light]]
- [[Windows - Defenses]]
