---
tags:
  - oob-read
  - heap-overflow
  - gnome
  - asan
type: procedure
tools:
  - '[[tools/Address-Sanitizer-ASAN]]'
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
updated_at: '2025-12-14T17:24:31.070Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 16723eed-0c95-4698-9099-80d3bf349a8d
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Detecting Memory Errors in GNOME with ASAN

## Summary

This procedure runs GNOME test suite and gnome-session with ASAN to uncover OOB reads in glib and heap overflows in parameter parsing, causing crashes during startup.

## Description

Glib's g_unichar_iswide_bsearch and token_stream_prepare access arrays OOB; gnome-session unbounded copy in init. Targets desktop env on Linux.

## Requirements

1. GNOME source with ASAN
2. Test suite runner
3. Malformed Unicode/GVariant inputs

## Defense

Defensive measures and detection strategies:

- Bounds check array access
- Sanitize params in session
- ASAN in desktop builds

## Objectives

1. OOB in Unicode parsing
2. Overflow in session params
3. Crash GNOME components

## Instructions

### Step 1: Run Test Suite with ASAN

**Context**: Test glib.

**Command** (ASAN env):
Set ASAN_OPTIONS and run gnome tests.

> OOB reads in bsearch/token.

### Step 2: Test Gnome-Session

**Context**: Startup parsing.

**Command** (ASAN):
Launch gnome-session with malformed params.

> Heap overflow detected.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Address-Sanitizer-ASAN]]

## Tags

- desktop-memory-bug
