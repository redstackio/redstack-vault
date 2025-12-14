---
id: cmd-022
data: >-
  valgrind --tool=memcheck ./src/curl -v -H "Sec-WebSocket-Key: $(python3 -c
  'print("A"*100)')" -H "Connection: upgrade" -H "Upgrade: websocket" --http1.1
  ws://echo.websocket.org/ 2>&1 | tee boundary_test.log
tags:
  - test
  - valgrind
  - boundary
type: command
output: Valgrind report with no errors
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:27.971Z'
verified: false
validated: true
submitted: true
---
# valgrind-boundary-test

## Command

```bash
valgrind --tool=memcheck ./src/curl -v -H "Sec-WebSocket-Key: $(python3 -c 'print("A"*100)')" -H "Connection: upgrade" -H "Upgrade: websocket" --http1.1 ws://echo.websocket.org/ 2>&1 | tee boundary_test.log
```

## Description

Tests oversized WebSocket key for buffer issues.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$(python3 -c 'print("A"*100)')` | Oversized input | Yes |

## Examples

### Basic Usage

```bash
valgrind ./src/curl -H "Key: AAAA..."
```

## Expected Output

No overflows.

## Related

- [[commands/valgrind-websocket-upgrade]]
