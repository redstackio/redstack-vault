---
id: tool-gdb
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:31.855Z'
platforms:
  - Linux
tags:
  - debugging
  - reverse-engineering
url: 'https://www.gnu.org/software/gdb/'
validated: true
submitted: true
---

# GDB

**Status**: Unverified

## Overview

GNU Debugger (GDB) is a powerful tool for debugging programs, used here to attach to Apache processes and inspect memory structures like the response brigade during PHP vulnerability exploitation.

## Description

GDB allows breakpoints, variable inspection, and memory dumping in running processes, essential for verifying root causes in server-side bugs like brigade bucket mishandling leading to XSS.

## Features

- Feature 1: Process attachment and live debugging
- Feature 2: Memory address printing and structure examination
- Feature 3: Scripting for automated analysis

## Installation

### Requirements

- GCC and build essentials on Linux

### Install Commands

```bash
# On Debian/Ubuntu
apt install gdb

# On CentOS/RHEL
yum install gdb
```

## Basic Usage

```bash
gdb --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -p | Attach to process by PID |
| -q | Quiet mode |
| -batch | Non-interactive mode |

## Examples

### Example 1: Basic Usage

```bash
gdb -p $(pgrep httpd)
```

### Example 2: Advanced Usage

```bash
gdb httpd core.dump
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process attachments to httpd via ptrace
- GDB binaries running on production servers

## Related Procedures

- [[procedures/Observe-and-Verify-Reflected-XSS-in-Response]]

## Related Tools

- [[tools/Netcat]]

## References

- Official documentation: https://www.gnu.org/software/gdb/
- Related resources: GDB manual
