---
url: ''
tags:
  - networking
type: tool
platforms:
  - Linux
description: 'Displays network connections, routing tables, and interface statistics'
id: 6223d4b0-3723-4938-9bd8-6a92281abf5b
created_at: '2025-12-14T04:08:47.991Z'
updated_at: '2025-12-14T04:08:47.991Z'
verified: false
validated: true
submitted: true
---
# netstat

**Status**: Unverified

## Overview

Netstat shows active network connections with PIDs, useful for discovering listening services like dockerd.

## Description

Provides detailed socket info; -tanp flags show TCP, numeric, with programs/PIDs for process enumeration.

## Features

- Feature 1: Connection listing
- Feature 2: PID association
- Feature 3: Interface stats

## Installation

### Requirements

- net-tools package

### Install Commands

```bash
apt install net-tools
```

## Basic Usage

```bash
netstat --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -t | TCP |
| -a | All |
| -n | Numeric |
| -p | Programs |

## Examples

### Example 1: Basic Usage

```bash
netstat -tanp
```

### Example 2: Advanced Usage

```bash
netstat -tanp | grep 2376
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Process Discovery]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Sudo netstat runs in logs

## Related Procedures


## Related Tools

- ss (modern alternative)

## References

- Man netstat
