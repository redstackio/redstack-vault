---
id: 92521d38-cb2c-4a8c-80c9-d65f044e5b6f
name: seatbelt-system-output-file
type: command
executor: cmd
data: 'Seatbelt.exe -group=system -outputfile="C:\Temp\system.txt"'
output: null
created_at: '2023-04-06T03:56:28.514109+00:00'
updated_at: '2023-04-10T20:37:50.966188+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - output
verified: true
validated: true
---

# seatbelt-system-output-file

## Command

```cmd
Seatbelt.exe -group=system -outputfile="C:\Temp\system.txt"
```

## Description

Runs system-focused checks and saves output to a file for later review.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -group=system | Limits to system configuration checks | Yes |
| -outputfile | Path to save results | Yes |

## Examples

### Basic Usage

```cmd
Seatbelt.exe -group=system -outputfile="C:\Temp\system.txt"
```

## Expected Output

system.txt with system details, e.g., "Installed Hotfixes: KB4012212 - MS17-010 Patched".

## Related

- [[commands/seatbelt-all-full-checks]]
- [[procedures/windows-privilege-escalation-using-powerup-privesccheck-and-wes-ng]]
