---
id: tool-uuid-2
url: 'https://www.man7.org/linux/man-pages/man1/ltrace.1.html'
tags:
  - tracing
  - syscalls
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.634Z'
alternatives:
  - strace
validated: true
submitted: true
---
# ltrace

**Status**: Unverified

## Overview

Traces library calls during execution to show OS-level resolution like inet_aton in SSRF bypass proofs.

## Description

ltrace intercepts dynamic library calls, useful for debugging IP resolution discrepancies between userland and kernel.

## Features

- Feature 1: Trace specific functions like inet_aton
- Feature 2: Filter output with grep
- Feature 3: Works with commands like ping

## Installation

### Requirements

- Linux system with development tools

### Install Commands

```bash
sudo apt install ltrace  # On Debian/Ubuntu
```

## Basic Usage

```bash
ltrace command
```

### Common Options

| Option | Description |
|--------|-------------|
| -f | Trace child processes |
| -e | Trace specific functions |

## Examples

### Example 1: Basic Usage

```bash
ltrace ping 0x7f.1
```

### Example 2: Advanced Usage

```bash
ltrace -e inet_aton ping 2130706433 2>&1 | grep inet_aton
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Process Discovery]] Process Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for ltrace processes tracing network commands
- Alert on syscall tracing in prod environments

## Related Procedures

- [[procedures/Bypass-SSRF-Filters-with-Hex-and-Decimal-IPs]]

## Related Tools

- [[tools/strace]]

## References

- ltrace man page
