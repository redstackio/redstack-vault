---
id: 311350ff-94d6-416a-aa40-90cbe2a17a75
type: command
executor: bash
data: ./Snaffler.exe -d $_DOMAIN -c $_DC_IP -s
output: null
created_at: '2023-04-06T03:56:03.238958+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
tags:
  - looting
  - smb
verified: true
validated: true
---

# snaffler-loot-domain-computers

## Command

```bash
./Snaffler.exe -d $_DOMAIN -c $_DC_IP -s
```

## Description

Loots sensitive files from all domain computers via DC.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d | Domain | Yes |
| -c | Domain controller IP | Yes |
| -s | Search for sensitive files | Yes |
| $_DOMAIN | e.g., domain.local | Yes |
| $_DC_IP | DC IP | Yes |

## Examples

### Basic Usage

```bash
./Snaffler.exe -d domain.local -c 10.10.10.5 -s
```

## Expected Output

```
[Snaffler] Found loot: \\host\share\password.txt
Log saved to snaffler.log
```

## Related

- [[procedures/Open-Shares-Enumeration]]
- [[tools/Snaffler]]
