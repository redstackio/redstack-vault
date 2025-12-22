---
id: 3a39a994-f107-4fbf-9c2d-221561284541
name: httprint
type: tool
verified: true
created_at: '2020-02-26T02:54:02.531712+00:00'
updated_at: '2023-05-30T19:50:34.900284+00:00'
commands:
  - '[[commands/httprint-scan-web-server-signatures]]'
platforms:
  - Linux
  - Web
tags:
  - Enumeration
  - Web Applications
url: 'http://net-square.com/httprint/'
validated: true
---

# httprint

**Status**: ✓ Verified

## Overview

httprint is a web server fingerprinting tool that identifies web servers and web-enabled devices by analyzing HTTP response characteristics, such as headers, error pages, and other behavioral traits. It is particularly useful for detecting obfuscated servers where banner strings have been altered by plugins like mod_security or servermask, or for devices without standard banners like routers, switches, and access points.

## Description

httprint performs signature-based fingerprinting by sending crafted HTTP requests and matching responses against a database of known server signatures. This allows for accurate identification even in environments where traditional methods like checking the Server header fail. It supports both HTTP and HTTPS and can fingerprint a wide range of servers, including Apache, IIS, and embedded devices. Common use cases include reconnaissance during penetration testing, verifying server configurations, and identifying potential misconfigurations or hidden services.

## Features

- Signature-based fingerprinting using HTTP response analysis
- Support for obfuscated servers and non-standard devices
- Confidence scoring for match accuracy
- HTTPS support with proxy integration
- Customizable request plugins for advanced probing

## Installation

### Requirements

- Linux environment (tested on Debian-based distributions like Kali Linux)
- Perl (for some plugins, though core is C-based)
- Root privileges not required, but network access is needed

### Install Commands

On Kali Linux, httprint is available in the repositories:

```bash
sudo apt update
sudo apt install httprint
```

For Ubuntu/Debian without Kali repos:

```bash
# Download from official source or compile
wget http://net-square.com/httprint/httprint.tar.gz
# Extract and follow manual installation instructions from readme
```

Manual compilation (if source is available):

```bash
# Assuming source tarball is downloaded
tar -xzf httprint-source.tar.gz
cd httprint
make
sudo make install
```

Signatures database is typically installed to /usr/share/httprint/signatures.txt.

## Basic Usage

```bash
httprint --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h | Specify the target host (e.g., -h http://example.com) |
| -s | Path to signatures file (e.g., -s signatures.txt) |
| -P | Use proxy for requests |
| -u | Update signatures database |
| -p | Specify port (default 80) |

## Examples

### Example 1: Basic Usage

Scan a web server for signatures:

```bash
httprint -h http://10.10.10.10 -s /usr/share/httprint/signatures.txt
```

### Example 2: Advanced Usage

Scan via proxy and custom port:

```bash
httprint -h http://example.com:8080 -s signatures.txt -P 127.0.0.1:8080
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Gather Victim Host Information]] Gather Victim Host Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual HTTP requests with specific patterns (e.g., multiple HEAD/GET variations)
- Network logs showing probes to common paths like /server-status or error pages
- Process monitoring for httprint executable
- IDS/IPS rules for fingerprinting signatures

## Related Procedures

- [[procedures/web-server-fingerprinting]]

## Related Tools

- [[tools/Nmap]]
- [[tools/WhatWeb]]

## References

- Official website: http://net-square.com/httprint/
- GitHub mirrors or archives for updated signatures
