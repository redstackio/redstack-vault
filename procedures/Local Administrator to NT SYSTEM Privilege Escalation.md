---
id: aa40cb8a-37b6-4f22-8b6b-a52efdfe3bf3
name: Local Administrator to NT SYSTEM Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.047361+00:00'
updated_at: '2023-04-10T20:37:35.513309+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[Bypass User Account Control|T1088 - Bypass User Account Control]]'
tags:
- '[[EoP - From local administrator to NT SYSTEM]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Open interactive command prompt as SYSTEM]]'
---

# Local Administrator to NT SYSTEM Privilege Escalation

## Summary

This procedure is used to escalate privileges from a local administrator account to the NT SYSTEM account, which has the highest level of privileges on a Windows machine. This technique can be used by attackers to gain full control of the target system and perform any action they wish. To accomplis

## Description

# Description

This procedure is used to escalate privileges from a local administrator account to the NT SYSTEM account, which has the highest level of privileges on a Windows machine. This technique can be used by attackers to gain full control of the target system and perform any action they wish. To accomplish this, the attacker first needs to gain access to a local administrator account on the target system. Then, they can use the 'Run Command as System User' command to execute commands as the NT SYSTEM account, effectively bypassing any restrictions and gaining full control of the system. This technique is particularly useful for attackers who want to maintain persistence on a compromised system, as the NT SYSTEM account is not subject to password expiration policies and is not easily detectable by security tools.

## Requirements

1. Access to a local administrator account on the target system

1. Ability to execute commands on the target system

## Defense

1. Limit the number of local administrator accounts on Windows systems

1. Implement least privilege policies to restrict access to sensitive system functions

1. Monitor for suspicious activity, such as unusual command execution or privilege escalation

## Objectives

1. Escalate privileges from a local administrator account to the NT SYSTEM account

1. Maintain persistence on a compromised system

# Instructions

1. To run a command as a system user, use PsExec.exe with the -i and -s flags followed by the command you want to run.

**Code**: [[PsExec.exe -i -s cmd.exe]]

> -i: Runs the program so that it interacts with the desktop of the session specified by session ID.
-s: Runs the remote process in the System account.

**Command** ([[Open interactive command prompt as SYSTEM]]):

```bash
PsExec.exe -i -s cmd.exe
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[Bypass User Account Control|T1088 - Bypass User Account Control]]

## Commands Used

- [[Open interactive command prompt as SYSTEM]]

## Tags

- [[EoP - From local administrator to NT SYSTEM]]
- [[Windows - Privilege Escalation]]
