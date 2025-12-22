---
id: 71b3ad9e-a933-442c-b19d-96453ee6faf4
type: command
executor: bash
data: put $_LOCAL_FILE
output: null
created_at: '2023-04-06T03:56:03.238520+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - smb
verified: true
validated: true
---

# smbclient-upload-file

## Command

```bash
put $_LOCAL_FILE
```

## Description

Uploads a local file to the SMB share (interactive).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| put | Upload command | Yes |
| $_LOCAL_FILE | Local file to upload | Yes |

## Examples

### Basic Usage

`put malware.exe`

## Expected Output

```
putting file malware.exe as \share\malware.exe (1.0 KiloBytes/sec)
```

## Related

- [[procedures/Open-Shares-Enumeration]]
- [[tools/Samba]]
