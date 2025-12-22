---
type: command
executor: command_prompt
data: >-
  schtasks /Create /SC MINUTE /MO $_MODIFIER /TN $_TASK_NAME /TR "cmd.exe /C
  '$_SCRIPT_PATH\$_SCRIPT_NAME'"
output: 'SUCCESS: The scheduled task "$_TASK_NAME" has successfully been created.'
created_at: '2023-06-01T00:00:00Z'
updated_at: '2023-06-01T00:00:00Z'
platforms:
  - Windows
tags:
  - persistence
  - schtasks
verified: true
validated: true
---

# schtasks-create-repeating-minute-task

## Command

```command_prompt
schtasks /Create /SC MINUTE /MO $_MODIFIER /TN $_TASK_NAME /TR "cmd.exe /C '$_SCRIPT_PATH\$_SCRIPT_NAME'"
```

## Description

This command uses the schtasks utility to create a new scheduled task on Windows that repeats every specified number of minutes, executing a batch script via cmd.exe. It is commonly used in persistence scenarios to periodically run malicious payloads, ensuring continued access or execution even after system restarts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /SC MINUTE | Schedule type: minute-based repetition | Yes |
| /MO $_MODIFIER | Modifier: number of minutes between runs (e.g., 5) | Yes |
| /TN $_TASK_NAME | Task name (e.g., pwn) | Yes |
| /TR "cmd.exe /C '$_SCRIPT_PATH\$_SCRIPT_NAME'" | Task run string: executes the batch file at the specified path using cmd.exe | Yes |
| $_MODIFIER | Interval in minutes (1-1439) | Yes |
| $_TASK_NAME | Unique name for the task | Yes |
| $_SCRIPT_PATH | Directory path for the script (e.g., C:\Windows\Tasks) | Yes |
| $_SCRIPT_NAME | Name of the batch file to execute (e.g., shell.bat) | Yes |

## Examples

### Basic Usage

```command_prompt
schtasks /Create /SC MINUTE /MO 5 /TN pwn /TR "cmd.exe /C 'C:\Windows\Tasks\shell.bat'"
```

### Advanced Usage

Add start time and run as SYSTEM:
```command_prompt
schtasks /Create /SC MINUTE /MO 5 /TN pwn /TR "cmd.exe /C 'C:\Windows\Tasks\shell.bat'" /ST 09:00 /RU SYSTEM /F
```

## Expected Output

```
C:\>schtasks /Create /SC MINUTE /MO 5 /TN pwn /TR "cmd.exe /C 'C:\Windows\Tasks\shell.bat'"
SUCCESS: The scheduled task "pwn" has successfully been created.
```

A success message confirms creation. Verify with `schtasks /query /tn $_TASK_NAME` to ensure the task is listed and active.

## Related

- [[procedures/Create-Windows-Scheduled-Task-for-Persistence]]
- [[commands/schtasks-query-task]]
- [[tools/windows-scheduled-tasks]]
