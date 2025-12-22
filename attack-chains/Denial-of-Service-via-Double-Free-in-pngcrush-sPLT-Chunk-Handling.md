---
tags:
  - dos
  - memory-corruption
  - double-free
  - pngcrush
  - cve-2015-7700
type: attack_chain
tools:
  - '[[tools/pngcrush]]'
  - '[[tools/Valgrind]]'
  - '[[tools/GDB]]'
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Trigger-Double-Free-Crash-in-pngcrush]]'
  - '[[procedures/Analyze-Memory-Errors-with-Valgrind]]'
  - '[[procedures/Debug-Segfault-with-GDB]]'
step_count: 3
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:37.379Z'
description: >-
  A multi-stage attack chain exploiting a double-free vulnerability in pngcrush
  versions prior to 1.7.87 to cause a segmentation fault and application crash,
  resulting in denial-of-service when processing PNG files with sPLT chunks.
skill_level: intermediate
impact_level: high
id: e2ba7f16-b053-48a2-a569-afec1a6d920f
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Denial-of-Service via Double-Free in pngcrush sPLT Chunk Handling

Multi-stage attack chain demonstrating exploitation of a double-free vulnerability in pngcrush to trigger a segmentation fault and denial-of-service by processing a maliciously crafted PNG file with an sPLT chunk.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Trigger Vulnerability] --> B[Analyze Memory Errors]
    B --> C[Debug Crash]
    C --> D[DoS Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/pngcrush]]
- [[tools/Valgrind]]
- [[tools/GDB]]

### Target Environment

- Linux OS
- Vulnerable pngcrush version < 1.7.87
- PNG file with sPLT chunk (e.g., ps1n0g08.png)

### Initial Access Requirements

- Local access to run pngcrush on the target system
- No network access required; affects local or service-integrated processing

## Detailed Attack Procedures

### Step 1: Trigger the Vulnerability
procedure: [[procedures/Trigger-Double-Free-Crash-in-pngcrush]]

**Objective**: Process a PNG file containing an sPLT chunk with vulnerable pngcrush to induce a double-free and segmentation fault, causing application crash.

**Instructions**: Obtain a PNG file with an sPLT chunk (e.g., ps1n0g08.png) and execute the pngcrush command to optimize it, which triggers the memory corruption during chunk handling.

Use [[commands/pngcrush-process-splt-png]]:

```bash
./pngcrush -reduce -brute ps1n0g08.png /dev/null
```

**Expected Output**: Application crashes with SIGSEGV; output may include optimization summary before fault, such as 'Best pngcrush method = 105 ... total 3.320 sec.' followed by segmentation fault.

**Success Indicators**:
- Segmentation fault occurs
- Application terminates unexpectedly

### Step 2: Analyze Memory Errors
procedure: [[procedures/Analyze-Memory-Errors-with-Valgrind]]

**Objective**: Use Valgrind to detect and confirm memory management issues like invalid reads, frees, and pointer errors during the pngcrush execution.

**Instructions**: Run the vulnerable command under Valgrind to capture detailed memory error reports, focusing on double-free in png_free_data.

Launch Valgrind with the pngcrush command:

```bash
valgrind --tool=memcheck ./pngcrush -reduce -brute ps1n0g08.png /dev/null
```

**Expected Output**: Valgrind reports invalid read of size 8 at png_free_data (png.c:542), invalid free at the same location, and unaddressable byte issues; allocation traced to png_set_sPLT and png_handle_sPLT; pointer 0x5555555555555555 not found.

**Success Indicators**:
- Double-free detected
- Invalid memory access confirmed

### Step 3: Debug the Crash
procedure: [[procedures/Debug-Segfault-with-GDB]]

**Objective**: Attach GDB to the crashing process to inspect the backtrace and registers, identifying the exact point of failure in libc_free.

**Instructions**: Compile pngcrush with debug symbols if needed, run under GDB, and execute backtrace and register inspection commands upon segfault.

Start GDB:

```bash
gdb --args ./pngcrush -reduce -brute ps1n0g08.png /dev/null
```

Then run `(gdb) run` to trigger, and upon crash:

Use [[commands/gdb-backtrace]]:

```bash
(gdb) bt
```

And [[commands/gdb-info-registers]]:

```bash
(gdb) i r
```

**Expected Output**: Backtrace shows libc_free (malloc.c:3709) called from png_free_data (png.c:542) to main (pngcrush.c:6061); registers include rdi=0x5555555555555555 (invalid pointer), rip=0x7ffff784a939.

**Success Indicators**:
- Backtrace confirms double-free call chain
- Invalid pointer in registers identified

## Attack Chain Summary

### Key Achievements

1. Successfully triggered double-free vulnerability in pngcrush via sPLT chunk processing
2. Confirmed memory corruption with Valgrind analysis
3. Debugged segfault root cause using GDB backtrace and registers

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]

---
*Last updated: 2023-10-01T00:00:00Z*
