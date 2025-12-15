---
tags:
  - dos
  - double-free
  - pngcrush
type: procedure
tools:
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
updated_at: '2025-12-14T17:26:37.376Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 34fb4fec-90fc-4ca5-855d-20cdfbf215c9
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Trigger-Double-Free-Crash-in-pngcrush

## Summary

This procedure exploits a double-free vulnerability in pngcrush versions prior to 1.7.87 by processing a PNG file with an sPLT chunk, leading to memory corruption, segmentation fault, and application denial-of-service.

## Description

The vulnerability occurs during the handling of the sPLT chunk in PNG files, where png_free_data is called twice on the same memory allocation without null checks, causing invalid memory operations and a crash in libc_free. This can affect any service or script using pngcrush for PNG optimization, such as image processing pipelines. The procedure requires a vulnerable installation and a test PNG file like ps1n0g08.png containing the sPLT chunk. Expected outcome is immediate application termination via SIGSEGV, demonstrating DoS potential.

## Requirements

1. pngcrush version < 1.7.87 installed on Linux
2. PNG file with sPLT chunk (e.g., download or craft ps1n0g08.png)
3. Local execution privileges

## Defense

Defensive measures and detection strategies:

- Upgrade to pngcrush 1.7.87 or later, which removes the erroneous double-free
- Input validation to reject or strip sPLT chunks in PNG processing services
- Monitor for segfaults in logs and use memory sanitizers in development

## Objectives

1. Induce memory corruption via double-free in sPLT handling
2. Cause pngcrush application crash
3. Demonstrate DoS impact on PNG processing

## Instructions

### Step 1: Prepare the Environment

**Context**: Ensure vulnerable pngcrush is available and obtain the test PNG file with sPLT chunk.

Download or place ps1n0g08.png in the working directory.

### Step 2: Execute pngcrush to Trigger Crash

**Context**: Run pngcrush with optimization options on the sPLT-containing PNG, which forces double-free during chunk freeing.

**Command** ([[commands/pngcrush-process-splt-png]]):
```bash
./pngcrush -reduce -brute ps1n0g08.png /dev/null
```

> This command processes ps1n0g08.png using -reduce to minimize chunks and -brute for method selection, outputting to /dev/null. It triggers invalid reads/writes in png_free_data (png.c:542), leading to SIGSEGV in libc_free due to double-free on sPLT allocation.

**Expected Output**: Partial optimization output like 'Best pngcrush method = 105 ... total 3.320 sec.' followed by 'Segmentation fault (core dumped)'.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/pngcrush-process-splt-png]]

## Tools Used

- [[tools/pngcrush]]

## Tags

- dos
- double-free
- pngcrush
