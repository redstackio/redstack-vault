---
id: c27c8eba-a5cd-415f-a9a3-c252aa84e3d1
name: Enumerate Windows for Missing Patches and Hotfixes (Sherlock)
type: procedure
verified: true
submitted: true
created_at: '2019-12-05T23:11:23.199789+00:00'
updated_at: '2023-05-25T19:58:43.927637+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[File System Permissions Weakness|T1044 - File System Permissions Weakness]]'
- '[[Permission Groups Discovery|T1069 - Permission Groups Discovery]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
platforms:
- Windows
tags:
- '[[data exposure]]'
- '[[Misconfiguration]]'
- '[[Service Attacks]]'
commands:
- '[[Sherlock Import Module and Enumerate Vulnerabilities]]'
---

# Enumerate Windows for Missing Patches and Hotfixes (Sherlock)

**Status**: ✓ Verified

## Summary

Use Sherlock to enumerate a Windows system for potential privilege escalation paths, including common vulnerabilities , unquoted service paths, missing patches, permission issues, and more. 

## Description

# Description

Use Sherlock to enumerate a Windows system for potential privilege escalation paths, including common vulnerabilities , unquoted service paths, missing patches, permission issues, and more.



# Instructions

1. Download Sherlock.ps1 and import it into a PowerShell session: [Download Sherlock from GitHub](https://github.com/rasta-mouse/Sherlock/)

2. Execute the script..





**Command** ([[Sherlock Import Module and Enumerate Vulnerabilities]]):

```bash
Find-AllVulns
```



Note: if executing Sherlock from a non-interactive session, append "Find-AllVulns" to the end of the script to automatically execute it.



## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[File System Permissions Weakness|T1044 - File System Permissions Weakness]]
- [[Permission Groups Discovery|T1069 - Permission Groups Discovery]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Sherlock Import Module and Enumerate Vulnerabilities]]

## Tags

- [[data exposure]]
- [[Misconfiguration]]
- [[Service Attacks]]


