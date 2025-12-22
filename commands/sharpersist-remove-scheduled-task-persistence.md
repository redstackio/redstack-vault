---
type: command
executor: powershell
data: SharPersist -t schtask -n "Some Task" -m remove
tags:
  - persistence
  - removal
platforms:
  - Windows
verified: true
validated: true
---

# sharpersist-remove-scheduled-task-persistence

## Command

```powershell
SharPersist -t schtask -n "Some Task" -m remove
```

## Description

Removes a standard scheduled task by name, deleting it from the scheduler.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-t schtask` | Type: Standard scheduled task | Yes |
| `-n <name>` | Task name to delete | Yes |
| `-m remove` | Remove mode | Yes |

## Examples

### Basic Usage

```powershell
SharPersist -t schtask -n "WindowsMaintenance" -m remove
```

### Advanced Usage

```powershell
SharPersist -t schtask -n "Some Task" -m remove; schtasks /delete /tn "Some Task" /f
```

## Expected Output

```
Scheduled task removed: Some Task
```

## Related

- [[procedures/Establish-Persistence-Using-SharPersist-in-Cobalt-Strike]]
- [[tools/Cobalt-Strike]]
