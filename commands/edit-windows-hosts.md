---
data: >-
  echo "127.0.0.1 www.google.example.com" >>
  %WINDIR%\sysnative\drivers\etc\hosts
tags:
  - hosts-file
  - dns-spoof
type: command
output: Domain www.google.example.com resolves to 127.0.0.1
executor: bash
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:58.605Z'
id: 4f822de8-c848-4126-a590-658f341de2f0
verified: false
validated: true
submitted: true
---
# edit-windows-hosts

## Command

```bash
echo "127.0.0.1 www.google.example.com" >> %WINDIR%\sysnative\drivers\etc\hosts
```

## Description

Appends a line to the Windows hosts file to map a fake domain to localhost, simulating a site that triggers Kaspersky's URL Advisor (requires hostname starting with 'www.google.'). Must be run as administrator to modify the protected file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `line` | The mapping entry, e.g., "127.0.0.1 www.google.example.com" | Yes |

## Examples

### Basic Usage

```bash
echo "127.0.0.1 www.google.example.com" >> %WINDIR%\sysnative\drivers\etc\hosts
```

### Advanced Usage

Use notepad or PowerShell for editing if echo fails due to permissions:

```bash
notepad %WINDIR%\sysnative\drivers\etc\hosts
```

## Expected Output

The file updates silently; verify with `ping www.google.example.com` showing "Pinging www.google.example.com [127.0.0.1]".

## Related

- [[Related Procedure|procedures/Setup-Kaspersky-Test-Environment]]
