---
id: 00e2e712-9f9a-46c4-be4a-f5ed1ef29c65
type: command
executor: bash
data: ./Snaffler.exe -i $_DIRECTORY -s
output: null
created_at: '2023-04-06T03:56:03.239086+00:00'
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

# snaffler-loot-specific-directory

## Command

```bash
./Snaffler.exe -i $_DIRECTORY -s
```

## Description

Loots a specific directory or share path.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i | Input directory | Yes |
| -s | Search | Yes |
| $_DIRECTORY | Path (e.g., C:\) | Yes |

## Examples

### Basic Usage

```bash
./Snaffler.exe -i C:\ -s
```

## Expected Output

```
[Snaffler] Scanning C:\...
Loot: C:\Users\admin\passwords.txt
```

## Related

- [[procedures/Open-Shares-Enumeration]]
- [[tools/Snaffler]]
