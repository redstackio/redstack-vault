---
id: cmd-001
data: notepad %WINDIR%\sysnative\drivers\etc\hosts
tags:
  - dns
  - hosts
type: command
output: >-
  Hosts file opened for editing; append '127.0.0.1 www.google.example.com' and
  save.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.186Z'
verified: false
validated: true
submitted: true
---
# Edit Windows Hosts File

## Command

```cmd
notepad %WINDIR%\sysnative\drivers\etc\hosts
```

## Description

Opens the Windows hosts file in Notepad for editing as administrator, allowing addition of IP-domain mappings to redirect traffic locally. Used here to point www.google.example.com to 127.0.0.1 for exploit delivery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| %WINDIR%\sysnative\drivers\etc\hosts | Path to hosts file (use sysnative for 64-bit compatibility) | Yes |

## Examples

### Basic Usage

```cmd
notepad %WINDIR%\sysnative\drivers\etc\hosts
```

Append line: 127.0.0.1 www.google.example.com

### Advanced Usage

Use echo for automation (run as admin):

```cmd
echo 127.0.0.1 www.google.example.com >> %WINDIR%\sysnative\drivers\etc\hosts
```

## Expected Output

File opens in Notepad; after edit and save, ping www.google.example.com resolves to 127.0.0.1. No output from command itself, but verification via ping.

## Related

- [[Related Procedure: Modify-Windows-Hosts-File-for-Domain-Redirect]]
