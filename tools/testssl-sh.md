---
url: 'https://testssl.sh'
tags:
  - ssl-test
  - recon
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:11.031Z'
id: 9130f748-ed8c-41ed-8e8e-4a8b8c2146d2
validated: true
submitted: true
---
# testssl-sh

**Status**: Unverified

## Overview

Command-line tool for testing SSL/TLS configurations, protocols, ciphers, and vulnerabilities on servers, useful for identifying MITM-enabling misconfigs.

## Description

Testssl.sh scans targets like apps.owncloud.com for cipher support, including anonymous ones on SMTP, providing grades and detailed reports for security assessments.

## Features

- Feature 1: Protocol and cipher enumeration
- Feature 2: Vulnerability checks (e.g., Heartbleed, BREACH)
- Feature 3: Custom OpenSSL support

## Installation

### Requirements

- Bash shell
- OpenSSL 1.0+ (Homebrew on macOS)

### Install Commands

```bash
# Clone and run
curl -s https://testssl.sh/testssl.sh -o testssl.sh && chmod +x testssl.sh
```

## Basic Usage

```bash
testssl.sh --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help |
| -e | List all ciphers |

## Examples

### Example 1: Basic Usage

```bash
./testssl.sh apps.owncloud.com
```

### Example 2: Advanced Usage

```bash
./testssl.sh --sneaky apps.owncloud.com:587
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing multiple TLS probes
- User-agent or banner matching testssl.sh

## Related Procedures

- [[procedures/Scan-SSL-TLS-Cipher-Support-with-Testssl]]

## Related Tools

- [[tools/sslyze]]
- [[tools/openssl-s-client]]

## References

- Official site: https://testssl.sh
- GitHub: https://github.com/drwetter/testssl.sh
