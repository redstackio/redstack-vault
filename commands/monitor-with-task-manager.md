---
data: Launch Task Manager and sort processes by memory
tags:
  - monitoring
type: command
output: GUI view of process memory increasing
executor: gui
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.285Z'
id: 26591078-9554-49b5-a4e1-fba7fd782ce0
verified: false
validated: true
submitted: true
---
# monitor-with-task-manager

## Command

```bash
# GUI: Ctrl+Shift+Esc > Processes > Sort by Memory
```

## Description

Uses Windows Task Manager to watch memory for the PoC executable during execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Process Name | memory_leak_poc.exe | Yes |

## Examples

### Basic Usage

Launch Task Manager and filter for the process.

## Expected Output

Memory column shows steady increase.

## Related

- [[Related Procedure: Monitor-Memory-Consumption]]
