---
tags:
  - gdb
  - crash
  - segfault
type: procedure
tools:
  - '[[tools/gdb]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/gdb-launch-multithread]]'
  - '[[commands/gdb-run-program]]'
  - '[[commands/gdb-backtrace]]'
verified: false
platforms:
  - Linux
  - POSIX
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:24:18.695Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: caecbe3c-4a28-4357-a42c-4c7912405f57
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Reproduce Crash with GDB

## Summary

Executes the multi-threaded curl example under GDB to capture the segmentation fault caused by the libcurl race condition during DNS timeouts.

## Description

With DNS blackholed and short timeout set, running the program triggers concurrent DNS resolutions, leading to corrupted sigjmp_buf in signal handlers and a crash in Curl_failf. GDB captures the backtrace confirming the vulnerability.

## Requirements

1. Compiled multithread binary and libcurl
2. GDB installed
3. Blackhole DNS configured

## Defense

Defensive measures and detection strategies:

- Use core dumps and crash reporting to analyze libcurl failures
- Thread-safe DNS libraries (e.g., c-ares) instead of built-in resolver
- Runtime monitoring for SIGSEGV in curl processes

## Objectives

1. Trigger and observe application crash
2. Analyze stack to confirm race in DNS timeout
3. Validate DoS impact

## Instructions

### Step 1: Launch GDB with Custom Library

**Context**: Start debugger with LD_LIBRARY_PATH for vulnerable libcurl.

**Command** ([[commands/gdb-launch-multithread]]):
```bash
LD_LIBRARY_PATH=./lib/.libs:$LD_LIBRARY_PATH gdb ./multithread
```

> Loads program with symbols. Expected output: GDB prompt; notes on no debug symbols if stripped.

### Step 2: Run the Program

**Context**: Execute to hit timeout and crash.

**Command** ([[commands/gdb-run-program]]):
```bash
r
```

> Runs threads for URL fetches. Expected output: SIGSEGV after ~2s in Thread 1, at Curl_failf.

### Step 3: Capture Backtrace

**Context**: Print stack after segfault.

**Command** ([[commands/gdb-backtrace]]):
```bash
bt
```

> Shows trace. Expected output: #0 in Curl_failf, #1 in Curl_resolv_timeout, confirming race.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/gdb-launch-multithread]]
- [[commands/gdb-run-program]]
- [[commands/gdb-backtrace]]

## Tools Used

- [[tools/gdb]]

## Tags

- debugging
- reproduction
- crash-analysis

