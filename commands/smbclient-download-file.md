---
id: fa5c51cf-20eb-43db-aadc-f280cd8c2275
type: command
executor: bash
data: get $_FILE_NAME
output: null
created_at: '2023-04-06T03:56:03.238498+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - smb
verified: true
validated: true
---

# smbclient-download-file

## Command

```bash
get $_FILE_NAME
```

## Description

Downloads a file from the SMB share to local machine (interactive).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| get | Download command | Yes |
| $_FILE_NAME | Remote file path | Yes |

## Examples

### Basic Usage

`get secrets.txt`

## Expected Output

```
getting file \share\secrets.txt of size 1024 as secrets.txt (1.0 KiloBytes/sec)
```

## Related

- [[procedures/Open-Shares-Enumeration]]
- [[tools/Samba]]
