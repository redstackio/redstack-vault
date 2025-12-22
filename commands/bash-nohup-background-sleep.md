---
type: command
executor: bash
data: nohup sleep 120 > /dev/null &
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Unix
tags:
  - backgrounding
  - evasion
verified: true
validated: true
---

# bash-nohup-background-sleep

## Command

```bash
nohup sleep 120 > /dev/null &
```

## Description

This command backgrounds a 2-minute sleep process using nohup, redirecting output to null. It is used to simulate a long-running task in command injection tests, evading timeouts by detaching from the parent shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sleep 120 | Duration in seconds (120 = 2 minutes); adjust for longer tasks | Yes |
| > /dev/null | Redirects stdout/stderr to null to suppress output | Yes |
| & | Backgrounds the process | Yes |

## Examples

### Basic Usage

```bash
nohup sleep 120 > /dev/null &
```

### Advanced Usage

For a custom duration or different command:

```bash
nohup your-long-command > /dev/null 2>&1 &
```

## Expected Output

The command outputs the PID of the backgrounded process, e.g., '[1] 12345', and returns to the prompt immediately. No further output is produced due to redirection. Verify with `ps aux | grep sleep` to see the process running.

## Related

- [[procedures/Background-Long-Running-Commands]]
