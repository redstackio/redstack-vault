---
url: 'https://man7.org/linux/man-pages/man8/netstat.8.html'
tags:
  - network
  - recon
type: tool
verified: false
platforms:
  - Linux
  - Unix
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.454Z'
id: 3a2a1ea8-31f1-45b0-98dc-9c37075d10f1
validated: true
submitted: true
---
# netstat

**Status**: Unverified

## Overview

netstat is a command-line tool for displaying network connections, routing tables, and interface statistics, commonly used in security testing to identify listening services and potential attack surfaces like exposed WebSocket ports.

## Description

In offensive security, netstat helps enumerate active ports and bindings, such as confirming a server listens on 0.0.0.0 for MiTM opportunities. It's pre-installed on most Unix-like systems, including Android via busybox.

## Features

- Feature 1: Displays active connections and listening ports
- Feature 2: Shows interface statistics and routing
- Feature 3: Supports protocol filtering (TCP/UDP)

## Installation

### Requirements

- Standard on Linux/Unix; for Android, use ADB or Termux

### Install Commands

```bash
# On Debian/Ubuntu
apt install net-tools

# On Android via Termux
pkg install net-tools
```

## Basic Usage

```bash
netstat --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-a` | All sockets |
| `-n` | Numeric output |
| `-t` | TCP only |

## Examples

### Example 1: Basic Usage

```bash
netstat -an
```

### Example 2: Advanced Usage

```bash
netstat -an | grep LISTEN
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for netstat executions in logs
- Network scans triggering IDS alerts

## Related Procedures

- [[procedures/Analyze-PoS-App-WebSocket-Server-Configuration]]

## Related Tools

- [[ss]]
- [[lsof]]

## References

- Official man page: https://man7.org/linux/man-pages/man8/netstat.8.html
