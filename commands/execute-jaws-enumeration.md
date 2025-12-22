---
id: 078c08e0-9795-4e20-a7ee-f4c0dddd9d83
name: execute-jaws-enumeration
type: command
executor: powershell
data: >-
  powershell.exe -ExecutionPolicy Bypass -File .\jaws-enum.ps1 -OutputFilename
  JAWS-Enum.txt
output: null
created_at: '2023-04-06T03:56:28.514299+00:00'
updated_at: '2023-04-10T20:37:50.966188+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - privesc
verified: true
validated: true
---

# execute-jaws-enumeration

## Command

```powershell
powershell.exe -ExecutionPolicy Bypass -File .\jaws-enum.ps1 -OutputFilename JAWS-Enum.txt
```

## Description

Executes the JAWS enumeration script to gather detailed Windows system information for privilege escalation analysis. Use after initial access to map the environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ExecutionPolicy Bypass | Allows script execution without policy restrictions | Yes |
| -File .\jaws-enum.ps1 | Path to the JAWS script file | Yes |
| -OutputFilename JAWS-Enum.txt | Name of the output file for results | Yes |

## Examples

### Basic Usage

```powershell
powershell.exe -ExecutionPolicy Bypass -File .\jaws-enum.ps1 -OutputFilename JAWS-Enum.txt
```

### Advanced Usage

If script is in a different directory: `-File C:\Temp\jaws-enum.ps1 -OutputFilename C:\Temp\enum.txt`

## Expected Output

Generates JAWS-Enum.txt with sections like "Users and Groups", "Services", and "Potential Privesc Vectors", e.g., listing writable directories or weak services.

## Related

- [[procedures/windows-privilege-escalation-using-powerup-privesccheck-and-wes-ng]]
- [[tools/JAWS]]
