---
id: b78dd6d8-9168-4b70-94d1-6deaf8a2e816
name: crackmapexec-brute-force-smb-users-using-rid
type: command
executor: bash
data: crackmapexec smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD --rid-brute
output: |-
  SMB 10.10.10.10 445 TARGET [+] Brute forcing RIDs
  500: TARGET\Administrator (SidTypeUser)
created_at: '2019-12-27T22:38:42.675767+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - rid
verified: true
validated: true
---

# crackmapexec-brute-force-smb-users-using-rid

## Command

```bash
crackmapexec smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD --rid-brute
```

## Description

Enumerates users via authenticated RID brute-force on SMB.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target IP | Yes |
| -u $_USERNAME | Valid username | Yes |
| -p $_PASSWORD | Valid password | Yes |
| --rid-brute | Enable RID cycling | Yes |

## Examples

### Basic Usage

```bash
crackmapexec smb 10.10.10.10 -u bob -p pass --rid-brute
```

## Expected Output

List of SID users.

## Related

- [[procedures/brute-force-smb-users-using-rid-authenticated]]
