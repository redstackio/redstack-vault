---
id: b1d886e8-59eb-494b-85ce-227135b7797e
name: MS11-080 AFD JoinLeaf Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.445225+00:00'
updated_at: '2023-04-10T20:37:43.835338+00:00'
tactics:
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
tags:
- '[[EoP - Common Vulnerabilities and Exposure]]'
- '[[MS11-080 (afd.sys) - Microsoft Windows XP/2003]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Download Exploit]]'
- '[[Use Metasploit Framework]]'
---

# MS11-080 AFD JoinLeaf Privilege Escalation

## Summary

MS11-080 is a privilege escalation vulnerability that exists in the way the Windows kernel-mode driver (afd.sys) handles certain IOCTL requests. An attacker with limited privileges can exploit this vulnerability to elevate their privileges on a target system. This vulnerability affects Microsoft Wi

## Description

# Description

MS11-080 is a privilege escalation vulnerability that exists in the way the Windows kernel-mode driver (afd.sys) handles certain IOCTL requests. An attacker with limited privileges can exploit this vulnerability to elevate their privileges on a target system. This vulnerability affects Microsoft Windows XP and Windows Server 2003.

To exploit this vulnerability, an attacker would need to execute code on a target system. There are several publicly available exploits that can be used to achieve this. Once the attacker has executed code on the target system, they can use MS11-080 to elevate their privileges to gain full control of the system.

This procedure can be used by an attacker to gain full control of a target system by exploiting a known vulnerability in a Windows kernel-mode driver. The business value of this procedure is that it allows an attacker to gain access to sensitive information or systems that they would not normally have access to.

## Requirements

1. Ability to execute code on a target system

## Defense

1. Apply the latest security patches and updates to all Windows systems

1. Use a host-based intrusion detection system (HIDS) to monitor for suspicious activity on Windows systems

1. Implement least privilege access controls to limit the impact of a successful privilege escalation attack

## Objectives

1. Gain elevated privileges on a target system

1. Gain full control of a target system

# Instructions

1. Use the provided Python or Metasploit exploit to escalate privileges on a Windows system by exploiting the AFD JoinLeaf vulnerability (MS11-080).

**Code**: [[Python: https://www.exploit-db.com/exploits/18176
]]

> This command requires access to the target system and knowledge of the system's vulnerabilities. The Python or Metasploit exploit can be used to gain elevated privileges on the system and potentially gain access to sensitive information or perform malicious actions.

**Command** ([[Download Exploit]]):

```bash
Python: https://www.exploit-db.com/exploits/18176
```

**Command** ([[Use Metasploit Framework]]):

```bash
exploit/windows/local/ms11_080_afdjoinleaf
```

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]

## Commands Used

- [[Download Exploit]]
- [[Use Metasploit Framework]]

## Tags

- [[EoP - Common Vulnerabilities and Exposure]]
- [[MS11-080 (afd.sys) - Microsoft Windows XP/2003]]
- [[Windows - Privilege Escalation]]
