---
tags:
  - memory-leak
  - poc-compilation
  - c-vulnerability
type: procedure
tools:
  - '[[tools/gcc]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/gcc-compile-memory-leak-poc]]'
verified: false
platforms:
  - Linux
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:28:28.304Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[OS Exhaustion Flood]]'
id: 1666f3d7-a7d3-43bc-b2e2-ca70a507d4f3
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Compile-Memory-Leak-PoC

## Summary

This procedure compiles a proof-of-concept C program that includes the vulnerable `bytes_to_hexstring` function from Hyperledger Fabric's utils.c and a loop to demonstrate memory allocation without freeing, preparing for execution to show the leak.

## Description

The `bytes_to_hexstring` function in common/utils.c allocates memory with malloc(len * 2 + 1) but does not free it, lacking error handling for NULL returns. This PoC replicates the function and calls it repeatedly. Compilation uses GCC on Linux or Windows environments with standard C libraries. Prerequisites include the source code file memory_leak_poc.c containing the vulnerable code and test loop.

## Requirements

1. GCC compiler installed
2. Source file memory_leak_poc.c with vulnerable function and loop
3. Standard C library access (malloc, stdio, stdlib)

## Defense

Defensive measures and detection strategies:

- Use static analysis tools like Coverity to detect leaks during code review
- Implement memory sanitizers (e.g., Valgrind) in CI/CD pipelines
- Monitor application memory usage in production with tools like Prometheus

## Objectives

1. Produce an executable PoC for testing the memory leak
2. Verify compilation without errors related to the vulnerable code
3. Prepare for demonstration of resource exhaustion

## Instructions

### Step 1: Prepare Source File

**Context**: Ensure the C source includes the `bytes_to_hexstring` function at line 33 and a main loop calling it 1,000,000 times without free.

No command needed; edit memory_leak_poc.c manually.

### Step 2: Compile with GCC

**Context**: Compile the source to create the binary, linking standard libraries implicitly.

**Command** ([[commands/gcc-compile-memory-leak-poc]]):
```bash
gcc memory_leak_poc.c -o memory_leak_poc
```

> Compiles the C file into an executable. Expected output: No errors, file 'memory_leak_poc' created.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques

- [[OS Exhaustion Flood]]

## Commands Used

- [[commands/gcc-compile-memory-leak-poc]]

## Tools Used

- [[tools/gcc]]

## Tags

- memory-leak
- poc-compilation
