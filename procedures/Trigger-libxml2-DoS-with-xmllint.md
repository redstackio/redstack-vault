---
id: p-trigger-libxml2-dos
tags:
  - dos
  - exploitation
  - libxml2
  - xmllint
  - memory-exhaustion
type: procedure
tools:
  - '[[tools/xmllint]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/xmllint-parse-valid]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:37.419Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# Trigger-libxml2-DoS-with-xmllint

## Summary

This procedure exploits a denial of service vulnerability in libxml2 by parsing a malicious LZMA-compressed XML file with xmllint, causing liblzma to attempt massive memory allocations and crash the application.

## Description

In an attack scenario, an adversary supplies a crafted LZMA XML to a libxml2-dependent application on Linux, triggering the vuln in xmlXzfileRead and xz_decomp. Outcomes include system resource exhaustion and crashes, as seen in xmllint tests with AddressSanitizer.

## Requirements

1. Compiled xmllint with libxml2 and liblzma support.
2. Malicious LZMA file (e.g., test000).
3. Sufficient system resources to observe exhaustion (or ASan for safe testing).

## Defense

Defensive measures and detection strategies:

- Patch libxml2 to limit decompression memory (e.g., via bounds in liblzma).
- Monitor process memory usage and alert on spikes during XML parsing; sandbox parsers.

## Objectives

1. Demonstrate DoS impact on libxml2 applications.
2. Validate vulnerability with reproducible crashes.
3. Highlight risks in XML processing pipelines.

## Instructions

### Step 1: Parse Malicious File

**Context**: Invoke xmllint to decompress and validate the XML, hitting the vuln in parser.c and xmlIO.c.

**Command** ([[commands/xmllint-parse-valid]]):

```bash
./xmllint --valid test000
```

> The --valid flag enables DTD validation, but the crash occurs in LZMA decompression; expect allocation failure for ~4GB, stack trace in lzma_code and xmlParseDocument.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion Floods

### Sub-Techniques


## Commands Used

- [[commands/xmllint-parse-valid]]

## Tools Used

- [[tools/xmllint]]

## Tags

- exploitation
- dos-trigger
