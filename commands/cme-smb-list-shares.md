---
type: command
executor: bash
data: cme smb $_TARGET -u $_USER -H $_HASH --shares
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - smb
  - enumeration
verified: true
validated: true
---

# cme-smb-list-shares

## Command

```bash
cme smb $_TARGET -u $_USER -H $_HASH --shares
```

## Description

Lists accessible SMB shares on target.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET | Target IP | Yes |
| -u $_USER | Username | Yes |
| -H $_HASH | Hash | Yes |
| --shares | List shares | Yes |

## Examples

### Basic Usage

```bash
cme smb 192.168.1.100 -u Administrator -H aad3b435b51404eeaad3b435b51404ee:5858d47a41e40b40f294b3100bea611f --shares
```

## Expected Output

Shares: "ADMIN$, C$, IPC$" with access levels.

## Related

- [[tools/CrackMapExec]]
