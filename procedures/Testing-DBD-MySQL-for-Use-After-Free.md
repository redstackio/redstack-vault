---
tags:
  - use-after-free
  - dbd-mysql
  - perl
  - asan
type: procedure
tools:
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
updated_at: '2025-12-14T17:24:31.059Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 5e3b0f19-953d-4288-abaa-c0ba4295da17
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Process Injection]]'
---
# Testing DBD::MySQL for Use-After-Free

## Summary

This procedure compiles and tests Perl's DBD::mysql with ASAN to detect use-after-free in my_login(), causing crashes or corruption (CVE-2015-8949).

## Description

Freed memory accessed post-free in login function. Targets MySQL bindings on Linux.

## Requirements

1. DBD::mysql source with ASAN
2. Perl environment
3. Test cases for login

## Defense

Defensive measures and detection strategies:

- Refcount properly in bindings
- ASAN for Perl extensions
- Patch CVE-2015-8949

## Objectives

1. Trigger UAF in my_login
2. Cause segfault/corruption
3. Expose DB connections

## Instructions

### Step 1: Compile with ASAN

**Context**: Enable detection.

**Command** (GCC/ASAN):
```bash
gcc -g -fsanitize=address dbd_sources
```

> Prepares module.

### Step 2: Test Login Function

**Context**: Run scenarios.

**Command** (Perl test):
Execute my_login with crafted inputs.

> ASAN reports UAF.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Process Injection]] Process Injection

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Address-Sanitizer-ASAN]]

## Tags

- db-binding-uaf
