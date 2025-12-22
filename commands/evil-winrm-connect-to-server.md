---
id: 4a0275b1-f59a-49b6-baf8-ad85ca69e52e
name: evil-winrm-connect-to-server
type: command
executor: bash
data: evil-winrm.rb -i $_TARGET_IP -u $_USER -p $_PASS
output: |-
  Evil-WinRM shell v2.3

  Info: Establishing connection to remote endpoint

  *Evil-WinRM* PS C:\Users\bob\Documents>
created_at: '2020-03-03T01:24:01.684830+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - winrm
  - remote-access
verified: true
validated: true
---

# evil-winrm-connect-to-server

## Command

```bash
evil-winrm.rb -i $_TARGET_IP -u $_USER -p $_PASS
```

## Description

Connects to a remote Windows host via WinRM to spawn an interactive PowerShell shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i $_TARGET_IP | Target IP | Yes |
| -u $_USER | Username | Yes |
| -p $_PASS | Password | Yes |

## Examples

### Basic Usage

```bash
evil-winrm.rb -i 10.10.10.10 -u bob -p secret
```

### With SSL

```bash
evil-winrm.rb -i 10.10.10.10 -u bob -p secret -S
```

## Expected Output

Description: Interactive PS prompt for command execution.

## Related

- [[procedures/Establish-WinRM-Remote-Shell]]
- [[tools/Evil-WinRM]]
