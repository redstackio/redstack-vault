---
id: cmd-top-cpu
data: top -p $(pgrep -f node)
tags:
  - monitoring
  - cpu
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.975Z'
verified: false
validated: true
submitted: true
---
# top-monitor-cpu

## Command

```bash
top -p $(pgrep -f node)
```

## Description

This command monitors CPU usage of Node.js processes in real-time using top, useful for validating resource exhaustion in DoS attacks targeting HTTP servers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p` | PID to monitor (dynamically from pgrep) | Yes |
| `$(pgrep -f node)` | Finds PIDs matching 'node' | Yes |

## Examples

### Basic Usage

```bash
top -p 1234
```

### Advanced Usage

```bash
top -p $(pgrep -f node) -d 1
```

> Updates every 1 second.

## Expected Output

Interactive display showing processes, with %CPU column highlighting high usage for Node.js.

## Related

- [[Related Procedure|Monitor-Resource-Exhaustion]]
