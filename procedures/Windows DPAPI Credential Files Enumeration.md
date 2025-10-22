---
id: 5383396c-195b-4763-baf4-5df3f46e2e71
name: Windows DPAPI Credential Files Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.251487+00:00'
updated_at: '2023-04-10T20:37:12.134637+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Data Protection API]]'
- '[[List Credential Files]]'
- '[[Windows - DPAPI]]'
commands:
- '[[List All Hidden Files and Directories in Microsoft Credentials Folder]]'
- '[[List Hidden Files and Directories in Microsoft Credentials Folder]]'
---

# Windows DPAPI Credential Files Enumeration

## Summary

The Windows Data Protection API (DPAPI) provides a way for software to securely store and retrieve data by using encryption. However, if an attacker gains access to a system, they can use DPAPI to enumerate and extract sensitive information such as credentials stored on the system. This procedure a

## Description

# Description

The Windows Data Protection API (DPAPI) provides a way for software to securely store and retrieve data by using encryption. However, if an attacker gains access to a system, they can use DPAPI to enumerate and extract sensitive information such as credentials stored on the system. This procedure aims to list credential files that can be used for further attacks. 

Technical Description: DPAPI uses a user's logon credentials to encrypt and decrypt data. The DPAPI system is based on two keys, one is stored in the user's profile and the other is stored in the system's Local Security Authority (LSA) process. The LSA key is protected by the user's logon credentials and is only accessible to the LSA process. When a user logs on, DPAPI uses the user's logon credentials to decrypt the user's profile key, which is then used to encrypt and decrypt data. 

Business Value: By obtaining credentials stored on a system, an attacker can gain access to other resources on the network, such as email accounts, sensitive data or other systems that the compromised user has access to. This can lead to data theft, unauthorized access and privilege escalation.

## Requirements

1. Authenticated access to the target system

1. Administrator or SYSTEM level privileges

1. Command-line tools such as Powershell or Mimikatz

## Defense

1. Implement strong password policies and multi-factor authentication to reduce the risk of credential theft

1. Restrict access to the DPAPI system to authorized users and applications

1. Monitor and analyze system logs for suspicious activity, such as failed logon attempts or unusual network traffic

## Objectives

1. List credential files on the target system

1. Obtain sensitive information such as usernames and passwords

# Instructions

1. This command will list all the Microsoft credentials stored locally and in roaming directory. It will also get the child items in the hidden directory of Microsoft credentials.

**Code**: [[dir /a:h C:\Users\username\AppData\Local\Microsoft]]

> The 'dir' command is used to list the directories and files in the specified path. The '/a:h' argument is used to show only hidden files and directories. The 'Get-ChildItem' command is used to retrieve the child items in the specified path. The '-Hidden' argument is used to show only hidden items.

**Command** ([[List Hidden Files and Directories in Microsoft Credentials Folder]]):

```bash
dir /a:h C:\Users\username\AppData\Local\Microsoft\Credentials\
dir /a:h C:\Users\username\AppData\Roaming\Microsoft\Credentials\

```

**Command** ([[List All Hidden Files and Directories in Microsoft Credentials Folder]]):

```bash
Get-ChildItem -Hidden C:\Users\username\AppData\Local\Microsoft\Credentials\
Get-ChildItem -Hidden C:\Users\username\AppData\Roaming\Microsoft\Credentials\
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[List All Hidden Files and Directories in Microsoft Credentials Folder]]
- [[List Hidden Files and Directories in Microsoft Credentials Folder]]

## Tags

- [[Data Protection API]]
- [[List Credential Files]]
- [[Windows - DPAPI]]
