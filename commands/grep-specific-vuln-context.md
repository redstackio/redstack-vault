---
id: cmd-024
data: 'grep -A5 -B5 "ws.c:1261\|vtls.c:1066\|wolfssl.c:1540" *.log'
tags:
  - search
  - context
type: command
output: Context around mentions if any
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:27.958Z'
verified: false
validated: true
submitted: true
---
# grep-specific-vuln-context

## Command

```bash
grep -A5 -B5 "ws.c:1261\|vtls.c:1066\|wolfssl.c:1540" *.log
```

## Description

Grep with context for specific vuln lines in logs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-A5 -B5` | Context lines | Yes |

## Examples

### Basic Usage

```bash
grep -A5 "ws.c:1261" *.log
```

## Expected Output

Context if matched.

## Related

- [[procedures/Analyzing-Valgrind-Logs-for-Memory-Errors]]
