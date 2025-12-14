---
id: proc-libcurl-reproduce-http2-001
tags:
  - http2
  - debug-build
  - reproduction
type: procedure
tools:
  - '[[tools/clang]]'
  - '[[tools/AddressSanitizer]]'
  - '[[tools/libcurl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/clang-compile-debugit-asan]]'
  - '[[commands/run-debugit-http2]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:18.498Z'
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
# Reproduce-Double-Free-UAF-with-Debug-Build-and-HTTP2

## Summary

This procedure uses a modified debugit.cpp in a multi-threaded setup to reliably reproduce double-free and UAF errors tied to HTTP/2 connection logic, confirming the vulnerability's specificity.

## Description

Targeting HTTP/2 endpoints triggers issues in multi_done (multi.c:556) and Curl_http2_done (http2.c:1183), where freed add buffers are accessed concurrently due to races in attachment. Does not occur with HTTP/1.1, isolating to HTTP/2 handling in http.c:1620 and Curl_add_buffer_free:1152.

## Requirements

1. Debug libcurl build with HTTP/2
2. debugit.cpp modified for multi-threading
3. HTTP/2 server for requests

## Defense

Defensive measures and detection strategies:

- Add reference counting for HTTP/2 buffers
- Synchronize attachment in Curl_attach_connection
- Test with HTTP/2-specific fuzzers

## Objectives

1. Trigger errors in HTTP/2 paths
2. Validate non-occurrence in HTTP/1.1
3. Assess exploitation difficulty

## Instructions

### Step 1: Compile Debug Test

**Context**: Build debugit.cpp with sanitizers.

**Command** ([[commands/clang-compile-debugit-asan]]):
```bash
clang++ -g -fsanitize=address debugit.cpp -o debugit_test -lcurl -lpthread
```

> Includes pthread for threading. Expected output: debugit_test executable.

### Step 2: Run HTTP/2 Reproduction

**Context**: Execute against HTTP/2 to trigger.

**Command** ([[commands/run-debugit-http2]]):
```bash
./debugit_test https://http2.example.com
```

> Runs multi-threaded requests. Expected output: ASAN errors in http2_done, e.g., double-free in thread T22.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/clang-compile-debugit-asan]]
- [[commands/run-debugit-http2]]

## Tools Used

- [[tools/clang]]
- [[tools/AddressSanitizer]]
- [[tools/libcurl]]

## Tags

- http2
- debug-build
- reproduction
