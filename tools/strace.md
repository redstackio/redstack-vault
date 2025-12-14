---
url: 'https://strace.io/'
tags:
  - tracing
  - debugging
  - syscall
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:22.373Z'
id: 7b378e4e-921d-4c98-99f1-b725b66dd61a
validated: true
submitted: true
---
# strace

**Status**: Unverified

## Overview

strace is a Linux diagnostic tool that traces system calls and signals, ideal for debugging server behaviors under load without source access.

## Description

Monitors processes for syscalls like network I/O to rule out server issues in vuln repro. Capabilities include filtering by type (e.g., network), forking support, and output logging. Used in security for analyzing black-box binaries or confirming clean ops during attacks.

## Features

- Feature 1: Real-time syscall tracing with timestamps
- Feature 2: Filtering (e.g., -e trace=network)
- Feature 3: Attachment to running PIDs without restart

## Installation

### Requirements

- Linux kernel with ptrace support

### Install Commands

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install strace
```

## Basic Usage

```bash
strace -h
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p PID` | Attach to process |
| `-e trace=...` | Filter syscalls |
| `-o file` | Output to file |

## Examples

### Example 1: Basic Usage

```bash
strace -p 1234 -o trace.log
```

### Example 2: Advanced Usage

```bash
strace -f -e trace=network ls /tmp
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Process Discovery]] Process Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- ptrace attachments in /proc
- High CPU from tracing
- strace processes in ps

## Related Procedures


## Related Tools

- [[tools/Burp-Suite]]

## References

- Official documentation: https://man7.org/linux/man-pages/man1/strace.1.html
