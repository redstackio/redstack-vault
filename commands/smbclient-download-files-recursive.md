---
id: new-uuid-for-mget
type: command
executor: bash
data: mget *
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - smb
verified: true
validated: true
---

# smbclient-download-files-recursive

## Command

```bash
mget *
```

## Description

Downloads all files recursively after setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| mget | Multiple get command | Yes |
| * | All files | Yes |

## Examples

### Basic Usage

`mget *`

## Expected Output

```
getting file \share\file1.txt (success)
getting file \share\dir\file2.txt (success)
```

## Related

- [[procedures/Open-Shares-Enumeration]]
- [[tools/Samba]]
