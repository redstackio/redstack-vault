---
id: 72ea53f8-52b3-431a-9d59-cbddcf10c0ca
name: Escalate from an Administrator Session to SYSTEM (Windows)
type: procedure
verified: false
submitted: false
created_at: '2020-07-06T23:55:46.950212+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Service Execution|T1035 - Service Execution]]'
platforms:
- Windows
tags:
- '[[administrator]]'
- '[[privileges]]'
commands:
- '[[PsExec Spawn a PowerShell Prompt as SYSTEM]]'
---

# Escalate from an Administrator Session to SYSTEM (Windows)

## Summary

Use PsExec.exe with Administrator privileges to spawn a SYSTEM shell. This approach spawns a new window and will not bypass UAC, making it suited for cases when the attacker has RDP or local access. 

## Description

# Description

Use PsExec.exe with Administrator privileges to spawn a SYSTEM shell. This approach spawns a new window and will not bypass UAC, making it suited for cases when the attacker has RDP or local access.



# Instructions

1. Copy PsExec to the target machine. [Download  PsExec from Microsoft](https://docs.microsoft.com/en-us/sysinternals/downloads/psexec)

2. Execute PsExec, specifying the local computer as the target.





**Command** ([[PsExec Spawn a PowerShell Prompt as SYSTEM]]):

```powershell
PsExec.exe -accepteula \\$_TARGET powershell.exe
```



Note: Replace "powershell.exe" with "cmd.exe" for a standard cmd prompt.

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Service Execution|T1035 - Service Execution]]

## Commands Used

- [[PsExec Spawn a PowerShell Prompt as SYSTEM]]

## Tags

- [[administrator]]
- [[privileges]]


