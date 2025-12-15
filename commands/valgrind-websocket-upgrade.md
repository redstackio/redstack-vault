---
id: cmd-019
data: >-
  valgrind --tool=memcheck --leak-check=full --track-origins=yes ./src/curl -v
  -H "Connection: upgrade" -H "Upgrade: websocket" -H "Sec-WebSocket-Version:
  13" --http1.1 ws://echo.websocket.org/ 2>&1 | tee websocket_test.log
tags:
  - test
  - valgrind
  - websocket
type: command
output: 'Valgrind report, e.g., no errors'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:27.994Z'
verified: false
validated: true
submitted: true
---
# valgrind-websocket-upgrade

## Command

```bash
valgrind --tool=memcheck --leak-check=full --track-origins=yes ./src/curl -v -H "Connection: upgrade" -H "Upgrade: websocket" -H "Sec-WebSocket-Version: 13" --http1.1 ws://echo.websocket.org/ 2>&1 | tee websocket_test.log
```

## Description

Runs Valgrind on cURL WebSocket upgrade test, logging to file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--tool=memcheck` | Memory tool | Yes |
| `2>&1 | tee ...` | Log output | Yes |

## Examples

### Basic Usage

```bash
valgrind --tool=memcheck ./src/curl ws://example.com
```

## Expected Output

==PID== HEAP SUMMARY: no leaks.

## Related

- [[procedures/Dynamic-Memory-Testing-of-cURL-with-Valgrind]]
