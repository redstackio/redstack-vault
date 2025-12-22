---
type: tool
verified: true
description: >-
  TShark is a command-line network protocol analyzer that captures live packet
  data or reads from saved capture files, providing detailed summaries of
  network traffic similar to Wireshark but optimized for terminal use.
url: 'https://www.wireshark.org/docs/man-pages/tshark.html'
platforms:
  - Linux
tags:
  - enumeration
  - network
commands:
  - '[[commands/tshark-read-pcap-hex-ascii-dump]]'
validated: true
---

# TShark

**Status**: Unverified

## Overview

TShark is the command-line version of Wireshark, a powerful network protocol analyzer used in security testing for capturing and analyzing network traffic. It excels at dissecting packets from live interfaces or PCAP files, making it ideal for reconnaissance, traffic analysis, and identifying unencrypted data in protocols like LDAP or HTTP during red team engagements.

## Description

TShark allows users to capture packets in real-time or offline from capture files, applying filters to focus on specific traffic types. Unlike tcpdump, which provides raw captures, TShark offers protocol dissection and human-readable summaries. It supports the same capture and display filters as Wireshark, enabling precise targeting of traffic such as specific ports, protocols, or IP ranges. Common use cases in offensive security include sniffing for credentials in clear-text protocols, analyzing application-layer data, and extracting artifacts from PCAPs for post-exploitation forensics.

## Features

- Feature 1: Real-time packet capture from network interfaces with BPF filters.
- Feature 2: Offline analysis of PCAP files with protocol decoding for hundreds of protocols.
- Feature 3: Hex and ASCII dumps for low-level packet inspection.
- Feature 4: Output formatting options including JSON, PDML, or text summaries.
- Feature 5: Integration with Wireshark filters for display and capture control.

## Installation

### Requirements

- Root or sudo access for live captures (due to raw socket needs).
- libpcap library (usually installed by default on Linux).

### Install Commands

```bash
# On Kali Linux (pre-installed)
sudo apt update && sudo apt install tshark

# On Ubuntu/Debian
sudo apt update && sudo apt install tshark

# On macOS (via Homebrew)
brew install wireshark

# On Windows
Download from https://www.wireshark.org/download.html and install the Wireshark suite (includes TShark)
```

## Basic Usage

```bash
tshark --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i <interface>` | Capture from specific interface (e.g., eth0) |
| `-r <file>` | Read packets from capture file |
| `-w <file>` | Write packets to capture file |
| `-f <filter>` | Capture filter (BPF syntax) |
| `-Y <filter>` | Display filter (Wireshark syntax) |
| `-x` | Add hex/ASCII dump of packet bytes |
| `-V` | Verbose packet dissection |
| `-c <count>` | Stop after capturing N packets |

## Examples

### Example 1: Basic Usage

Capture 10 packets on interface eth0:

```bash
tshark -i eth0 -c 10
```

### Example 2: Advanced Usage

Read a PCAP file and filter for HTTP traffic with hex dump:

```bash
tshark -r capture.pcap -Y "http" -x
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]] Network Sniffing
- [[Standard Application Layer Protocol]] Application Layer Protocol

### Tactics

- [[Discovery]] Discovery
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Process monitoring for tshark.exe or tshark binary execution, especially with raw socket privileges.
- Detection method 2: Network anomalies from promiscuous mode on interfaces (e.g., via ethtool or ifconfig).
- Detection method 3: File system artifacts like temporary PCAP files in /tmp or user directories.
- Detection method 4: Sysmon Event ID 1 for process creation with command-line arguments containing -i or -r flags.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Wireshark]]
- [[tools/tcpdump]]

## References

- Official documentation: https://www.wireshark.org/docs/man-pages/tshark.html
- Capture filters guide: https://wiki.wireshark.org/CaptureFilters
- Display filters reference: https://www.wireshark.org/docs/man-pages/tshark.html#dfref
