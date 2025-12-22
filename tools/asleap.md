---
id: 44282bca-467b-41fd-8fd3-008a92ee741f
type: tool
verified: true
created_at: '2019-08-28T21:17:38.002767+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - wireless
  - credential-access
  - brute-force
  - leap
  - mschapv2
url: 'https://www.kali.org/tools/asleap/'
validated: true
---

# asleap

**Status**: Unverified

## Overview

asleap is a tool designed to exploit vulnerabilities in Cisco's Lightweight Extensible Authentication Protocol (LEAP) wireless networks. It performs offline dictionary attacks against LEAP authentication exchanges, which use a variant of MS-CHAPv2. The tool can also target Point-to-Point Tunneling Protocol (PPTP) and other MS-CHAPv2 implementations by specifying challenge and response values manually. It is commonly used in wireless penetration testing to recover weak passwords from captured authentication packets.

## Description

LEAP, a proprietary Cisco protocol, relies on MS-CHAPv2 for authentication, making it vulnerable to dictionary-based cracking due to the ability to perform offline attacks. asleap accelerates this process by extracting challenges and responses from captured traffic (e.g., via packet captures) and attempting to crack them using wordlists. It supports reading from PCAP files or direct input of challenge/response pairs, enabling testers to assess the strength of LEAP-protected networks or legacy PPTP VPNs. Note that LEAP is deprecated and insecure; modern WPA2/3 should be used instead.

## Features

- Offline dictionary attacks on LEAP and MS-CHAPv2 hashes
- Support for PCAP file input to extract authentication exchanges
- Manual specification of challenge and response for targeted cracking
- Integration with wordlist-based brute-forcing for weak password recovery
- Compatible with wireless packet captures from tools like airodump-ng

## Installation

### Requirements

- Linux environment (Kali Linux recommended)
- Wireless network interface card (for capturing traffic, if not using pre-captured PCAPs)
- Wordlist for dictionary attacks (e.g., rockyou.txt)

### Install Commands

```bash
# On Kali Linux (pre-installed)
# No action needed

# On Ubuntu/Debian
sudo apt update
sudo apt install asleap

# From source (if needed)
git clone https://github.com/jordanwiens/asleap.git
cd asleap
make
sudo make install
```

## Basic Usage

```bash
asleap --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-C, --challenge` | Specify the NT challenge (hex string) |
| `-R, --response` | Specify the NT response (hex string) |
| `-W, --wordlist` | Path to the dictionary wordlist file |
| `-r, --read` | Read authentication exchanges from PCAP file |
| `-f, --file` | Output file for results (default: stdout) |
| `-h, --help` | Show help message |

## Examples

### Example 1: Basic Usage

Crack a known MS-CHAPv2 challenge/response pair using a wordlist.

See [[commands/asleap-crack-mschapv2-with-dictionary]] for details.

### Example 2: Advanced Usage

Extract and crack LEAP credentials from a PCAP file.

See [[commands/asleap-crack-leap-from-pcap]] for details.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Password Guessing]] Password Guessing (dictionary attacks on captured credentials)
- [[Private Keys]] Unsecured Credentials (exploiting weak wireless auth)

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual network traffic analysis on legacy LEAP or PPTP protocols
- Presence of asleap binary or processes on compromised systems
- High CPU usage during offline cracking attempts
- Logs of PCAP file access or wordlist processing in forensic analysis

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/aircrack-ng]] (for capturing wireless packets)
- [[tools/Hashcat]] (for advanced hash cracking)
- [[tools/john-the-ripper]] (alternative password cracker)

## References

- Official Kali Tools page: https://www.kali.org/tools/asleap/
- Source code: https://github.com/jordanwiens/asleap
- Wireless security documentation: https://www.aircrack-ng.org/
