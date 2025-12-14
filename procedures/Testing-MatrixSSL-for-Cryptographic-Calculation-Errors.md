---
tags:
  - crypto-flaw
  - matrixssl
  - calculation-error
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credential Dumping]]'
updated_at: '2025-12-14T17:24:31.090Z'
skill_level: advanced
impact_level: high
detection_risk: low
sub_techniques: []
id: 7ee7039c-701d-4d0d-bbc6-0b17d507945d
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Credential Dumping]]'
---
# Testing MatrixSSL for Cryptographic Calculation Errors

## Summary

This procedure tests MatrixSSL's modular exponentiation and reverse functions against OpenSSL, revealing crashes on zero inputs and incorrect results, potentially allowing private key extraction via CRT errors (CVEs 2016-6885/6/7).

## Description

pstm_exptmod crashes on zero base/modulus; pstm_reverse underflows on zero size. Compare outputs on edge cases. Targets SSL libraries on Linux.

## Requirements

1. MatrixSSL and OpenSSL sources
2. Test harness for exptmod/reverse
3. Edge case inputs (zero base, equal mod/base)

## Defense

Defensive measures and detection strategies:

- Handle zero/edge in crypto ops
- Fuzz crypto primitives
- Use audited libs like OpenSSL

## Objectives

1. Crash on invalid inputs
2. Wrong computation results
3. Enable key recovery

## Instructions

### Step 1: Compare Exptmod

**Context**: Test modular exp.

**Command** (Manual test):
Run pstm_exptmod with zero base/modulus == base.

> Crashes or wrong results vs OpenSSL.

### Step 2: Test Reverse

**Context**: Check buffer reverse.

**Command** (Manual):
Call pstm_reverse on zero-size input.

> Underflow/crash.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Credential Dumping]] OS Credential Dumping

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- crypto-error
- ssl-lib
