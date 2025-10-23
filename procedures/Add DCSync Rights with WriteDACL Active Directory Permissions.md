---
id: 870ad407-c447-4a42-aa71-d830638e00d7
name: Add DCSync Rights with WriteDACL Active Directory Permissions
type: procedure
verified: true
submitted: true
created_at: '2020-03-16T00:35:46.352047+00:00'
updated_at: '2023-05-25T19:43:13.389277+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
platforms:
- Windows
tags:
- '[[Active Directory]]'
commands:
- '[[Create a Windows PSCredential Object]]'
- '[[PowerView Add DCSync Rights to a User]]'
---

# Add DCSync Rights with WriteDACL Active Directory Permissions

**Status**: ✓ Verified

## Summary

Users with WriteDACL permissions to a domain can add the appropriate ACE in order to perform a DCSync attack. DCSync involves the simulation of a domain controller, which is used to connect to a legitimate domain controller and dump password hashes. 

## Description

# Description

Users with WriteDACL permissions to a domain can add the appropriate ACE in order to perform a DCSync attack. DCSync involves the simulation of a domain controller, which is used to connect to a legitimate domain controller and dump password hashes.





## Objectives

The DCSync attack involves simulating a domain controller and requesting password data from a legitimate domain controller. An attacker with WriteDACL permissions can add the appropriate Access Control Entry (ACE) to the domain's Domain Object to grant themselves the rights necessary to retrieve password data for any user in the domain.



1. Create a credential object using valid credentials (if needed)

2. Using PowerView add dcsync rights to a user







# Instructions

1. Download and import [Powerview (dev branch) from GitHub](https://github.com/PowerShellMafia/PowerSploit/blob/dev/Recon/PowerView.ps1).

2. (Optional) It may be necessary to create a PS Credentials object of the user with WriteDACL privileges to the domain.





**Command** ([[Create a Windows PSCredential Object]]):

```bash
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "$_DOMAIN\$_USER", $Pass
```





3. Use PowerView's Add-DomainObjectAcl cmdlet to add DCSync rights to a user (not necessarily the same user as the one with WriteDACL). 





**Command** ([[PowerView Add DCSync Rights to a User]]):

```bash
Add-DomainObjectAcl  -Rights DCSync -TargetDomain $_DOMAIN -PrincipalIdentity $_USER -Credential $Cred
```



Note: The "Credential" argument may not be necessary if the current session is already running as that user.

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Create a Windows PSCredential Object]]
- [[PowerView Add DCSync Rights to a User]]

## Tags

- [[Active Directory]]


