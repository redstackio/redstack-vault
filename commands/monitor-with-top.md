---
data: top -p $(pgrep memory_leak_poc)
tags:
  - monitoring
type: command
output: Real-time process stats showing increasing RSS memory
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.288Z'
id: 25b8a9ef-ac73-4a88-a812-6d5c96ebc09e
verified: false
validated: true
submitted: true
---
# monitor-with-top

## Command

```bash
top -p $(pgrep memory_leak_poc)
```

## Description

Monitors the specific PoC process memory usage on Linux to observe leak-induced growth.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p $(pgrep memory_leak_poc)` | PID of the process | Yes |

## Examples

### Basic Usage

```bash
top -p $(pgrep memory_leak_poc)
```

## Expected Output

Interactive display with RSS column rising from 1776 KB to 32,000+ KB.

## Related

- [[Related Procedure: Monitor-Memory-Consumption]]
