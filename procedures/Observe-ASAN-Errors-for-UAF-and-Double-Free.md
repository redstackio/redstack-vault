---
id: proc-libcurl-observe-asan-001
tags:
  - asan
  - uaf
  - double-free
  - debugging
type: procedure
tools:
  - '[[tools/AddressSanitizer]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/run-with-asan-log]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:18.501Z'
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
# Observe-ASAN-Errors-for-UAF-and-Double-Free

## Summary

This procedure captures and analyzes AddressSanitizer output during the stress test to identify UAF and double-free errors on shared connection pointers, confirming the race condition impact.

## Description

Errors manifest in functions like multi_done, reuse_conn, and Curl_attach_connection, where threads (e.g., T18, T22) access freed HTTP/2 add buffers (e.g., 0x604000459250). Adding a random sleep after unlock in url.c:1372 increases consistency. This step validates memory corruption from inadequate synchronization in the connection cache.

## Requirements

1. Running stress test with ASAN enabled
2. Log capture tools (e.g., redirect to file)
3. Knowledge of stack traces for analysis

## Defense

Defensive measures and detection strategies:

- Integrate ASAN in unit tests for multi-threaded code
- Use heap profilers to track buffer lifetimes
- Audit lock/unlock pairs in connection logic

## Objectives

1. Detect UAF on connection items
2. Identify double-free in buffer handling
3. Correlate errors to specific code paths

## Instructions

### Step 1: Run with Enhanced Logging

**Context**: Execute the test with ASAN options to log detailed errors.

**Command** ([[commands/run-with-asan-log]]):
```bash
ASAN_OPTIONS=abort_on_error=1:log_path=asan_log.%p ./curl_test https://http2.example.com 50
```

> Captures errors to files like asan_log.12345. Expected output: Detailed reports with addresses, threads, and stacks showing frees in Curl_add_buffer_free.

### Step 2: Analyze Output

**Context**: Review logs for patterns.

No command; manually inspect logs for indicators like "double-free on 0x604000459250 in thread T22".

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/run-with-asan-log]]

## Tools Used

- [[tools/AddressSanitizer]]

## Tags

- asan
- uaf
- double-free
- debugging
