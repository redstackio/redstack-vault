---
id: proc-libcurl-setup
tags:
  - libcurl
  - setup
  - ipv6
type: procedure
tools:
  - '[[tools/libcurl]]'
  - '[[tools/gcc]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/lsb-release-identify-environment]]'
  - '[[commands/compile-parserbatch-test]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:36.080Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-Up-libcurl-Application-for-URL-Fetching

## Summary

This procedure configures a web application to use libcurl for processing user-supplied URLs, assuming parsed hostnames enforce network interface restrictions via IPv6 zone IDs, setting the stage for exploitation.

## Description

In a Linux environment like Ubuntu 20.04, integrate libcurl into application code for HTTP fetching. The app trusts libcurl's CURLU API (e.g., curl_url_set for CURLUPART_HOST) to parse URLs and route link-local IPv6 addresses to specific interfaces like eth0. This setup is vulnerable if libcurl omits zone IDs, allowing unintended routing. Prerequisites include IPv6 enabled and libcurl installed.

## Requirements

1. Linux system (e.g., Ubuntu 20.04) with IPv6 networking
2. libcurl library installed
3. GCC compiler for building test code
4. Application code integrating libcurl for URL requests

## Defense

Defensive measures and detection strategies:

- Validate URLs with alternative parsers (e.g., Python urllib) before libcurl processing
- Enforce strict interface binding in application code, ignoring libcurl's parsed host
- Monitor for anomalous IPv6 connections to link-local addresses on default interfaces

## Objectives

1. Establish a vulnerable application relying on libcurl for URL handling
2. Verify environment supports IPv6 zone IDs
3. Prepare for submission of malformed URLs

## Instructions

### Step 1: Identify Environment

**Context**: Confirm the testing platform supports the required setup.

**Command** ([[commands/lsb-release-identify-environment]]):
```bash
lsb_release -a
```

> Displays system details like Distributor ID: Ubuntu, Release: 20.04. Ensure IPv6 is enabled via `ip addr show`.

### Step 2: Compile Test Code

**Context**: Build a simple C program to integrate and test libcurl parsing.

**Command** ([[commands/compile-parserbatch-test]]):
```bash
gcc parserbatch.c -o parserbatch -lcurl
```

> Compiles without errors if libcurl is linked properly. The source (parserbatch.c) should use CURLU API to parse URLs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/lsb-release-identify-environment]]
- [[commands/compile-parserbatch-test]]

## Tools Used

- [[tools/libcurl]]
- [[tools/gcc]]

## Tags

- libcurl
- setup
- ipv6
