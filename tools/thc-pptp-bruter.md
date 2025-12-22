---
id: 351c09cb-8a77-43b1-ae6b-18569a5d7249
type: tool
verified: true
created_at: '2019-08-28T21:17:43.232738+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - brute-force
  - vpn
  - pptp
  - credential-access
url: 'https://github.com/vanhauser-thc/thc-pptp-bruter'
validated: true
---

# thc-pptp-bruter

**Status**: Unverified

## Overview

thc-pptp-bruter is a specialized brute force tool designed for attacking PPTP (Point-to-Point Tunneling Protocol) VPN endpoints listening on TCP port 1723. It supports the MSChapV2 authentication mechanism and is optimized for high-speed password guessing, capable of attempting up to 300 passwords per second by exploiting weaknesses in Microsoft's anti-brute force protections. Commonly used in penetration testing for credential recovery on Windows and Cisco-based VPN gateways.

## Description

This standalone tool performs offline and online brute force attacks against PPTP VPN servers. It handles the full PPTP handshake and MSChapV2 challenge-response authentication, making it effective against legacy VPN implementations that lack robust rate limiting. The tool is particularly useful in red team engagements targeting enterprise networks with outdated VPN configurations, allowing testers to demonstrate the risks of weak credentials in VPN access points.

## Features

- High-speed brute forcing (up to 300 attempts/second) via optimized MSChapV2 handling
- Support for single username/password, password lists, or username lists
- Multi-threading for parallel attempts to accelerate cracking
- Standalone binary with no external dependencies beyond standard libraries
- Tested compatibility with Windows Server and Cisco VPN gateways
- Verbose output for monitoring progress and logging results

## Installation

### Requirements

- Linux environment (Kali Linux recommended)
- GCC compiler and make utilities
- libpcap-dev for network packet handling

### Install Commands

```bash
# Clone the repository
git clone https://github.com/vanhauser-thc/thc-pptp-bruter.git

# Navigate to the directory and build
cd thc-pptp-bruter
make
sudo make install
```

On Kali Linux, it may be available via package manager:

```bash
sudo apt update
sudo apt install thc-pptp-bruter
```

## Basic Usage

```bash
thc-pptp-bruter --help
```

This displays all available options, including flags for usernames, passwords, hosts, and threads.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -u USER | Specify a single username |
| -U USERS | Specify a username list file |
| -p PASS | Specify a single password |
| -P PASSLIST | Specify a password list file |
| -h HOST | Target PPTP host IP/hostname |
| -t THREADS | Number of threads for multi-threaded attacks |
| -v | Verbose output mode |

## Examples

### Example 1: Basic Usage

Brute force with a single username and password list:

```bash
thc-pptp-bruter -u admin -P /usr/share/wordlists/rockyou.txt -h 192.168.1.1
```

### Example 2: Advanced Usage

Multi-threaded attack with username enumeration using a common password:

```bash
thc-pptp-bruter -U /path/to/usernames.txt -p defaultpass -h vpn.example.com -t 10
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force
- [[Password Spraying]] Password Spraying

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual volume of TCP/1723 connections from a single source IP
- Failed authentication logs in VPN server (e.g., Windows Event ID 20275 for RRAS)
- Network traffic analysis showing rapid MSChapV2 challenge-response patterns
- Process monitoring for 'pptp-bruter' binary on attacker machines
- IDS/IPS rules for PPTP protocol anomalies or brute force thresholds

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Hydra]]
- [[Medusa]]
- [[tools/ncrack]]

## References

- Official GitHub Repository: https://github.com/vanhauser-thc/thc-pptp-bruter
- THC Tools Documentation: http://www.thc.org/thc-pptp-bruter/
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1110/
