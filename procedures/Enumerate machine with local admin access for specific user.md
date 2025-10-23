---
id: db73e1c2-90a3-47f3-9a95-01338cca67aa
name: Enumerate machine with local admin access for specific user
type: procedure
verified: false
submitted: false
created_at: '2023-01-12T06:56:21.041867+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Windows
tags:
- '[[Pivot]]'
- '[[privileges]]'
commands:
- '[[Enumerate computers in domain for local admin PowerUp]]'
- '[[Enumerate computers in domain for local admin PowerView]]'
- '[[PSRemotingLocalAdminAccess.ps1]]'
---

# Enumerate machine with local admin access for specific user

## Summary

Try to find a machine on domain that local user has local admin access. 

## Description

# Description

Try to find a machine on domain that local user has local admin access.



## Objective

1. Local administrator access on domain machine.



# Instructions

1.  Enumerate computers in the domain for local admin access using PowerUp / PowerSploit.

Requires SMB and RPC ports open.





**Command** ([[Enumerate computers in domain for local admin PowerUp]]):

```bash
Find-LocalAdminAccess -Verbose
```



2. (Optional) Try with PowerView. If RPC and SMB ports are blocked try with WMI.





**Command** ([[Enumerate computers in domain for local admin PowerView]]):

```bash
Find-WMILocalAdminAccess.ps1
```



3. (Optional) Try Nishang If both don't work which uses WinRM





**Command** ([[PSRemotingLocalAdminAccess.ps1]]):

```powershell
PSRemotingLocalAdminAccess.ps1
```











## Platforms

- Windows

## Commands Used

- [[Enumerate computers in domain for local admin PowerUp]]
- [[Enumerate computers in domain for local admin PowerView]]
- [[PSRemotingLocalAdminAccess.ps1]]

## Tags

- [[Pivot]]
- [[privileges]]


