---
type: tool
verified: true
created_at: '2019-08-28T21:17:19.361012+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - dos
  - rtp
  - voip
  - flood
url: 'https://www.kali.org/tools/rtpflood/'
validated: true
---

# rtpflood

**Status**: Unverified

## Overview

rtpflood is a command-line tool designed to generate and flood RTP (Real-time Transport Protocol) packets to any device processing RTP streams, such as VoIP servers, PBX systems, or media gateways. It is commonly used in penetration testing to simulate denial-of-service (DoS) attacks by overwhelming the target with fake RTP audio streams, causing resource exhaustion or service disruption.

## Description

The tool creates synthetic RTP packets mimicking multiple concurrent audio calls, which can overload the target's CPU or bandwidth. It supports basic flooding and options for source IP/port spoofing, making it suitable for testing VoIP infrastructure resilience. rtpflood is part of the Kali Linux distribution and is typically used in reconnaissance and impact assessment phases of red team engagements targeting communication systems.

## Features

- Feature 1: Generates RTP packets simulating G.711 audio codec streams
- Feature 2: Supports source IP and port specification for controlled or spoofed floods
- Feature 3: Configurable packet rate and duration for realistic attack simulation
- Feature 4: Lightweight and runs from the command line without GUI dependencies

## Installation

### Requirements

- Linux environment with UDP packet generation capabilities (root privileges often required for raw sockets)
- Network interface capable of high packet rates

### Install Commands

```bash
# On Kali Linux (pre-installed)
# No action needed

# On Ubuntu/Debian
sudo apt update
sudo apt install rtpflood

# From source (if needed)
git clone https://github.com/Pepelux/rtpflood.git
cd rtpflood
make
sudo make install
```

## Basic Usage

```bash
rtpflood --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -s <ip> | Specify source IP address |
| -p <port> | Specify source port |
| -l <length> | Set packet length in bytes |
| -r <rate> | Set packet rate (packets per second) |

## Examples

### Example 1: Basic Usage

Flood a target SIP server on port 5060:

```bash
rtpflood 192.168.1.100 5060
```

### Example 2: Advanced Usage

Flood with spoofed source and custom rate:

```bash
rtpflood -s 10.0.0.50 -p 10000 -r 1000 192.168.1.100 5060
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion Flood: UDP Flood

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Sudden increase in inbound RTP/UDP packets from a single or spoofed source to VoIP ports (e.g., 5060, 16384-32767)
- Detection method 2: Network IDS alerts for high-volume UDP floods or anomalous RTP headers (e.g., via Snort rules for G.711 payloads)
- Detection method 3: Server logs showing resource spikes correlated with RTP processing errors

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/scapy]] (for custom packet crafting)
- [[tools/hping3]] (for general UDP flooding)

## References

- Official Kali Documentation: https://www.kali.org/tools/rtpflood/
- GitHub Repository: https://github.com/Pepelux/rtpflood
- Related Resource: VoIP Security Testing Guide
