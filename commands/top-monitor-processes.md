---
data: top
tags:
  - monitoring
  - cpu
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.642Z'
id: 6f357dff-ef5a-4b5f-a4c3-c0389c348390
verified: false
validated: true
submitted: true
---
# top-monitor-processes

## Command

```bash
top
```

## Description

This command provides a real-time view of system processes, sorted by CPU usage, to observe high resource consumption from vulnerable curl executions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Default sorting by CPU | No |

## Examples

### Basic Usage

```bash
top
```

### Advanced Usage

```bash
top -p $(pgrep curl)
```

## Expected Output

Interactive display showing processes with columns like PID, USER, %CPU, %MEM. curl appears with ~100% CPU during the DoS loop.

## Related

- [[commands/curl-mqtt-dos-trigger]]
- [[procedures/Observe-Resource-Consumption-with-top]]
