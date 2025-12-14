---
id: proc-reverse-swapnote-parser
tags:
  - reverse-engineering
  - disassembly
  - vulnerability-analysis
type: procedure
tools:
  - '[[tools/Ghidra]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Nintendo 3DS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:23:41.406Z'
skill_level: advanced
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Reverse-Engineer-Swapnote-TLRF-Parser

## Summary

This procedure involves disassembling and analyzing the Nintendo 3DS Swapnote application's binary to identify vulnerabilities in the TLRF chunk parser, specifically unsafe memcpy operations that enable heap overflows.

## Description

In the context of exploiting embedded applications like Swapnote on the 3DS, reverse engineering reveals how the parser handles TLRF chunks in message files. The app uses fixed-size heap buffers (e.g., heap_buffer_0 and heap_buffer_1) and calls memcpy with user-controlled sizes and offsets from the TLRF_buffer without bounds checking. This allows attackers to overflow chunks and manipulate heap structures via unsafe unlink techniques, leading to code execution. Prerequisites include access to the Swapnote binary (extracted via homebrew tools) and familiarity with ARM disassembly.

## Requirements

1. Nintendo 3DS with homebrew access to dump Swapnote binary
2. Disassembler tool like Ghidra installed on a host machine
3. Knowledge of 3DS file formats and ARM Thumb instruction set

## Defense

Defensive measures and detection strategies:

- Patch Swapnote or disable StreetPass on vulnerable firmware
- Monitor for anomalous app crashes during message parsing
- Use firmware updates that address heap safety in system apps

## Objectives

1. Locate TLRF parsing routines in the binary
2. Identify memcpy calls vulnerable to user input
3. Confirm exploit primitives like heap overflow and unlink

## Instructions

### Step 1: Extract and Load Binary

**Context**: Obtain the Swapnote executable for analysis.

Use 3DS homebrew tools to dump the app binary, then load it into [[tools/Ghidra]].

### Step 2: Disassemble Parser

**Context**: Navigate to TLRF handling code.

In Ghidra, search for strings like "TLRF" and follow cross-references to the parsing function. Analyze heap allocations and memcpy calls.

### Step 3: Identify Vulnerabilities

**Context**: Pinpoint unsafe operations.

Examine offsets: look for memcpy destinations at heap buffers and sources/sizes from user-controlled TLRF_buffer (e.g., offsets 0x70C for size, 0x6DC for offset).

**Expected Output**: Annotated disassembly showing overflow paths.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Ghidra]]

## Tags

- [[reverse-engineering]]
- [[disassembly]]
