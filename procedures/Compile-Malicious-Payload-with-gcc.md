---
tags:
  - rce
  - compilation
  - shared-library
type: procedure
tools:
  - '[[tools/gcc-compiler]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/gcc-build-evil-engine]]'
platforms:
  - Linux
  - POSIX
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Dynamic Linker Hijacking]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: e553ce95-54ac-4ec1-8fd9-285d513ed6f4
created_at: '2025-12-14T17:23:31.218Z'
updated_at: '2025-12-14T17:23:31.218Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Dynamic Linker Hijacking]]'
---
# Compile-Malicious-Payload-with-gcc

## Summary

Compiles the malicious C source code into a position-independent shared library (.so) file that can be loaded by curl's --engine option to trigger RCE.

## Description

This step uses GCC to build evil_engine.c into evil_engine.so, ensuring position-independent code (-fPIC) for dynamic loading. The resulting library's constructor executes code when loaded, exploiting curl's lack of path validation for .so files. Applicable in testing curl vulnerabilities on Linux/POSIX systems.

## Requirements

1. evil_engine.c file from previous procedure
2. GCC compiler installed
3. Write permissions in current directory

## Defense

Defensive measures and detection strategies:

- Scan for suspicious .so compilations in build logs
- Enforce code signing for shared libraries
- Use static analysis tools to detect constructor-based payloads

## Objectives

1. Produce loadable .so file
2. Enable library hijacking for RCE
3. Validate compilation without errors

## Instructions

### Step 1: Compile the Source

**Context**: Build the C file into a shared object using GCC flags for PIC and shared output.

**Command** ([[commands/gcc-build-evil-engine]]):

```bash
gcc -fPIC -shared -o evil_engine.so evil_engine.c
```

> Compiles evil_engine.c into evil_engine.so. -fPIC generates position-independent code, -shared creates the .so, -o specifies output. Expected: No output on success; file created.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]
- [[Dynamic Linker Hijacking]]

### Sub-Techniques


## Commands Used

- [[commands/gcc-build-evil-engine]]

## Tools Used

- [[tools/gcc-compiler]]

## Tags

- [[rce]]
- [[compilation]]
