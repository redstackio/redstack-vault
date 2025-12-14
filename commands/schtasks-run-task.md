---
id: schtasks-run-001
data: schtasks /run /I /TN EOP
tags:
  - execution
  - scheduled-task
type: command
output: 'SUCCESS: Attempted to run the scheduled task "EOP".'
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.075Z'
verified: false
validated: true
submitted: true
---
# schtasks-run-task

## Command

```cmd
schtasks /run /I /TN EOP
```

## Description

Runs a specified scheduled task immediately and interactively, ignoring constraints, to trigger SYSTEM-level execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /run | Command to run the task | Yes |
| /I | Ignore constraints and run now | Yes |
| /TN EOP | Task name: EOP | Yes |

## Examples

### Basic Usage

```cmd
schtasks /run /I /TN EOP
```

### Advanced Usage

For different task: schtasks /run /I /TN OtherTask

## Expected Output

"SUCCESS: Attempted to run the scheduled task \"EOP\"." followed by task payload execution.

## Related

- [[Related Procedure|procedures/Verify-Admin-Privileges-and-Escalate-to-SYSTEM]]
