---
id: f205a84f-7dcc-43aa-8a6f-25a61217310e
name: fake_dns6d
type: tool
verified: true
created_at: '2019-08-28T21:17:17.808740+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - icmp6
  - spoofing
  - packet-crafting
  - exploitation
url: 'https://github.com/dhondta/fake_dns6d'
validated: true
---

# fake_dns6d

**Status**: Unverified

## Overview

fake_dns6d is a comprehensive toolset designed to exploit weaknesses in IPv6 and ICMP6 protocols. It includes utilities for packet crafting, spoofing DNS responses over IPv6, and launching denial-of-service attacks via ICMP6 floods. Commonly used in red teaming for network protocol testing and evasion in IPv6 environments.

## Description

The tool provides a suite of Python-based scripts and a packet factory library to manipulate IPv6 traffic. It targets inherent flaws like lack of authentication in ICMP6 neighbor discovery and DNS resolution in dual-stack networks. Ideal for simulating attacks such as router advertisement spoofing, DNS poisoning in IPv6, and protocol fuzzing to identify vulnerabilities.

## Features

- Feature 1: DNS spoofing over IPv6 for traffic redirection
- Feature 2: ICMP6 flood attacks to disrupt network services
- Feature 3: Custom packet factory for crafting malformed IPv6/ICMP6 packets
- Feature 4: Support for scapy integration for advanced packet manipulation
- Feature 5: Verbose logging and interface selection for precise control

## Installation

### Requirements

- Python 3.6+
- Scapy library (pip install scapy)
- Root privileges for raw socket access
- Linux kernel with IPv6 enabled

### Install Commands

```bash
# Clone the repository (assuming GitHub source)
git clone https://github.com/dhondta/fake_dns6d.git
cd fake_dns6d

# Install dependencies
pip install -r requirements.txt

# For Kali/Ubuntu
sudo apt update && sudo apt install python3-scapy
```

## Basic Usage

```bash
fake_dns6d --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Enable verbose output for debugging |
| -i, --interface | Specify network interface (e.g., eth0) |
| --target | IPv6 target address |

## Examples

### Example 1: Basic Usage

Spoof a DNS response:

```bash
fake_dns6d --spoof-dns --target 2001:db8::1 --fake-response 2001:db8::dead:beef --interface eth0
```

### Example 2: Advanced Usage

Launch an ICMP6 flood:

```bash
fake_dns6d --icmp6-flood --target 2001:db8::1 --packets 10000 --interface eth0 --rate 1000
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service (ICMP6 floods)
- [[LLMNR-NBT-NS Poisoning and SMB Relay]] Adversary-in-the-Middle (DNS spoofing)
- [[Network Service Scanning]] Network Service Scanning (protocol probing)

### Tactics

- [[Impact]] Impact (DoS)
- [[Defense Evasion]] Defense Evasion (spoofing)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual ICMP6 traffic volumes or malformed packets (monitor with Wireshark or tcpdump)
- Detection method 2: DNS query/response mismatches in IPv6 traffic logs
- Detection method 3: High outbound raw IPv6 packets from unexpected sources (netstat or ss -u)
- Detection method 4: Presence of scapy processes or fake_dns6d binaries in process lists

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Scapy]]
- [[tools/THC-IPV6]]

## References

- Official GitHub: https://github.com/dhondta/fake_dns6d
- IPv6 Security Considerations: RFC 7113
- Scapy Documentation: https://scapy.net
