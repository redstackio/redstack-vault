---
id: cmd-kill-browser-process
data: kill -9 $pid
tags:
  - recovery
  - dos
  - process
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.431Z'
verified: false
validated: true
submitted: true
---
# kill-browser-process

## Command

```bash
kill -9 $pid
```

## Description

This command forcefully terminates a frozen browser process (e.g., Brave) by its process ID (PID) in Linux environments, used to recover from a DoS-induced hang.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-9` | Signal for immediate termination (SIGKILL) | Yes |
| `$pid` | Process ID of the target browser instance | Yes |

## Examples

### Basic Usage

```bash
kill -9 1234
```

### Advanced Usage

First find PID:
```bash
ps aux | grep brave
kill -9 $(pgrep brave)
```

## Expected Output

No output if successful; the process terminates immediately, freeing system resources.

## Related

- [[Related Procedure|procedures/Observe-and-Recover-from-Browser-Freeze]]
