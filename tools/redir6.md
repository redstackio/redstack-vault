---
id: 1ccdeeb4-a6ca-48c4-956a-e80d591e03f1
type: tool
verified: true
created_at: '2019-08-28T21:17:32.712222+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - icmp6
  - redirection
  - packet-craft
url: 'https://github.com/salesforce/redir6'
commands:
  - '[[commands/redir6-ipv6-redirect-attack]]'
  - '[[commands/redir6-packet-factory-create-icmp6]]'
  - '[[commands/redir6-analyze-ipv6-traffic]]'
validated: true
---

# redir6

**Status**: Unverified

## Overview

Redir6 is a specialized toolkit designed to exploit inherent protocol weaknesses in IPv6 and ICMPv6. It provides capabilities for performing redirection attacks, crafting custom packets, and analyzing IPv6 traffic, making it useful for security testing, red teaming, and research into IPv6 network vulnerabilities.

## Description

Redir6 targets weaknesses such as improper handling of ICMPv6 Redirect messages, Router Advertisements, and other IPv6 control protocols. The tool includes a packet factory library for easy creation of malformed or spoofed packets, enabling attacks like traffic interception, denial of service, or reconnaissance in IPv6 environments. It is particularly valuable in testing IPv6 implementations for compliance and security gaps.

## Features

- **Redirection Attacks**: Send forged ICMPv6 Redirect messages to hijack traffic flows.
- **Packet Factory Library**: Programmatic creation of IPv6 and ICMPv6 packets for custom exploits.
- **Traffic Analysis**: Parse and identify vulnerabilities in captured IPv6 packets.
- **Spoofing Support**: Easily spoof source addresses to mimic legitimate network elements.
- **Cross-Platform Packet Sending**: Compatible with common network interfaces on Linux.

## Installation

### Requirements

- Linux kernel with IPv6 support enabled.
- libpcap for packet capture and injection (usually pre-installed on security distros).
- GCC or compatible compiler for building from source.

### Install Commands

```bash
# Clone the repository (assuming GitHub source)
git clone https://github.com/salesforce/redir6.git
cd redir6

# Compile the tool
make

# Install (optional, to /usr/local/bin)
sudo make install
```

On Kali Linux, it may be available via apt: `sudo apt update && sudo apt install redir6` (if packaged).

## Basic Usage

```bash
redir6 --help
```

This displays available options, including attack modes, factory commands, and analysis flags.

### Common Options

| Option | Description |
|--------|-------------|
| -i, --interface | Specify network interface |
| -v, --verbose | Enable verbose output for debugging |
| --help | Show help message |
| --version | Display tool version |

## Examples

### Example 1: Basic Usage (Perform Redirection)

```bash
redir6 -i eth0 --redirect-to 2001:db8::attacker
```

### Example 2: Advanced Usage (Craft and Send Packet)

First craft a packet:
```bash
redir6-packet-factory --type icmp6 --create-redirect --target 2001:db8::victim --output custom.pcap
```

Then send it:
```bash
redir6 --send custom.pcap -i eth0
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning (for IPv6 discovery)
- [[Network Denial of Service]] Network Denial of Service (via ICMPv6 floods or redirects)
- [[Windows Remote Management]] Windows Remote Services (adapted for IPv6 traffic manipulation)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual ICMPv6 Redirect or Router Advertisement packets in network logs (e.g., via Snort or Suricata rules for IPv6 anomalies).
- Traffic redirection anomalies detected by IPv6-aware firewalls (e.g., ip6tables logs showing unexpected route changes).
- Packet captures showing spoofed source IPs in ICMPv6 messages.
- Process monitoring for redir6 binary or libpcap usage on suspicious hosts.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/scapy]] (for general packet crafting)
- [[tools/Nmap]] (for IPv6 scanning)

## References

- Official GitHub: https://github.com/salesforce/redir6
- IPv6 Security Considerations: RFC 7113
- Related Research: Black Hat presentations on IPv6 attacks
