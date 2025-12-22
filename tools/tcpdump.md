---
url: 'https://www.tcpdump.org/'
tags:
  - packet-capture
  - network-analysis
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.373Z'
id: e1094db6-de1d-4ddc-a1be-5bc5bc3a015f
validated: true
submitted: true
---
# tcpdump

**Status**: Unverified

## Overview

tcpdump is a command-line packet analyzer that captures and displays network traffic, essential for reverse-engineering protocols like MySQL's LOAD DATA LOCAL INFILE.

## Description

It allows filtering and dumping packets to pcap files for later analysis with tools like Wireshark. In this context, it's used to capture MySQL traffic on port 3306 to identify the FB packet.

## Features

- Feature 1: Real-time packet capture and filtering (e.g., by port or host)
- Feature 2: Output to pcap for offline analysis
- Feature 3: Hex and ASCII decoding of payloads

## Installation

### Requirements

- Linux/Unix system

### Install Commands

```bash
# On Debian/Ubuntu
sudo apt update && sudo apt install tcpdump

# On CentOS/RHEL
sudo yum install tcpdump
```

## Basic Usage

```bash
tcpdump --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i | Specify interface (e.g., -i lo)
| -w | Write to file (e.g., -w capture.pcap)
| -X | Hex and ASCII output

## Examples

### Example 1: Basic Usage

```bash
tcpdump -i lo port 3306
```

### Example 2: Advanced Usage

```bash
tcpdump -i lo -w mysql.pcap port 3306 -c 100
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for tcpdump executions
- High network I/O on analysis interfaces

## Related Procedures

- [[procedures/Analyze-MySQL-LOAD-DATA-LOCAL-INFILE-Protocol-with-tcpdump]]
- [[procedures/Capture-and-Analyze-FB-Packet-in-MySQL-Traffic]]

## Related Tools

- [[tools/wireshark]]

## References

- Official documentation: https://www.tcpdump.org/manpages/tcpdump.1.html
