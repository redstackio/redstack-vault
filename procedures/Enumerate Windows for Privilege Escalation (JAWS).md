---
id: 4eff9751-b999-40e5-8cbc-9eafaa949d7f
name: Enumerate Windows for Privilege Escalation (JAWS)
type: procedure
verified: false
submitted: false
created_at: '2019-11-26T19:36:52.606652+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
- '[[File System Permissions Weakness|T1044 - File System Permissions Weakness]]'
- '[[Permission Groups Discovery|T1069 - Permission Groups Discovery]]'
- '[[Process Discovery|T1057 - Process Discovery]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
- '[[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]'
- '[[System Service Discovery|T1007 - System Service Discovery]]'
platforms:
- Windows
tags:
- '[[data exposure]]'
- '[[Misconfiguration]]'
- '[[Service Attacks]]'
commands:
- '[[JAWS Enumerate for Privilege Escalation ]]'
---

# Enumerate Windows for Privilege Escalation (JAWS)

## Summary

JAWS (Just Another [Enumeration] Script) identifies potential privilege escalation paths on Windows systems. 

## Description

# Description

JAWS (Just Another [Enumeration] Script) identifies potential privilege escalation paths on Windows systems.

# Instructions

[Download JAWS from GitHub](https://github.com/411Hall/JAWS) and copy it to the target to run locally.

**Command** ([[JAWS Enumerate for Privilege Escalation ]]):

```bash
Import-Module .\jaws-enum.ps1 -OutputFileName $_OUTPUT.txt
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]
- [[File and Directory Discovery|T1083 - File and Directory Discovery]]
- [[File System Permissions Weakness|T1044 - File System Permissions Weakness]]
- [[Permission Groups Discovery|T1069 - Permission Groups Discovery]]
- [[Process Discovery|T1057 - Process Discovery]]
- [[System Information Discovery|T1082 - System Information Discovery]]
- [[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]
- [[System Service Discovery|T1007 - System Service Discovery]]

## Commands Used

- [[JAWS Enumerate for Privilege Escalation ]]

## Tags

- [[data exposure]]
- [[Misconfiguration]]
- [[Service Attacks]]
