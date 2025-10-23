---
id: eb683f57-96b0-4a83-a7b7-5b34e26787bb
name: Windows - EoP Privileged File Write via DiagHub Standard Collector Service
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.301278+00:00'
updated_at: '2023-04-10T20:37:35.922113+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
sub_techniques:
- '[[Bypass User Account Control|T1548.002 - Bypass User Account Control]]'
tags:
- '[[DiagHub]]'
- '[[EoP - Privileged File Write]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Check System32 Directory]]'
---

# Windows - EoP Privileged File Write via DiagHub Standard Collector Service

## Summary

This procedure exploits a vulnerability in the DiagHub Standard Collector Service to escalate privileges and gain access to sensitive files. The DiagHub Standard Collector Service is a legitimate Windows service that is used to collect diagnostic information. By abusing the service, an attacker can

## Description

# Description

This procedure exploits a vulnerability in the DiagHub Standard Collector Service to escalate privileges and gain access to sensitive files. The DiagHub Standard Collector Service is a legitimate Windows service that is used to collect diagnostic information. By abusing the service, an attacker can write to sensitive files that would normally require elevated privileges.

To execute this attack, the attacker must first gain access to the target system and then execute the DiagHub Standard Collector Service command. Once executed, the attacker can use the service to write to sensitive files, such as system binaries or configuration files. This can allow the attacker to escalate privileges and gain access to sensitive information.

This procedure can be used by attackers to gain access to sensitive information or perform other malicious activities.

 

## Requirements

1. Access to the target system

1. Execution of the DiagHub Standard Collector Service command

 

## Defense

1. Ensure that all systems are patched and up-to-date to prevent exploitation of known vulnerabilities

1. Monitor for suspicious activity, such as unexpected changes to system files or the execution of suspicious commands

1. Implement the principle of least privilege to limit the impact of privilege escalation attacks

 

## Objectives

1. Escalate privileges on the target system

1. Gain access to sensitive files and information

 

# Instructions

1. To manage the DiagHub service, you can use the 'sc' command in the Command Prompt. For example, to start the service, run 'sc start DiagHub' and to stop the service, run 'sc stop DiagHub'.

 



**Code**: [[C:\Windows\System32]]



> The 'sc' command is used to communicate with the Service Control Manager and services. The 'start' and 'stop' arguments are used to respectively start and stop the DiagHub service. Note that administrative privileges are required to run these commands.



**Command** ([[Check System32 Directory]]):

```bash
C:\Windows\System32
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

- [[Check System32 Directory]]

## Tags

- [[DiagHub]]
- [[EoP - Privileged File Write]]
- [[Windows - Privilege Escalation]]


