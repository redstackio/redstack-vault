---
id: tool-time
url: 'https://man7.org/linux/man-pages/man1/time.1.html'
tags:
  - benchmark
  - timing
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.586Z'
validated: true
submitted: true
---
# time

**Status**: Verified

## Overview

time is a Unix command-line utility that measures the execution time of other commands, useful in security testing to quantify performance impacts like delays from ReDoS exploits.

## Description

It reports real, user, and system time for a command. In offensive ops, it's prefixed to tools like curl to demonstrate DoS effects through timing anomalies.

## Features

- Feature 1: Real-time wall clock measurement
- Feature 2: User and system CPU time breakdown
- Feature 3: Simple integration as prefix

## Installation

### Requirements

- Built-in on Unix-like systems

### Install Commands

```bash
# Usually pre-installed; on minimal systems
sudo apt install time
```

## Basic Usage

```bash
time --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p` | POSIX output format |
| `-v` | Verbose details |

## Examples

### Example 1: Basic Usage

```bash
time curl http://example.com
```

### Example 2: Advanced Usage

```bash
time -v curl -I http://localhost:8000
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]]

### Tactics

- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- Rarely logged directly; detect via wrapped command patterns in scripts
- Timing anomalies in exploit attempts

## Related Procedures

- [[procedures/Trigger-ReDoS-DoS-Using-Curl]]

## Related Tools

- [[/usr/bin/time]]

## References

- Man page: https://man7.org/linux/man-pages/man1/time.1.html
