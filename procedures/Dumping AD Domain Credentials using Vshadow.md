---
id: 192bcb4c-32bd-4ac9-8943-7af6b39e9a82
name: Dumping AD Domain Credentials using Vshadow
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.854354+00:00'
updated_at: '2023-04-10T20:26:27.002499+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Dumping AD Domain Credentials]]'
- '[[Using Vshadow]]'
commands:
- '[[Copy ntds.dit from Shadow Copy]]'
- '[[Copy VSS to Destination Directory]]'
- '[[Create Volume Shadow Copy]]'
---

# Dumping AD Domain Credentials using Vshadow

## Summary

Dumping AD domain credentials is a critical step in any attack that targets an Active Directory environment. By using Vshadow, an attacker can create a shadow copy of the NTDS.DIT file, which contains all the domain's user and password hashes. This technique allows an attacker to extract password h

## Description

# Description

Dumping AD domain credentials is a critical step in any attack that targets an Active Directory environment. By using Vshadow, an attacker can create a shadow copy of the NTDS.DIT file, which contains all the domain's user and password hashes. This technique allows an attacker to extract password hashes offline and crack them using password cracking tools. By obtaining valid user credentials, an attacker can move laterally within the network and escalate privileges. Dumping AD domain credentials using Vshadow is a stealthy technique that can be used to bypass endpoint protection and detection mechanisms.

## Requirements

1. Access to the target Active Directory environment

1. Permissions to create a shadow copy of the NTDS.DIT file

1. Vshadow utility

## Defense

1. Implement proper access control mechanisms to limit access to the NTDS.DIT file

1. Monitor for any suspicious activity related to Vshadow usage

1. Enforce strong password policies to prevent password cracking attacks

## Objectives

1. Extract password hashes from the NTDS.DIT file

1. Crack password hashes using password cracking tools

1. Obtain valid user credentials

1. Move laterally within the network

1. Escalate privileges

# Instructions

1. To copy the NTDS.DIT file using VSSAdmin, follow these steps:
1. Open Command Prompt as Administrator.
2. Type 'vssadmin create shadow /for=C:' to create a shadow copy of the C: drive.
3. Type 'Copy Shadow_Copy_Volume_Name\windows\ntds\ntds.dit c:\ntds.dit' to copy the NTDS.DIT file from the shadow copy to the C: drive.

**Code**: [[vssadmin create shadow /for=C: 
Copy Shadow_Copy_V]]

> This command creates a shadow copy of the C: drive using VSSAdmin and then copies the NTDS.DIT file from the shadow copy to the C: drive. The NTDS.DIT file is a database file used by Active Directory to store information about users, groups, and other objects. This command can be useful for backing up or restoring Active Directory data.

**Command** ([[Create Volume Shadow Copy]]):

```bash
vssadmin create shadow /for=C:
```

**Command** ([[Copy ntds.dit from Shadow Copy]]):

```bash
Copy Shadow_Copy_Volume_Name\windows\ntds\ntds.dit c:\ntds.dit
```

2. Use this command to create a copy of a Volume Shadow Copy. The copied data will be saved in the specified destination directory.

**Code**: [[Import-Module .\Copy-VSS.ps1
Copy-VSS
Copy-VSS -De]]

> - Import-Module .\Copy-VSS.ps1: This imports the PowerShell module containing the Copy-VSS function.
- Copy-VSS: This command creates a Volume Shadow Copy of the specified drive.
- Copy-VSS -DestinationDir C:\ShadowCopy\: This command copies the Volume Shadow Copy to the specified destination directory.

**Command** ([[Copy VSS to Destination Directory]]):

```bash
Import-Module .\Copy-VSS.ps1
Copy-VSS
Copy-VSS -DestinationDir C:\ShadowCopy\
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Copy ntds.dit from Shadow Copy]]
- [[Copy VSS to Destination Directory]]
- [[Create Volume Shadow Copy]]

## Tags

- [[Active Directory Attacks]]
- [[Dumping AD Domain Credentials]]
- [[Using Vshadow]]
