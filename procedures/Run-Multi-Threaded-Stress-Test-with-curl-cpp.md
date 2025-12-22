---
id: proc-libcurl-stress-test-001
tags:
  - stress-test
  - multi-threaded
  - connection-reuse
type: procedure
tools:
  - '[[tools/libcurl]]'
  - '[[tools/AddressSanitizer]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/run-curl-cpp-stress-test]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:18.513Z'
skill_level: advanced
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Run-Multi-Threaded-Stress-Test-with-curl-cpp

## Summary

This procedure executes a C++ program (curl.cpp) that creates multiple threads, each using separate easy handles to perform HTTP requests, forcing libcurl to reuse connections and expose the race condition in CURL_LOCK_DATA_CONNECT sharing.

## Description

The test simulates concurrent access to the connection cache, where threads share the same pointer without proper locking, leading to premature reuse before a connection is marked in-use (url.c:1194). This is particularly evident with HTTP/2 due to additional buffers in http2.c. Run on a sanitized build to catch errors; reproduction may require multiple runs due to timing sensitivity.

## Requirements

1. Compiled curl_test executable with ASAN
2. Access to an HTTP/2 endpoint (e.g., https://http2.github.io)
3. Sufficient system resources for 50+ threads

## Defense

Defensive measures and detection strategies:

- Implement finer-grained locking in connection caches
- Use atomic operations for CONN_INUSE checks
- Fuzz multi-threaded code with tools like ThreadSanitizer

## Objectives

1. Trigger concurrent connection pointer sharing
2. Force race in multi-threaded easy handle usage
3. Observe initial signs of memory instability

## Instructions

### Step 1: Execute Stress Test

**Context**: Launch the test with configurable thread and request counts to stress the connection mechanism.

**Command** ([[commands/run-curl-cpp-stress-test]]):
```bash
./curl_test https://http2.example.com 100  # Threads: 100, Requests per thread: 100
```

> Runs for several minutes, outputting request logs and potential ASAN warnings. Expected output: Thread activity logs, intermittent crashes if race triggers.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/run-curl-cpp-stress-test]]

## Tools Used

- [[tools/libcurl]]
- [[tools/AddressSanitizer]]

## Tags

- stress-test
- multi-threaded
- connection-reuse
