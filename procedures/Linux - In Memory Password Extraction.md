---
id: 98f05350-7204-4903-8196-940198f55651
name: Linux - In Memory Password Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.540878+00:00'
updated_at: '2023-04-10T20:34:24.371838+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[In memory passwords]]'
- '[[Linux - Privilege Escalation]]'
- '[[Looting for passwords]]'
---

# Linux - In Memory Password Extraction

## Summary

Linux systems store passwords in memory while they are in use. Attackers can extract these passwords from memory and use them to escalate privileges or move laterally within a network. This procedure focuses on extracting passwords from memory on Linux systems. By searching for passwords in memory,

## Description

# Description

Linux systems store passwords in memory while they are in use. Attackers can extract these passwords from memory and use them to escalate privileges or move laterally within a network. This procedure focuses on extracting passwords from memory on Linux systems. By searching for passwords in memory, an attacker can gain access to sensitive information and perform actions that would otherwise require elevated privileges. This procedure can be used as part of a larger attack or as a standalone technique.

 

## Requirements

1. Access to a Linux system

1. Ability to run commands on the system

 

## Defense

1. Implement strong password policies to make it more difficult for attackers to extract passwords from memory

1. Use anti-virus and anti-malware software to detect and prevent attacks that attempt to extract passwords from memory

1. Monitor system logs for suspicious activity, such as attempts to extract passwords from memory

 

## Objectives

1. Extract passwords from memory on Linux systems

1. Escalate privileges or move laterally within a network

 

# Instructions

1. Use the 'strings' command to search for printable strings in memory. The '-n10' option limits the output to the first 10 characters of each string. The output is then piped to the 'grep' command to search for the case-insensitive string 'PASS'.

 



**Code**: [[strings /dev/mem -n10 | grep -i PASS]]



> This command can be useful for identifying passwords or other sensitive information that may be stored in memory. However, it should be noted that accessing memory in this way can be risky and may cause system instability or crashes.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Tags

- [[In memory passwords]]
- [[Linux - Privilege Escalation]]
- [[Looting for passwords]]


