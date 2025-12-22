---
id: proc-uuid-2
tags:
  - asan
  - squid-build
  - debugging
type: procedure
tools:
  - '[[tools/AddressSanitizer]]'
  - '[[tools/gcc]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/configure-squid-with-asan]]'
  - '[[commands/run-squid-with-asan]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:19.228Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Build-and-Run-Squid-with-AddressSanitizer

## Summary

This procedure compiles Squid Cache from source with AddressSanitizer (ASAN) enabled to detect heap overflows, then runs it in foreground mode for reproduction and debugging of the vulnerability.

## Description

ASAN instruments the code to catch memory errors like the heap overflow in base64 decoding. Building with -fsanitize=address and running with abort_on_error=true allows observation of the overflow when the crafted request is sent. This is essential for verifying the vulnerability on Linux systems with gcc support.

## Requirements

1. Squid source code downloaded
2. gcc compiler with ASAN support
3. Build dependencies for Squid (e.g., make, autotools)
4. Root or sufficient privileges to compile and run

## Defense

Defensive measures and detection strategies:

- Avoid running production Squid with debug sanitizers
- Patch Squid to fix buffer bounds checking
- Use memory-safe languages or additional runtime checks
- Log and alert on ASAN-detected errors in staging

## Objectives

1. Enable runtime detection of heap overflows
2. Reproduce the vulnerability in a controlled environment
3. Capture detailed error reports for analysis

## Instructions

### Step 1: Configure Build with ASAN

**Context**: Set compiler flags to include ASAN for overflow detection during compilation.

**Command** ([[commands/configure-squid-with-asan]]):
```bash
CFLAGS="-O0 -g -fsanitize=address" CXXFLAGS="${CFLAGS}" ./configure
```

> Configures Squid build with no optimization (-O0), debug symbols (-g), and ASAN (-fsanitize=address). Expected output: Successful configure script completion.

### Step 2: Build Squid

**Context**: Compile the source after configuration.

**Command** (Standard make):
```bash
make
make install
```

> Builds the Squid binary with ASAN instrumentation. Expected output: Compiled sbin/squid executable.

### Step 3: Run Squid with ASAN Options

**Context**: Launch Squid in foreground with ASAN configured to abort on errors and high debug verbosity.

**Command** ([[commands/run-squid-with-asan]]):
```bash
ASAN_OPTIONS="abort_on_error=true" ./sbin/squid --foreground -d 100
```

> Starts Squid; -d 100 enables detailed logging, --foreground keeps it in terminal. Expected output: Startup logs and readiness for requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/configure-squid-with-asan]]
- [[commands/run-squid-with-asan]]

## Tools Used

- [[tools/AddressSanitizer]]
- [[tools/gcc]]

## Tags

- asan
- squid-build
- debugging
