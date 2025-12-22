---
id: proc-libcurl-setup-001
tags:
  - setup
  - libcurl
  - test-env
type: procedure
tools:
  - '[[tools/gcc]]'
  - '[[tools/libcurl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/identify-ubuntu-version]]'
  - '[[commands/compile-libcurl-test]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:55.541Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-libcurl-Test-Application

## Summary

This procedure sets up a test environment simulating a vulnerable web application that uses libcurl to parse and fetch user-supplied URLs, focusing on IPv6 handling to demonstrate parsing inconsistencies.

## Description

In a Linux environment like Ubuntu 20.04, compile a custom C program that integrates libcurl for URL parsing and HTTP requests. This mimics applications trusting libcurl's hostname extraction for interface-specific routing, vulnerable to zone ID stripping. Prerequisites include libcurl installed (v7.68.0) and a C compiler. Expected outcome: A runnable test binary that processes URLs from input files, revealing parsing deviations from RFC 6874.

## Requirements

1. Linux OS (Ubuntu 20.04 or equivalent) with libcurl development libraries.
2. Source code file 'parserbatch.c' implementing libcurl URL parsing tests.
3. Network setup with multiple interfaces supporting IPv6 link-local addresses.

## Defense

Defensive measures and detection strategies:

- Use alternative URL parsers (e.g., Python urllib) that correctly handle zone IDs.
- Validate parsed hostnames against submitted URLs to detect stripping.
- Monitor libcurl versions and apply patches for known parsing issues.

## Objectives

1. Establish a reproducible environment for testing libcurl IPv6 parsing.
2. Confirm libcurl version and compilation success.
3. Prepare for URL submission and parsing demonstration.

## Instructions

### Step 1: Identify Environment

**Context**: Verify the testing platform to ensure compatibility with libcurl v7.68.0.

**Command** ([[commands/identify-ubuntu-version]]):
```bash
lsb_release -a
```

> This command outputs distribution details. Expected: Distributor ID: Ubuntu, Release: 20.04.

### Step 2: Compile Test Program

**Context**: Build the C test code linking libcurl to simulate application URL handling.

**Command** ([[commands/compile-libcurl-test]]):
```bash
gcc parserbatch.c -o parserbatch -lcurl
```

> Compiles without errors if libcurl is available. Creates executable for parsing tests.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/identify-ubuntu-version]]
- [[commands/compile-libcurl-test]]

## Tools Used

- [[tools/gcc]]
- [[tools/libcurl]]

## Tags

- setup
- libcurl
- test-env
