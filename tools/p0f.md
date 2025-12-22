---
id: f09654b7-28b2-47d2-8c42-5a953844cd34
type: tool
name: p0f
verified: true
created_at: '2019-08-28T21:17:29.070043+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - macOS
tags:
  - Fingerprint
  - Network
  - Passive
  - OS-Fingerprinting
  - Reconnaissance
url: 'https://lcamtuf.coredump.cx/p0f3/README'
commands:
  - '[[commands/list-network-interfaces]]'
  - '[[commands/p0f-passive-os-fingerprinting]]'
validated: true
---

# p0f

**Status**: Unverified

## Overview

p0f is a passive traffic fingerprinting tool used for identifying operating systems and other system details from TCP/IP communications without generating any additional network traffic. It is commonly used in offensive security for reconnaissance, network mapping, and stealthy information gathering during red team engagements.

## Description

p0f performs passive OS fingerprinting by analyzing TCP packet signatures such as SYN packets, options, and window sizes. It can detect firewalls, estimate network distance, identify connection types (e.g., NAT, load balancers), and provide details like OS version, uptime, and interface types. Unlike active tools like Nmap, p0f operates silently, making it ideal for avoiding detection in sensitive environments. It supports filtering with libpcap syntax and can output results in various formats for further analysis.

## Features

- Feature 1: Passive OS and kernel fingerprinting from TCP SYN/ACK packets
- Feature 2: Detection of NAT, firewalls, and load balancers
- Feature 3: Uptime estimation and distance calculation to remote hosts
- Feature 4: Custom signature support for new OS versions
- Feature 5: Output to files or pipes for integration with other tools

## Installation

### Requirements

- Linux kernel with libpcap support
- Root privileges for packet capture (or configured capabilities)

### Install Commands

```bash
# On Debian/Ubuntu
sudo apt update
sudo apt install p0f

# On Kali Linux (pre-installed in most cases)
sudo apt update
sudo apt install p0f

# From source (if needed)
cd /tmp
git clone https://github.com/lcamtuf/p0f.git
cd p0f
make
sudo make install
```

## Basic Usage

```bash
p0f --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i $_INTERFACE` | Specify the network interface to listen on |
| `-p` | Enable promiscuous mode |
| `-f $_SIGNATURE_FILE` | Use custom signature file |
| `-o $_OUTPUT_FILE` | Log output to file |
| `-s $_FILTER` | Apply libpcap filter (e.g., "tcp port 80") |

## Examples

### Example 1: Basic Usage

Listen on the default interface for passive fingerprinting:

```bash
sudo p0f -i eth0
```

### Example 2: Advanced Usage

Fingerprint HTTP traffic only and log to file:

```bash
sudo p0f -i eth0 "tcp port 80" -o fingerprints.log
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Hardware]] Hardware
- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Process monitoring for 'p0f' binary with packet capture privileges
- Detection method 2: Unusual libpcap usage or promiscuous mode on interfaces
- Detection method 3: Log analysis for passive fingerprinting patterns in network tools

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]]
- [[tools/tcpdump]]

## References

- Official documentation: https://lcamtuf.coredump.cx/p0f3/README
- GitHub repository: https://github.com/lcamtuf/p0f
