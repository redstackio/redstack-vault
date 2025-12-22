---
id: cmd-023
data: >-
  grep -n "Invalid\|heap-buffer-overflow\|stack-buffer-overflow\|ERROR SUMMARY"
  *.log
tags:
  - search
  - logs
type: command
output: Lines with errors if any
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:27.966Z'
verified: false
validated: true
submitted: true
---
# grep-log-errors

## Command

```bash
grep -n "Invalid\|heap-buffer-overflow\|stack-buffer-overflow\|ERROR SUMMARY" *.log
```

## Description

Searches logs for memory errors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-n` | Line numbers | Yes |
| `*.log` | Files | Yes |

## Examples

### Basic Usage

```bash
grep -n "ERROR" *.log
```

## Expected Output

No matches or error lines.

## Related

- [[procedures/Analyzing-Valgrind-Logs-for-Memory-Errors]]
