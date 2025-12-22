---
id: c3d47148-d045-48ae-b65a-1674ff817cf0
type: tool
verified: true
created_at: '2020-02-22T05:15:06.784664+00:00'
updated_at: '2023-05-30T19:51:26.200390+00:00'
platforms:
  - Linux
tags:
  - cryptography
  - heartbleed
  - vulnerability
  - network
url: 'https://github.com/Lazza/Heartbleed'
validated: true
---

# heartbleed-poc

**Status**: ✓ Verified

## Overview

heartbleed-poc is a Python-based proof-of-concept tool for testing and exploiting the Heartbleed vulnerability (CVE-2014-0160) in OpenSSL versions prior to 1.0.1g. It sends malformed TLS heartbeat requests to remote servers to trigger memory leaks, potentially exposing sensitive data such as private keys, passwords, and server memory contents. Commonly used in penetration testing to assess vulnerable HTTPS services.

## Description

The tool establishes a TLS connection to the target server on port 443 (or a specified port), negotiates the heartbeat extension, and requests oversized heartbeat responses. Due to the buffer over-read flaw in vulnerable OpenSSL implementations, the server echoes back more data than requested, leaking up to 64KB of process memory per request. This can be repeated to dump larger portions of memory. It supports specifying the number of attempts and output files for the leaked data in hexadecimal format.

## Features

- Tests for Heartbleed vulnerability presence
- Dumps leaked memory in hex format for analysis
- Supports custom ports and multiple heartbeat requests
- Outputs to file for offline review of sensitive data
- Works over standard HTTPS/TLS connections

## Installation

### Requirements

- Python 2.7 (the script is not compatible with Python 3)
- Git for cloning the repository
- Network access to the target server on port 443 (or specified)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/Lazza/Heartbleed.git
cd Heartbleed

# No additional installation needed; the script is standalone
```

On Kali Linux, it may require installing Python 2 if not present:

```bash
sudo apt update && sudo apt install python2 git
```

## Basic Usage

```bash
python2 heartbleed-poc.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p PORT, --port PORT` | Target port (default: 443) |
| `-n NUM, --num NUM` | Number of heartbeat requests (default: 1) |
| `-f FILE, --file FILE` | Output file for hex dump |
| `-s, --starttls` | Use STARTTLS for protocols like SMTP/IMAP |

## Examples

### Example 1: Basic Usage

Scan a single target and perform one heartbeat request:

```bash
python2 heartbleed-poc.py 10.10.10.10
```

### Example 2: Advanced Usage

Dump memory with multiple requests and save to file on a custom port:

```bash
python2 heartbleed-poc.py 10.10.10.10 -p 8443 -n 5 -f memory_leak.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Unsecured Credentials]] Unsecured Credentials (for extracting keys from memory)

### Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic: Unusual TLS heartbeat requests (type 24) with oversized payloads on port 443
- Server logs: Repeated TLS handshake attempts from a single source
- Memory dumps: Presence of hex-encoded server memory leaks in logs or files
- Process monitoring: Python 2 processes connecting to HTTPS ports with heartbeat extensions
- IDS signatures: Alerts for CVE-2014-0160 exploitation attempts

## Related Procedures

No related procedures documented yet.

## Related Tools

- [[tools/openssl]] (for manual TLS testing)
- [[tools/Nmap]] (for initial port scanning)
- [[tools/Wireshark]] (for capturing TLS traffic)

## References

- Official GitHub Repository: https://github.com/Lazza/Heartbleed
- CVE Details: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0160
- OpenSSL Heartbleed Advisory: https://www.openssl.org/news/secadv/20140407.txt
