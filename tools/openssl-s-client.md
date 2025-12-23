---
url: 'https://www.openssl.org/'
tags:
  - https
  - network
  - tls
type: tool
platforms:
  - Linux
  - macOS
  - Windows
description: >-
  Command-line tool for establishing HTTPS connections and sending custom
  requests quietly.
id: 4ac14abe-222a-4216-877c-49595e3434e0
created_at: '2025-12-14T03:16:25.616Z'
updated_at: '2025-12-14T03:16:25.616Z'
verified: false
validated: true
submitted: true
---
# OpenSSL-s-client

**Status**: Unverified

## Overview

OpenSSL's s_client is a diagnostic tool for testing SSL/TLS connections, used here to pipe raw HTTP data over HTTPS without verbose output, enabling precise request crafting for vulnerability exploitation.

## Description

It establishes a client-side TLS connection to a server, allowing manual HTTP request input. In security testing, it's paired with scripts to send unencoded payloads to web applications, as in this stored XSS injection.

## Features

- Feature 1: Quiet mode to suppress handshake details
- Feature 2: Connect to specific host/port for HTTPS
- Feature 3: Bidirectional data piping for custom protocols

## Installation

### Requirements

- OpenSSL library (usually pre-installed on Unix-like systems)

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update && sudo apt install openssl

# On macOS (via Homebrew)
brew install openssl
```

## Basic Usage

```bash
openssl s_client -connect example.com:443 -quiet
```

### Common Options

| Option | Description |
|--------|-------------|
| `-connect` | Host:port to connect to |
| `-quiet` | Suppress verbose output |
| `-showcerts` | Display server certificates |

## Examples

### Example 1: Basic Usage

```bash
openssl s_client -connect drive.uber.com:443 -quiet
```

### Example 2: Advanced Usage

```bash
echo "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n" | openssl s_client -connect example.com:443 -quiet
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Standard Application Layer Protocol]]
- [[Network Service Scanning]]

### Tactics

- [[Command and Control]]

## Detection

Indicators and methods for detecting this tool's usage:

- Firewall logs for outbound TLS connections from openssl
- IDS alerts on anomalous HTTPS requests

## Related Procedures

- [[procedures/Inject-Malformed-HTTP-Request-to-Trigger-Stored-XSS]]

## Related Tools

- [[tools/Perl]]

## References

- Official documentation: https://www.openssl.org/docs/man1.1.1/man1/s_client.html
