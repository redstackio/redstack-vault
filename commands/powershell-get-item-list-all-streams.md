---
id: 30df47a8-fb92-488c-8a47-e0b448c55d4b-updated
name: powershell-get-item-list-all-streams
type: command
executor: powershell
data: Get-Item -Path $_FILE_PATH -Stream *
output: null
created_at: '2023-04-06T03:56:29.347279+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - discovery
  - file-system
verified: true
validated: true
---

# powershell-get-item-list-all-streams

## Command

```powershell
Get-Item -Path $_FILE_PATH -Stream *
```

## Description

This PowerShell command retrieves the specified file and lists all associated Alternate Data Streams (ADS), helping identify hidden data like stored passwords in NTFS files. Use it during reconnaissance of file systems for credential looting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FILE_PATH | Path to the target file (e.g., C:\Users\user\flag.txt) | Yes |
| -Stream * | Specifies to include all streams (primary and alternate) | Yes |

## Examples

### Basic Usage

```powershell
Get-Item -Path flag.txt -Stream *
```

### Advanced Usage

```powershell
Get-Item -Path C:\Windows\System32\config.txt -Stream * -Force
```

## Expected Output

```

    Directory: C:\path\to\file

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         4/6/2023   3:56 AM           1024 flag.txt
-a----         4/6/2023   3:56 AM             32 flag.txt:Flag:$DATA

```

This shows the main file and any ADS like ':Flag:$DATA'.

## Related

- [[procedures/Loot-Passwords-from-Alternate-Data-Stream]]
- [[commands/powershell-get-content-ads-stream]]
