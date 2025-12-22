---
id: 11eeb915-9a2a-4ddb-afa9-a04c9fb3919d
name: foremost
type: tool
verified: true
created_at: '2019-08-28T21:17:41.036511+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - forensics
  - file-recovery
  - post-exploitation
url: 'https://github.com/korczis/foremost'
commands:
  - '[[commands/foremost-basic-recovery]]'
  - '[[commands/foremost-recover-specific-types]]'
  - '[[commands/foremost-config-based-recovery]]'
validated: true
---

# foremost

**Status**: Unverified

## Overview

Foremost is a command-line forensic tool designed for recovering deleted or lost files from disk images, raw devices, or file systems. It uses file headers, footers, and internal data structures to carve files without relying on the file system metadata, making it ideal for data recovery in incident response, post-exploitation scenarios, or digital forensics investigations.

## Description

Foremost operates by scanning input data byte-by-byte and matching patterns defined in its configuration or built-in signatures. It supports common file types like images (JPEG, GIF), documents (PDF, OLE), archives (ZIP, GZIP), and more. Users can specify file types via command-line flags or a custom config file for advanced carving. The tool is particularly useful in offensive security for retrieving deleted artifacts (e.g., logs, configs) after gaining access, or in defensive forensics to recover evidence from compromised systems. It works on disk images created by tools like dd, or directly on block devices.

## Features

- File carving based on headers/footers and embedded structures for reliable recovery
- Support for built-in signatures of 20+ common file formats
- Custom configuration for adding new file type definitions
- Output organization by file type with audit logs
- Verbose mode for real-time progress monitoring
- Recursive scanning of image files or direct device access

## Installation

### Requirements

- Linux environment (Kali Linux recommended for pre-built packages)
- Root access for scanning raw devices
- Sufficient disk space for output directories

### Install Commands

```bash
# On Kali Linux (pre-installed)
# No action needed

# On Ubuntu/Debian
apt update && apt install foremost

# From source (GitHub)
git clone https://github.com/korczis/foremost.git
cd foremost
./configure && make && sudo make install
```

## Basic Usage

```bash
foremost --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Display help message and usage |
| -V, --version | Show version information |
| -v | Enable verbose output |
| -q | Quiet mode (minimal output) |
| -t TYPE | Specify file types (e.g., -t jpg,pdf) |
| -c CONFIG | Use custom config file |
| -i INPUT | Input file or device |
| -o OUTPUT | Output directory |

## Examples

### Example 1: Basic Usage

Scan a disk image for all supported file types:

```bash
[[commands/foremost-basic-recovery]]
```

### Example 2: Advanced Usage

Recover only image and document files from a raw device:

```bash
[[commands/foremost-recover-specific-types]]
```

### Example 3: Custom Config

Use a modified config for specific carving rules:

```bash
[[commands/foremost-config-based-recovery]]
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Data from Local System]] Data from Local System (file recovery in post-exploitation)
- [[Archive via Utility]] Archive Collected Data: Archive via Utility (recovering archived files)

### Tactics

- [[Collection]] Collection
- [[Exfiltration]] Exfiltration

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring: Look for 'foremost' processes scanning devices (e.g., via ps aux or auditd)
- File system changes: Creation of output directories with timestamped recovered files
- Disk I/O anomalies: High read activity on images/devices without corresponding writes
- Log entries: Syslog or command history showing foremost invocations

## Related Procedures

- [[procedures/Recover-Deleted-Files-Using-Foremost]]
- [[procedures/Forensic-Analysis-of-Disk-Images]]

## Related Tools

- [[tools/DD]] (for creating disk images)
- [[tools/scalpel]] (alternative carver)
- [[tools/testdisk]] (file system recovery)

## References

- Official GitHub: https://github.com/korczis/foremost
- Man page: man foremost
- Forensic usage guide: https://www.sans.org/blog/digital-forensics-file-carving/

*Last updated: 2023-10-01*
