---
id: d21f4d1c-fd9e-4aae-922d-a60b4724abf5
type: tool
verified: true
created_at: '2019-08-28T21:17:33.362892+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - sctp
  - scanning
  - telecom
  - reconnaissance
url: 'https://github.com/ValdikSS/sctp-tools'
commands:
  - '[[commands/sctpscan-host-discovery]]'
  - '[[commands/sctpscan-port-scan]]'
  - '[[commands/sctpscan-verbose-scan]]'
validated: true
---

# sctpscan

**Status**: Unverified

## Overview

sctpscan is a specialized scanning tool for the Stream Control Transmission Protocol (SCTP), designed to discover SCTP-enabled hosts and services. It is particularly useful in telecommunications environments for identifying entry points in SS7 and SIGTRAN over IP networks, as well as high-performance networks like Internet2. Common use cases include penetration testing of telecom core infrastructures and protocol-specific reconnaissance.

## Description

sctpscan functions similarly to tools like nmap but focuses exclusively on SCTP, a transport layer protocol that provides reliable, message-oriented communication. It supports host discovery, port scanning, and verbose logging to detect SCTP associations on target systems. This tool is invaluable for red team operations targeting telecom or carrier-grade networks, where SCTP is prevalent for signaling protocols. It helps map out potential attack surfaces by identifying open SCTP endpoints without relying on traditional TCP/UDP scanners.

## Features

- Host discovery via SCTP INIT chunks to check protocol support
- Port scanning for specific SCTP services (e.g., ports 2905 for M3UA)
- Verbose output for detailed association traces and error diagnostics
- Support for custom source ports, interfaces, and TTL values
- Scanning of IP ranges for large-scale telecom network enumeration

## Installation

### Requirements

- Linux kernel with SCTP support (most modern distributions)
- lksctp-tools package for SCTP libraries

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update
sudo apt install lksctp-tools git build-essential

# Clone and build from source (recommended for latest version)
git clone https://github.com/ValdikSS/sctp-tools.git
cd sctp-tools/sctpscan
make
sudo make install
```

For Kali Linux, it may be available via apt: `sudo apt install sctp-tools`.

## Basic Usage

```bash
sctpscan --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -V | Show version information |
| -H | Host discovery mode |
| -p | Specify ports to scan |
| -v | Verbose output level (1-3) |
| -i | Network interface to use |
| -s | Source port |
| -t | TTL value |

## Examples

### Example 1: Basic Usage

Host discovery on a single target:

```bash
sctpscan -H 192.168.1.100
```

### Example 2: Advanced Usage

Scan specific ports with verbosity:

```bash
sctpscan -v 2 -p 2905,5000 10.0.0.50
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[System Network Configuration Discovery]] System Network Configuration Discovery

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual SCTP traffic from scanning tools (monitor for INIT chunks floods)
- Network logs showing SCTP associations to non-standard ports
- Process monitoring for sctpscan binary or related libraries
- IDS rules for SCTP protocol anomalies in telecom segments

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]]
- [[tools/hping3]]

## References

- Official repository: https://github.com/ValdikSS/sctp-tools
- SCTP RFC: https://datatracker.ietf.org/doc/html/rfc4960
- Telecom pentesting guide: Various SS7/SIGTRAN resources
