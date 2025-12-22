---
id: fe65660d-8693-472b-809c-81a3a5313e60
name: nping
type: tool
verified: true
created_at: '2019-08-28T21:17:20.955026+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - packet-crafting
  - network-testing
  - nmap
  - icmp
  - tcp
  - udp
url: 'https://nmap.org/nping/'
validated: true
---

# nping

**Status**: Unverified

## Overview

Nping is a packet generation and response analysis tool included in the Nmap suite. It allows users to craft and send custom network packets (ICMP, TCP, UDP) for testing network devices, firewalls, intrusion detection systems, and performance evaluation in security assessments.

## Description

Nping provides low-level control over packet construction, enabling precise manipulation of headers, payloads, and timing. It supports scripting for automated tests and can capture responses for analysis. Commonly used in offensive security for evading detection, simulating attacks like SYN floods or ICMP tunneling, and in defensive scenarios for validating network configurations.

## Features

- Feature 1: Custom packet crafting for ICMP, TCP, and UDP protocols with full header control.
- Feature 2: Response capture and analysis, including RTT calculations and packet tracing.
- Feature 3: Scripting engine for complex packet sequences and conditional responses.
- Feature 4: Cross-platform support with raw socket access on Unix and WinPcap/Npcap on Windows.

## Installation

### Requirements

- Root/admin privileges for raw socket access.
- Npcap (Windows) or libpcap (Unix) for packet capture.

### Install Commands

```bash
# Kali Linux (pre-installed with Nmap)
sudo apt update && sudo apt install nmap

# Ubuntu
sudo apt update && sudo apt install nmap

# Windows: Download from https://nmap.org/download.html and install Nmap (includes nping)
# macOS
brew install nmap
```

## Basic Usage

```bash
nping --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Increase verbosity level |
| --icmp | Use ICMP protocol |
| --tcp | Use TCP protocol |
| --udp | Use UDP protocol |
| -c <count> | Number of packets to send |
| -p <port> | Destination port |

## Examples

### Example 1: Basic Usage

```bash
nping --icmp 192.168.1.1
```

### Example 2: Advanced Usage

```bash
nping --tcp -p 80 --flags SYN 8.8.8.8
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service (for flood simulations)
- [[Network Service Scanning]] Network Service Scanning (for port probing)

### Tactics

- [[Impact]] Impact
- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual packet patterns in network traffic logs (e.g., malformed headers or rapid packet bursts).
- Detection method 2: Process monitoring for nping.exe or nping binary execution on endpoints.
- Detection method 3: IDS/IPS signatures for crafted packets like non-standard ICMP types or TCP flags.

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

- Official documentation: https://nmap.org/book/nping.html
- Nmap project: https://nmap.org
