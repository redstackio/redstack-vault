---
id: d50f9ec5-ab44-4b8f-9dd0-c928c5362097
name: List Local Users and Group Membership on Windows
type: procedure
verified: true
submitted: true
created_at: '2020-03-20T20:55:41.162948+00:00'
updated_at: '2023-05-25T19:45:28.136939+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Owner/User Discovery|T1033 - System Owner/User Discovery]]'
platforms:
- Windows
tags:
- '[[Enumeration]]'
- '[[Operating Systems]]'
- '[[security]]'
commands:
- '[[List a Local Windows User''s Info and Group Membership]]'
- '[[List Local Windows Users]]'
---

# List Local Users and Group Membership on Windows

**Status**: ✓ Verified

## Summary

Query a Windows system for a list of users, then request basic account information and group membership of a user. 

## Description

# Description

Query a Windows system for a list of users, then request basic account information and group membership of a user.

# Instructions

1. Get a list of local users

**Command** ([[List Local Windows Users]]):

```bash
net user
```

2. Query a specific user for account information and group membership

**Command** ([[List a Local Windows User's Info and Group Membership]]):

```bash
net user $_USER
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Owner/User Discovery|T1033 - System Owner/User Discovery]]

## Commands Used

- [[List a Local Windows User's Info and Group Membership]]
- [[List Local Windows Users]]

## Tags

- [[Enumeration]]
- [[Operating Systems]]
- [[security]]
