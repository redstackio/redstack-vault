---
id: 33c20a42-7b05-42d0-ab55-df7fbe295a77
type: tool
verified: true
created_at: '2019-08-28T21:17:35.869762+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - ipv6
  - tcp
  - exploitation
  - network-attack
url: 'https://www.si6networks.com/tools/ipv6toolkit/'
commands:
  - '[[commands/tcp6-send-syn-packet]]'
  - '[[commands/tcp6-send-rst-packet]]'
  - '[[commands/tcp6-tcp-opt-attack]]'
validated: true
---

# tcp6

**Status**: Unverified

## Overview

tcp6 is a specialized tool from the SI6 Networks' IPv6 Toolkit designed to send arbitrary TCP segments over IPv6 networks. It is primarily used for performing TCP-based attacks, such as sequence number prediction, connection hijacking, and denial-of-service scenarios, as well as testing IPv6 TCP implementations for vulnerabilities.

## Description

tcp6 enables security researchers and penetration testers to craft and transmit custom TCP packets, including setting specific flags, sequence numbers, acknowledgments, and options. This makes it invaluable for assessing the security of IPv6-enabled devices and networks by simulating real-world TCP attacks. It is part of a broader suite of IPv6 security assessment tools but focuses specifically on TCP protocol manipulation. Common use cases include TCP reset attacks to disrupt connections, SYN flood simulations, and testing for flaws in TCP option handling.

## Features

- Crafting arbitrary TCP segments with custom headers (source/destination, ports, sequence/ACK numbers, flags, window size)
- Support for IPv6-specific options like hop limit and interface binding
- Attack modes for TCP resets, idle scans, and option-based exploits
- Verbose logging and packet capture integration for analysis
- No payload data transmission, focusing on header manipulation

## Installation

### Requirements

- Linux kernel with IPv6 support enabled
- libpcap for packet capture (usually pre-installed on security distros)
- GCC and make for compilation if building from source

### Install Commands

On Kali Linux or Ubuntu:

```bash
sudo apt update
sudo apt install ipv6toolkit
```

If not available in repositories, download and compile from source:

```bash
wget https://www.si6networks.com/tools/ipv6toolkit/ipv6toolkit-2.0.tar.gz
 tar -xzf ipv6toolkit-2.0.tar.gz
 cd ipv6toolkit-2.0
 ./configure
 make
 sudo make install
```

## Basic Usage

```bash
tcp6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `-v` | Verbose output for debugging |
| `-l` | Enable libpcap logging to capture sent packets |
| `-s SOURCE` | Source IPv6 address |
| `-d DST` | Destination IPv6 address |
| `-p SPORT` | Source port |
| `-P DPORT` | Destination port |
| `-F FLAGS` | TCP flags (e.g., S for SYN, R for RST, A for ACK) |

## Examples

### Example 1: Basic Usage

Send a TCP SYN packet to test connectivity:

```bash
tcp6 -s 2001:db8::1 -d 2001:db8::2 -p 12345 -P 80 -F S -l
```

### Example 2: Advanced Usage

Perform a TCP reset attack by sending RST packets:

```bash
tcp6 -s 2001:db8::fake -d 2001:db8::target -p 80 -P 12345 -F R -A 1000 -S 500 -l -v
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning (for port probing via TCP)
- [[Network Denial of Service]] Network Denial of Service (TCP reset/flood attacks)
- [[Transfer Data to Cloud Account]] Transfer Data to Cloud Account (if combined with exfil over TCP)

### Tactics

- [[Discovery]] Discovery
- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual IPv6 TCP packets with invalid sequence numbers or flags (monitor with Wireshark or tcpdump)
- High volume of RST or SYN packets from spoofed sources
- Libpcap traces showing crafted packets (check /proc/net/tcp6 anomalies)
- Process monitoring for tcp6 binary execution in security logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/addr6]]
- [[tools/scan6]]
- [[tools/Nmap]]

## References

- Official documentation: https://www.si6networks.com/tools/ipv6toolkit/
- GitHub mirror (if available): Search for SI6 IPv6 Toolkit
- Man page: `man tcp6` after installation
