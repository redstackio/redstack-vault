---
url: 'https://www.openssl.org/'
tags:
  - tls
  - crypto
  - testing
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:31.089Z'
id: 0caf99b7-f0e8-42b0-bf57-7ee491fd2403
validated: true
submitted: true
---
# OpenSSL

**Status**: Unverified

## Overview

OpenSSL is a robust toolkit for TLS/SSL operations, commonly used in security testing for handshakes, certificate validation, and session management.

## Description

OpenSSL supports TLS 1.3, client authentication, session resumption, and custom SNI handling, making it ideal for exploiting protocol misconfigurations like NGINX virtual host session sharing.

## Features

- Feature 1: TLS client/server simulation with s_client/s_server
- Feature 2: Session ticket handling and resumption
- Feature 3: Certificate and key management

## Installation

### Requirements

- C compiler (gcc/clang)
- Perl

### Install Commands

```bash
# On Ubuntu/Debian
apt update && apt install openssl

# Or from source
wget https://www.openssl.org/source/openssl-3.0.0.tar.gz
# Extract and compile
./config && make && make install
```

## Basic Usage

```bash
openssl s_client --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-connect` | Specify host:port |
| `-tls1_3` | Use TLS 1.3 |
| `-cert` | Client certificate |

## Examples

### Example 1: Basic Usage

```bash
openssl s_client -connect example.com:443
```

### Example 2: Advanced Usage

```bash
openssl s_client -connect example.com:443 -tls1_3 -servername example.com -cert client.crt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic with OpenSSL user-agent or debug output
- Unusual TLS handshakes in server logs

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

- Official documentation: https://www.openssl.org/docs/
- Related resources: https://wiki.openssl.org/
