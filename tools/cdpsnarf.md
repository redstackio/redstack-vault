---
id: c89426ab-6371-47c1-985d-f8d034310818
name: cdpsnarf
type: tool
verified: true
created_at: '2019-08-28T21:17:24.126475+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - network
  - cdp
  - cisco
url: 'https://www.mindcry.org/projects/cdpsnarf.html'
validated: true
---

# cdpsnarf

**Status**: Unverified

## Overview

cdpsnarf is a specialized network sniffer designed to capture and extract detailed information from Cisco Discovery Protocol (CDP) packets. It is commonly used in offensive security operations for network reconnaissance on Cisco-based environments, revealing device details without direct access to the devices.

## Description

cdpsnarf intercepts CDP advertisements sent by Cisco devices to discover neighboring devices, interfaces, and configurations. It provides comprehensive output equivalent to the Cisco 'show cdp neighbors detail' command, including time intervals between advertisements, source MAC addresses, CDP version, TTL, checksum, device ID, software version, platform, IP addresses, port ID, capabilities, and duplex status. The tool supports both live sniffing and offline analysis of PCAP files, making it versatile for passive network mapping in red team engagements.

## Features

- Feature 1: Extracts time intervals, source MAC, CDP version, TTL, and checksum from packets
- Feature 2: Parses device metadata including ID, software version, platform, addresses, port ID, capabilities, and duplex
- Feature 3: Supports saving captured packets to PCAP format and reading from existing PCAP dumps
- Feature 4: Optional debugging output for troubleshooting packet parsing
- Feature 5: Compatible with IPv4 and IPv6 CDP packets

## Installation

### Requirements

- Linux environment with libpcap development libraries
- GCC compiler for building from source
- Root privileges for packet capture

### Install Commands

```bash
# Download source from official site or repository
wget https://www.mindcry.org/files/cdpsnarf-0.1.4.tar.gz

tar -xzf cdpsnarf-0.1.4.tar.gz
cd cdpsnarf-0.1.4

# Compile
make

# Install (optional, or just use ./cdpsnarf)
sudo make install
```

On Kali Linux, it may be available via apt or manual build as above.

## Basic Usage

```bash
cdpsnarf --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --interface | Specify interface for live sniffing |
| -r, --read | Read packets from PCAP file |
| -w, --write | Write captured packets to PCAP file |
| -d, --debug | Enable debugging information |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

Live sniffing on interface:

```bash
cdpsnarf -i eth0
```

### Example 2: Advanced Usage

Read from PCAP with debug:

```bash
cdpsnarf -r capture.pcap -d
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[System Network Configuration Discovery]] System Network Configuration Discovery

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for libpcap-based sniffing processes (e.g., via ps aux | grep cdpsnarf)
- Detection method 2: Network IDS alerts on unusual CDP traffic analysis or PCAP file access
- Detection method 3: File system monitoring for cdpsnarf binaries or compilation artifacts

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

## References

- Official project page: https://www.mindcry.org/projects/cdpsnarf.html
- GitHub mirror (if available): Search for cdpsnarf forks
- Related: Cisco CDP documentation
