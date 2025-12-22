---
id: 55e9f99d-4559-4727-99e5-d897eeaa5345
type: tool
verified: true
created_at: '2019-08-28T21:17:25.499247+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - forensics
  - pcap
  - traffic-analysis
  - extraction
url: 'http://www.xplico.org/'
validated: true
---

# xplico

**Status**: Unverified

## Overview

Xplico is an open-source tool designed for extracting application-layer data from network traffic captures, such as PCAP files. It focuses on reconstructing higher-level content like emails (via POP, IMAP, SMTP), web traffic (HTTP contents), VoIP calls (SIP, MGCP, H.323), file transfers (FTP, TFTP), and more. Unlike traditional protocol analyzers like Wireshark, Xplico emphasizes application data reconstruction over low-level packet dissection, making it useful for forensic analysis, incident response, and security investigations.

## Description

Xplico operates as a network forensic analysis tool that processes captured traffic to recover meaningful application data. Users can upload PCAP files to its web-based interface, where built-in modules automatically detect and extract content from various protocols. It supports a wide range of applications, including web browsing artifacts, email communications, and multimedia streams. Xplico is particularly valuable in offensive security for analyzing captured traffic during red team operations or for blue teams in post-incident forensics to identify exfiltrated data or command-and-control communications.

## Features

- **Protocol Support**: Extracts data from HTTP, FTP, TFTP, SMTP, POP, IMAP, SIP, MGCP, H.323, and others.
- **Web Interface**: User-friendly GUI for uploading PCAPs and viewing extracted content.
- **Modular Design**: Extensible with custom input and output modules for specific protocols.
- **Output Formats**: Generates reports, files, and database entries for easy review.
- **Automation**: Can run as a daemon for continuous processing of traffic.

## Installation

### Requirements

- Linux distribution (Debian/Ubuntu-based preferred)
- Root or sudo access
- Dependencies: Python 2/3, SQLite, various protocol libraries (e.g., libpcap)
- At least 1GB RAM for processing large captures

### Install Commands

On Kali Linux (pre-compiled package available):

```bash
sudo apt update
sudo apt install xplico
```

On Ubuntu/Debian:

```bash
sudo apt update
sudo apt install xplico
```

Manual installation from source:

```bash
sudo apt install git build-essential libpcap-dev python3
cd /opt
sudo git clone https://github.com/iagox86/xplico.git
cd xplico
sudo make
sudo make install
```

After installation, configure the database and modules as per the official documentation.

## Basic Usage

```bash
tool-name --help
```

Xplico primarily uses a service-based model. Start the service using [[commands/xplico-start-service]], then access the web interface at http://127.0.0.1:81/ (default port). Upload a PCAP file via the GUI to begin extraction.

### Common Options

Xplico service management uses standard systemd options; direct CLI options are limited to module configuration.

| Option | Description |
|--------|-------------|
| `-h, --help` | Not directly applicable; use service help |
| `--verbose` | Enable in web interface for detailed logs |

## Examples

### Example 1: Basic Usage

Start the service and access the interface:

```bash
sudo service xplico start
# Then open browser to http://localhost:81/
# Upload pcap_file.pcap and select extraction modules
```

### Example 2: Advanced Usage

Process a PCAP for HTTP and email extraction:

1. Start service with [[commands/xplico-start-service]]
2. In web UI, upload PCAP
3. Enable HTTP and SMTP modules
4. View extracted web contents and emails in the output panel

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]] Network Sniffing (for capturing traffic to analyze)
- [[Web Protocols]] Web Protocols (extracting HTTP/SMTP data)

### Tactics

- [[Collection]] Collection
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Running processes: xplicod, xplico_webapp
- Open ports: TCP 81 (default web interface)
- Log entries in /var/log/xplico/
- Unusual CPU/disk usage during PCAP processing

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Wireshark]] (complementary packet analyzer)
- [[tools/TShark]] (CLI traffic capture)
- [[tools/tcpdump]] (packet capture for input to Xplico)

## References

- Official website: http://www.xplico.org/
- GitHub repository: https://github.com/iagox86/xplico
- Documentation: Included in /usr/share/doc/xplico/
