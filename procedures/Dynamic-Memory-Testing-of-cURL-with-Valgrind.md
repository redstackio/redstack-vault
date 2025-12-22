---
id: proc-003
tags:
  - dynamic-analysis
  - valgrind
  - memory-testing
  - curl
type: procedure
tools:
  - '[[tools/valgrind]]'
  - '[[tools/python3]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/valgrind-websocket-upgrade]]'
  - '[[commands/valgrind-ssl-test]]'
  - '[[commands/valgrind-ssl-error-test]]'
  - '[[commands/valgrind-boundary-test]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:28:28.091Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Dynamic-Memory-Testing-of-cURL-with-Valgrind

## Summary

This procedure runs Valgrind memcheck on cURL invocations for WebSocket upgrades, SSL requests, error handling, and boundary inputs to detect buffer overflows or leaks in vulnerable components.

## Description

Dynamic testing simulates attack paths like oversized WebSocket keys or invalid certs to trigger potential strcpy() overflows. Using --tool=memcheck with leak checks, it logs outputs to files. No overflows were triggered due to length checks, but risks for corruption/DoS remain. Requires built cURL and internet for test endpoints.

## Requirements

1. Built cURL binary with sanitizers
2. Valgrind installed
3. Network access to ws://echo.websocket.org and https://httpbin.org
4. Python3 for input generation

## Defense

Defensive measures and detection strategies:

- Run applications under Valgrind in staging
- Monitor for memory errors in production logs
- Fuzz test with AFL++ for boundary conditions

## Objectives

1. Test WebSocket, SSL, and error paths
2. Detect invalid memory accesses
3. Validate boundary handling

## Instructions

### Step 1: WebSocket Upgrade Test

**Context**: Check for overflows during protocol upgrade.

**Command** ([[commands/valgrind-websocket-upgrade]]):
```bash
valgrind --tool=memcheck --leak-check=full --track-origins=yes ./src/curl -v -H "Connection: upgrade" -H "Upgrade: websocket" -H "Sec-WebSocket-Version: 13" --http1.1 ws://echo.websocket.org/ 2>&1 | tee websocket_test.log
```

> Logs potential errors in ws.c:1261.

### Step 2: SSL Backend Test

**Context**: Enumerate backends for buffer issues.

**Command** ([[commands/valgrind-ssl-test]]):
```bash
valgrind --tool=memcheck --leak-check=full ./src/curl -v https://httpbin.org/get 2>&1 | tee ssl_test.log
```

> Tests vtls.c:1066.

### Step 3: SSL Error Handling Test

**Context**: Trigger WolfSSL errors with bad cert.

**Command** ([[commands/valgrind-ssl-error-test]]):
```bash
valgrind --tool=memcheck --leak-check=full ./src/curl -v --cert /nonexistent/cert.pem https://httpbin.org/get 2>&1 | tee ssl_error_test.log
```

> Checks wolfssl.c:1540.

### Step 4: Boundary Condition Test

**Context**: Use oversized key to probe limits.

**Command** ([[commands/valgrind-boundary-test]]):
```bash
valgrind --tool=memcheck ./src/curl -v -H "Sec-WebSocket-Key: $(python3 -c 'print("A"*100)')" -H "Connection: upgrade" -H "Upgrade: websocket" --http1.1 ws://echo.websocket.org/ 2>&1 | tee boundary_test.log
```

> Generates 100 'A's input.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques

- None

## Commands Used

- [[commands/valgrind-websocket-upgrade]]
- [[commands/valgrind-ssl-test]]
- [[commands/valgrind-ssl-error-test]]
- [[commands/valgrind-boundary-test]]

## Tools Used

- [[tools/valgrind]]
- [[tools/python3]]

## Tags

- [[dynamic-analysis]]
- [[tools/valgrind]]
- [[memory-testing]]
- [[curl]]
