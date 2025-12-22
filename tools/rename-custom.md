---
url: >-
  https://github.com/sroettger/35c3ctf_chals/blob/master/logrotate/exploit/rename.c
tags:
  - exploitation
  - race-condition
type: tool
verified: false
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:24:19.191Z'
id: 3a4ed735-fe99-4c14-b322-a66dba757bff
validated: true
submitted: true
---
# rename-custom

**Status**: Unverified

## Overview

Custom C program designed for offensive security testing to demonstrate TOCTOU races by atomically swapping file names in a loop using the renameat2 syscall, specifically for exploiting libcurl's fopen vulnerability.

## Description

The rename tool is a simple C binary that takes two path arguments and enters an infinite loop calling renameat2 with the RENAME_EXCHANGE flag to swap their names. This creates a precise timing window for race conditions between file checks (stat) and operations (fopen). It's used in local privilege escalation or data leakage scenarios where symlink following can be manipulated. Compiled from open-source code, it's lightweight and runs silently in the background.

## Features

- Feature 1: Atomic file/directory name exchange via renameat2 syscall
- Feature 2: Infinite loop for sustained race window creation
- Feature 3: Minimal dependencies (standard libc); no network or external libs needed

## Installation

### Requirements

- GCC compiler
- Linux kernel supporting renameat2 (most modern)
- Source code from GitHub

### Install Commands

```bash
# Download and compile
git clone https://github.com/sroettger/35c3ctf_chals.git
cd 35c3ctf_chals/logrotate/exploit
gcc -o rename rename.c
```

## Basic Usage

```bash
./rename --help  # (if implemented; otherwise no help flag)
```

### Common Options

| Option | Description |
|--------|-------------|
| None | Paths as argv[1] and argv[2] |

## Examples

### Example 1: Basic Usage

```bash
./rename a b
```

Swaps 'a' and 'b' continuously.

### Example 2: Advanced Usage

```bash
nohup ./rename a b > /dev/null 2>&1 &
```

Runs detached in background.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Tactics

- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for repeated renameat2 syscalls in loops (e.g., via auditd rules)
- Process listings showing 'rename' binary with path arguments
- File system event logs for rapid swaps in target directories

## Related Procedures

- [[procedures/Execute-Symlink-Swapping-with-Custom-Rename-Tool]]

## Related Tools

- [[tools/curl]]

## References

- Source: https://github.com/sroettger/35c3ctf_chals/blob/master/logrotate/exploit/rename.c
- CVE-2023-32001 report
