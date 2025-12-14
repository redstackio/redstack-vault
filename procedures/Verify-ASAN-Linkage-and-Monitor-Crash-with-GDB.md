---
id: proc-uuid-3
tags:
  - gdb
  - asan-verify
  - crash-analysis
type: procedure
tools:
  - '[[tools/GDB]]'
  - '[[tools/ldd]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/check-asan-with-ldd]]'
  - '[[commands/check-asan-with-proc-maps]]'
  - '[[commands/find-squid-pid]]'
  - '[[commands/attach-gdb-to-squid]]'
  - '[[commands/gdb-backtrace]]'
  - '[[commands/gdb-print-decodedlen]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:19.224Z'
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
# Verify-ASAN-Linkage-and-Monitor-Crash-with-GDB

## Summary

This procedure checks if AddressSanitizer is properly linked to the Squid binary or process, then attaches GDB to monitor the crash triggered by the exploit, capturing backtraces and variable values to confirm the heap overflow.

## Description

After building with ASAN, verify linkage using ldd or procfs maps. Upon sending the exploit, Squid aborts due to overflow; GDB attachment allows inspection of the call stack (from base64_decode to CacheManager::ParseHeaders) and the decodedLen variable exceeding 8192 bytes. This confirms the vulnerability on Linux.

## Requirements

1. Running Squid process with ASAN
2. GDB installed
3. Access to /proc filesystem for PID inspection
4. Exploit request already sent to trigger crash

## Defense

Defensive measures and detection strategies:

- Disable GDB attachments in production (e.g., via ptrace restrictions)
- Monitor for SIGABRT signals in Squid processes
- Use intrusion detection for anomalous proxy requests
- Regularly audit binary linkages for debug tools

## Objectives

1. Confirm ASAN instrumentation is active
2. Capture crash details for vulnerability analysis
3. Validate overflow parameters like decodedLen

## Instructions

### Step 1: Check ASAN Linkage with ldd

**Context**: Verify if the Squid binary is dynamically linked to libasan.

**Command** ([[commands/check-asan-with-ldd]]):
```bash
ldd squid | grep asan
```

> Lists dependencies; looks for libasan.so. Expected output: libasan.so.5 => /usr/lib/libasan.so.5 if linked.

### Step 2: Alternative Check with Proc Maps

**Context**: For running process, search memory maps for ASAN libraries.

**Command** ([[commands/check-asan-with-proc-maps]]):
```bash
grep asan /proc/<Squid PID>/maps
```

> Replace <Squid PID> with actual PID; expected output: Lines with 'asan' if loaded.

### Step 3: Find Squid Child PID

**Context**: Identify the correct process ID for attachment, focusing on the child process.

**Command** ([[commands/find-squid-pid]]):
```bash
pgrep squid | tail -n 1
```

> Gets the last (child) PID. Expected output: Numeric PID.

### Step 4: Attach GDB to Process

**Context**: Quietly attach GDB to the crashing Squid process.

**Command** ([[commands/attach-gdb-to-squid]]):
```bash
gdb -q -p $(pgrep squid | tail -n 1)
```

> Attaches to PID; expected output: GDB prompt.

### Step 5: Capture Backtrace on Crash

**Context**: After SIGABRT, print the call stack to locate the overflow.

**Command** ([[commands/gdb-backtrace]]):
```bash
(gdb) bt
```

> Shows stack from raise() to base64 decoding in CacheManager::ParseHeaders. Expected output: Detailed backtrace.

### Step 6: Print Overflowed Variable

**Context**: Inspect decodedLen to confirm it exceeds buffer size.

**Command** ([[commands/gdb-print-decodedlen]]):
```bash
(gdb) p decodedLen
```

> Prints variable value. Expected output: $21 = 43011 (or similar >8192).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/check-asan-with-ldd]]
- [[commands/check-asan-with-proc-maps]]
- [[commands/find-squid-pid]]
- [[commands/attach-gdb-to-squid]]
- [[commands/gdb-backtrace]]
- [[commands/gdb-print-decodedlen]]

## Tools Used

- [[tools/GDB]]
- [[tools/ldd]]

## Tags

- gdb
- asan-verify
- crash-analysis
