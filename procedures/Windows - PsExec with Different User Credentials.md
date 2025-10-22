---
id: a70607d6-b605-45ed-9b69-b9c00459c3d4
name: Windows - PsExec with Different User Credentials
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.317463+00:00'
updated_at: '2023-04-10T20:37:57.510632+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Scheduled Task|T1053 - Scheduled Task]]'
- '[[Valid Accounts|T1078 - Valid Accounts]]'
tags:
- '[[Other methods]]'
- '[[PsExec - Sysinternal]]'
- '[[Windows - Using credentials]]'
commands:
- '[[Switch to NT Authority/System on srv01.domain.local]]'
---

# Windows - PsExec with Different User Credentials

## Summary

This procedure involves using PsExec, a Sysinternal tool, to execute a command as a different user and switch to the system account. This can be useful for lateral movement within a network or for privilege escalation. PsExec is a legitimate tool used by system administrators, but can also be used 

## Description

# Description

This procedure involves using PsExec, a Sysinternal tool, to execute a command as a different user and switch to the system account. This can be useful for lateral movement within a network or for privilege escalation. PsExec is a legitimate tool used by system administrators, but can also be used maliciously by attackers who have obtained valid credentials. By using PsExec with different user credentials, an attacker can execute commands on a remote system with elevated privileges, allowing them to move laterally within the network or escalate privileges. The business value of this procedure is that it allows an attacker to gain access to sensitive information and systems, potentially leading to data theft or disruption of operations.

## Requirements

1. Valid credentials for a user with administrative privileges on the target system

1. Access to the network where the target system is located

1. PsExec tool

## Defense

1. Implement strong password policies and multi-factor authentication to prevent attackers from obtaining valid credentials

1. Monitor for suspicious activity, such as unusual logins or use of PsExec

1. Restrict access to sensitive systems and information to limit the impact of a potential attack

## Objectives

1. Execute a command as a different user with elevated privileges

1. Move laterally within a network

1. Escalate privileges

# Instructions

1. To execute a command as a different user and switch to the system account, use the PsExec.exe tool with the following command:

PsExec.exe \\server -u domain\username -p password cmd.exe -s

Replace 'server', 'domain', 'username', and 'password' with the appropriate values for your environment. The '-s' argument switches the user context to the local system account.

**Code**: [[PS C:\> PsExec.exe  \\srv01.domain.local -u DOMAIN]]

> This command allows you to execute a command on a remote server as a different user and switch to the system account. This can be useful for performing administrative tasks that require elevated privileges. The PsExec.exe tool is part of the Sysinternals suite of tools and can be downloaded from Microsoft's website. The '-u' argument specifies the user account to use for the remote connection, '-p' specifies the password for the user account, and 'cmd.exe' specifies the command to execute on the remote server. The '-s' argument switches the user context to the local system account, which can be useful for performing tasks that require elevated privileges.

**Command** ([[Switch to NT Authority/System on srv01.domain.local]]):

```bash
PsExec.exe \\srv01.domain.local -u DOMAIN\username -p password cmd.exe -s
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Scheduled Task|T1053 - Scheduled Task]]
- [[Valid Accounts|T1078 - Valid Accounts]]

## Commands Used

- [[Switch to NT Authority/System on srv01.domain.local]]

## Tags

- [[Other methods]]
- [[PsExec - Sysinternal]]
- [[Windows - Using credentials]]
