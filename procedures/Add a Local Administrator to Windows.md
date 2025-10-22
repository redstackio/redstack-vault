---
id: 770de051-9fcd-4885-ac01-2afbe6aa2212
name: Add a Local Administrator to Windows
type: procedure
verified: true
submitted: true
created_at: '2019-11-14T00:19:34.820853+00:00'
updated_at: '2023-05-25T19:55:55.881162+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Create Account|T1136 - Create Account]]'
platforms:
- Windows
tags:
- '[[administrator]]'
- '[[Setup]]'
commands:
- '[[Windows Add a New User]]'
- '[[Windows Add a User to the Local Administrators Group]]'
---

# Add a Local Administrator to Windows

**Status**: ✓ Verified

## Summary

After escalating privileges to gain code execution as a local Administrator, it is often preferable to add an additional user with local Administrator rights, rather than using the standard Administrator account. 

## Description

# Description

After escalating privileges to gain code execution as a local Administrator, it is often preferable to add an additional user with local Administrator rights, rather than using the standard Administrator account.

# Instructions

1. Add a new user and specify the password

**Command** ([[Windows Add a New User]]):

```bash
net user $_USERNAME $_PASSWORD /add
```

2. Add the user to the local Administrators group

**Command** ([[Windows Add a User to the Local Administrators Group]]):

```bash
net localgroup Administrators $_USERNAME /add
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Create Account|T1136 - Create Account]]

## Commands Used

- [[Windows Add a New User]]
- [[Windows Add a User to the Local Administrators Group]]

## Tags

- [[administrator]]
- [[Setup]]
