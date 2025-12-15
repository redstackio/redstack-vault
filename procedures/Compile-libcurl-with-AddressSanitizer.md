---
id: proc-libcurl-compile-asan-001
tags:
  - compilation
  - sanitizer
  - debug-build
type: procedure
tools:
  - '[[tools/clang]]'
  - '[[tools/AddressSanitizer]]'
  - '[[tools/libcurl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/clang-compile-libcurl-asan]]'
  - '[[commands/clang-compile-curl-cpp-asan]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:18.531Z'
skill_level: advanced
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Compile-libcurl-with-AddressSanitizer

## Summary

This procedure compiles libcurl from source and a custom C++ test file using Clang with AddressSanitizer enabled, preparing the environment to detect memory errors such as use-after-free and double-free in multi-threaded connection handling.

## Description

In the context of reproducing the libcurl race condition, this step sets up a debug build by cloning the libcurl GitHub repository, configuring it with debug and HTTP/2 support, and compiling with ASAN flags. The test code (curl.cpp) is also built to link against this sanitized library. This enables runtime detection of heap issues stemming from inadequate synchronization in CURL_LOCK_DATA_CONNECT, particularly in url.c and multi.c. Prerequisites include a Linux system with Clang and nghttp2 libraries installed.

## Requirements

1. Linux environment with Clang compiler and development headers
2. Git to clone libcurl source
3. nghttp2 library for HTTP/2 support
4. Custom curl.cpp file implementing multi-threaded easy handles

## Defense

Defensive measures and detection strategies:

- Use static analysis tools like Coverity during development to catch synchronization issues
- Enable thread sanitizers in CI/CD pipelines to detect races early
- Monitor for ASAN-like errors in production crash logs using tools like Crashpad

## Objectives

1. Produce a sanitized libcurl build for error instrumentation
2. Compile test executable to exercise connection reuse
3. Ensure HTTP/2 is enabled for vulnerability triggering

## Instructions

### Step 1: Clone and Configure libcurl

**Context**: Fetch the latest source and prepare for debug build.

**Command** ([[commands/clang-compile-libcurl-asan]]):
```bash
git clone https://github.com/curl/curl.git
cd curl
./configure --enable-debug --with-nghttp2
make clean
make
```

> This configures and builds libcurl with debug symbols and HTTP/2, taking about 5-10 minutes. Expected output: libcurl.a or libcurl.so in the build directory.

### Step 2: Compile Test Code with ASAN

**Context**: Build the C++ reproduction code with sanitizer flags.

**Command** ([[commands/clang-compile-curl-cpp-asan]]):
```bash
clang++ -g -fsanitize=address -fsanitize=undefined -I/path/to/curl/include curl.cpp -o curl_test -L/path/to/curl/lib -lcurl
```

> Links against the built libcurl, enabling ASAN for heap checks. Expected output: curl_test executable ready for execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/clang-compile-libcurl-asan]]
- [[commands/clang-compile-curl-cpp-asan]]

## Tools Used

- [[tools/clang]]
- [[tools/AddressSanitizer]]
- [[tools/libcurl]]

## Tags

- compilation
- sanitizer
- libcurl
