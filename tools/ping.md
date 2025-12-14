---
id: tool-uuid-3
url: 'https://www.man7.org/linux/man-pages/man8/ping.8.html'
tags:
  - network-test
  - resolution
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.629Z'
validated: true
submitted: true
---
# ping

**Status**: Unverified

## Overview

Used with ltrace to trigger IP resolution for tracing OS behavior in malformed IP tests.

## Description

Standard network utility to send ICMP echoes, here used to invoke inet_aton for alternative IP formats.

## Features

- Feature 1: Resolves hostnames/IPs at OS level
- Feature 2: Counts and timeouts for testing
- Feature 3: Verbose output for debugging

## Installation

### Requirements

- Standard on Linux

### Install Commands

```bash
# Usually pre-installed
sudo apt install iputils-ping
```

## Basic Usage

```bash
ping host
```

### Common Options

| Option | Description |
|--------|-------------|
| -c | Count of pings |
| -i | Interval |

## Examples

### Example 1: Basic Usage

```bash
ping 127.0.0.1
```

### Example 2: Advanced Usage

```bash
ping -c 1 0x7f.1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[System Network Configuration Discovery]] System Network Configuration Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs for ICMP to internal IPs
- Combined with tracing tools

## Related Procedures

- [[procedures/Bypass-SSRF-Filters-with-Hex-and-Decimal-IPs]]

## Related Tools

- [[tools/ltrace]]

## References

- ping man page
