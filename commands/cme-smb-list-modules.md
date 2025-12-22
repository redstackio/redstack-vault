---
type: command
executor: bash
data: cme smb -L
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

# cme-smb-list-modules

## Command

```bash
cme smb -L
```

## Description

Lists available SMB modules in CrackMapExec.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -L | List modules flag | Yes |

## Examples

### Basic Usage

```bash
cme smb -L
```

## Expected Output

Module list: "rdp, mimikatz, metinject, ...".

## Related

- [[tools/CrackMapExec]]
