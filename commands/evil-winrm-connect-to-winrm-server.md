---
id: 4a0275b1-f59a-49b6-baf8-ad85ca69e52e
name: evil-winrm-connect-to-winrm-server
type: command
executor: bash
data: evil-winrm -i $_TARGET_IP -u $_USERNAME -p $_PASSWORD
output: |-
  Evil-WinRM shell v2.3
  *Evil-WinRM* PS C:\Users\user>
created_at: '2020-03-03T01:24:01.684830+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - remote-shell
  - winrm
verified: true
validated: true
---

# evil-winrm-connect-to-winrm-server

## Command

```bash
evil-winrm -i $_TARGET_IP -u $_USERNAME -p $_PASSWORD
```

## Description

Connects to WinRM for interactive PS shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i $_TARGET_IP | Target IP | Yes |
| -u $_USERNAME | Username | Yes |
| -p $_PASSWORD | Password | Yes |

## Examples

### Basic Usage

```bash
evil-winrm -i 10.10.10.10 -u admin -p pass
```

## Expected Output

PS prompt for interaction.

## Related

- [[procedures/spawn-interactive-shell-with-winrm-linux]]
