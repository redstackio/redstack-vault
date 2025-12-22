---
tags:
  - race-condition
  - libcurl
  - denial-of-service
  - dns-timeout
  - siglongjmp
type: attack_chain
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
complexity: medium
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Patch-libcurl-to-Enable-Alarm-Timeout]]'
  - '[[procedures/Build-Modified-libcurl-Library]]'
  - '[[procedures/Modify-and-Compile-Multi-Threaded-curl-Example]]'
  - '[[procedures/Configure-DNS-to-Blackhole-Server]]'
  - '[[procedures/Reproduce-Crash-with-GDB]]'
step_count: 5
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:24:18.730Z'
description: >-
  Demonstrates exploitation of a race condition in libcurl's synchronous DNS
  resolver using alarm timeouts, leading to application crashes in
  multi-threaded environments without proper threading support.
skill_level: intermediate
impact_level: high
id: 0d81c1b5-aaf8-4182-9971-84d7a3e30c4d
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# libcurl Siglongjmp Race Condition for Multi-Threaded DNS Denial of Service

Multi-stage attack chain demonstrating reproduction of CVE-2023-28320, a race condition in libcurl's DNS resolver that causes segmentation faults in multi-threaded applications during timeouts on platforms without threading support.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Patch libcurl Source] --> B[Compile Modified libcurl]
    B --> C[Compile Multi-Threaded Example]
    C --> D[Configure Blackhole DNS]
    D --> E[Execute and Trigger Crash]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/gdb]]
- Compiler tools (gcc, make)
- libcurl source code

### Target Environment

- Linux/POSIX platform without full threading support (e.g., older systems or specific configs)
- Access to libcurl source and build environment
- No specific ports or services; local compilation and execution

### Initial Access Requirements

- Source code access to libcurl (e.g., from curl.se)
- Development environment with C compiler
- No credentials or network position needed beyond local setup

## Detailed Attack Procedures

### Step 1: Patch libcurl to Enable Alarm Timeout
procedure: [[procedures/Patch-libcurl-to-Enable-Alarm-Timeout]]

**Objective**: Force libcurl to use the vulnerable alarm-based timeout codepath for DNS resolutions.

**Instructions**: Apply a patch to define USE_ALARM_TIMEOUT in lib/hostip.c to enable the synchronous resolver path.

**Expected Output**: Modified source file ready for compilation.

**Success Indicators**:
- Patch applied without errors
- #define USE_ALARM_TIMEOUT visible in hostip.c

### Step 2: Build Modified libcurl Library
procedure: [[procedures/Build-Modified-libcurl-Library]]

**Objective**: Compile the patched libcurl source to produce a vulnerable library.

**Instructions**: Use standard build commands to compile libcurl after patching.

**Expected Output**: libcurl.so.4 built in ./lib/.libs/.

**Success Indicators**:
- Build completes successfully
- Library file generated

### Step 3: Modify and Compile Multi-Threaded curl Example
procedure: [[procedures/Modify-and-Compile-Multi-Threaded-curl-Example]]

**Objective**: Adapt the official multi-threaded example to trigger short DNS timeouts.

**Instructions**: Download the example from curl.se, add CURLOPT_TIMEOUT=2, and compile against the modified libcurl.

**Expected Output**: Executable multithread binary.

**Success Indicators**:
- Compilation succeeds
- Timeout option integrated

### Step 4: Configure DNS to Blackhole Server
procedure: [[procedures/Configure-DNS-to-Blackhole-Server]]

**Objective**: Redirect DNS queries to a non-responsive server to force timeouts.

**Instructions**: Update /etc/resolv.conf to point to 3.219.212.117 (blackhole.webpagetest.org).

**Expected Output**: DNS queries timeout consistently.

**Success Indicators**:
- DNS resolution fails with timeouts
- No responses from blackhole server

### Step 5: Reproduce Crash with GDB
procedure: [[procedures/Reproduce-Crash-with-GDB]]

**Objective**: Run the multi-threaded program under debugger to capture the segmentation fault.

**Instructions**: Launch with custom library path using [[commands/gdb-launch-multithread]], then [[commands/gdb-run-program]], and [[commands/gdb-backtrace]] on crash.

```bash
LD_LIBRARY_PATH=./lib/.libs:$LD_LIBRARY_PATH gdb ./multithread
r
bt
```

**Expected Output**: SIGSEGV in Curl_failf during Curl_resolv_timeout.

**Success Indicators**:
- Program crashes with segfault
- Backtrace shows race in DNS timeout handler

## Attack Chain Summary

### Key Achievements

1. Enabled vulnerable alarm timeout path in libcurl
2. Reproduced multi-threaded DNS race condition
3. Confirmed DoS via application crash

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]]

### MITRE ATT&CK Tactics

- [[Impact]]

---
*Last updated: 2024-01-01T00:00:00Z*
