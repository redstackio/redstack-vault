---
id: 2b05aa34-daea-4416-b5e1-20fb126b07ba
name: clear-windows-event-logs-wevtutil
type: command
executor: cmd
data: |-
  wevtutil cl System
  wevtutil cl Security
output: null
created_at: '2023-04-06T03:56:27.717967+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - defense-evasion
  - log-clearing
verified: true
validated: true
---

# clear-windows-event-logs-wevtutil

## Command

```cmd
wevtutil cl $_LOG_NAME
```

## Description

This command uses the built-in Windows wevtutil.exe utility to clear a specified event log, removing all entries to erase forensic evidence. It is typically run elevated to target logs like System or Security for defense evasion during post-exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_LOG_NAME` | Name of the event log to clear (e.g., System, Security, Application) | Yes |
| `cl` | Clear log flag | Built-in |

## Examples

### Basic Usage

Clear the System log:

```cmd
wevtutil cl System
```

### Advanced Usage

Clear multiple logs in sequence:

```cmd
wevtutil cl System && wevtutil cl Security
```

## Expected Output

When successful, the command outputs:

```
Log cleared successfully.
```

If the log is protected or privileges are insufficient:

```
Error: Access denied.
```

Verify clearance by checking Event Viewer or querying record count with `wevtutil gl $_LOG_NAME` (should show 0 records).

## Related

- [[procedures/Clear-Windows-Event-Logs-for-Evasion]]
