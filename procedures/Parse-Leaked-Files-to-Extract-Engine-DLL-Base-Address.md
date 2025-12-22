---
id: proc-5
tags:
  - csgo
  - parsing
  - aslr-break
type: procedure
tools:
  - '[[tools/Python]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Windows
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:23:54.616Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Parse-Leaked-Files-to-Extract-Engine-DLL-Base-Address

## Summary

This procedure analyzes uploaded leaked files using known spray patterns to unpack and compute the base address of engine.dll, breaking ASLR.

## Description

Scan binary data for unique prop values from spray, then at matching offset, unpack the vtable_ptr (8-byte little-endian), and subtract the known OFFSET_VTABLE (e.g., 0x10) to derive engine_base.

## Requirements

1. Received leaked files from upload
2. Knowledge of spray patterns and offsets

## Defense

- Initialize heap memory before allocation
- Obfuscate DLL base calculations
- Validate pointer dereferences

## Objectives

1. Locate sprayed objects in leak
2. Recover ASLR-randomized base
3. Enable subsequent pointer calculations

## Instructions

### Step 1: Scan and Unpack

**Context**: Use Python struct to parse.

**Command** (Custom Python snippet):
```python
import struct
with open('leaked_file.bin', 'rb') as f:
    data = f.read()
# Scan for 0x1337ee00
offset = data.find(b'\x00\xee\x37\x13')
if offset != -1:
    vtable_ptr = struct.unpack('<Q', data[offset:offset+8])[0]
    engine_base = vtable_ptr - 0x10  # OFFSET_VTABLE
    print(f'Engine base: {hex(engine_base)}')
```

> Expected output: Valid engine_base like 0x140000000.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[System Information Discovery]] System Information Discovery

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Python]]

## Tags

- csgo
- parsing
- aslr-break
