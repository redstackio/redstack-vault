---
url: >-
  https://github.com/sroettger/35c3ctf_chals/blob/master/logrotate/exploit/rename.c
tags:
  - exploit
  - race
type: tool
platforms:
  - Linux
description: Custom C program for atomic file name swapping to exploit TOCTOU races.
id: a4b271c7-bd38-4cf9-b5b9-f6149eb53d92
created_at: '2025-12-14T17:24:19.377Z'
updated_at: '2025-12-14T17:24:19.377Z'
verified: false
validated: true
submitted: true
---
# rename-custom-swapper

**Status**: Unverified

## Overview

Custom tool to demonstrate libcurl TOCTOU by continuously swapping file names atomically, used in offensive security for race condition exploits on Linux filesystems.

## Description

The rename.c source uses <sys/syscall.h> and <linux/fs.h> to call syscall(SYS_renameat2, AT_FDCWD, oldpath, AT_FDCWD, newpath, RENAME_EXCHANGE) in a while(1) loop, enabling rapid, atomic exchanges between symlink and directory for tricking stat/fopen.

## Features

- Feature 1: Infinite loop for persistent race window
- Feature 2: Atomic swaps via renameat2 syscall
- Feature 3: Minimal dependencies, Linux-specific

## Installation

### Requirements

- GCC compiler
- Linux kernel with renameat2 support

### Install Commands

```bash
# Download source
git clone https://github.com/sroettger/35c3ctf_chals.git
cd 35c3ctf_chals/logrotate/exploit
# Compile
gcc rename.c -o rename
```

## Basic Usage

```bash
./rename --help  # No help; positional args only
```

### Common Options

| Option | Description |
|--------|-------------|
| argv[1] | Old file path |
| argv[2] | New file path |

## Examples

### Example 1: Basic Usage

```bash
./rename a b  # Swap a and b continuously
```

### Example 2: Advanced Usage

```bash
# Run detached
nohup ./rename a b > /dev/null &
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Syscall traces showing repeated renameat2 with RENAME_EXCHANGE
- Detection method 2: Process named 'rename' with high CPU from loop

## Related Procedures

- [[procedures/Execute-Continuous-File-Swapping]]

## Related Tools

- [[tools/curl]]

## References

- GitHub source: https://github.com/sroettger/35c3ctf_chals/blob/master/logrotate/exploit/rename.c
