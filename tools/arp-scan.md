---
id: 4eff78d1-b802-4f14-b9b0-372e473e4326
type: tool
verified: true
description: >-
  Command-line tool for discovering hosts on local networks using ARP requests,
  retrieving IP and MAC addresses with vendor lookup.
url: 'https://github.com/royhills/arp-scan'
created_at: '2019-08-28T21:17:39.320426+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Unix
tags:
  - reconnaissance
  - network-discovery
  - arp
validated: true
---

# arp-scan

**Status**: Unverified

## Overview

arp-scan is a fast, lightweight command-line tool designed for sending ARP probes to discover hosts on a local area network (LAN). It identifies live devices by their IP and MAC addresses and can perform OUI (Organizationally Unique Identifier) lookups to identify hardware vendors. It's commonly used in penetration testing for initial network mapping and device inventory in environments where higher-layer protocols like ICMP are filtered.

## Description

The tool operates at Layer 2 of the OSI model by crafting and sending ARP Request packets to specified IP ranges. Responses reveal active hosts without requiring privileged access beyond raw socket permissions. arp-scan supports threading for speed, custom timeouts, and output formatting (e.g., CSV, XML). It's particularly effective on local subnets but limited to the same broadcast domain as the scanning host.

## Features

- Host discovery via ARP requests on local networks
- Automatic MAC address to vendor mapping using built-in OUI database
- Support for scanning specific IP ranges, interfaces, or local networks
- Configurable timeouts, retries, and verbosity levels
- Output in multiple formats including tab-separated, CSV, and XML
- Non-root operation possible with capabilities or setuid

## Installation

### Requirements

- libpcap development libraries
- GCC or compatible compiler for building from source
- Root privileges for raw socket access (or configure setuid)

### Install Commands

On Ubuntu/Debian/Kali:

```bash
sudo apt update
sudo apt install arp-scan
```

On macOS (via Homebrew):

```bash
brew install arp-scan
```

From source (Linux/Unix):

```bash
wget https://github.com/royhills/arp-scan/releases/download/arp-scan-1.10.0/arp-scan-1.10.0.tar.gz
tar -xzf arp-scan-1.10.0.tar.gz
cd arp-scan-1.10.0
./configure
make
sudo make install
sudo make install-ethertool
```

## Basic Usage

```bash
arp-scan --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -l, --localnet | Scan the local network automatically |
| -I, --interface=IFACE | Use a specific network interface |
| --arptimeout=TIMEOUT | Set ARP response timeout in ms (default: 500) |
| --retry=NUM | Number of ARP requests to send per host (default: 3) |
| -v, --verbose | Increase output verbosity |
| -q, --quiet | Suppress non-essential output |
| -M, --format=FORMAT | Output format (normal, csv, xml, grepable) |

## Examples

### Example 1: Basic Usage

Scan the local network:

See [[commands/arp-scan-local-network-scan]]

### Example 2: Advanced Usage

Scan a specific IP range:

See [[commands/arp-scan-ip-range-scan]]

### Example 3: Advanced Usage

Scan using a specific interface:

See [[commands/arp-scan-specific-interface]]

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote System Discovery]] Remote System Discovery
- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- High volume of ARP Request packets from a single source IP/MAC
- ARP traffic patterns inconsistent with normal network behavior (e.g., broadcasts to unused IPs)
- Process monitoring for 'arp-scan' binary execution
- Network IDS alerts on anomalous ARP activity (e.g., Snort rules for ARP storms)
- Log analysis of command-line invocations in audit logs

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
- [[tools/netdiscover]]
- [[tools/ettercap]]

## References

- Official GitHub Repository: https://github.com/royhills/arp-scan
- Man Page: https://linux.die.net/man/8/arp-scan
- OUI Database: Included with tool or downloadable from IEEE
