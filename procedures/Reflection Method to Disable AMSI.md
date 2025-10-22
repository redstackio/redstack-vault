---
id: ca78687e-2495-4336-9cf1-6f08621eb67f
name: Reflection Method to Disable AMSI
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.004051+00:00'
updated_at: '2023-04-10T20:36:19.006499+00:00'
tags:
- '[[Using Matt Graebers Reflection method]]'
commands:
- '[[Set AmsiInitFailed to true]]'
---

# Reflection Method to Disable AMSI

## Summary

The Reflection method is used to disable the Antimalware Scan Interface (AMSI), which is a Windows feature that allows applications and services to integrate with any installed antivirus software. By disabling AMSI, attackers can bypass antivirus detection and execute malicious code without being d

## Description

# Description

The Reflection method is used to disable the Antimalware Scan Interface (AMSI), which is a Windows feature that allows applications and services to integrate with any installed antivirus software. By disabling AMSI, attackers can bypass antivirus detection and execute malicious code without being detected. This technique is commonly used by attackers to evade detection and gain persistence on a compromised system. The Reflection method works by loading a .NET assembly into memory and invoking its methods using reflection. This allows attackers to bypass the AMSI scan and execute malicious code.

## Requirements

1. Administrator or SYSTEM privileges

1. Access to a .NET assembly

## Defense

1. Ensure that antivirus software is up-to-date and configured to detect and block attempts to disable AMSI

1. Monitor for suspicious activity, such as attempts to load .NET assemblies into memory or invoke methods using reflection

1. Implement least privilege access controls to limit the ability of attackers to escalate privileges and gain access to sensitive systems

## Objectives

1. Disable AMSI to evade detection by antivirus software

1. Execute malicious code without being detected

# Instructions

1. To disable AMSI, execute the following PowerShell command:

**Code**: [[[Ref].Assembly.GetType('System.Management.Automati]]

> This command disables the Antimalware Scan Interface (AMSI) in PowerShell. AMSI is a Microsoft interface that allows antivirus programs to integrate with PowerShell and scan scripts for malicious code. By default, PowerShell 5.0 and later versions have AMSI enabled. Disabling AMSI can bypass antivirus detection and allow execution of potentially malicious scripts.

**Command** ([[Set AmsiInitFailed to true]]):

```bash
[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)
```

## Commands Used

- [[Set AmsiInitFailed to true]]

## Tags

- [[Using Matt Graebers Reflection method]]
