---
id: 42aacf85-c555-46db-a9b4-42750bc61c69
type: tool
verified: true
created_at: '2019-08-28T21:17:31.886940+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - evasion
  - network
  - ids
  - dos
url: 'http://www.anzen.com/research/fragrouter.html'
validated: true
---

# fragrouter

**Status**: Unverified

## Overview

Fragrouter is a network intrusion detection evasion toolkit designed to fragment and manipulate IP packets, implementing various attacks outlined in the 1998 Secure Networks paper on insertion, evasion, and denial of service techniques. It acts as a one-way router that transforms incoming packets into fragmented streams to bypass NIDS/IPS systems.

## Description

Fragrouter forwards packets from an attacker machine through specified fragmentation modes to a victim, exploiting weaknesses in network stack reassembly. Common use cases include testing IDS evasion during penetration tests, simulating DoS via fragment overload, and inserting deceptive traffic to confuse monitoring tools. It supports multiple fragmentation strategies like basic splitting, overlapping fragments (teardrop), and insertion attacks.

## Features

- Feature 1: Multiple fragmentation modes (e.g., basic, teardrop, insertion) for diverse evasion techniques
- Feature 2: Rule-based filtering with libpcap for targeted packet manipulation
- Feature 3: Support for IP, TCP, UDP, and ICMP fragmentation to evade signature-based detection
- Feature 4: Integration with traffic generators like hping3 or nmap for amplified attacks

## Installation

### Requirements

- Linux kernel with IP forwarding enabled
- libpcap development libraries
- Root privileges for raw socket access

### Install Commands

```bash
# On Kali Linux (pre-installed in some versions)
sudo apt update && sudo apt install fragrouter

# On Ubuntu/Debian from source (if not in repos)
sudo apt install libpcap-dev build-essential
git clone https://github.com/old-repos/fragrouter.git  # Note: Original source is archived
cd fragrouter && make && sudo make install

# Enable IP forwarding
sudo sysctl -w net.ipv4.ip_forward=1
```

## Basic Usage

```bash
fragrouter --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -f <filter> | libpcap filter expression (e.g., "tcp port 80") |
| -F <mode> | Fragmentation mode (1-15, see man page) |
| -B <mtu> | Base MTU for fragmentation |
| -m <mtu> | Maximum segment size |
| -t | Enable TCP reassembly simulation |

## Examples

### Example 1: Basic Usage

Set up basic fragmentation on interface eth0 targeting a web server:

```bash
fragrouter -F 1 eth0 192.168.1.100 80
```

### Example 2: Advanced Usage

Teardrop DoS with traffic piping:

```bash
hping3 --flood -S 192.168.1.100 -p 80 | fragrouter -F 8 eth0 192.168.1.100 80
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Obfuscated Files or Information]] Obfuscated Files or Information
- [[Encrypted Channel]] Encrypted Channel (for evading inspection)

### Tactics

- [[Defense Evasion]] Defense Evasion
- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual IP fragmentation patterns in network traffic (e.g., overlapping offsets via tcpdump: "tcpdump -i eth0 ip[6:2] & 0x1fff != 0")
- Detection method 2: High volume of incomplete fragments causing reassembly failures in IDS logs (Snort/Suricata rules for frag anomalies)
- Detection method 3: Process monitoring for fragrouter binary or libpcap usage on edge devices
- Detection method 4: Anomaly in packet MTU/MSS sizes deviating from baseline

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/hping3]]
- [[scapy]]
- [[tools/nping]]

## References

- Original paper: "Insertion, Evasion, and Denial of Service: Eluding Network Intrusion Detection" (Secure Networks, 1998)
- Man page: man fragrouter
- Kali Tools: https://www.kali.org/tools/fragrouter
