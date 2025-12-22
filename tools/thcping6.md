---
id: 233eaa2d-d171-46cf-8750-03ba26bc9df3
type: tool
verified: true
created_at: '2019-08-28T21:17:31.334103+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - icmp6
  - network
  - exploitation
url: 'https://github.com/vanhauser-thc/thc-ipv6'
validated: true
---

# thcping6

**Status**: Unverified

## Overview

thcping6 is a command-line tool from the THC-IPv6 toolkit designed for sending ICMPv6 echo requests (pings) over IPv6 networks. It exploits protocol weaknesses in IPv6 and ICMPv6 for security testing, reconnaissance, and potential denial-of-service simulations. Commonly used in penetration testing to assess IPv6 connectivity, spoofing capabilities, and network resilience.

## Description

thcping6 provides advanced IPv6 pinging functionality beyond standard tools like ping6, including support for source address specification, flooding, looping, and integration with packet crafting libraries. It is part of a broader suite for attacking IPv6 protocol vulnerabilities, making it valuable for red team operations targeting IPv6-enabled infrastructures. The tool includes an easy-to-use packet factory library for custom ICMPv6 packet construction.

## Features

- Feature 1: Basic ICMPv6 echo requests with customizable packet sizes and counts
- Feature 2: Source IP spoofing and interface binding for evasion and testing
- Feature 3: Flood mode for high-rate packet transmission to simulate DoS attacks
- Feature 4: Loop mode for continuous pinging until interrupted
- Feature 5: Integration with libnet for advanced packet manipulation

## Installation

### Requirements

- Linux kernel with IPv6 support
- libnet-dev and libpcap-dev libraries
- GCC compiler

### Install Commands

```bash
# Clone the THC-IPv6 repository
git clone https://github.com/vanhauser-thc/thc-ipv6.git
cd thc-ipv6

# Install dependencies (on Ubuntu/Debian)
apt update && apt install libnet-dev libpcap-dev libpcre3-dev libev-dev

# Compile and install
./configure
make
make install
```

For Kali Linux, the toolkit is available via apt:

```bash
apt update && apt install thc-ipv6
```

## Basic Usage

```bash
thcping6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v, --verbose | Enable verbose output for debugging |
| -c <count> | Send specified number of pings |
| -s <source> | Specify source IPv6 address or interface |
| -f | Flood mode: Send packets as fast as possible |
| -L | Loop mode: Ping continuously until interrupted |

## Examples

### Example 1: Basic Usage

```bash
thcping6 2001:db8::1
```

Sends default ICMPv6 pings to the target IPv6 address.

### Example 2: Advanced Usage

```bash
thcping6 -s fe80::2%eth0 -c 10 -f 2001:db8::1
```

Floods the target with 10 pings from a specified source interface.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning (for reconnaissance via pings)
- [[Network Denial of Service]] Network Denial of Service (via flood pings)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual ICMPv6 echo request volumes or patterns from libnet-based tools
- Detection method 2: Network logs showing high-rate IPv6 traffic from unexpected sources
- Detection method 3: Process monitoring for thcping6 binary or THC-IPv6 toolkit processes

## Related Commands

- [[commands/thcping6-basic-ipv6-ping]]
- [[commands/thcping6-ipv6-ping-flood]]
- [[commands/thcping6-ipv6-ping-with-source]]

## Related Tools

- [[scapy]] (Python packet crafting alternative)
- [[tools/hping3]] (IPv4/IPv6 packet generator)

## References

- Official GitHub: https://github.com/vanhauser-thc/thc-ipv6
- THC-IPv6 Documentation: Included in repository README
