---
id: f45d9845-b58d-47ab-8a66-b41b76df04de
type: tool
verified: true
created_at: '2019-08-28T21:17:36.954432+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Unix
tags:
  - evasion
  - network
  - ids-testing
  - traffic-manipulation
url: 'https://www.monkey.org/~dugsong/fragroute/'
commands:
  - '[[commands/fragroute-basic-intercept]]'
  - '[[commands/fragroute-fragment-packets]]'
  - '[[commands/fragroute-delay-packets]]'
  - '[[commands/fragroute-drop-packets]]'
validated: true
---

# fragroute

**Status**: Unverified

## Overview

Fragroute is a network tool designed to intercept, modify, and rewrite egress traffic destined for a specified host. It implements various evasion and denial-of-service techniques described in the Secure Networks paper "Insertion, Evasion, and Denial of Service: Eluding Network Intrusion Detection" (January 1998). Commonly used in penetration testing to evaluate the robustness of network intrusion detection systems (IDS), firewalls, and TCP/IP stack implementations against fragmentation, delay, and other manipulations.

## Description

Fragroute features a simple ruleset language to delay, duplicate, drop, fragment, overlap, print, reorder, segment, source-route, or otherwise manipulate outbound packets to a target host. It supports minimal randomized or probabilistic behavior. Written to aid in testing network security controls, it should be used ethically and only in authorized environments. Note: This is an older tool (circa 2001) and may require compilation on modern systems; alternatives like Scapy or custom iptables rules can achieve similar effects.

## Features

- **Traffic Interception**: Captures and modifies all egress packets to a target.
- **Ruleset Language**: Supports actions like fragment, delay, drop, duplicate, order, print, segment, and source-route.
- **Protocol Filtering**: Rules can target specific protocols (e.g., tcp, udp, icmp, tftp).
- **Probabilistic Modifications**: Random delays or drops for realistic testing.
- **Background Operation**: Runs silently, allowing integration with other tools like nmap or custom scripts.

## Installation

### Requirements

- Linux/Unix system with libpcap development libraries.
- GCC compiler.
- Root privileges for raw socket access.

### Install Commands

```bash
# Download source (if available from official site or GitHub mirrors)
wget https://www.monkey.org/~dugsong/fragroute/fragroute-1.2.tar.gz

tar -xzf fragroute-1.2.tar.gz
cd fragroute-1.2

# Compile
./configure
make
sudo make install

# Alternative: On Kali/Debian, may be available in repos or build from source
sudo apt update
sudo apt install libpcap-dev build-essential
# Then compile as above
```

For modern distributions, check GitHub forks (e.g., search "fragroute github") for patched versions compatible with current kernels.

## Basic Usage

```bash
fragroute --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -f <rules> | Load rules from file or inline string |
| -B <if> | Bind to specific network interface |
| -m <mtu> | Set maximum transmission unit |
| -u | Run in UDP mode only |

## Examples

### Example 1: Basic Usage

Intercept traffic to a target using a rules file:

```bash
fragroute -f basic.rules 192.168.1.100
```

Where `basic.rules` contains: `tcp>print;`

### Example 2: Advanced Usage

Apply fragmentation and delay:

```bash
fragroute -f 'tcp>fragment:8@0+;delayfirst:500' 192.168.1.100
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Software Packing]] Software Packing (for evasion via packet manipulation)
- [[Disable or Modify Tools]] Disable or Modify Tools (impairing IDS via evasion)
- [[Endpoint Denial of Service]] Endpoint Denial of Service (via drop/delay rules)

### Tactics

- [[Defense Evasion]] Defense Evasion
- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual packet fragmentation or overlaps in network traffic (e.g., via Wireshark filters: ip.flags.mf == 1).
- Anomalous delays or drops in TCP handshakes (monitor with tcpdump: tcp.analysis.lost_segment).
- Process monitoring for fragroute binary or libpcap usage on edge hosts.
- IDS signatures for known fragroute patterns (e.g., overlapping fragments).
- Network flow analysis showing probabilistic packet loss to specific targets.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/scapy]]
- [[tools/Nmap]]
- [[tools/tcpdump]]

## References

- Official site: https://www.monkey.org/~dugsong/fragroute/
- Original paper: "Insertion, Evasion, and Denial of Service: Eluding Network Intrusion Detection" (1998)
- GitHub mirrors for source code and patches
