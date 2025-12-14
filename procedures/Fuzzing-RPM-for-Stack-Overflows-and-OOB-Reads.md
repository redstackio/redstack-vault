---
tags:
  - stack-overflow
  - oob-read
  - null-deref
  - rpm
  - fuzzing
type: procedure
tools:
  - '[[tools/American-Fuzzy-Lop-AFL]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/rpm-install-fuzzed]]'
  - '[[commands/rpm-query-fuzzed]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:24:31.064Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7987941a-f5b2-473a-849f-0041bb1b844c
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Fuzzing RPM for Stack Overflows and OOB Reads

## Summary

This procedure fuzzes RPM package manager with AFL to trigger stack overflows in glob expansion, OOB reads in header verification, and null derefs in formatting, crashing on malformed RPMs.

## Description

Recursive glob without depth limit overflows stack; headerVerifyInfo accesses beyond bounds; stringFormat null in rpmtd. Targets package tools on Linux.

## Requirements

1. RPM binary
2. AFL fuzzer
3. Fuzzed RPM files

## Defense

Defensive measures and detection strategies:

- Limit glob recursion
- Bounds check headers
- Null-check formats

## Objectives

1. Overflow stack in glob
2. OOB in verification
3. Crash on install/query

## Instructions

### Step 1: Fuzz RPM Install

**Context**: Trigger during -i.

**Command** ([[commands/rpm-install-fuzzed]]):
```bash
rpm -i [input]
```

> Stack overflow, OOB, null ptr.

### Step 2: Fuzz Query Info

**Context**: Header checks.

**Command** ([[commands/rpm-query-fuzzed]]):
```bash
rpm -qi -p -- [input]
```

> OOB read crash.

### Step 3: AFL Session

**Context**: Generate inputs.

**Command** (AFL):
afl-fuzz on rpm binaries.

> Finds multiple bugs.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques

- None

## Commands Used

- [[commands/rpm-install-fuzzed]]
- [[commands/rpm-query-fuzzed]]

## Tools Used

- [[tools/American-Fuzzy-Lop-AFL]]

## Tags

- package-fuzzing
- rpm-bug
