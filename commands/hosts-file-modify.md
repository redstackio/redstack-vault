---
id: cmd-hosts-file-modify
data: >-
  echo "127.0.0.1 www.google.example.com" >>
  %WINDIR%\sysnative\drivers\etc\hosts
tags:
  - spoofing
  - hosts
type: command
output: null
executor: bash
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.169Z'
verified: false
validated: true
submitted: true
---
# hosts-file-modify

## Command

```bash
echo "127.0.0.1 www.google.example.com" >> %WINDIR%\sysnative\drivers\etc\hosts
```

## Description

Appends a domain mapping to the Windows hosts file to spoof resolution to localhost, used in domain spoofing for triggering vulnerabilities like universal XSS on simulated high-value sites.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| entry | The mapping line, e.g., '127.0.0.1 www.google.example.com' | Yes |

## Examples

### Basic Usage

```bash
echo "127.0.0.1 www.google.example.com" >> %WINDIR%\sysnative\drivers\etc\hosts
```

### Advanced Usage

```bash
# Use notepad for manual edit if echo fails
notepad %WINDIR%\sysnative\drivers\etc\hosts
```

## Expected Output

No output on success; verify with ping showing resolution to 127.0.0.1.

## Related

- [[Related Procedure|procedures/Configure-Hosts-File-for-Domain-Spoofing]]
