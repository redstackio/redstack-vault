---
tags:
  - fuzzing
  - dos
  - endless-loop
  - pdf
type: procedure
tools:
  - '[[tools/American-Fuzzy-Lop-AFL]]'
  - '[[tools/LibFuzzer]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:24:31.123Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
id: 5ca96223-beb5-46a8-a5af-d4dcd5d6c0c4
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Fuzzing PDF Parsers for Endless Loop DoS

## Summary

This procedure fuzzes PDF libraries like qpdf to find cross-reference table inputs causing infinite loops, leading to high CPU and OOM DoS in parsers such as pdf.js, PDFium, and Ghostscript.

## Description

Naive xref table handling loops endlessly on malformed PDFs. Use AFL and libfuzzer on qpdf; test outputs on multiple parsers. Targets document viewers on Linux.

## Requirements

1. AFL and libfuzzer installed
2. qpdf source for fuzzing
3. Sample malformed PDFs with bad xref
4. Parsers like Firefox/Chrome for verification

## Defense

Defensive measures and detection strategies:

- Limit recursion depth in parsers
- Timeout on PDF processing
- Fuzz test libraries pre-release

## Objectives

1. Induce infinite loop in xref
2. Cause resource exhaustion
3. DoS viewers/parsers

## Instructions

### Step 1: Fuzz qpdf with AFL

**Context**: Generate crashing inputs.

**Command** (AFL setup):
Run AFL on qpdf binary with seed inputs.

> Finds endless loop after minutes; high CPU/OOM.

### Step 2: Fuzz with LibFuzzer

**Context**: In-process fuzzing.

**Command** (LibFuzzer):
Compile qpdf with libfuzzer; run on corpus.

> Confirms loop in xref handling.

### Step 3: Test on Parsers

**Context**: Verify cross-library impact.

**Command** (Manual):
Open fuzzed PDF in Firefox, Chrome, Ghostscript.

> DoS in pdf.js, PDFium, etc.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques

- None

## Commands Used

- None extracted

## Tools Used

- [[tools/American-Fuzzy-Lop-AFL]]
- [[tools/LibFuzzer]]

## Tags

- pdf-dos
- fuzzing
