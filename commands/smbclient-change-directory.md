---
id: 7cfe4a02-03f6-43b3-81e3-c5974f184672
type: command
executor: bash
data: cd $_DIRECTORY
output: null
created_at: '2023-04-06T03:56:03.238426+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - smb
verified: true
validated: true
---

# smbclient-change-directory

## Command

```bash
cd $_DIRECTORY
```

## Description

Changes directory within the SMB share (interactive).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| cd | Change directory command | Yes |
| $_DIRECTORY | Target folder (e.g., Windows) | Yes |

## Examples

### Basic Usage

`cd Windows`

## Expected Output

```
smb: \share\Windows\>
```

## Related

- [[procedures/Open-Shares-Enumeration]]
- [[tools/Samba]]
