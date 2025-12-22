---
id: 34d1ff99-4bd7-4728-9176-b5e6517523c0
type: tool
name: cisco-torch
verified: true
description: >-
  Cisco Torch is a mass scanning, fingerprinting, and exploitation tool designed
  for discovering and attacking Cisco network devices.
url: 'https://packetstormsecurity.com/files/65279/cisco-torch-1.2.tar.gz'
tags:
  - cisco
  - scanning
  - fingerprinting
  - brute-force
  - reconnaissance
  - exploitation
platforms:
  - Linux
  - Network
commands:
  - '[[commands/cisco-torch-basic-host-scan]]'
  - '[[commands/cisco-torch-service-fingerprint]]'
  - '[[commands/cisco-torch-dictionary-brute-force]]'
category: Reconnaissance
created_at: '2019-08-28T21:17:20.702693+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
validated: true
---

# cisco-torch

**Status**: Unverified

## Overview

Cisco Torch is a specialized tool for mass scanning, fingerprinting, and exploiting Cisco network devices. It is particularly useful for identifying remote Cisco hosts running services such as Telnet, SSH, HTTP/HTTPS, NTP, and SNMP, and then launching targeted dictionary attacks against those services. Developed to address limitations in existing tools, it emphasizes efficiency through process forking and multi-method application-layer fingerprinting.

## Description

Cisco Torch was created during the development of the book 'Hacking Exposed Cisco Networks' to provide a fast and comprehensive way to discover vulnerable Cisco infrastructure. Unlike basic scanners, it forks multiple background processes for parallel scanning, maximizing speed across large IP ranges. It supports simultaneous fingerprinting techniques to accurately identify device types and versions. Once services are discovered, the tool can initiate brute-force attacks using wordlists, focusing on common weak credentials in Cisco environments. It is ideal for penetration testing Cisco-heavy networks, such as enterprise routers, switches, and firewalls.

## Features

- **Mass Scanning**: Rapid discovery of Cisco devices across IP ranges using forking for efficiency.
- **Service Fingerprinting**: Identifies Telnet, SSH, Web (HTTP/HTTPS), NTP, and SNMP services with version detection.
- **Dictionary Attacks**: Automated brute-force against discovered services using customizable wordlists.
- **Multi-Method Detection**: Combines banner grabbing, protocol probes, and timing analysis for accurate fingerprinting.
- **Output Logging**: Generates detailed logs of scans, fingerprints, and attack results for analysis.

## Installation

### Requirements

- Perl 5 (with modules: Net::Telnet, Net::SSH::Perl, IO::Socket::SSL, Getopt::Long)
- Wordlists for brute-force (e.g., rockyou.txt)
- Root privileges for raw socket operations (optional but recommended for speed)

### Install Commands

```bash
# Download the tool (version 1.2)
wget https://dl.packetstormsecurity.net/cisco/cisco-torch-1.2.tar.gz

tar -xzf cisco-torch-1.2.tar.gz
cd cisco-torch-1.2

# Install Perl dependencies (on Debian/Ubuntu)
apt update
apt install libnet-telnet-perl libnet-ssh-perl libio-socket-ssl-perl libgetopt-long-perl

# Make executable
chmod +x cisco-torch.pl
```

On Kali Linux, it may require manual dependency installation as it's not in repositories.

## Basic Usage

```bash
./cisco-torch.pl -z 192.168.1.0/24
```

### Common Options

| Option | Description |
|--------|-------------|
| `-z` | Specify IP range for scanning (CIDR or list) |
| `-s` | Enable service scanning (Telnet, SSH, etc.) |
| `-f` | Perform fingerprinting on discovered hosts |
| `-C` | Path to common credentials wordlist for attacks |
| `-h` | Show help |
| `-v` | Verbose output |
| `-o` | Output file for results |

## Examples

### Example 1: Basic Usage

Scan a single host for Cisco services:

```bash
./cisco-torch.pl -s -f 192.168.1.1
```

### Example 2: Advanced Usage

Mass scan a subnet, fingerprint, and brute-force with wordlist:

```bash
./cisco-torch.pl -z 10.0.0.0/24 -s -f -C /usr/share/wordlists/rockyou.txt -o scan_results.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[Password Guessing]] Password Guessing
- [[Active Scanning]] Active Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual Perl process spawning with high network I/O (e.g., multiple forked processes).
- Traffic patterns: High-volume SYN scans or protocol probes to Cisco ports (23, 22, 80, 443, 123, 161).
- Failed login attempts on Cisco services from a single source IP.
- Log entries for banner grabs or SNMP queries in device logs.
- Presence of cisco-torch.pl or its dependencies in process lists.

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
- [[tools/Hydra]]
- [[tools/snmpcheck]]

## References

- Official download: https://packetstormsecurity.com/files/65279/cisco-torch-1.2.tar.gz
- Book reference: 'Hacking Exposed Cisco Networks'
- GitHub mirror (community): https://github.com/rapid7/cisco-torch (unofficial)
