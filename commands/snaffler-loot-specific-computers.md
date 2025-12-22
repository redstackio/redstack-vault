---
id: fc399a8f-3208-4729-98e8-8b7ae8a0f886
type: command
executor: bash
data: ./Snaffler.exe -n $_COMPUTERS -s
output: null
created_at: '2023-04-06T03:56:03.239036+00:00'
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

# snaffler-loot-specific-computers

## Command

```bash
./Snaffler.exe -n $_COMPUTERS -s
```

## Description

Loots specific computers listed by name.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | Comma-separated computer names | Yes |
| -s | Search mode | Yes |
| $_COMPUTERS | e.g., computer1,computer2 | Yes |

## Examples

### Basic Usage

```bash
./Snaffler.exe -n computer1,computer2 -s
```

## Expected Output

```
[Snaffler] Looting computer1...
Found: \\computer1\C$\secrets\key.pem
```

## Related

- [[procedures/Open-Shares-Enumeration]]
- [[tools/Snaffler]]
