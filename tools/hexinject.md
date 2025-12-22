---
id: 33eea5ce-8e59-4e6d-9767-195612b26779
type: tool
verified: true
created_at: '2019-08-28T21:17:30.632597Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - network
  - sniffing
  - injection
  - packet-craft
url: 'https://github.com/securityoffensive/HexInject'
validated: true
---

# hexinject

**Status**: Unverified

## Overview

HexInject is a versatile command-line tool for packet injection and sniffing, providing raw network access. It excels in creating shell scripts for reading, intercepting, and modifying network traffic transparently, making it ideal for network security testing, protocol analysis, and custom packet crafting in offensive security operations.

## Description

HexInject offers a framework for low-level network manipulation, supporting sniffing in hex mode, direct packet injection, and hex editing of captures. It integrates well with other CLI tools like tcpdump or xxd, enabling automated workflows for traffic analysis and simulation of network-based attacks. Commonly used in red teaming for man-in-the-middle scenarios or fuzzing network protocols.

## Features

- Feature 1: Real-time packet sniffing with hex and ASCII output
- Feature 2: Raw packet injection from hex strings or files
- Feature 3: Built-in hex editor for modifying captured traffic
- Feature 4: Scriptable interface for automation in bash/pipes
- Feature 5: Support for common interfaces (Ethernet, WiFi)

## Installation

### Requirements

- Linux kernel with raw socket support
- gcc and make for compilation
- Root privileges for network operations

### Install Commands

```bash
# Clone the repository
git clone https://github.com/securityoffensive/HexInject.git
cd HexInject

# Compile and install
make
sudo make install

# Verify installation
hexinject --help
```

On Kali Linux, it may be available via apt: `sudo apt install hexinject` (check availability).

## Basic Usage

```bash
hexinject --help
```

Displays usage options, including modes for sniff (-s), inject (-c), and edit (-C).

### Common Options

| Option | Description |
|--------|-------------|
| -i, --interface | Specify network interface |
| -s | Sniff mode |
| -c | Inject mode with hex data |
| -C | Edit capture file |
| -h, --help | Show help |
| -v | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
hexinject -i eth0 -s
```

Starts sniffing on eth0, outputting packets in hex.

### Example 2: Advanced Usage

```bash
hexinject -i eth0 -c "4500003c000040004011abcd0a0000010a0000020800"
```

Injects an ICMP ping packet to 10.0.0.2.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]] Network Sniffing
- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[T1025.004]] Indicator Removal on Host (for traffic manipulation)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for raw socket creations (e.g., via auditd or sysdig)
- Detection method 2: Unusual network traffic patterns or hex-encoded processes
- Detection method 3: Process listings showing hexinject binary
- Detection method 4: Increased promiscuous mode on interfaces (ifconfig/ethtool)

## Related Procedures

No related procedures linked yet.

## Related Tools

- [[tools/tcpdump]]
- [[tools/scapy]]
- [[tools/Wireshark]]

## References

- Official GitHub: https://github.com/securityoffensive/HexInject
- Man page: `man hexinject` after installation

*Last updated: 2023-10-01T00:00:00Z*
