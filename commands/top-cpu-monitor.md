---
id: cmd-uuid-6
data: watch -n 1 'top -p $(pgrep node)'
tags:
  - monitor
  - cpu
type: command
output: CPU usage at 100%
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.649Z'
verified: false
validated: true
submitted: true
---
# top-cpu-monitor

## Command

```bash
watch -n 1 'top -p $(pgrep node)'
```

## Description

Monitors CPU usage of Node.js processes in real-time.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-n 1` | Update every 1 second | Yes |
| `top -p $(pgrep node)` | Target Node.js PID | Yes |

## Examples

### Basic Usage

```bash
watch -n 1 'top -p $(pgrep node)'
```

## Expected Output

Real-time CPU percentage display.

## Related

- [[procedures/Send-Large-SETTINGS-Frames]]
