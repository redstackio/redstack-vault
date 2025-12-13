---
url: ''
tags:
  - network-analysis
type: tool
platforms:
  - Linux
  - Windows
description: >-
  Command-line packet analyzer mentioned as alternative for capturing network
  traffic.
id: 8009cbab-1269-4946-afb0-0fcd07e542a3
created_at: '2025-12-13T09:01:21.736Z'
updated_at: '2025-12-13T09:01:21.736Z'
verified: false
validated: true
submitted: true
---
# tcpdump

**Status**: Unverified

## Overview

tcpdump is a command-line tool for capturing and analyzing network packets, alternative to Wireshark for traffic verification.

## Description

Used to capture HTTP requests and confirm conflicting headers in smuggling tests.

## Features

- Feature 1: Packet dumping
- Feature 2: Filtering expressions
- Feature 3: Output to files

## Installation

### Requirements

- libpcap

### Install Commands

```bash
# On Ubuntu: sudo apt install tcpdump
```

## Basic Usage

```bash
tcpdump --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i` | Interface |
| `-w` | Write to file |

## Examples

### Example 1: Basic Usage

```bash
tcpdump -i eth0
```

### Example 2: Advanced Usage

```bash
tcpdump -i eth0 tcp port 80 -w capture.pcap
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: tcpdump processes
- Detection method 2: Packet capture files

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

## References

- Official documentation: https://www.tcpdump.org/manpages/tcpdump.1.html
