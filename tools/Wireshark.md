---
id: tool-001
url: 'https://www.wireshark.org/'
tags:
  - network-capture
  - traffic-analysis
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.426Z'
validated: true
submitted: true
---
# Wireshark

**Status**: Unverified

## Overview

Wireshark is a free, open-source network protocol analyzer used for capturing and inspecting network traffic in detail, ideal for demonstrating MITM vulnerabilities like token exposure in HTTP requests during security testing.

## Description

Wireshark allows deep packet inspection, filtering by protocols (e.g., HTTP), and analysis of request/response flows. In offensive security, it's commonly used to capture unencrypted data in transit, such as security tokens in password reset links, to validate interception risks without actual MITM deployment.

## Features

- Feature 1: Real-time packet capture and display filtering
- Feature 2: Protocol dissection for HTTP, TCP/IP, etc.
- Feature 3: Exportable captures for further analysis

## Installation

### Requirements

- Compatible OS (Linux, Windows, macOS)
- Administrative privileges for interface access

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update && sudo apt install wireshark

# On macOS with Homebrew
brew install --cask wireshark
```

## Basic Usage

```bash
wireshark &
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i <interface>` | Capture on specific network interface |
| `-k` | Start capture immediately |
| `-w <file>` | Write capture to file |

## Examples

### Example 1: Basic Usage

```bash
wireshark -i eth0 -k -w capture.pcap
```

### Example 2: Advanced Usage

Filter for HTTP traffic during link access:

```bash
wireshark -i lo -f "http" -w http_capture.pcap
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]]

### Tactics

- [[Defense Evasion]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual packet capture processes on endpoints
- High network I/O from analysis tools

## Related Procedures

- [[procedures/Intercept-Token-via-Network-Traffic-Capture]]

## Related Tools

- [[tcpdump]]
- [[tshark]]

## References

- Official documentation: https://www.wireshark.org/docs/
- Related resources: Wireshark User's Guide
