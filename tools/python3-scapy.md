---
url: 'https://scapy.net/'
tags:
  - network
  - packet-craft
type: tool
verified: false
platforms:
  - Linux
  - Python
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.862Z'
id: 56500e19-f7d8-4026-a985-67e0f3de4341
validated: true
submitted: true
---
# python3-scapy

**Status**: Unverified

## Overview

Python library for packet manipulation, sniffing, and forging, ideal for MITM and network attacks in security testing.

## Description

Scapy allows interactive packet construction and dissection. In this exploit, it's used to intercept HTTP requests to the metadata service and inject SSH keys.

## Features

- Feature 1: Packet sniffing (sniff())
- Feature 2: Packet forging and sending (sendp())
- Feature 3: Protocol dissection

## Installation

### Requirements

- Python 3

### Install Commands

```bash
apt install python3-scapy
# Or pip install scapy
pip3 install scapy
```

## Basic Usage

```bash
python3 -c "from scapy.all import *; sniff()
```

### Common Options

| Option | Description |
|--------|-------------|
| sniff() | Capture packets |
| send() | Send packets |
| IP()/TCP() | Layer constructors |

## Examples

### Example 1: Basic Usage

```bash
python3 -c "from scapy.all import *; p = IP()/TCP(); send(p)"
```

### Example 2: Advanced Usage

```bash
python3 -c "from scapy.all import *; packets = sniff(filter='tcp port 80', count=10); wrpcap('capture.pcap', packets)"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Tactics

- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- scapy processes
- Unusual raw socket usage
- Packet injection anomalies

## Related Procedures

- [[procedures/Execute-MITM-Exploit-Script-for-Privilege-Escalation]]

## Related Tools

- [[tools/wireshark]]

## References

- Official documentation: https://scapy.readthedocs.io/
