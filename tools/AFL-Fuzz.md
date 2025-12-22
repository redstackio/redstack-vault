---
id: tool-afl-fuzz
url: 'http://lcamtuf.coredump.cx/afl/'
tags:
  - fuzzing
  - discovery
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.457Z'
validated: true
submitted: true
---
# afl-fuzz

**Status**: Unverified

## Overview

AFL-Fuzz (American Fuzzy Lop) is a security-oriented fuzzer for discovering bugs like crashes, hangs, and memory issues in software, commonly used in vulnerability research for protocols like HTTP/2.

## Description

AFL instruments binaries to track code coverage during input mutations, efficiently finding edge cases. In offensive security, it's used to fuzz server modules (e.g., mod_http2) for DoS triggers like resource leaks. Supports network fuzzing via extensions for protocols over TCP.

## Features

- Feature 1: Genetic mutation of inputs based on coverage feedback
- Feature 2: Hang detection for resource exhaustion flaws
- Feature 3: Parallel fuzzing across cores for faster discovery

## Installation

### Requirements

- Linux kernel with ptrace support
- GCC/Clang for compilation

### Install Commands

```bash
# From source
git clone https://github.com/google/AFL.git
cd AFL
make
afl-gcc --version  # Verify
```

Or via package: `apt install afl-fuzz`

## Basic Usage

```bash
afl-fuzz -i input -o output -- /target/binary @@
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i dir` | Input corpus directory |
| `-o dir` | Output/findings directory |
| `-t msec` | Timeout per run (e.g., 1000 for 1s) |

## Examples

### Example 1: Basic Usage

```bash
afl-fuzz -i http2_samples -o findings -- ./http2_test_harness @@
```

### Example 2: Advanced Usage

```bash
afl-fuzz -i corpus -o out -t 5000 -m 100 -- /usr/sbin/httpd -X @@  # Fuzz Apache in single-process mode
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- High CPU usage from afl-fuzz processes
- Instrumented binaries with AFL signatures in memory dumps
- Network traffic spikes during fuzz sessions

## Related Procedures


## Related Tools

- [[Related Tool 1|tools/honggfuzz]]
- [[Related Tool 2|tools/libfuzzer]]

## References

- Official documentation: http://lcamtuf.coredump.cx/afl/documentation/
- Related resources: AFL documentation on fuzzing servers
