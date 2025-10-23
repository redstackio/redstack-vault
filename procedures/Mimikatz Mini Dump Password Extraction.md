---
id: 5ff62170-0910-4dbb-8ded-e9e12119dfdb
name: Mimikatz Mini Dump Password Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.220833+00:00'
updated_at: '2023-04-10T20:37:16.909051+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Mini Dump]]'
- '[[Windows - Mimikatz]]'
---

# Mimikatz Mini Dump Password Extraction

## Summary

Mimikatz is a powerful post-exploitation tool that can be used to extract plaintext passwords from memory on a compromised Windows system. This procedure specifically focuses on using Mimikatz to extract passwords from a memory dump file. A memory dump file is created by dumping the contents of a p

## Description

# Description

Mimikatz is a powerful post-exploitation tool that can be used to extract plaintext passwords from memory on a compromised Windows system. This procedure specifically focuses on using Mimikatz to extract passwords from a memory dump file. A memory dump file is created by dumping the contents of a process's memory to a file, which can then be analyzed offline. By using Mimikatz on a memory dump file, an attacker can extract plaintext passwords that were stored in memory at the time the dump was taken. This technique can be useful for obtaining passwords for privileged accounts, which can then be used to further escalate privileges and move laterally within a network.

From a technical perspective, this procedure involves creating a memory dump file using a tool like ProcDump or Task Manager, and then running Mimikatz on the dump file to extract passwords. The business value of this procedure is that it allows an attacker to obtain sensitive information that can be used to further compromise a network.

 

## Requirements

1. Local or remote access to a Windows system

1. Ability to create a memory dump file using a tool like ProcDump or Task Manager

1. Mimikatz binary

 

## Defense

1. Implement strong password policies and regularly rotate passwords

1. Monitor for suspicious activity related to memory dump files and Mimikatz usage

1. Restrict access to sensitive systems and accounts to only authorized personnel

 

## Objectives

1. Extract plaintext passwords from a memory dump file

1. Obtain credentials for privileged accounts

1. Escalate privileges and move laterally within a network

 

# Instructions

1. To extract logon passwords using Mimikatz, follow these steps:
1. Open a PowerShell window.
2. Navigate to the directory where Mimikatz is located.
3. Execute the command `.\mimikatz.exe "sekurlsa::minidump lsass.dmp"`.
4. Execute the command `sekurlsa::logonPasswords`.
5. The logon passwords will be displayed.

 



**Code**: [[mimikatz # sekurlsa::minidump lsass.dmp
mimikatz #]]



> This command is used to extract logon passwords from a Windows memory dump using Mimikatz. The `sekurlsa::minidump` command is used to load the memory dump file `lsass.dmp`. The `sekurlsa::logonPasswords` command is then used to extract the logon passwords from the memory dump.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Tags

- [[Mini Dump]]
- [[Windows - Mimikatz]]


