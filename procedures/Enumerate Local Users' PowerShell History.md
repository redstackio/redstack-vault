---
id: d028a34c-3ab4-4e50-b9c2-5fd51ae5a7d0
name: Enumerate Local Users' PowerShell History
type: procedure
verified: true
submitted: true
created_at: '2020-06-24T23:40:58.220763+00:00'
updated_at: '2023-05-25T19:59:39.474418+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
techniques:
- '[[Data from Local System|T1005 - Data from Local System]]'
platforms:
- Windows
tags:
- '[[data exposure]]'
- '[[Enumeration]]'
commands:
- '[[Enumerate Local Users'' PowerShell History]]'
---

# Enumerate Local Users' PowerShell History

**Status**: ✓ Verified

## Summary

Display the contents of all local users' PowerShell history. 

## Description

# Description

Display the contents of all local users' PowerShell history.

# Instructions

**Command** ([[Enumerate Local Users' PowerShell History]]):

```powershell
Get-ChildItem -Path "C:\Users\*\APPDATA\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt" | Get-Content
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]

### Techniques

- [[Data from Local System|T1005 - Data from Local System]]

## Commands Used

- [[Enumerate Local Users' PowerShell History]]

## Tags

- [[data exposure]]
- [[Enumeration]]
