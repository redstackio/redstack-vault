---
data: schtasks /run /I /TN EOP
tags:
  - privilege-escalation
  - scheduled-task
type: command
output: 'SUCCESS: Attempted to run the scheduled task "EOP"'
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.396Z'
id: 2ad4659e-9c56-4e88-b516-3b07464da9de
verified: false
validated: true
submitted: true
---
# Schtasks Run Elevated Task

## Command

```cmd
schtasks /run /I /TN EOP
```

## Description

Runs a pre-created scheduled task immediately, ignoring constraints, to execute as SYSTEM on Windows.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /run | Run the task | Yes |
| /I | Ignore constraints | Yes |
| /TN EOP | Task name | Yes |

## Examples

### Basic Usage

```cmd
schtasks /run /I /TN EOP
```

### Advanced Usage

Use with custom task names.

## Expected Output

"SUCCESS: Attempted to run the scheduled task \"EOP\"".

## Related

- [[Related Procedure: Execute Scheduled Task as SYSTEM]]
