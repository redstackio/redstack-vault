---
id: 123e4567-e89b-12d3-a456-426614174009
name: Wireshark
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.766Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - network-analysis
  - packet-capture
url: 'https://www.wireshark.org/'
validated: true
submitted: true
---

# Wireshark

**Status**: Unverified

## Overview

Wireshark is a free, open-source packet analyzer used for capturing and inspecting network traffic, ideal for verifying SSRF by observing server-side connections.

## Description

Wireshark supports deep inspection of protocols like HTTP, allowing filters for POST requests and timing analysis. In SSRF scenarios, it captures client requests and infers server behavior from responses and any leaked traffic.

## Features

- Feature 1: Live packet capture and offline analysis
- Feature 2: Rich display filters (e.g., http.request.method == "POST")
- Feature 3: Export to formats like .pcap for sharing (e.g., http.7z)

## Installation

### Requirements

- Standard user privileges
- Network interface access

### Install Commands

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install wireshark

# macOS (via Homebrew)
brew install --cask wireshark

# Windows: Download from official site
```

## Basic Usage

```bash
tshark -i eth0 -f "tcp port 80" -w capture.pcap
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i <interface>` | Capture on specific interface |
| `-f <filter>` | Capture filter (BPF) |
| `-w <file>` | Write to file |

## Examples

### Example 1: Basic Usage

```bash
wireshark -i lo -k -w ssrf_capture.pcap
```
Start GUI capture on loopback.

### Example 2: Advanced Usage

```bash
tshark -i eth0 -f "host test-4925.myshopify.com" -Y "http contains 'image[src]'" -w analysis.pcap
```
CLI capture and display filter for SSRF requests.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Network Sniffing]] Network Sniffing

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Process names: wireshark.exe, tshark
- High network I/O on analysis machines
- .pcap files in temp directories

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tcpdump]]
- [[Burp Suite]]

## References

- Official documentation: https://www.wireshark.org/docs/
- Related resources: Wireshark User's Guide
