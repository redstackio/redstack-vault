---
type: command
executor: bash
data: cme smb -M $_MODULE -o $_OPTIONS=VALUE
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - smb
  - exploitation
verified: true
validated: true
---

# cme-smb-run-module

## Command

```bash
cme smb -M $_MODULE -o $_OPTIONS=VALUE
```

## Description

Runs a specific SMB module with options.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -M $_MODULE | Module name | Yes |
| -o $_OPTIONS=VALUE | Option-value pairs | No |

## Examples

### Basic Usage

```bash
cme smb -M mimikatz -o LIST_ONLY=True
```

## Expected Output

Module execution results, e.g., dumped credentials.

## Related

- [[tools/CrackMapExec]]
