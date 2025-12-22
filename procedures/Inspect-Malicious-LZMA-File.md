---
id: p-inspect-lzma-file
tags:
  - file-analysis
  - hex-dump
  - lzma
  - dos
type: procedure
tools:
  - '[[tools/od]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/od-hex-dump]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:37.422Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Inspect-Malicious-LZMA-File

## Summary

This procedure examines the binary structure of a malicious LZMA-compressed file to identify crafted elements, such as manipulated headers, that cause excessive memory consumption in libxml2's decompression process.

## Description

Targeted at security researchers analyzing DoS vulnerabilities, this involves dumping the hex contents of a fuzzed LZMA file (e.g., test000) on a Linux system. It reveals how invalid compression properties lead to unbounded allocations in liblzma, aiding in root cause analysis for patches.

## Requirements

1. Access to the malicious LZMA file generated from fuzzing.
2. od utility installed (standard on Linux).
3. Basic understanding of LZMA format (e.g., dictionary size fields).

## Defense

Defensive measures and detection strategies:

- Validate LZMA headers for sanity (e.g., cap dictionary size) before decompression.
- Log and alert on unusual file inspection patterns in forensics tools.

## Objectives

1. Reveal the specific binary artifacts exploiting libxml2.
2. Confirm the file's malicious nature without executing it.
3. Document findings for vulnerability reporting.

## Instructions

### Step 1: Dump File Contents

**Context**: Use a hex dump to inspect the LZMA file's structure, focusing on header fields that request large memory.

**Command** ([[commands/od-hex-dump]]):

```bash
od -tx1 ./test000
```

> This outputs one-byte hexadecimal per line, highlighting patterns like oversized values (e.g., 20000000 for dictionary size), which trick liblzma into allocating gigabytes.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/od-hex-dump]]

## Tools Used

- [[tools/od]]

## Tags

- file-inspection
- binary-analysis
