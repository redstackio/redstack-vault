---
url: ''
tags:
  - network-analysis
type: tool
platforms:
  - Linux
  - Windows
description: >-
  Network protocol analyzer to capture and verify HTTP traffic showing
  conflicting headers.
id: e982e0a7-2c45-45f0-a45b-94b562d8bfc3
created_at: '2025-12-13T09:01:21.746Z'
updated_at: '2025-12-13T09:01:21.746Z'
verified: false
validated: true
submitted: true
---
# Wireshark

**Status**: Unverified

## Overview

Wireshark is a network protocol analyzer used to capture and inspect packet-level data, ideal for verifying vulnerabilities in HTTP traffic.

## Description

In security operations, it's used to analyze requests for anomalies like conflicting headers in HTTP smuggling tests.

## Features

- Feature 1: Packet capturing and filtering
- Feature 2: Protocol dissection
- Feature 3: Exportable captures

## Installation

### Requirements

- libpcap on Linux

### Install Commands

```bash
# On Ubuntu: sudo apt install wireshark
```

## Basic Usage

```bash
wireshark
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i` | Interface to capture | 
| `-f` | Capture filter |

## Examples

### Example 1: Basic Usage

```bash
tshark -i eth0 -f "tcp port 80"
```

### Example 2: Advanced Usage

```bash
wireshark -r capture.pcap
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Promiscuous mode on interfaces
- Detection method 2: Running processes named wireshark

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

## References

- Official documentation: https://www.wireshark.org/docs/
