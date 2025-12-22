---
id: 8bf1d3b8-2044-4793-9360-aa78b154b782
name: Unicornscan
type: tool
verified: true
created_at: '2019-08-28T21:17:25.577899+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - scanning
  - tcp
  - udp
url: 'http://www.unicornscan.org/'
commands:
  - '[[commands/unicornscan-tcp-port-scan]]'
  - '[[commands/unicornscan-udp-port-scan]]'
  - '[[commands/unicornscan-banner-grab]]'
validated: true
---

# Unicornscan

**Status**: Unverified

## Overview

Unicornscan is a new information gathering and correlation engine built for and by members of the security research and testing communities. It was designed to provide an engine that is Scalable, Accurate, Flexible, and Efficient. It is released for the community to use under the terms of the GPL license. Unicornscan serves as a user-land distributed TCP/IP stack, offering a superior interface for introducing stimuli into and measuring responses from TCP/IP-enabled devices or networks.

## Description

Unicornscan excels in asynchronous, stateless scanning, making it ideal for large-scale network reconnaissance in offensive security operations. It supports advanced features like TCP flag variations, banner grabbing, and protocol-specific UDP scanning. Common use cases include host discovery, port scanning, service enumeration, and passive OS/application identification during penetration testing and red team engagements.

## Features

- Asynchronous stateless TCP scanning with all variations of TCP flags.
- Asynchronous stateless TCP banner grabbing.
- Asynchronous protocol-specific UDP scanning (sending signatures to elicit responses).
- Active and passive remote OS, application, and component identification by analyzing responses.
- PCAP file logging and filtering.
- Relational database output.
- Custom module support.
- Customized data-set views.

## Installation

### Requirements

- Linux kernel with raw socket support.
- libpcap development libraries.
- GCC compiler.

### Install Commands

```bash
# On Kali Linux (pre-installed)
# No action needed

# On Ubuntu/Debian (compile from source)
git clone https://github.com/aryobichi/unicornscan.git
cd unicornscan
./autogen.sh
./configure
make
sudo make install

# Verify installation
unicornscan -V
```

## Basic Usage

```bash
unicornscan --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-V` | Display version information |
| `-l $_LOGFILE` | Log output to PCAP file |
| `-r $_RATE` | Set packet rate (pps) |
| `-mT` | TCP mode |
| `-mU` | UDP mode |

## Examples

### Example 1: Basic Usage

Perform a basic TCP SYN scan on a target.

```bash
unicornscan 192.168.1.100:1-1000
```

### Example 2: Advanced Usage

UDP scan with rate limiting and PCAP logging.

```bash
unicornscan -mU -r 1000 -l scan.pcap 192.168.1.0/24:53,123
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual high-volume, asynchronous TCP/UDP traffic patterns from a single source.
- Partial TCP handshakes or stateless scans triggering IDS rules for port scanning.
- PCAP logs showing rapid packet bursts at specified rates.
- Network flow data indicating banner grabbing attempts on common services.

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
- [[tools/masscan]]

## References

- Official website: http://www.unicornscan.org/
- GitHub repository: https://github.com/aryobichi/unicornscan
- Kali Linux tools page: https://www.kali.org/tools/unicornscan/
