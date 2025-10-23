---
id: abeaac88-5f4e-4374-a841-73f91c9cacce
name: Dumping AD Domain Credentials using Esentutl.exe
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.936946+00:00'
updated_at: '2023-04-10T20:25:54.563094+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credentials in Files|T1081 - Credentials in Files]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Dumping AD Domain Credentials]]'
- '[[Using esentutl.exe]]'
commands:
- '[[Backup ntds.dit file using esentutl.exe]]'
---

# Dumping AD Domain Credentials using Esentutl.exe

## Summary

Dumping AD Domain Credentials using Esentutl.exe is a technique used to extract the NTDS.dit file from the Active Directory Domain Services (AD DS) database. This file contains hashed credentials of all domain users and computers, including the KRBTGT account, which is used to encrypt all Kerberos 

## Description

# Description

Dumping AD Domain Credentials using Esentutl.exe is a technique used to extract the NTDS.dit file from the Active Directory Domain Services (AD DS) database. This file contains hashed credentials of all domain users and computers, including the KRBTGT account, which is used to encrypt all Kerberos tickets in the domain. An attacker can use these credentials to escalate privileges, move laterally, and ultimately gain domain administrator access. 

Esentutl.exe is a built-in Windows utility that allows for the management of Extensible Storage Engine (ESE) databases, including the AD DS database. By using Esentutl.exe to dump the NTDS.dit file, an attacker can extract the hashed credentials and then use a tool like Mimikatz to perform pass-the-hash attacks.

 

## Requirements

1. Access to a domain-joined Windows machine.

1. Administrative privileges on the machine.

1. Access to the NTDS.dit file.

 

## Defense

1. Implement strong password policies and use complex and unique passwords for all domain accounts.

1. Limit access to the NTDS.dit file and use file system permissions to restrict access to only authorized users.

1. Monitor for suspicious activity, such as unusual access to the NTDS.dit file, and use tools like Mimikatz to detect and prevent pass-the-hash attacks.

 

## Objectives

1. Extract the NTDS.dit file from the AD DS database.

1. Extract hashed credentials of all domain users and computers, including the KRBTGT account.

1. Use the extracted credentials to escalate privileges, move laterally, and ultimately gain domain administrator access.

 

# Instructions

1. To extract the NTDS.dit file, use the esentutl.exe command with the following arguments:
/y - Forces the overwriting of the destination file if it already exists
/vss - Uses the Volume Shadow Copy Service (VSS) to copy the file
c:\windows\ntds\ntds.dit - Specifies the source file to be copied
/d c:\folder\ntds.dit - Specifies the destination file path and name.

 



**Code**: [[esentutl.exe /y /vss c:\windows\ntds\ntds.dit /d c]]



> The NTDS.dit file is a critical file in Active Directory that contains the Active Directory database. This file is locked by the system and cannot be copied or moved while the domain controller is running. The esentutl.exe command can be used to extract the file using the Volume Shadow Copy Service (VSS) to create a snapshot of the file, which can then be copied to another location for analysis or backup purposes.



**Command** ([[Backup ntds.dit file using esentutl.exe]]):

```bash
esentutl.exe /y /vss c:\windows\ntds\ntds.dit /d c:\folder\ntds.dit
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credentials in Files|T1081 - Credentials in Files]]

## Commands Used

- [[Backup ntds.dit file using esentutl.exe]]

## Tags

- [[Active Directory Attacks]]
- [[Dumping AD Domain Credentials]]
- [[Using esentutl.exe]]


