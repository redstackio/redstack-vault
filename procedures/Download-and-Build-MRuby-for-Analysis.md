---
id: proc-mruby-build
tags:
  - build
  - mrbuby
  - analysis
type: procedure
tools:
  - '[[tools/GCC]]'
  - '[[tools/ASAN]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:30.756Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Download-and-Build-MRuby-for-Analysis

## Summary

This procedure involves downloading the MRuby source code and compiling it on a Linux x64 system using GCC with AddressSanitizer (ASAN) enabled to prepare an environment for vulnerability analysis and reproduction of the null pointer dereference issue.

## Description

MRuby is a lightweight Ruby interpreter often embedded in applications like Shopify Scripts. To analyze the vulnerability discovered on January 31, 2017, the source code must be downloaded and built with debugging and sanitization tools. This setup allows detection of memory errors such as null pointer dereferences during execution. The build process uses GCC on Linux to create a sandboxed MRuby binary compatible with Ruby 2.3.1 environments. Prerequisites include a Linux development setup with GCC and ASAN support.

## Requirements

1. Linux x64 operating system with development tools installed
2. Internet access to download MRuby source (version as of 2017-01-31)
3. GCC compiler with AddressSanitizer support

## Defense

Defensive measures and detection strategies:

- Use static analysis tools like Coverity or Clang Static Analyzer during builds to catch null pointer issues early
- Enable runtime sanitizers in production builds for embedded interpreters to log memory errors without crashing
- Regularly update MRuby to patched versions to mitigate known vulnerabilities

## Objectives

1. Prepare a reproducible environment for exploiting the DoS vulnerability
2. Enable memory error detection for accurate crash analysis
3. Verify build integrity before executing malicious scripts

## Instructions

### Step 1: Download MRuby Source

**Context**: Obtain the MRuby codebase from the official repository as it existed on January 31, 2017, to match the vulnerability discovery context.

No specific command; use git or direct download to fetch the source into a local directory.

> Expected: MRuby source tree extracted and ready for configuration.

### Step 2: Configure and Build with ASAN

**Context**: Configure the build to include AddressSanitizer for detecting null pointer dereferences and compile using GCC.

Run the MRuby build script with ASAN flags:

```bash
make -j4 WITH_ASAN=1
```

> This compiles MRuby on x64 Linux, enabling ASAN to instrument the binary for memory safety checks. Expected output: Built binaries including the sandbox executable, with no compilation errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/GCC]]
- [[tools/ASAN]]

## Tags

- build
- mrbuby
- analysis
