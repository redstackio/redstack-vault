---
id: 9cd2a119-87d5-44bc-a38e-c990c12570ef
type: command
executor: bash
data: |-
  use $_SHARE_NAME
  cd $_DIRECTORY
output: null
created_at: '2023-04-06T03:56:03.238716+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - smb
verified: true
validated: true
---

# smbclient-select-share

## Command

```bash
use $_SHARE_NAME
cd $_DIRECTORY
```

## Description

Selects a share and navigates to a directory (interactive).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| use | Select share command | Yes |
| cd | Change dir | Yes |
| $_SHARE_NAME | Share (e.g., Users) | Yes |
| $_DIRECTORY | Folder | Yes |

## Examples

### Basic Usage

`use Users`
`cd Documents`

## Expected Output

```
Connected to share.
smb: \Users\Documents\>
```

## Related

- [[procedures/Open-Shares-Enumeration]]
- [[tools/Samba]]
