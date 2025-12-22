---
id: 0bdb7d19-9394-4470-ba5d-ead70a2177b3
type: tool
verified: true
created_at: '2019-08-28T21:17:31.394924+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
commands:
  - '[[commands/tlssled-scan-ssl-tls-configuration]]'
platforms:
  - Linux
  - Web
tags:
  - data-encryption
  - enumeration
  - network
  - ssl
  - tls
url: 'http://www.taddong.com/tools/TLSSLed_v1.3.sh'
validated: true
---

# TLSSLed

**Status**: Unverified

## Overview

TLSSLed is a lightweight Linux shell script designed for assessing the security of SSL/TLS implementations on HTTPS web servers. It performs automated checks for common misconfigurations and vulnerabilities, making it ideal for reconnaissance in penetration testing to identify weak encryption practices early in an engagement.

## Description

TLSSLed evaluates key aspects of a target's SSL/TLS setup, including support for outdated protocols like SSLv2, insecure ciphers such as NULL or low-strength (40/56-bit) options, availability of strong ciphers (e.g., AES), certificate signing algorithms (flagging MD5), and renegotiation capabilities. The tool outputs a summary report highlighting potential weaknesses, helping pentesters prioritize targets with poor configurations. It operates over the network without requiring agent installation on the target.

## Features

- **Protocol Detection**: Checks for legacy SSLv2 support.
- **Cipher Suite Analysis**: Identifies NULL ciphers and weak key lengths (40/56 bits) while verifying strong cipher availability.
- **Certificate Validation**: Detects MD5-signed certificates.
- **Renegotiation Testing**: Assesses secure vs. insecure renegotiation support.
- **Simple Reporting**: Generates a concise textual summary of findings.

## Installation

### Requirements

- Linux environment (e.g., Kali, Ubuntu) with bash and basic networking tools (openssl implied for underlying checks).
- Internet access for downloading the script.

### Install Commands

```bash
# Download the script
wget http://www.taddong.com/tools/TLSSLed_v1.3.sh -O TLSSLed.sh

# Make it executable
chmod +x TLSSLed.sh
```

On Kali Linux, it is not pre-installed, so manual download is required. For Ubuntu/Debian:

```bash
sudo apt update && sudo apt install wget
wget http://www.taddong.com/tools/TLSSLed_v1.3.sh -O TLSSLed.sh
chmod +x TLSSLed.sh
```

## Basic Usage

```bash
./TLSSLed.sh --help
```

The script does not have a formal --help flag but accepts a target host and optional port as arguments.

### Common Options

| Option | Description |
|--------|-------------|
| None (positional) | Target host (required) |
| Port (positional) | Optional port (defaults to 443) |

## Examples

### Example 1: Basic Usage

Scan a standard HTTPS server:

```bash
./TLSSLed.sh example.com
```

### Example 2: Advanced Usage

Scan on a custom port:

```bash
./TLSSLed.sh example.com 8443
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic: Outbound connections to target ports 443/HTTPS with SSL/TLS handshake probes (monitor for multiple cipher negotiations).
- Process monitoring: Execution of TLSSLed.sh or wget/curl downloading the script from taddong.com.
- Log analysis: Web server logs showing repeated SSL handshakes from a single source IP.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]] (for broader port scanning)
- [[TestSSL.sh]] (more comprehensive SSL testing)

## References

- Official download: http://www.taddong.com/tools/TLSSLed_v1.3.sh
- Related resources: OWASP SSL/TLS Testing Guide
