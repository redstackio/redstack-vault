---
id: tool-proc-filesystem
url: 'https://www.kernel.org/doc/html/latest/filesystems/proc.html'
tags:
  - recon
  - memory
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.241Z'
validated: true
submitted: true
---
# /proc filesystem

**Status**: Unverified

## Overview

The /proc filesystem in Linux provides a pseudo-filesystem for accessing process information, including memory maps (/proc/<pid>/maps), used to locate heap, SHM, and library addresses without advanced tools.

## Description

In security testing, /proc/<pid>/maps reveals mapped regions (e.g., rw-p for PHP heap, rw-s for Apache SHM), enabling attackers to plan memory-based exploits like UAF targeting specific addresses.

## Features

- Feature 1: Real-time process memory layout
- Feature 2: No installation required (built into Linux kernel)
- Feature 3: Filterable with grep for permissions and libraries

## Installation

### Requirements

- Linux kernel with procfs mounted (default)

### Install Commands

```bash
# Already available; mount if needed
mount -t proc proc /proc
```

## Basic Usage

```bash
cat /proc/<pid>/maps
```

### Common Options

N/A (file-based)

## Examples

### Example 1: Basic Usage

```bash
cat /proc/6318/maps | grep rw-p
```

### Example 2: Advanced Usage

```bash
cat /proc/6318/maps | grep libphp | grep rw-s
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Process Discovery]] Process Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Access to /proc/<sensitive_pid>/maps by non-root users
- Auditd logs showing cat/grep on /proc
- Container escapes via procfs

## Related Procedures

- [[procedures/Locate-Apache-Shared-Memory-and-Bucket-Structures]]

## Related Tools

- [[tools/GDB]]

## References

- Kernel docs: https://www.kernel.org/doc/html/latest/filesystems/proc.html
