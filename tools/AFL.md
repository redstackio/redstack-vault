---
id: tool-afl-001
url: 'http://lcamtuf.coredump.cx/afl/'
name: AFL
tags:
  - fuzzing
  - vulnerability-discovery
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.055Z'
validated: true
submitted: true
---
# AFL

**Status**: Unverified

## Overview

AFL (American Fuzzy Lop) is a security-oriented fuzzer used to discover vulnerabilities by generating malformed inputs and testing target binaries or libraries for crashes, memory errors, and other issues. In security testing, it's commonly used for finding buffer overflows in parsers like image processing code.

## Description

AFL employs genetic algorithms to mutate input seeds efficiently, focusing on code coverage to uncover edge cases. For Node.js modules like canvas, it instruments the code during compilation to track execution paths. It's ideal for discovering DoS vulnerabilities in media parsing by fuzzing with image formats such as PNG, JPG, and GIF.

## Features

- Feature 1: Persistent mode for fast fuzzing of scripted targets like Node.js
- Feature 2: Crash minimization and analysis tools
- Feature 3: Dictionary-based mutation for structured inputs like image headers

## Installation

### Requirements

- Linux kernel with ptrace support
- GCC or Clang for instrumentation
- Sufficient disk space for corpus and findings

### Install Commands

```bash
# Download and build from source
wget http://lcamtuf.coredump.cx/afl/releases/afl-latest.tgz
tar -zxvf afl-latest.tgz
cd afl-*
make
sudo make install
```

## Basic Usage

```bash
afl-fuzz -i input_dir -o output_dir -- target @@
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i` | Input seed directory |
| `-o` | Output directory for findings |
| `-m` | Memory limit per instance |

## Examples

### Example 1: Basic Usage

```bash
afl-fuzz -i seeds -o findings -- /usr/bin/node parse_image.js @@
```

Fuzzes a Node.js script loading images.

### Example 2: Advanced Usage

```bash
afl-fuzz -i seeds -o findings -m 500 -t 1000 -- /usr/bin/node parse_image.js @@
```

Sets memory limit and timeout.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service (for crash discovery)

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- High CPU usage from afl-fuzz processes
- Presence of afl-instrumented binaries
- Large output directories with crash logs

## Related Procedures

- [[procedures/Fuzz-Node-js-Canvas-for-Image-Parsing-Vulnerabilities]]

## Related Tools

- [[tools/ascii-art]]

## References

- Official documentation: http://lcamtuf.coredump.cx/afl/documentation/
- Related resources: AFL documentation on fuzzing Node.js
