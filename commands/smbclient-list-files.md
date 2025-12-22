---
id: a4daae45-276f-4335-85ba-62cf867c8316
type: command
executor: bash
data: ls
output: null
created_at: '2023-04-06T03:56:03.238782+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - smb
verified: true
validated: true
---

# smbclient-list-files

## Command

```bash
ls
```

## Description

Lists files and directories in the current SMB share directory (interactive command).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ls | List command | Yes |

## Examples

### Basic Usage

After connecting: `ls`

## Expected Output

```
  .                                   D        0  Sat Dec 10 12:34:56 2022
  ..
  file.txt                           N  1024  Sat Dec 10 12:34:56 2022
```

## Related

- [[procedures/Open-Shares-Enumeration]]
- [[tools/Samba]]
