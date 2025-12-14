---
tags:
  - cfi
  - type-mismatch
  - curl
type: procedure
tools:
  - '[[tools/Clang]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/configure-curl-cfi]]'
  - '[[commands/make-curl]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Compromise Client Software Binary]]'
updated_at: '2025-12-14T17:24:31.104Z'
skill_level: advanced
impact_level: medium
detection_risk: low
sub_techniques: []
id: ca5c2411-f783-4052-a0ca-01e2c9b3a9f2
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Compromise Client Software Binary]]'
---
# Building Curl with CFI to Detect Type Mismatches

## Summary

This procedure configures and compiles curl with Clang Control Flow Integrity (CFI) to detect function pointer type mismatches in callbacks, preventing indirect call exploits.

## Description

Curl's tool_header_cb and tool_write_cb have void* vs char* mismatches for curl_write_callback, violating CFI. Build with -fsanitize=cfi, -flto, etc., to catch at compile time. Targets network tools on Linux.

## Requirements

1. Clang compiler with gold linker
2. Curl source code
3. LTO support enabled
4. No shared libs (--disable-shared)

## Defense

Defensive measures and detection strategies:

- Enforce strict function signatures
- Use CFI in builds
- Static analysis for pointer types

## Objectives

1. Enable CFI compilation
2. Detect type violations
3. Prevent call exploits

## Instructions

### Step 1: Configure with CFI Flags

**Context**: Set up Clang and flags.

**Command** ([[commands/configure-curl-cfi]]):
```bash
./configure CC=clang CXX=clang++ LD=clang CFLAGS="-fsanitize=cfi -fvisibility=hidden -fuse-ld=gold -flto" CXXFLAGS="-fsanitize=cfi -fvisibility=hidden -fuse-ld=gold -flto" LDFLAGS="-fsanitize=cfi -fvisibility=hidden -fuse-ld=gold -flto" --disable-shared
```

> Configures for CFI-enabled build.

### Step 2: Build Curl

**Context**: Compile and catch errors.

**Command** ([[commands/make-curl]]):
```bash
make
```

> Fails on type mismatch in callbacks.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Compromise Client Software Binary]] Compromise Client Software Binary

### Sub-Techniques

- None

## Commands Used

- [[commands/configure-curl-cfi]]
- [[commands/make-curl]]

## Tools Used

- [[tools/Clang]]

## Tags

- cfi-violation
- build-hardening
