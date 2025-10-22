---
id: 8b003bc1-d0f3-468f-9079-293dba6d6c6a
name: Dump a Process's Memory (PowerShell)
type: procedure
verified: true
submitted: true
created_at: '2020-01-02T19:41:41.041387+00:00'
updated_at: '2023-05-25T19:54:29.827940+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
techniques:
- '[[Data from Local System|T1005 - Data from Local System]]'
platforms:
- Windows
tags:
- '[[data exposure]]'
- '[[memory]]'
commands:
- '[[Get-Process List Running Processes]]'
- '[[Out-Minidump Dump the Memory of a Process]]'
---

# Dump a Process's Memory (PowerShell)

**Status**: ✓ Verified

## Summary

Dump a process's memory  into a file using PowerSploit's Out-Minidump cmdlet. 

## Description

# Description

Dump a process's memory  into a file using PowerSploit's Out-Minidump cmdlet.

# Instructions

1. Download PowerSploit's Out-Minidump and import it into a PowerShell session: [Download from GitHub](https://github.com/PowerShellMafia/PowerSploit/blob/dev/Exfiltration/Out-Minidump.ps1)

2. Identify a process to target.

**Command** ([[Get-Process List Running Processes]]):

```bash
Get-Process
```

3. Execute Get-Process and specify the process name, pipe the output into Out-Minidump, and specify a directory to output the results.

**Command** ([[Out-Minidump Dump the Memory of a Process]]):

```bash
Get-Process -Name $_NAME | Out-Minidump -DumpFilePath $_PATH
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]

### Techniques

- [[Data from Local System|T1005 - Data from Local System]]

## Commands Used

- [[Get-Process List Running Processes]]
- [[Out-Minidump Dump the Memory of a Process]]

## Tags

- [[data exposure]]
- [[memory]]
