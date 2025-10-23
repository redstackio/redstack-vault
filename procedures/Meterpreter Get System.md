---
id: af9684d2-0eef-454c-8612-cb8ed4126960
name: Meterpreter Get System
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.371881+00:00'
updated_at: '2023-04-10T20:25:01.583917+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[Bypass User Account Control|T1088 - Bypass User Account Control]]'
tags:
- '[[Get System]]'
- '[[Metasploit]]'
- '[[Meterpreter - Basic]]'
commands:
- '[[Get Server User]]'
- '[[System Access via Named Pipe Impersonation]]'
---

# Meterpreter Get System

## Summary

Meterpreter is a powerful tool in the Metasploit framework that allows an attacker to control a compromised system. The 'Get System' command is used to escalate privileges on the target system. With this command, an attacker can obtain the highest level of privileges on the system, which allows the

## Description

# Description

Meterpreter is a powerful tool in the Metasploit framework that allows an attacker to control a compromised system. The 'Get System' command is used to escalate privileges on the target system. With this command, an attacker can obtain the highest level of privileges on the system, which allows them to perform any action on the target machine. This technique is commonly used to gain persistence and maintain access to the target system. The business value of this attack is that an attacker can maintain access to the target system for an extended period of time, potentially leading to data theft or other malicious activities.

 

## Requirements

1. Access to the target system

1. Meterpreter installed on the attacker's machine

 

## Defense

1. Implement the principle of least privilege to limit the privileges of user accounts

1. Use multi-factor authentication to prevent unauthorized access to sensitive systems

1. Regularly monitor and review system logs for suspicious activity

 

## Objectives

1. Escalate privileges on the target system

1. Gain persistence on the target system

1. Maintain access to the target system

 

# Instructions

1. The `getsystem` command is used to elevate the privileges of the current session to that of the local system. The `getuid` command is used to retrieve the user ID of the current session. These commands are commonly used in post-exploitation scenarios where the attacker has already gained access to a system and is looking to escalate their privileges and gather information about the system.

 



**Code**: [[meterpreter > getsystem
...got system via techniqu]]



> The `getsystem` command has no arguments. The `getuid` command also has no arguments. Both commands are executed within the Meterpreter shell, which is a post-exploitation tool used by attackers to interact with compromised systems. The `getsystem` command uses a variety of techniques to elevate privileges, including named pipe impersonation, token manipulation, and DLL injection. The `getuid` command simply retrieves the user ID of the current session, which can be useful for identifying the level of access that the attacker has on the compromised system.



**Command** ([[System Access via Named Pipe Impersonation]]):

```bash
getsystem
```





**Command** ([[Get Server User]]):

```bash
getuid
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[Bypass User Account Control|T1088 - Bypass User Account Control]]

## Commands Used

- [[Get Server User]]
- [[System Access via Named Pipe Impersonation]]

## Tags

- [[Get System]]
- [[Metasploit]]
- [[Meterpreter - Basic]]


