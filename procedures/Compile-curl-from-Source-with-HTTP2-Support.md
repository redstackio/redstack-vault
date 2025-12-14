---
tags:
  - compile
  - build
  - http2
type: procedure
tools:
  - '[[tools/wget]]'
  - '[[tools/tar]]'
  - '[[tools/configure]]'
  - '[[tools/make]]'
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/wget-download-curl-source]]'
  - '[[commands/configure-curl-build]]'
  - '[[commands/make-build-curl]]'
  - '[[commands/curl-version-check]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:24:19.166Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: fc80a18a-b2dd-4e3c-9f9d-31620d3fa4af
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Compile-curl-from-Source-with-HTTP2-Support

## Summary

This procedure compiles curl version 8.16.0 from source with OpenSSL and nghttp2 support to ensure the target version is used for testing the HTTP/2 TOCTOU vulnerability in a local environment.

## Description

In a Linux environment, download the curl source tarball, extract it, configure the build to include OpenSSL for TLS and nghttp2 for HTTP/2, then compile the binary. This sets up a reproducible environment for exploiting the certificate validation bypass. Prerequisites include build tools like gcc and development headers for OpenSSL and nghttp2.

## Requirements

1. Linux system with wget, tar, autoconf tools, gcc, OpenSSL dev headers, nghttp2 dev headers
2. Internet access for downloading source
3. Write permissions in working directory

## Defense

Defensive measures and detection strategies:

- Monitor for unusual compilation activities in shared environments using process auditing (e.g., auditd)
- Enforce use of pre-built, verified binaries from trusted sources

## Objectives

1. Obtain and build curl 8.16.0 with required features
2. Verify the binary supports HTTP/2 and TLS
3. Prepare for vulnerability testing

## Instructions

### Step 1: Download and Extract Source

**Context**: Fetch the curl 8.16.0 tarball and extract it to prepare the build directory.

**Command** ([[commands/wget-download-curl-source]]):
```bash
wget -q https://curl.se/download/curl-8.16.0.tar.gz && tar -xzf curl-8.16.0.tar.gz
```

> Downloads quietly and extracts to curl-8.16.0 directory.

### Step 2: Configure Build

**Context**: Run configure script to enable OpenSSL and nghttp2 support while suppressing output.

**Command** ([[commands/configure-curl-build]]):
```bash
./configure --with-openssl --with-nghttp2 > /dev/null
```

> Prepares Makefiles with TLS and HTTP/2 enabled.

### Step 3: Compile Binary

**Context**: Build the curl executable from source.

**Command** ([[commands/make-build-curl]]):
```bash
make > /dev/null
```

> Compiles src/curl binary.

### Step 4: Verify Compilation

**Context**: Check the version and features of the built binary.

**Command** ([[commands/curl-version-check]]):
```bash
./src/curl --version
```

> Confirms curl 8.16.0 with libcurl/8.16.0, OpenSSL/3.0.2, nghttp2/1.43.0.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/wget-download-curl-source]]
- [[commands/configure-curl-build]]
- [[commands/make-build-curl]]
- [[commands/curl-version-check]]

## Tools Used

- [[tools/wget]]
- [[tools/tar]]
- [[tools/configure]]
- [[tools/make]]
- [[tools/curl]]

## Tags

- compile
- build
- http2
