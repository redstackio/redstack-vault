---
tags:
  - asan
  - report
  - detection
type: procedure
tools:
  - '[[tools/AddressSanitizer]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:26:22.081Z'
sub_techniques: []
id: c86a9f70-506f-4c44-b66b-16bc87249e1a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Observe-AddressSanitizer-Report

## Summary

This procedure reviews the AddressSanitizer output from the curl execution to confirm the heap-buffer-overflow in cookie handling, specifically the out-of-bounds read in strchr during path comparison.

## Description

After running curl, ASan reports the error: READ of size 1 at invalid address, in replace_existing at lib/cookie.c:~39, where clist->spath is empty string post-sanitization, so spath+1 skips NUL and searches for '/'. No leak possible due to read-only nature, but confirms vulnerability.

## Requirements

1. Previous curl execution with ASan
2. Console access to view output

## Defense

Defensive measures and detection strategies:

- Integrate ASan in fuzzing/CI
- Use fuzzers like AFL for cookie inputs
- Audit string functions in code

## Objectives

1. Verify OOB read occurrence
2. Analyze stack trace for root cause
3. Document for patching

## Instructions

### Step 1: Review ASan Output

**Context**: Examine console for error report post-curl run.

**Command**: No command; observe runtime output.

> Look for 'heap-buffer-overflow' message, shadow bytes, stack trace pointing to strchr and cookie.c:39.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/AddressSanitizer]]

## Tags

- asan
- report
- detection
