---
type: tool
verified: true
platforms:
  - BSD
  - Linux
  - Mac OS X
  - Windows
tags:
  - enumeration
  - fingerprint
  - network
url: 'http://xprobe.sourceforge.net/'
commands:
  - '[[commands/xprobe2-fingerprint-os]]'
validated: true
---

# xprobe2

**Status**: ✓ Verified

## Overview

xprobe2 is an active operating system fingerprinting tool designed for network reconnaissance. It uses fuzzy signature matching, probabilistic guesses, multiple match criteria, and a customizable signature database to identify target operating systems, distinguishing it from signature-only tools like p0f or nmap's OS detection.

## Description

xprobe2 actively probes targets with ICMP, TCP, UDP, and protocol-specific packets (e.g., SMB, SNMP) to elicit responses that reveal OS characteristics. It's particularly useful in early reconnaissance phases for mapping network assets and tailoring subsequent attacks based on OS-specific vulnerabilities. The tool supports modular probing and can handle firewalled or filtered networks better than passive fingerprinters.

## Features

- Fuzzy matching for robust OS identification even with variations in responses
- Probabilistic scoring for guess confidence (e.g., 93% Linux)
- Modular architecture with pluggable ping, infogather, and fingerprint modules
- Support for ICMP echo, timestamp, address mask, TCP handshakes, RST packets, SMB, and SNMPv2c
- Customizable signature database for adding new OS fingerprints
- Distance calculation via TTL for network topology mapping

## Installation

### Requirements

- GCC compiler and make utilities
- libpcap development libraries (for packet capture)
- Perl (for some scripts)

### Install Commands

xprobe2 is not available in standard repositories for most distributions and requires compilation from source.

```bash
# Download source from official site or archive
wget https://sourceforge.net/projects/xprobe/files/xprobe2/0.3/xprobe2-0.3.tar.gz

tar -xzf xprobe2-0.3.tar.gz
cd xprobe2-0.3

# Configure and compile
./configure
make
sudo make install
```

For Kali Linux, it may be available via community packages or can be installed similarly. On Windows, use Cygwin or compile with MinGW.

## Basic Usage

```bash
xprobe2 --help
```

This displays available options, including module selection and signature files.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and exit |
| -v, --verbose | Increase verbosity level for detailed output |
| -s FILE | Use custom signature database file |
| -p MODULE | Specify probe modules to load (e.g., -p icmp_echo,tcp_hshake) |
| -o FILE | Output results to a file |

## Examples

### Example 1: Basic Usage

```bash
xprobe2 10.10.10.10
```

Performs default fingerprinting on the target, loading all modules and providing an OS guess.

### Example 2: Advanced Usage

```bash
xprobe2 -v -s custom_os.sig -p tcp_hshake,smb 192.168.1.100
```

Uses a custom signature file with verbose output, limiting to TCP handshake and SMB modules for a Windows target.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

- Network-based IDS signatures for unusual ICMP/TCP/UDP probes (e.g., timestamp requests, address mask queries)
- Firewall logs showing connections to common ports (139/445 for SMB, 161 for SNMP)
- Process monitoring for xprobe2 execution on compromised hosts
- Anomaly detection in TTL patterns or probe sequences

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
- [[tools/p0f]]
- [[Ettercap]]

## References

- Official project: http://xprobe.sourceforge.net/
- SourceForge archive: https://sourceforge.net/projects/xprobe/
- Usage guide: Man page or included documentation after installation
