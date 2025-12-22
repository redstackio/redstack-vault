---
id: 83dafaae-3530-4110-9e15-ce9fa010a65b
name: ace
type: tool
verified: true
created_at: '2019-08-28T21:17:26.622621+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - voip
  - enumeration
  - reconnaissance
  - dhcp
  - tftp
  - http
url: >-
  https://github.com/rapid7/metasploit-framework/blob/master/documentation/modules/auxiliary/voip/ace.rb
commands:
  - '[[commands/ace-basic-enumeration]]'
validated: true
---

# ace

**Status**: Unverified

## Overview

ACE (Automated Corporate Enumerator) is a VoIP corporate directory enumeration tool designed for security testing. It mimics the behavior of an IP phone to retrieve name and extension entries from a corporate directory, leveraging protocols like DHCP, TFTP, and HTTP. This tool is useful in red team engagements for discovering internal user information in VoIP environments without direct authentication.

## Description

ACE automates the enumeration of VoIP corporate directories by simulating an IP phone's interactions. It discovers directory entries that would typically be accessible via a phone's screen interface, such as names and phone extensions. Developed as part of VoIP security research (inspired by tools like VoIP Hopper), ACE targets future attack vectors where adversaries enumerate users by name rather than IP addresses or random streams. The tool requests directory data over DHCP for configuration, TFTP for firmware/config files, and HTTP for directory downloads, then parses and outputs the results to a text file for further use in VoIP assessment tools like SIPVicious or Metasploit modules.

## Features

- Mimics legitimate IP phone behavior to avoid detection
- Supports multiple protocols: DHCP, TFTP, HTTP
- Outputs enumerated data (names, extensions) to a parseable text file
- Integrates with broader VoIP attack toolchains
- Lightweight Perl-based implementation for quick deployment

## Installation

### Requirements

- Perl 5 (with modules: Net::DHCP, Net::TFTP, LWP::UserAgent)
- Root privileges for network interface manipulation
- Network access to the target VoIP environment

### Install Commands

```bash
# On Kali/Ubuntu (install dependencies)
sudo apt update
sudo apt install perl libnet-dhcp-perl libnet-tftp-perl libwww-perl

# Clone the repository (assuming GitHub source)
git clone https://github.com/foofus/ace.git /opt/ace
cd /opt/ace
chmod +x ace.pl

# Or use Metasploit integration (if available)
msfconsole -q -x "use auxiliary/voip/ace; set INTERFACE eth0; run"
```

For macOS:
```bash
brew install perl
cpan Net::DHCP Net::TFTP LWP::UserAgent
# Then clone as above
```

## Basic Usage

```bash
perl ace.pl -i eth0
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i, --interface INTERFACE` | Network interface to use for enumeration (e.g., eth0) |
| `-o, --output FILE` | Output file for directory entries (default: ace_output.txt) |
| `-h, --help` | Show help message |
| `-v, --verbose` | Enable verbose logging |

## Examples

### Example 1: Basic Usage

Run ACE on the default interface to enumerate the VoIP directory:

```bash
sudo perl /opt/ace/ace.pl -i eth0 -o directory.txt
```

This simulates an IP phone joining the network, requests config via DHCP/TFTP, downloads the directory via HTTP, and saves names/extensions to directory.txt.

### Example 2: Advanced Usage

Run with verbose output on a specific interface:

```bash
sudo perl /opt/ace/ace.pl -i wlan0 -v -o voip_enum.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Vulnerability Scanning]] Active Scanning: Vulnerability Scanning (for VoIP services)
- [[Network Service Scanning]] Network Service Scanning (VoIP directory discovery)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual DHCP requests mimicking IP phones on the network
- TFTP/HTTP traffic to VoIP servers from non-phone devices
- Perl processes with network modules active (e.g., ps aux | grep ace.pl)
- Log analysis for anomalous directory downloads in VoIP PBX logs (e.g., Asterisk, Cisco CUCM)
- Network monitoring for spoofed MAC addresses or DHCP discover packets

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[SIPVicious]]
- [[VoIP Hopper]]
- [[tools/Wireshark]]

## References

- Original research: SensePost VoIP security tools
- GitHub repository: https://github.com/foofus/ace (or integrated in Metasploit)
- VoIP enumeration guide: https://www.blackhillsinfosec.com/voip-penetration-testing/
