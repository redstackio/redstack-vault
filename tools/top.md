---
url: ''
tags:
  - monitoring
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.279Z'
id: bd3ecf66-f564-492e-ba03-f6be00b4bfb2
validated: true
submitted: true
---
# top

**Status**: Unverified

## Overview

Linux command-line tool for real-time system and process monitoring, used to observe memory leak in PoC.

## Description

Displays CPU, memory, and per-process stats interactively, ideal for tracking RSS growth during vulnerability exploitation.

## Features

- Feature 1: Real-time updates
- Feature 2: Process filtering by PID
- Feature 3: Memory usage breakdown

## Installation

### Requirements

- Standard on most Linux distros

### Install Commands

```bash
# If missing: sudo apt install procps
```

## Basic Usage

```bash
top --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p` | Monitor specific PID |
| `-d` | Update interval |

## Examples

### Example 1: Basic Usage

```bash
top
```

### Example 2: Advanced Usage

```bash
top -p 1234
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]]

### Tactics

- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- top process running
- User monitoring suspicious processes

## Related Procedures

- [[procedures/Monitor-Memory-Consumption]]

## Related Tools

- [[htop]]

## References

- Man page: man top
