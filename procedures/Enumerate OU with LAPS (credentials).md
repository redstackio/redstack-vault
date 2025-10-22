---
id: d9132d25-4309-4deb-81c9-d88cb7840d95
name: Enumerate OU with LAPS (credentials)
type: procedure
verified: false
submitted: false
created_at: '2023-01-12T18:59:53.055904+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Permission Groups Discovery|T1069 - Permission Groups Discovery]]'
platforms:
- Windows
tags:
- '[[Enumeration]]'
commands:
- '[[Enumerate OU with LAPS PowerView]]'
---

# Enumerate OU with LAPS (credentials)

## Summary

Domain joined computers can use LAPS (Local Administrator Password). The domain control the password and requires a user with ACL permissions to access the plain text password. Two artifacts in OU enumeration that LAPS use: ms-Mcs-AdmPwd and Mcs-AdmPwdExpirationTime 

## Description

# Description

Domain joined computers can use LAPS (Local Administrator Password). The domain control the password and requires a user with ACL permissions to access the plain text password.

Two artifacts in OU enumeration that LAPS use: ms-Mcs-AdmPwd and Mcs-AdmPwdExpirationTime

## Objective

1. Check domain joined computers for LAPS by looking at OUs

# Instructions

1. Enumerate Domain OU for LAPS artifacts

Look for ObjectAceType: ms-Mcs-AdmPwd

**Command** ([[Enumerate OU with LAPS PowerView]]):

```bash
Get-DomainOU | Get-DomainObjectAcl -ResolveGUIDs | WhereObject {($_.ObjectAceType -like 'ms-Mcs-AdmPwd') -and 
($_.ActiveDirectoryRights -match 'ReadProperty')} | ForEach-Object {$_ | AddMember NoteProperty 'IdentityName' $(Convert-SidToName 
$_.SecurityIdentifier);$_}
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Permission Groups Discovery|T1069 - Permission Groups Discovery]]

## Commands Used

- [[Enumerate OU with LAPS PowerView]]

## Tags

- [[Enumeration]]
