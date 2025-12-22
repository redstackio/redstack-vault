---
url: 'http://www.gnu.org/software/gdb/'
tags:
  - debugging
  - crash-analysis
type: tool
platforms:
  - Linux
description: GNU Debugger for analyzing program crashes and runtime behavior
id: cdda5a7d-8908-48f2-892e-474bc7a8468b
created_at: '2025-12-11T03:47:48.046Z'
updated_at: '2025-12-11T03:47:48.046Z'
verified: false
validated: true
submitted: true
---
# GDB

**Status**: Unverified

## Overview

GDB is the GNU Debugger, used for debugging programs by attaching to processes, setting breakpoints, and inspecting memory, stacks, and registers during crashes or runtime.

## Description

In offensive security, GDB is employed to analyze exploits like the mruby Decimal crash, providing backtraces and register dumps to understand vulnerability root causes.

## Features

- Process attachment and continuation
- Backtrace inspection
- Register and memory examination

## Installation

### Requirements

- Linux system
- GCC toolchain

### Install Commands

```bash
sudo apt install gdb
```

## Basic Usage

```bash
gdb --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `attach <pid>` | Attach to running process |

## Examples

### Example 1: Basic Usage

```bash
gdb attach 10251
```

### Example 2: Advanced Usage

```bash
gdb attach 10251
c
bt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for GDB process attachments to sensitive applications
- Log debugger invocations in production environments

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #lldb
- #valgrind

## References

- Official documentation: http://www.gnu.org/software/gdb/
- Related resources: GDB manual
