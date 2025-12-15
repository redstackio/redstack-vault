---
tags:
  - compilation
  - libcurl
  - build
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Linux
  - POSIX
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:24:18.705Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: ccdf2719-0dfd-4591-8c6f-c84cb499fd00
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Build Modified libcurl Library

## Summary

Compiles the patched libcurl source to generate a shared library vulnerable to the siglongjmp race condition during DNS timeouts.

## Description

After patching hostip.c, this procedure builds libcurl using autotools or cmake, producing libcurl.so.4 with the enabled USE_ALARM_TIMEOUT path. The resulting library can be used in applications to trigger crashes in multi-threaded DNS resolutions due to unprotected global sigjmp_buf.

## Requirements

1. Patched libcurl source
2. Autotools (autoconf, automake) or build script
3. GCC or compatible C compiler

## Defense

Defensive measures and detection strategies:

- Use official, patched libcurl builds
- Scan binaries for custom or vulnerable libcurl versions
- Employ static analysis tools to detect alarm-based timeouts in code

## Objectives

1. Produce vulnerable libcurl shared object
2. Ensure compatibility for linking with test applications
3. Validate build for race condition path

## Instructions

### Step 1: Prepare Build Environment

**Context**: Run configure to set up build.

**Command** (Configure):
```bash
./configure --enable-shared
```

> Generates Makefile for shared library build. Expected output: Configuration summary without errors.

### Step 2: Compile Library

**Context**: Build the modified source.

**Command** (Make):
```bash
make
```

> Compiles libcurl, focusing on hostip.c changes. Expected output: libcurl.so.4 in ./lib/.libs/, build logs showing no errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- build
- compilation
- vulnerability

