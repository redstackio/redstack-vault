---
id: 2492177b-707f-4d70-9e06-992f79543cb1
name: Windows Privilege Escalation - Evaluating Vulnerable Drivers
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:29.805756+00:00'
updated_at: '2023-04-10T20:37:50.319089+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
tags:
- '[[EoP - Evaluating Vulnerable Drivers]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Enumerating driver services and checking file signatures]]'
- '[[Listing all drivers installed on the system]]'
---

# Windows Privilege Escalation - Evaluating Vulnerable Drivers

## Summary

The Windows Privilege Escalation - Evaluating Vulnerable Drivers procedure involves identifying vulnerable drivers that can be exploited to escalate privileges on a Windows machine. This technique can be used by attackers to gain access to sensitive information or perform malicious actions on the c

## Description

# Description

The Windows Privilege Escalation - Evaluating Vulnerable Drivers procedure involves identifying vulnerable drivers that can be exploited to escalate privileges on a Windows machine. This technique can be used by attackers to gain access to sensitive information or perform malicious actions on the compromised system.

To perform this procedure, the attacker must first enumerate the drivers installed on the system using the 'Windows Driver Enumeration' command. The attacker can then analyze the drivers to identify any vulnerabilities that can be exploited to escalate privileges.

This procedure can be valuable for attackers who have already gained access to a system with low privileges and are looking to escalate their privileges to gain access to sensitive information or perform malicious actions.

## Requirements

1. Access to a Windows machine with low privileges

1. Ability to execute the 'Windows Driver Enumeration' command

## Defense

1. Regularly update and patch drivers to mitigate vulnerabilities

1. Implement the principle of least privilege to limit the impact of privilege escalation attacks

1. Use intrusion detection and prevention systems to detect and prevent privilege escalation attacks

## Objectives

1. Identify vulnerable drivers that can be exploited for privilege escalation

1. Escalate privileges on a compromised Windows system

# Instructions

1. Use the driverquery.exe tool to list all installed drivers on the system. Use the --no-msft option to exclude Microsoft drivers. Check the file signatures of the drivers to identify any malicious drivers.

**Code**: [[# Native binary
PS C:\Users\Swissky> driverquery.e]]

> The 'driverquery.exe' tool is a built-in Windows utility that allows users to view a list of all installed drivers on the system. By default, it displays the module name, display name, driver type, and link date of each driver. The '--no-msft' option can be used to exclude Microsoft drivers from the list. Checking the file signatures of the drivers can help identify any malicious drivers that may have been installed on the system. This technique can be useful for identifying rootkits and other types of malware that use kernel-level drivers to hide their presence on the system.

**Command** ([[Enumerating driver services and checking file signatures]]):

```bash
DriverQuery.exe --no-msft
```

**Command** ([[Listing all drivers installed on the system]]):

```bash
driverquery.exe /fo table /si
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]

## Commands Used

- [[Enumerating driver services and checking file signatures]]
- [[Listing all drivers installed on the system]]

## Tags

- [[EoP - Evaluating Vulnerable Drivers]]
- [[Windows - Privilege Escalation]]
