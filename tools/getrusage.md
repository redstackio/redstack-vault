---
url: ''
tags:
  - system-call
  - monitoring
type: tool
verified: false
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.273Z'
id: 92565ea1-073a-4471-9bf5-ef9af5588b00
validated: true
submitted: true
---
# getrusage

**Status**: Unverified

## Overview

C system call to retrieve resource usage stats for a process, used in PoC to print max resident set size (memory in KB).

## Description

Called with RUSAGE_SELF in the PoC loop to log memory usage, helping quantify the leak from unfreed mallocs in `bytes_to_hexstring`.

## Features

- Feature 1: Retrieves max RSS
- Feature 2: User and system CPU time
- Feature 3: Page faults and swaps

## Installation

### Requirements

- Standard C library (<sys/resource.h> on Unix)

### Install Commands

Included in libc; no separate install.

## Basic Usage

```c
struct rusage usage; getrusage(RUSAGE_SELF, &usage); printf("Memory: %ld KB", usage.ru_maxrss);
```

### Common Options

| Option | Description |
|--------|-------------|
| `RUSAGE_SELF` | Current process stats |
| `RUSAGE_CHILDREN` | Child processes |

## Examples

### Example 1: Basic Usage

```c
getrusage(RUSAGE_SELF, &usage);
```

### Example 2: Advanced Usage

Integrate in loop for periodic logging.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]]

### Tactics

- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- Code including <sys/resource.h>
- Logs of ru_maxrss values

## Related Procedures

- [[procedures/Execute-Memory-Leak-PoC]]

## Related Tools

- [[Valgrind]]

## References

- Man page: man getrusage
