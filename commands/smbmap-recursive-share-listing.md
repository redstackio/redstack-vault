---
id: 270d3691-2796-451c-8caf-45ef54e66cb9
type: command
executor: bash
data: smbmap -H $_TARGET_IP -R
output: null
created_at: '2023-04-06T03:56:03.238110+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - discovery
  - smb
verified: true
validated: true
---

# smbmap-recursive-share-listing

## Command

```bash
smbmap -H $_TARGET_IP -R
```

## Description

Performs a recursive listing of files and directories in accessible SMB shares using null session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H | Target IP address | Yes |
| -R | Enable recursive listing | Yes |
| $_TARGET_IP | IP of the target | Yes |

## Examples

### Basic Usage

```bash
smbmap -H 10.10.10.10 -R
```

## Expected Output

```
[+] Enumerating shares on 10.10.10.10....
//10.10.10.10/IPC$ (IPC$)
//10.10.10.10/C$ (C$)
    DR  \Windows
        DR  \System32
            ...
```

## Related

- [[procedures/Open-Shares-Enumeration]]
- [[tools/SMBMap]]
