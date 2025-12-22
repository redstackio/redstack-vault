---
id: 1f18633a-25ff-4d4a-a5a7-009b213c60b9
name: get-process-list-running-processes
type: command
executor: powershell
data: Get-Process
output: |-
  PS C:\> Get-Process
  Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
  ... lsass  ...
created_at: '2020-01-02T18:45:14.101739+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - processes
verified: true
validated: true
---

# get-process-list-running-processes

## Command

```powershell
Get-Process
```

## Description

Lists all running processes with details like PID and name.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Name $_NAME | Filter by name (optional) | No |

## Examples

### Basic Usage

```powershell
Get-Process
```

### Filtered

```powershell
Get-Process -Name lsass
```

## Expected Output

Table of processes.

## Related

- [[procedures/dump-process-memory-powershell]]
