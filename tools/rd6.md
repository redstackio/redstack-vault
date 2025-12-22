---
id: 3016e7dc-c6fb-4235-b3bb-5ed18dbf1d7d
type: tool
verified: true
created_at: '2019-08-28T21:17:37.410899+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - icmpv6
  - redirect
  - network-attack
  - security-assessment
url: 'https://github.com/six2dez/ipv6-toolkit'
validated: true
---

# rd6

**Status**: Unverified

## Overview

rd6 is a specialized tool from the SI6 Networks' IPv6 Toolkit designed for sending arbitrary ICMPv6 Redirect messages. It is used in IPv6 security assessments to test network resiliency against redirect-based attacks, such as man-in-the-middle (MITM) scenarios or traffic redirection. Common use cases include evaluating how IPv6-enabled devices and routers handle unexpected redirects, troubleshooting IPv6 routing issues, and simulating real-world attacks to identify weaknesses in Neighbor Discovery Protocol (NDP) implementations.

## Description

The rd6 tool allows users to craft and transmit custom ICMPv6 Redirect messages, which inform receivers to reroute traffic to a specified gateway. This can be leveraged to perform security assessments of IPv6 networks by simulating attacks that exploit ICMPv6 processing flaws. For example, attackers could redirect traffic to a malicious host for interception or denial-of-service effects. rd6 supports various options for specifying source/destination addresses, gateways, targets, and message types (e.g., standard redirects or DNS redirects). It is part of a broader suite of IPv6 tools including addr6, flow6, frag6, and others, but focuses specifically on redirect message manipulation. The tool requires root privileges and an IPv6-capable interface.

## Features

- **Custom Message Crafting**: Specify source IP, destination IP, gateway IP, and target IP for precise control over redirect messages.
- **Interface Binding**: Bind to specific network interfaces for targeted testing.
- **Advanced Redirect Types**: Support for DNS redirect attacks (-D option) and redirects to all nodes (-A option).
- **Verbose Output**: Detailed logging of sent packets for analysis.
- **Attack Simulation**: Facilitate MITM or traffic diversion tests without complex scripting.

## Installation

### Requirements

- Linux system with IPv6 support enabled.
- Root or sudo privileges for raw socket access.
- libnetfilter-queue and libpcap development libraries (for compilation).

### Install Commands

On Kali Linux (pre-packaged):
```bash
sudo apt update
sudo apt install ipv6-toolkit
```

On Ubuntu/Debian (from source):
```bash
sudo apt update
sudo apt install git build-essential libnetfilter-queue-dev libpcap-dev libnet1-dev libdnet-dev libfdisk-dev bison flex

git clone https://github.com/six2dez/ipv6-toolkit.git
cd ipv6-toolkit/source
./configure
make
sudo make install
```

On macOS (via Homebrew, limited support):
```bash
brew install --HEAD https://raw.githubusercontent.com/Homebrew/homebrew-core/f123c4c0bdde0a3b8f7e3a1a4c3b2d5e6f7a8b9c/Formula/i/ipv6-toolkit.rb
```
(Note: Full functionality may require additional setup for raw sockets.)

## Basic Usage

```bash
rd6 --help
```

This displays the help menu with all available options.

### Common Options

| Option | Description |
|--------|-------------|
| `-i, --interface` | Specify the network interface to use (e.g., eth0) |
| `-s, --src-addr` | Source IPv6 address for the packet |
| `-d, --dst-addr` | Destination IPv6 address (target receiving the redirect) |
| `-g, --gateway` | Redirect gateway IPv6 address |
| `-t, --target` | Original target IP being redirected |
| `-A` | Send redirect to all nodes multicast address |
| `-D` | Perform DNS redirect attack |
| `-v` | Verbose output |
| `-h` | Show help |

## Examples

### Example 1: Basic Usage

Send a basic ICMPv6 redirect message on interface eth0, redirecting traffic from a target to a fake gateway.

```bash
sudo rd6 -i eth0 -s 2001:db8::1 -d 2001:db8::2 -g 2001:db8::dead:beef -t 2001:db8::3
```

### Example 2: Advanced Usage

Send a DNS redirect attack to spoof DNS responses via redirect.

```bash
sudo rd6 -i eth0 -D -s 2001:db8::1 -d 2001:db8::2 -g 2001:db8::fake-dns
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[LLMNR-NBT-NS Poisoning and SMB Relay]] LLMNR/NBT-NS Poisoning and Name Resolution Spoofing (adapted for IPv6 NDP)
- [[Network Denial of Service]] Network Denial of Service (via redirect floods or disruptions)

### Tactics

- [[Discovery]] Discovery (network mapping via redirects)
- [[Privilege Escalation]] Privilege Escalation (MITM for credential capture)

## Detection

Indicators and methods for detecting this tool's usage:

- **Network Traffic Monitoring**: Look for anomalous ICMPv6 Redirect messages (Type 137) with unexpected source IPs or gateways using tools like Wireshark or tcpdump: `tcpdump -i eth0 ip6 proto icmp6 and 'icmp6[0] == 137'`.
- **System Logs**: Check for raw socket creations or unusual IPv6 traffic spikes in firewall logs (e.g., iptables or nftables rules for ICMPv6).
- **Process Monitoring**: Identify rd6 binary execution via `ps aux | grep rd6` or endpoint detection tools flagging IPv6 toolkit processes.
- **NDP Validation**: Enable Router Advertisement Guard (RA Guard) or DHCPv6 snooping on switches/routers to drop invalid redirects.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/addr6]] (IPv6 address analysis)
- [[tools/ra6]] (Router Advertisement sender)
- [[tools/ns6]] (Neighbor Solicitation sender)
- [[tools/scan6]] (IPv6 scanning)

## References

- Official GitHub Repository: https://github.com/six2dez/ipv6-toolkit
- SI6 Networks Documentation: http://www.si6networks.com/tools/ipv6toolkit/
- IPv6 Security Best Practices: RFC 7113 (Implementation of ICMPv6 Redirect Protection)
