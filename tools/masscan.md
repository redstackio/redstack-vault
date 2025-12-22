---
id: f552db8e-79cd-4cc9-89c1-46bf28e46b45
name: masscan
type: tool
verified: true
created_at: '2019-08-28T21:17:26.818074+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - Enumeration
  - Network
  - port-scanner
url: 'https://github.com/robertdavidgraham/masscan'
commands:
  - '[[commands/masscan-scan-ip-list-for-ports]]'
validated: true
---

# masscan

**Status**: Verified

## Overview

Masscan is the fastest known Internet port scanner, capable of scanning the entire Internet in under 6 minutes by transmitting up to 10 million packets per second. It produces output similar to Nmap, the most famous port scanner, but operates more like scanrand, unicornscan, and ZMap using asynchronous transmission. Masscan is significantly faster than these alternatives and offers flexibility in specifying arbitrary address and port ranges. It is commonly used in offensive security for rapid network reconnaissance and port discovery during penetration testing and red team engagements.

## Description

Masscan uses a custom TCP/IP stack to achieve its high speed, which can conflict with the local system's TCP/IP stack for operations beyond simple port scans. To mitigate this, use the --source-ip (-S) option to bind to a separate IP address, or configure the operating system to firewall the ports masscan uses. It supports SYN scans by default and can output results in formats compatible with other tools like Nmap. Masscan is ideal for large-scale scans where speed is critical, such as identifying open ports across IP ranges or lists in reconnaissance phases.

## Features

- High-speed asynchronous scanning: Up to 10 million packets per second.
- Flexible input/output: Supports IP lists, CIDR ranges, and various output formats (list, JSON, XML).
- Custom TCP/IP stack: Enables ultra-fast scanning but requires careful configuration to avoid conflicts.
- Rate limiting: Adjustable packet rates to control scan intensity and avoid detection.
- Port range specification: Scan specific ports or full ranges efficiently.
- Banner grabbing: Optional service version detection similar to Nmap's -sV.

## Installation

### Requirements

- Linux kernel with root privileges for raw socket access.
- Build tools (gcc, make) for compilation from source.

### Install Commands

On Kali Linux (pre-installed):
```bash
# Already available as 'masscan'
```

On Ubuntu/Debian:
```bash
sudo apt update
sudo apt install masscan
git clone https://github.com/robertdavidgraham/masscan.git
cd masscan
make
sudo make install
```

On macOS (using Homebrew):
```bash
git clone https://github.com/robertdavidgraham/masscan.git
cd masscan
make
sudo make install
```

## Basic Usage

```bash
masscan --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -p, --ports | Specify ports or ranges (e.g., 80,22-443).
| --rate | Packets per second (default: 100000).
| -iL | Input from list file of IPs/hosts.
| -oL | Output in list format.
| --source-ip (-S) | Bind to a specific source IP to avoid stack conflicts.
| -v | Verbose output.
| --banners | Grab service banners/versions.

## Examples

### Example 1: Basic Usage

Scan a single IP for common ports:
```bash
sudo masscan 192.168.1.1 -p80,443 --rate=1000
```

### Example 2: Advanced Usage

Scan an IP list for a port range and output to file:
```bash
sudo masscan -iL targets.txt --rate=5000 -p1-1000 -oL results.list
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- High-volume SYN packets from a single source without corresponding responses (incomplete handshakes).
- Unusual packet rates or source IP binding patterns in firewall logs.
- Process monitoring for 'masscan' binary execution, often requiring root privileges.
- Network IDS alerts for port scan signatures (e.g., Snort rules for masscan-like traffic).

## Related Procedures

No related procedures linked yet.

## Related Tools

- [[tools/Nmap]]
- [[tools/zmap]]

## References

- Official GitHub: https://github.com/robertdavidgraham/masscan
- Blog post by author: http://blog.erratasec.com/2013/11/masscan-fastest-internet-port-scanner.html
