---
id: new-uuid-for-setup
type: command
executor: bash
data: |-
  mask ""
  recurse ON
  prompt OFF
  lcd $_LOCAL_DIR
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

# smbclient-recursive-download-setup

## Command

```bash
mask ""
recurse ON
prompt OFF
lcd $_LOCAL_DIR
```

## Description

Sets up smbclient for recursive file download.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| mask "" | Clear file mask | Yes |
| recurse ON | Enable recursion | Yes |
| prompt OFF | No prompts | Yes |
| lcd | Local change dir | Yes |
| $_LOCAL_DIR | Local save path | Yes |

## Examples

### Basic Usage

Enter each in smbclient prompt.

## Expected Output

```
Mask cleared.
Recursion enabled.
Prompts off.
Local dir changed.
```

## Related

- [[procedures/Open-Shares-Enumeration]]
- [[tools/Samba]]
