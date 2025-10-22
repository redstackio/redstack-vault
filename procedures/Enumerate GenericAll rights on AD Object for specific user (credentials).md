---
id: 1124ef37-ed21-4189-8afe-ed30e1fbaf86
name: Enumerate GenericAll rights on AD Object for specific user (credentials)
type: procedure
verified: false
submitted: false
created_at: '2023-01-12T18:36:32.706786+00:00'
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
- '[[Enumerate GenericAll rights on AD Object]]'
---

# Enumerate GenericAll rights on AD Object for specific user (credentials)

## Summary

Active Directory object permission GenericAll grants full rights to the object. Can add user to a group, or reset the password. 

## Description

# Description

Active Directory object permission GenericAll grants full rights to the object. Can add user to a group, or reset the password.

## Objective

1. Find GenericAll rights on AD Object for the attacking user.

2. In output look for 

    ActiveDirectoryRights: GenericAll

# Instructions

1. Enumerate account name

**Command** ([[Enumerate GenericAll rights on AD Object]]):

```bash
Get-ObjectAcl -SamAccountName $USERNAME -ResolveGUIDs | ? {$_.ActiveDirectoryRights -eq "GenericAll"}
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Permission Groups Discovery|T1069 - Permission Groups Discovery]]

## Commands Used

- [[Enumerate GenericAll rights on AD Object]]

## Tags

- [[Enumeration]]
