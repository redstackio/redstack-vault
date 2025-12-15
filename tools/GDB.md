---
id: tool-uuid-1
url: 'https://www.gnu.org/software/gdb/'
tags:
  - debug
  - gdb
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.169Z'
validated: true
submitted: true
---
# GDB

**Status**: Unverified

## Overview

GNU Debugger (GDB) is a powerful tool for debugging programs, attaching to processes, and inspecting crashes like the Squid heap overflow.

## Description

GDB allows attaching to running processes, printing backtraces, and examining variables during exploitation analysis. In this context, it's used to capture SIGABRT details and confirm decodedLen overflow.

## Features

- Feature 1: Process attachment and control
- Feature 2: Backtrace and variable printing
- Feature 3: Breakpoint setting and stepping

## Installation

### Requirements

- Linux with development tools

### Install Commands

```bash
# On Ubuntu/Debian
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
| -q, --quiet | Suppress welcome messages |
| -p PID | Attach to process |
| -ex "cmd" | Execute command on startup |

## Examples

### Example 1: Basic Usage

```bash
gdb ./squid
```

### Example 2: Advanced Usage

```bash
gdb -q -p 1234 -ex "bt"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Process named 'gdb' attaching to targets
- ptrace system calls in logs
- GDB in running processes

## Related Procedures

- [[procedures/Verify-ASAN-Linkage-and-Monitor-Crash-with-GDB]]

## Related Tools

- [[tools/AddressSanitizer]]

## References

- Official documentation: https://www.gnu.org/software/gdb/documentation/
