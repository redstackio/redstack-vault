---
id: 25dba789-1058-4247-82b4-bf20671e0afb
name: JEA for Limiting PowerShell Usage
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.436581+00:00'
updated_at: '2023-04-10T20:37:06.712732+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
sub_techniques:
- '[[Bypass User Account Control|T1548.002 - Bypass User Account Control]]'
tags:
- '[[Just Enough Administration]]'
- '[[Powershell]]'
- '[[Windows - Defenses]]'
commands:
- '[[Add computer to domain]]'
- '[[Create a new Windows Service]]'
- '[[Create new PowerShell Session Configuration]]'
- '[[Start a new process]]'
---

# JEA for Limiting PowerShell Usage

## Summary

Just Enough Administration (JEA) is a security technology available in PowerShell that enables administrators to delegate limited administrative access to end-users. This procedure focuses on using JEA to limit PowerShell usage to only non-default cmdlets. By doing so, it reduces the attack surface

## Description

# Description

Just Enough Administration (JEA) is a security technology available in PowerShell that enables administrators to delegate limited administrative access to end-users. This procedure focuses on using JEA to limit PowerShell usage to only non-default cmdlets. By doing so, it reduces the attack surface for attackers who may attempt to use PowerShell to execute malicious commands. By limiting the number of cmdlets that users can execute, it also helps to prevent accidental misuse of PowerShell. The technical implementation of this procedure involves creating a JEA endpoint that only allows non-default cmdlets to be executed.

## Requirements

1. Windows Server 2012 or later

1. PowerShell version 5.0 or later

1. Permissions to create JEA endpoints

## Defense

1. Regularly review and update the list of non-default cmdlets allowed in the JEA endpoint

1. Enforce the principle of least privilege by only granting users the necessary permissions to perform their tasks

1. Monitor PowerShell usage for any suspicious activity

## Objectives

1. Limit PowerShell usage to only non-default cmdlets

1. Reduce the attack surface for attackers using PowerShell

1. Prevent accidental misuse of PowerShell

# Instructions

1. Use the following commands to perform advanced actions in PowerShell:

**Code**: [[Set-PSSessionConfiguration
Start-Process
New-Servi]]

> 1. Set-PSSessionConfiguration: This cmdlet allows you to configure session configurations for remote PowerShell sessions.
2. Start-Process: This cmdlet starts one or more processes on the local computer.
3. New-Service: This cmdlet creates a new Windows service.
4. Add-Computer: This cmdlet adds the local computer to a domain or workgroup.

**Command** ([[Create new PowerShell Session Configuration]]):

```bash
Set-PSSessionConfiguration
```

**Command** ([[Start a new process]]):

```bash
Start-Process
```

**Command** ([[Create a new Windows Service]]):

```bash
New-Service
```

**Command** ([[Add computer to domain]]):

```bash
Add-Computer
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

- [[Add computer to domain]]
- [[Create a new Windows Service]]
- [[Create new PowerShell Session Configuration]]
- [[Start a new process]]

## Tags

- [[Just Enough Administration]]
- [[Powershell]]
- [[Windows - Defenses]]
