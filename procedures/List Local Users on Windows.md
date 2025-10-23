---
id: 1b0f90a1-de62-468a-9ddf-3a2184c45a9e
name: List Local Users on Windows
type: procedure
verified: true
submitted: true
created_at: '2020-03-18T01:08:37.487388+00:00'
updated_at: '2023-05-25T19:56:08.874667+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Owner/User Discovery|T1033 - System Owner/User Discovery]]'
platforms:
- Windows
tags:
- '[[Enumeration]]'
commands:
- '[[List Local Windows Users]]'
---

# List Local Users on Windows

**Status**: ✓ Verified

## Summary

List local users on a Windows system using command prompt or PowerShell. 

## Description

# Description

List local users on a Windows system using command prompt or PowerShell.





## Objectives

Local account information is important to an attacker, as it can provide them with valid credentials for lateral movement or privilege escalation. The information obtained from listing local users can also be used to map out the environment and identify potential targets for further exploitation.



1. Identify the local users on the windows machine



# Instructions





**Command** ([[List Local Windows Users]]):

```bash
net user
```





## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Owner/User Discovery|T1033 - System Owner/User Discovery]]

## Commands Used

- [[List Local Windows Users]]

## Tags

- [[Enumeration]]


