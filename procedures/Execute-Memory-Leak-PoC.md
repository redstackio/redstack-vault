---
tags:
  - memory-leak
  - dos
  - poc-execution
type: procedure
tools:
  - '[[tools/getrusage]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/run-memory-leak-poc]]'
  - '[[commands/c-loop-memory-leak-demo]]'
verified: false
platforms:
  - Linux
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:28:28.300Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[OS Exhaustion Flood]]'
id: 05a33802-622f-4b53-a8c8-8809cc553644
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Execute-Memory-Leak-PoC

## Summary

This procedure runs the compiled PoC to repeatedly invoke the vulnerable `bytes_to_hexstring` function, allocating memory without freeing it, and uses getrusage to log increasing consumption, simulating DoS in long-running Hyperledger Fabric applications.

## Description

Execution triggers the memory leak by calling malloc in a loop without free, and for large len values, the integer overflow in size_t k = len * 2 + 1 can cause buffer overflows on 32-bit systems. The PoC runs 1,000,000 iterations on a 10-byte sample array, printing memory every 100,000 iterations via getrusage(RUSAGE_SELF). Expected outcome: Memory usage rises from ~1776 KB to over 32,000 KB.

## Requirements

1. Compiled executable memory_leak_poc
2. Permissions to execute binaries
3. System with sufficient initial memory to observe growth

## Defense

Defensive measures and detection strategies:

- Add free() calls after using returned strings and check malloc for NULL
- Use 64-bit integers for size calculations to prevent overflow
- Deploy runtime memory profilers like AddressSanitizer

## Objectives

1. Trigger repeated memory allocations to exhaust resources
2. Log memory usage to quantify the leak
3. Demonstrate potential for system instability or DoS

## Instructions

### Step 1: Run the Executable

**Context**: Launch the PoC to start the loop of vulnerable function calls.

**Command** ([[commands/run-memory-leak-poc]]):
```bash
./memory_leak_poc
```

> Executes the binary, outputting 'Starting memory leak test...' followed by iteration and memory logs. Expected: Gradual memory increase without crashes.

### Step 2: Include Loop in Custom Code

**Context**: For custom reproduction, embed a loop like the extracted example to call bytes_to_hexstring without free.

**Command** ([[commands/c-loop-memory-leak-demo]]):
```c
for (int i = 0; i < 10000; i++) { uint8_t data[10] = {0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09}; char* hex_str = bytes_to_hexstring(data, 10); // Do something with hex_str but forget to free it }
```

> Simulates the leak in application code; monitor externally as no output, but memory grows.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques

- [[OS Exhaustion Flood]]

## Commands Used

- [[commands/run-memory-leak-poc]]
- [[commands/c-loop-memory-leak-demo]]

## Tools Used

- [[tools/getrusage]]

## Tags

- memory-leak
- dos
