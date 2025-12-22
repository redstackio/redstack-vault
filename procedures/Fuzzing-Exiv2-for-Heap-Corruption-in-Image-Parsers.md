---
tags:
  - heap-overflow
  - oob-read
  - exiv2
  - image-parser
type: procedure
tools:
  - '[[tools/American-Fuzzy-Lop-AFL]]'
  - '[[tools/Address-Sanitizer-ASAN]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Process Injection]]'
updated_at: '2025-12-14T17:24:31.108Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 8ee9517e-3f75-49b5-9999-06728335248c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Process Injection]]'
---
# Fuzzing Exiv2 for Heap Corruption in Image Parsers

## Summary

This procedure fuzzes exiv2 library with AFL and ASAN to uncover heap overflows and OOB reads in TIFF, JP2, and WebP parsers, enabling potential RCE via metadata handling.

## Description

Exiv2's ul2Data overflows by one byte in TIFF; JP2 memcpy exceeds buffer; WebP memcmp reads beyond stack. Fuzz malformed files to trigger. Targets image processing apps on Linux.

## Requirements

1. Exiv2 source compiled with ASAN
2. AFL for fuzzing
3. Malformed image files (TIFF/JP2/WebP)
4. Image viewers for verification

## Defense

Defensive measures and detection strategies:

- Bounds check all metadata copies
- Sanitize image inputs
- Use ASAN in CI/CD

## Objectives

1. Trigger heap corruption
2. Cause OOB reads
3. Enable info disclosure/RCE

## Instructions

### Step 1: Compile Exiv2 with ASAN

**Context**: Enable detection.

**Command** (GCC/ASAN):
```bash
gcc -g -fsanitize=address exiv2_sources
```

> Prepares for fuzzing.

### Step 2: Fuzz with AFL

**Context**: Find crashes.

**Command** (AFL):
Run afl-fuzz on exiv2 binary with image seeds.

> Heap overflow in TIFF; OOB in JP2/WebP.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Process Injection]] Process Injection

### Sub-Techniques

- None

## Commands Used

- None extracted

## Tools Used

- [[tools/American-Fuzzy-Lop-AFL]]
- [[tools/Address-Sanitizer-ASAN]]

## Tags

- heap-corruption
- image-fuzzing
