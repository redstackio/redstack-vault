---
id: 55027df5-3342-4e23-9124-d3aa3f73a355
name: Enumerate group membership of user
type: procedure
verified: false
submitted: false
created_at: '2023-01-12T07:19:09.943097+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Windows
tags:
- '[[Active Directory]]'
- '[[Enumeration]]'
commands:
- '[[Enumerate group membership AD Module]]'
- '[[Enumerate group membership PowerView]]'
- '[[Get group members]]'
---

# Enumerate group membership of user

## Summary

The a user could be included in privileged groups. Use this command to check. 

## Description

# Description

The a user could be included in privileged groups. Use this command to check.



## Objective

1. Identify if a user is member of privileged group



# Instructions

1.  User the powerview script to check against a specific user





**Command** ([[Enumerate group membership PowerView]]):

```bash
Get-NetGroup -UserName $USER
```





2. (Optional)  ActiveDirectory powershell command version.





**Command** ([[Enumerate group membership AD Module]]):

```bash
Get-ADPrincipalGroupMembership -Identity $USER
```





3. (Optional) Get users inside of a specific group name.



**Command** ([[Get group members]]):

```bash
Get-NetGroupMember [-GroupName “Domain Admins”]

```





## Platforms

- Windows

## Commands Used

- [[Enumerate group membership AD Module]]
- [[Enumerate group membership PowerView]]
- [[Get group members]]

## Tags

- [[Active Directory]]
- [[Enumeration]]


