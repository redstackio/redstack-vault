---
tags:
  - memory-analysis
  - valgrind
  - double-free
type: procedure
tools:
  - '[[tools/Valgrind]]'
  - '[[tools/pngcrush]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/pngcrush-process-splt-png]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:37.374Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 99b36b98-5ecb-4c76-ad81-2786a580407a
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Analyze-Memory-Errors-with-Valgrind

## Summary

This procedure uses Valgrind to dynamically analyze memory errors in pngcrush execution, identifying the double-free and invalid pointer issues that lead to the segmentation fault when processing sPLT chunks.

## Description

Valgrind's memcheck tool detects invalid reads, frees, and uninitialized values during runtime. In this scenario, it reveals the double-free in png_free_data (png.c:542) on sPLT chunk memory allocated by png_set_sPLT and png_handle_sPLT. This analysis confirms the vulnerability's root cause and helps in debugging without relying solely on crash dumps. Prerequisites include Valgrind installation and the vulnerable pngcrush setup.

## Requirements

1. Valgrind installed on Linux
2. Vulnerable pngcrush and sPLT PNG file
3. Basic familiarity with memory debugging output

## Defense

Defensive measures and detection strategies:

- Integrate Valgrind or AddressSanitizer in CI/CD for software testing
- Log and alert on memory error patterns in production environments
- Avoid processing untrusted PNGs in automated tools

## Objectives

1. Detect invalid memory operations in pngcrush
2. Trace double-free to sPLT handling code
3. Validate vulnerability for reporting or patching

## Instructions

### Step 1: Run Valgrind on pngcrush

**Context**: Instrument the vulnerable pngcrush execution with Valgrind to capture all memory events.

**Command** ([[commands/pngcrush-process-splt-png]]):
```bash
valgrind --tool=memcheck ./pngcrush -reduce -brute ps1n0g08.png /dev/null
```

> Valgrind wraps the execution, reporting errors like invalid read of size 8 at address 0x..., invalid free, and 'Address 0x5555555555555555 is not stack'd, malloc'd or (recently) free'd'. Allocation stack traces back to png_set_sPLT.

**Expected Output**: Detailed error log including 'Invalid read of size 8' at png_free_data (png.c:542), 'Invalid free() / delete' at same location, and summary of 2 errors in 1 blocks possibly lost.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/pngcrush-process-splt-png]]

## Tools Used

- [[tools/Valgrind]]

## Tags

- memory-analysis
- valgrind
- double-free
