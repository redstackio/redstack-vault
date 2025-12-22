---
url: 'https://www.gnu.org/software/coreutils/df'
tags:
  - disk-usage
type: tool
verified: false
platforms:
  - Linux
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.572Z'
id: 56e87003-36c7-44da-b125-a85ade0ab4a5
validated: true
submitted: true
---
# df

**Status**: Unverified

## Overview

df reports filesystem disk space usage, essential for monitoring exhaustion in DoS scenarios.

## Description

Displays total, used, and available space across mounts, helping verify attack impact on host storage.

## Features

- Feature 1: Human-readable formats
- Feature 2: Specific path querying
- Feature 3: Inode usage option

## Installation

### Requirements

- Coreutils package

### Install Commands

```bash
sudo apt install coreutils
```

## Basic Usage

```bash
df --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h | Human-readable |
| -T | Filesystem type |

## Examples

### Example 1: Basic Usage

```bash
df -h
```

### Example 2: Advanced Usage

```bash
df -h /var/lib/kubelet
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[File and Directory Discovery]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Routine; focus on context of high usage alerts

## Related Procedures

- [[procedures/Confirm-Host-Disk-Exhaustion]]

## Related Tools

- [[tools/du]]

## References

- Man page: man df
