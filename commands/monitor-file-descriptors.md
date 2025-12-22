---
id: cmd-001
data: 'ls -l /proc/{PID}/fd | wc -l && ls -l /proc/{PID}/map_files | wc -l'
tags:
  - monitoring
  - procfs
type: command
output: 'Two numbers: count of file descriptors and count of map_files'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.712Z'
verified: false
validated: true
submitted: true
---
# monitor-file-descriptors

## Command

```bash
ls -l /proc/{PID}/fd | wc -l && ls -l /proc/{PID}/map_files | wc -l
```

## Description

Counts open file descriptors and mapped files for a Linux process to monitor resource leaks, useful for detecting exhaustion in attacks like the Node.js HTTP2 DoS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{PID}` | Process ID to monitor (e.g., Node.js server PID) | Yes |

## Examples

### Basic Usage

```bash
ls -l /proc/1234/fd | wc -l && ls -l /proc/1234/map_files | wc -l
```

### Advanced Usage

```bash
watch -n 1 'ls -l /proc/{PID}/fd | wc -l'
```

For continuous monitoring.

## Expected Output

Two integers separated by newline or space, e.g., '25
10', indicating FD and map_files counts.

## Related

- [[commands/send-malformed-http-request]]
- [[procedures/Monitor-Server-File-Descriptors]]
