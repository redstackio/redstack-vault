---
id: 4a0275b1-f59a-49b6-baf8-ad85ca69e52e
name: evil-winrm-rb-connect-with-credentials
type: command
executor: bash
data: evil-winrm.rb -i $_TARGET_IP -u $_USERNAME -p $_PASSWORD
output: >-
  root@kali:~/Documents/evil-winrm# ./evil-winrm.rb -i 10.10.10.10 -u bob -p
  secretpass


  Evil-WinRM shell v2.3


  Info: Establishing connection to remote endpoint


  *Evil-WinRM* PS C:\Users\bob\Documents>
created_at: '2020-03-03T01:24:01.684830+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - winrm
  - shell
verified: true
validated: true
---

# evil-winrm-rb-connect-with-credentials

## Command

```bash
evil-winrm.rb -i $_TARGET_IP -u $_USERNAME -p $_PASSWORD
```

## Description

Connects to WinRM using plaintext creds for shell access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i $_TARGET_IP | Target IP | Yes |
| -u $_USERNAME | Username | Yes |
| -p $_PASSWORD | Password | Yes |

## Examples

### Basic Usage

```bash
evil-winrm.rb -i 10.10.10.10 -u admin -p pass123
```

## Expected Output

Evil-WinRM shell v2.3
*Evil-WinRM* PS C:\Users\>

## Related

- [[procedures/Spawn-Interactive-WinRM-Shell-from-Linux-with-Credentials]]
