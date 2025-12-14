---
tags:
  - python
  - mmap
  - setup
type: procedure
tools:
  - '[[tools/mmap-test-py]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Windows
  - Linux
techniques:
  - '[[Python]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: bc7b8a87-2f77-49bc-bdea-2944e9679869
created_at: '2025-12-14T17:25:13.167Z'
updated_at: '2025-12-14T17:25:13.167Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Map-File-Using-Python-mmap-Module

## Summary

This procedure initializes a memory-mapped file object using Python's mmap module, establishing the pos and size boundaries necessary for subsequent exploitation steps in the information disclosure attack.

## Description

In the context of exploiting the Python 2.7.12 mmap vulnerability, this step creates a file and maps it into memory. The mmap object maintains invariants like pos <= size, which are later broken. This is performed locally on a system running Python 2.7.12, requiring file system write access. Expected outcome is a valid mmap handle ready for manipulation.

## Requirements

1. Python 2.7.12 installed
2. Write access to a local directory for creating test files
3. No network or elevated privileges needed

## Defense

Defensive measures and detection strategies:

- Use Python 3.x versions where this bug is fixed
- Monitor file I/O operations in Python scripts for unusual mmap usage
- Implement code audits for legacy Python applications using mmap

## Objectives

1. Create a stable mmap object for the file
2. Verify initial pos and size values
3. Prepare for invariant-breaking resize operation

## Instructions

### Step 1: Create and Map the File

**Context**: Open a file and map it to memory to initialize the object.

```python
import mmap
import os

# Create a test file of known size
with open('testfile', 'wb') as f:
    f.write(b'A' * 1024)

# Map the file with full length
with open('testfile', 'r+b') as f:
    mm = mmap.mmap(f.fileno(), 0)
    print(f"Initial pos: {mm.tell()}, size: {mm.size()}")
```

> This code creates a 1024-byte file filled with 'A's and maps it, outputting pos=0 and size=1024. Success confirms the setup.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/mmap-test-py]]

## Tags

- [[Python]]
- [[mmap]]
- [[setup]]
