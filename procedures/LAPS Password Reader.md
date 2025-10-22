---
id: 39fd3f3d-e405-472d-8383-e151f0618342
name: LAPS Password Reader
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.498776+00:00'
updated_at: '2023-04-10T20:26:25.209593+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Determine if LAPS is installed]]'
- '[[Reading LAPS Password]]'
commands:
- '[[Check Admpwd.dll file]]'
- '[[Get Admpwd.dll file hash]]'
- '[[Get Admpwd.dll file signature]]'
---

# LAPS Password Reader

## Summary

The LAPS Password Reader procedure is used to determine if the Local Administrator Password Solution (LAPS) is installed on the targeted Active Directory environment and, if so, to retrieve the password for the local administrator account on each machine. LAPS is a Microsoft tool that provides a so

## Description

# Description

The LAPS Password Reader procedure is used to determine if the Local Administrator Password Solution (LAPS) is installed on the targeted Active Directory environment and, if so, to retrieve the password for the local administrator account on each machine. LAPS is a Microsoft tool that provides a solution for managing local administrator account passwords. It stores the password for each computer's local administrator account in Active Directory, which can be retrieved by users with proper permissions. Attackers can use this procedure to retrieve the password and gain access to the targeted machines. The procedure involves checking the integrity of the Admpwd.dll file to determine if LAPS is installed, and then using the appropriate commands to retrieve the password.

## Requirements

1. Access to the targeted Active Directory environment.

1. Proper permissions to retrieve the LAPS password.

1. Tools to check the integrity of the Admpwd.dll file and retrieve the password.

## Defense

1. Ensure that proper permissions are in place to restrict access to the LAPS password.

1. Regularly monitor the integrity of the Admpwd.dll file to detect any modifications or tampering.

1. Consider using alternative solutions for managing local administrator account passwords to reduce the risk of LAPS-related attacks.

## Objectives

1. Retrieve the local administrator password for each machine in the targeted Active Directory environment.

1. Gain access to the targeted machines using the retrieved password.

# Instructions

1. Run the following commands in PowerShell to check the integrity of the LAPS Admpwd.dll file:

**Code**: [[Get-ChildItem 'c:\program files\LAPS\CSE\Admpwd.dl]]

> This set of PowerShell commands will retrieve the Admpwd.dll file from the specified location, calculate its hash value and check its digital signature. This is useful for verifying that the file has not been tampered with and is safe to use.

**Command** ([[Check Admpwd.dll file]]):

```bash
Get-ChildItem 'c:\program files\LAPS\CSE\Admpwd.dll'
```

**Command** ([[Get Admpwd.dll file hash]]):

```bash
Get-FileHash 'c:\program files\LAPS\CSE\Admpwd.dll'
```

**Command** ([[Get Admpwd.dll file signature]]):

```bash
Get-AuthenticodeSignature 'c:\program files\LAPS\CSE\Admpwd.dll'
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Check Admpwd.dll file]]
- [[Get Admpwd.dll file hash]]
- [[Get Admpwd.dll file signature]]

## Tags

- [[Active Directory Attacks]]
- [[Determine if LAPS is installed]]
- [[Reading LAPS Password]]
