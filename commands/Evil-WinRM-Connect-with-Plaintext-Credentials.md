---
type: command
executor: bash
data: evil-winrm -i $_TARGET_IP -u $_USERNAME -p $_PASSWORD
output: |-
  Evil-WinRM shell v3.0

  Info: Establishing connection to remote endpoint

  *Evil-WinRM* PS C:\Users\testuser> 
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - winrm
  - shell
verified: true
validated: true
---

# Evil-WinRM-Connect-with-Plaintext-Credentials

## Command

```bash
evil-winrm -i $_TARGET_IP -u $_USERNAME -p $_PASSWORD
```

## Description

Connects to WinRM service using basic auth with username and password for interactive shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i | Target IP | Yes |
| -u | Username | Yes |
| -p | Password | Yes |

## Examples

### Basic Usage

```bash
evil-winrm -i 192.168.1.10 -u user -p pass
```

### Advanced Usage

```bash
evil-winrm -i 192.168.1.10 -u user -p pass -s upload.ps1
```

Upload script.

## Expected Output

Interactive PowerShell prompt.

## Related

- [[procedures/Spawn-Interactive-WinRM-Shell-from-Linux]]
- [[tools/Evil-WinRM]]
