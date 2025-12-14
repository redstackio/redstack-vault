---
tags:
  - compilation
  - gcc
  - binary-building
type: procedure
tools:
  - '[[tools/GCC-Compiler]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/compile-test-binary]]'
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Execution through Module Load]]'
updated_at: '2025-12-14T17:28:59.017Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 9c79bb88-efe2-414b-a1f3-5fab8f8846fc
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Execution through Module Load]]'
---
# Compile-Malicious-Executable

## Summary

This procedure compiles the malicious C source code into an executable binary that will be used to replace the legitimate 'console' binary during the race condition exploit.

## Description

Using GCC, the 'test.c' file is compiled into 'a.out', a standard executable that can be linked and substituted in the filesystem. This step prepares the payload for timed replacement in a user-writable directory, exploiting the lack of locking in the SUID binary's verification process.

## Requirements

1. GCC installed on macOS (via Xcode Command Line Tools)
2. 'test.c' file from previous procedure
3. Writable current directory

## Defense

Defensive measures and detection strategies:

- Restrict GCC usage in user environments or monitor compilation events
- Use file integrity monitoring on directories near SUID binaries
- Employ AppArmor or similar to confine compiler tools

## Objectives

1. Produce a runnable malicious executable
2. Ensure compatibility with macOS execution environment
3. Prepare for hardlink substitution

## Instructions

### Step 1: Compile the Source

**Context**: Build 'test.c' into an executable to enable system call execution under root.

**Command** ([[commands/compile-test-binary]]):
```bash
gcc test.c
```

> This compiles 'test.c' to 'a.out' by default. No additional flags needed for basic functionality. Expected output: 'a.out' file created; verify with `file a.out` showing Mach-O executable.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Execution through Module Load]] Shared Modules

### Sub-Techniques


## Commands Used

- [[commands/compile-test-binary]]

## Tools Used

- [[tools/GCC-Compiler]]

## Tags

- compilation
- gcc
- binary-building
