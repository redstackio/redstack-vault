---
id: tool-ping-927413
url: 'https://www.man7.org/linux/man-pages/man8/ping.8.html'
tags:
  - network
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.599Z'
validated: true
submitted: true
---
# ping

**Status**: Unverified

## Overview

Ping is a network utility for testing reachability and resolving domains to IPs, used in initial Zomato recon.

## Description

Sends ICMP echoes to check host availability and gather basic network info. Essential for starting scans.

## Features

- Feature 1: IP resolution
- Feature 2: Latency measurement
- Feature 3: Packet loss detection

## Installation

### Requirements

- Standard on most OS

### Install Commands

```bash
# Usually pre-installed
```

## Basic Usage

```bash
ping --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-c` | Count of pings |
| `-i` | Interval |

## Examples

### Example 1: Basic Usage

```bash
ping zomato.com
```

### Example 2: Advanced Usage

```bash
ping -c 4 zomato.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- High ICMP traffic
- Log anomalous pings

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool: nmap]]

## References

- Official man page
