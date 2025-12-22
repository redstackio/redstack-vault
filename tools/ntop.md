---
id: 9f176aae-0055-403d-9861-21dd6bd687d6
name: ntop
type: tool
verified: true
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - Network
  - Monitoring
  - Reconnaissance
url: 'http://www.ntop.org/'
commands:
  - '[[commands/ntop-start-interactive]]'
  - '[[commands/ntop-start-with-interface]]'
  - '[[commands/ntop-start-web-mode]]'
validated: true
---

# ntop

**Status**: Unverified

## Overview

ntop is a network traffic monitoring tool that provides real-time insights into network usage, similar to the Unix 'top' command but focused on traffic flows, protocols, and hosts. In security testing, it is commonly used for reconnaissance, traffic analysis, and identifying anomalous network behavior during red team engagements or incident response.

## Description

ntop captures and analyzes network packets using libpcap, displaying statistics on bandwidth usage, active connections, and protocol distributions. It supports both interactive terminal mode for quick local monitoring and web mode for remote access via a built-in HTTP server. This makes it useful for passive network discovery without generating significant noise. ntop is lightweight and portable across Unix-like systems, though it is an older tool (largely superseded by ntopng for modern features).

## Features

- Real-time traffic monitoring by host, protocol, and application
- Interactive terminal display or web-based interface
- Packet capture integration via libpcap
- Bandwidth and throughput statistics
- Host and flow tracking for anomaly detection

## Installation

### Requirements

- libpcap development libraries
- Unix-like system (Linux recommended)
- Root privileges for packet capture on most interfaces

### Install Commands

For Ubuntu/Debian:

```bash
sudo apt update
sudo apt install ntop
```

For Kali Linux (may require adding repositories or compiling from source):

```bash
sudo apt update
sudo apt install ntop
```

From source (if not available in repos):

```bash
wget http://www.ntop.org/ntop.tar.gz  # Check official site for latest
tar -xzf ntop.tar.gz
cd ntop
./configure
make
sudo make install
```

## Basic Usage

```bash
ntop --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i <interface>` | Specify network interface to monitor (e.g., eth0) |
| `-w <port>` | Start web server on specified port (default 3000) |
| `-n` | Numeric IP addresses (no DNS resolution) |
| `-v` | Increase verbosity |
| `-h` | Show help |

## Examples

### Example 1: Basic Usage

Start interactive monitoring on default interface:

```bash
sudo ntop
```

### Example 2: Advanced Usage

Monitor specific interface and start web server:

```bash
sudo ntop -i eth0 -w 8080
```

Access the web interface at http://localhost:8080.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]] Network Sniffing
- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'ntop' binary with elevated privileges
- Unusual libpcap usage or packet capture on monitoring interfaces
- Web server startup on non-standard ports (e.g., 3000, 8080)
- Network traffic patterns showing passive sniffing without active probes

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/tcpdump]]
- [[tools/Wireshark]]
- [[ntopng]]

## References

- Official website: http://www.ntop.org/
- Source code and documentation: ftp://ftp.ntop.org/
- libpcap integration: http://www.tcpdump.org/
